# Copyright 2021 Spirent Communications.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Code to integrate Prox Traffic generator with vineperf test framework.

"""

import csv
import logging
import os
import subprocess

from conf import settings
from core.results.results_constants import ResultsConstants
from tools.pkt_gen import trafficgen
from tools.pkt_gen.prox.runrapid import RapidTestManager

class Prox(trafficgen.ITrafficGenerator):
    """
    Prox Traffic Generator
    """
    _logger = logging.getLogger(__name__)
    _liveresults_file = settings.getValue("TRAFFICGEN_STC_LIVERESULTS_FILE")

    def connect(self):
        """
        Do nothing.
        """
        return self

    def disconnect(self):
        """
        Do nothing.
        """
        pass

    def send_burst_traffic(self, traffic=None, duration=20):
        """
        Do nothing.
        """
        return None

    def send_rfc2889_forwarding(self, traffic=None, tests=1, _duration=20):
        """
        Send traffic per RFC2889 Forwarding test specifications.
        """
        raise NotImplementedError('Not implemented by PROX')

    def send_rfc2889_caching(self, traffic=None, tests=1, _duration=20):
        """
        Send as per RFC2889 Addr-Caching test specifications.
        """
        raise NotImplementedError('Not implemented by PROX')

    def send_rfc2889_learning(self, traffic=None, tests=1, _duration=20):
        """
        Send traffic per RFC2889 Addr-Learning test specifications.
        """
        raise NotImplementedError('Not implemented by PROX')

    def send_cont_traffic(self, traffic=None, duration=30):
        """
        Send Custom - Continuous Test traffic
        Reuse RFC2544 throughput test specifications along with
        'custom' configuration
        """
        raise NotImplementedError('Not implemented by PROX')

    def prepare_config_files():
        """
        Prepare the configuration files here
        """

    def send_rfc2544_throughput(self, traffic=None, tests=1, duration=20,
                                lossrate=0.0):
        """
        Send traffic per RFC2544 throughput test specifications.
        """
        # Check if it is baremetal or cloud
        if not of settings.getValue('Openstack')
        test_params = RapidTestManager.get_defaults()
        # Update the testparams accordingly
        framesize = settings.getValue("TRAFFICGEN_PROX_FRAME_SIZE")
        if traffic and 'l2' in traffic:
            if 'framesize' in traffic['l2']:
                framesize = traffic['l2']['framesize']
        settings.setValue("TRAFFICGEN_PROX_FRAME_SIZE", framesize)

        
        test_manager = RapidTestManager()
        test_result, _ = test_manager.run_tests(self.test_params)
        # if cloud, just call the run_rapid script, right set of parameters.



    def send_rfc2544_back2back(self, traffic=None, tests=1, duration=20,
                               lossrate=0.0):
        """
        Send traffic per RFC2544 BacktoBack test specifications.
        """
        raise NotImplementedError('Not implemented by PROX')

    def start_cont_traffic(self, traffic=None, duration=30):
        raise NotImplementedError('Not implemented by PROX')

    def stop_cont_traffic(self):
        raise NotImplementedError('Not implemented by PROX')

    def start_rfc2544_back2back(self, traffic=None, tests=1, duration=20,
                                lossrate=0.0):
        raise NotImplementedError('Not implemented by PROX')

    def wait_rfc2544_back2back(self):
        raise NotImplementedError('Not implemented by PROX')

    def start_rfc2544_throughput(self, traffic=None, tests=1, duration=20,
                                 lossrate=0.0):
        raise NotImplementedError('Not implemented by PROX')

    def wait_rfc2544_throughput(self):
        raise NotImplementedError('Not implemented by PROX')
