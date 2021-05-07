# Build HELICS and GridLAB-D (GLD).
# HELICS resource: https://docs.helics.org/en/latest/installation/docker.html

# Set up environment variables in "base" stage.
FROM python:3.7-slim-buster as base

# Branches/tags for HELICS and GLD
# Latest release as of 2021-05-07
ENV HELICS_BRANCH=v2.7.0
# Tip of develop as of 2021-05-07
ENV GLD_BRANCH=7d2931eeb4c22520328cb02bad8dca1f13b74bb1

# Where to put our built software?
ENV HELICS_INSTALL_PATH=/usr/local
ENV GLD_INSTALL_PATH=/usr/local

# Patch the Python path so it can find helics.py.
ENV PYTHONPATH ${HELICS_INSTALL_PATH}/python

# GridLAB-D required environment variables:
ENV CXXFLAGS=-I${GLD_INSTALL_PATH}/share/gridlabd \
    # No need to patch the path when using standard /usr/local location.
    # PATH=${PATH}:/usr/local/bin \
    GLPATH=${GLD_INSTALL_PATH}/lib/gridlabd:${GLD_INSTALL_PATH}/share/gridlabd \
    # (Maybe) need to update the LD_LIBRARY_PATH so GridLAB-D can find
    # the HELICS libraries.
    LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${HELICS_INSTALL_PATH}/lib

FROM base as builder
# Install building dependencies.
RUN apt-get update && apt-get install -y \
  autoconf \
  automake \
  build-essential \
  cmake \
  g++ \
  gcc \
  git \
  libboost-dev \
  libboost-filesystem-dev \
  libboost-program-options-dev \
  libboost-test-dev \
  libtool \
  libzmq5-dev \
  make \
  # HARD-CODE to match Python version.
  python3.7-dev \
  swig

# (Shallowly) clone HELICS.
RUN git clone https://github.com/GMLC-TDC/HELICS.git \
  --branch ${HELICS_BRANCH} --depth 1 --single-branch /tmp/helics

# Follow HELICS template and work in an empty building directory.
WORKDIR /tmp/helics/build

# Run cmake
RUN cmake \
  -DBUILD_PYTHON_INTERFACE=ON \
  # HARD-CODE Python paths.
  -DPYTHON_INCLUDE_DIR=/usr/include/python3.7/ \
  -DPYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython3.7m.so \
  -DCMAKE_INSTALL_PREFIX=${HELICS_INSTALL_PATH} \
  ..

# Make and install.
# WORKDIR /tmp/helics
RUN make -j8 && make -j8 install

# Build GridLAB-D (and its dependency, Xerces)
WORKDIR /tmp/gridlab-d

# Shallowly clone the repository. Special sequence of commands in order
# to only fetch the state of the repo at a single sha.
# https://stackoverflow.com/a/43136160/11052174
RUN git init && \
    git remote add origin https://github.com/gridlab-d/gridlab-d.git && \
    git fetch --depth 1 origin ${GLD_BRANCH} && \
    git checkout FETCH_HEAD

# Install Xerces.
WORKDIR /tmp/gridlab-d/third_party
RUN perl -E "print '*' x 80" && \
    printf '\nInstalling Xerces...\n' && \
    tar -xzf xerces-c-3.2.0.tar.gz && \
    cd /tmp/gridlab-d/third_party/xerces-c-3.2.0 && \
    ./configure --prefix=${GLD_INSTALL_PATH} --disable-static CFLAGS=-O2 CXXFLAGS=-O2 && \
    make -j $(($(nproc) + 1)) && \
    make -j $(($(nproc) + 1)) install

# Install GridLAB-D
WORKDIR /tmp/gridlab-d
RUN perl -E "print '*' x 80" && \
    printf '\nInstalling GridLAB-D...\n' && \
    autoreconf -isf && \
    # http://gridlab-d.shoutwiki.com/wiki/Builds
    # http://gridlab-d.shoutwiki.com/wiki/Connection:helics_msg
    ./configure --prefix=${GLD_INSTALL_PATH} --with-helics=${HELICS_INSTALL_PATH} --with-xerces=${GLD_INSTALL_PATH} --enable-silent-rules 'CFLAGS=-g -O2 -w' 'CCFLAGS=-g -O2 -w' 'CXXFLAGS=-g -O2 -w -std=c++14' 'LDFLAGS=-g -O2 -w' && \
    make -j $(($(nproc) + 1)) && \
    make -j $(($(nproc) + 1)) install && \
    perl -E "print '*' x 80" && \
    printf "\nWe're all done building!\n"

FROM base as runner

# Copy over the installed program files.
COPY --from=builder ${HELICS_INSTALL_PATH} ${HELICS_INSTALL_PATH}
COPY --from=builder ${GLD_INSTALL_PATH} ${GLD_INSTALL_PATH}

# Install HELICS library dependencies.
RUN apt-get update && apt-get install -y --no-install-recommends \
    # libboost versions do not match HELICS docs - Debian Buster has
    # 1.67.0, while whatever Ubuntu version they used has 1.65.1.
    # This newer version seems to work just fine.
    libboost-filesystem1.67.0 \
    libboost-program-options1.67.0 \
    libboost-test1.67.0 \
    libzmq5 \
    python3-dev \
    && \
    apt-get clean && \
    apt-get autoclean -y && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /models

# Run the GridLAB-D.
ENTRYPOINT ["gridlabd"]
