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
LOG = logging.getLogger('grid_controller')
LOG.setLevel(logging.INFO)


def main():
    # Create message federate.
    fed = h.helicsCreateMessageFederateFromConfig('grid_controller.json')
    LOG.info("Message federate created")

    # Gather the endpoints (ep).
    ep_dict = {}
    for ep_idx in range(h.helicsFederateGetEndpointCount(fed)):
        # Get an endpoint object.
        ep_obj = h.helicsFederateGetEndpointByIndex(fed, ep_idx)
        # Extract name, type, and destination.
        ep_name = h.helicsEndpointGetName(ep_obj)
        ep_type = h.helicsEndpointGetType(ep_obj)
        ep_dest = h.helicsEndpointGetDefaultDestination(ep_obj)

        # Store the object and data type in the appropriate container.
        _ep_dict = {'ep': ep_obj, 'dtype': ep_type, 'destination': ep_dest}
        ep_dict[ep_name] = _ep_dict

        LOG.info('Registered endpoint %s', ep_name)

    # Enter execution mode #
    h.helicsFederateEnterExecutingMode(fed)
    LOG.info("Entering execution mode.")

    for t, control_signal in zip(count(), range(16, -17, -1)):

        # Get time.
        time_request = t * 60
        LOG.debug('Requesting time from broker: %d', time_request)
        current_time = h.helicsFederateRequestTime(fed, time_request)
        LOG.info('*' * 80)
        LOG.info('Received time from broker: %s', current_time)

        # Either send out commands in to GridLAB-D, or log output from
        # GridLAB-D.
        for ep_name, ep_data in ep_dict.items():
            try:
                destination = ep_data['destination'].split('/')[1]
            except (KeyError, IndexError):
                # Log output from GridLAB-D
                # Skip if there's no message. Not very Pythonic, but is
                # HELICS best practice.
                if not h.helicsEndpointHasMessage(ep_data['ep']):
                    LOG.warning('No message found on %s', ep_name)
                else:
                    # Grab the message and raw data from the endpoint.
                    msg = h.helicsEndpointGetMessage(ep_data['ep'])

                    LOG.info('GridLAB-D reports %s at %s',
                             ep_name.split('/')[1], msg.data)
            else:
                msg = h.helicsEndpointCreateMessageObject(ep_data['ep'])
                LOG.info('Sending %s to %s.', str(control_signal), destination)
                h.helicsMessageSetData(msg, str(control_signal))
                h.helicsEndpointSendMessage(ep_data['ep'], msg)

    h.helicsFederateFinalize(fed)
    LOG.info("Federate finalized.")

    h.helicsFederateFree(fed)


if __name__ == '__main__':
    main()
