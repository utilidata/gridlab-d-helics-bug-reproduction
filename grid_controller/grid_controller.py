# -*- coding: utf-8 -*-
"""This file represents an extension/modification of the following
file:
https://github.com/GMLC-TDC/HELICS-Examples/blob/310bec41df2155d0aec65444639ea36c92cf3b23/python/pi-exchange/pisender.py

The corresponding license is reproduced below:

BSD 3-Clause License

Copyright (c) 2017-2019, Battelle Memorial Institute; Lawrence Livermore National Security, LLC; Alliance for Sustainable Energy, LLC.
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""
# Standard library:
import argparse
from itertools import count
import logging
import sys
import time

# Third party:
import helics as h

logging.basicConfig(
    stream=sys.stdout, level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] [%(name)s]: %(message)s")
LOG = logging.getLogger('tap_controller')
LOG.setLevel(logging.INFO)


def main(broker_address="helics-broker:4545", log_level=None):
    fed_init_string = "--federates=1"
    delta_t = 1.0

    if broker_address is not None:
        fed_init_string += f' --broker_address=tcp://{broker_address}'

    helics_version = h.helicsGetVersion()

    LOG.info("Helics version = %s", helics_version)

    # Create Federate Info object that describes the federate properties #
    fed_info = h.helicsCreateFederateInfo()

    # Set Federate name #
    fed_name = "tap_controller"
    h.helicsFederateInfoSetCoreName(fed_info, fed_name)

    # Set core type from string #
    h.helicsFederateInfoSetCoreTypeFromString(fed_info, "zmq")

    # Set up logging.
    if log_level is not None:
        h.helicsFederateInfoSetIntegerProperty(
            fed_info, h.helics_property_int_log_level, log_level
        )

    # Federate init string #
    h.helicsFederateInfoSetCoreInitString(fed_info, fed_init_string)

    # Set the message interval (timedelta) for federate. Note the
    # HELICS minimum message time interval is 1 ns and by default
    # it uses a time delta of 1 second. What is provided to the
    # setTimedelta routine is a multiplier for the default timedelta.

    # Set one second message interval #
    h.helicsFederateInfoSetTimeProperty(
        fed_info, h.helics_property_time_delta, delta_t)

    # Create combination federate #
    combo_fed = h.helicsCreateCombinationFederate(fed_name, fed_info)
    LOG.info("Combination federate created")

    # Register the publications #
    pub_dict = {}
    for phase in 'ABC':
        key = f"tap_{phase}"
        pub = h.helicsFederateRegisterTypePublication(
            combo_fed, key, "int", "")
        pub_dict[key] = pub

    LOG.info("Tap position publications registered.")

    # Register the subscriptions.
    sub_dict = {}
    for phase in 'ABC':
        key = f"voltage_{phase}"
        sub = h.helicsFederateRegisterSubscription(
            combo_fed, f"gld_federate/{key}", "V"
        )
        sub_dict[key] = sub

    LOG.info("Voltage message subscriptions registered.")

    # Also subscribe to tap positions to confirm that they happen.
    tap_sub = h.helicsFederateRegisterSubscription(
        combo_fed, f"gld_federate/tap_A", ""
    )

    # Enter execution mode #
    h.helicsFederateEnterExecutingMode(combo_fed)
    LOG.info("Entering execution mode.")

    for t, tap in zip(count(), range(16, -17, -1)):

        # Get time.
        current_time = h.helicsFederateRequestTime(combo_fed, t * 60)
        LOG.info('*' * 80)
        LOG.info('Received time from broker: %s', current_time)

        # Grab current tap.
        LOG.info('GridLAB-D reports tap_A at position %d',
                 h.helicsInputGetInteger(tap_sub))

        # Publish tap positions.
        for pub in pub_dict.values():
            h.helicsPublicationPublishDouble(pub, tap)

        LOG.info("Commanded taps to position %d", tap)

        # Log voltages.
        for phase, sub in sub_dict.items():
            real, imag = h.helicsInputGetComplex(sub)
            v = complex(float(real), float(imag))
            LOG.debug('Phase %s real: %f', phase, real)
            LOG.debug('Phase %s imag: %f', phase, imag)
            LOG.info(f'Phase {phase} voltage is {abs(v):.2f}.')

    h.helicsFederateFinalize(combo_fed)
    LOG.info("Federate finalized.")

    h.helicsFederateFree(combo_fed)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--broker_address',
        help=('IP address (or host) and port of broker, e.g., "0.0.0.0:4545" '
              'or "helics-broker:4545"'),
        default='helics-broker:4545'
    )
    args = parser.parse_args()
    main(broker_address=args.broker_address)
