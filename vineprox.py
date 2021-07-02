import logging
import os
import sys
import argparse
import re
import time
import csv
import datetime
import shutil
import unittest
import locale
import copy
import glob
import subprocess
import ast
import xmlrunner
from tabulate import tabulate
from conf import merge_spec
from conf import settings
from tools import tasks


VERBOSITY_LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}

_CURR_DIR = os.path.dirname(os.path.realpath(__file__))

def parse_param_string(values):
    """
    Parse and split a single '--test-params' argument.

    This expects either 'x=y', 'x=y,z' or 'x' (implicit true)
    values. For multiple overrides use a ; separated list for
    e.g. --test-params 'x=z; y=(a,b)'
    """
    results = {}

    if values == '':
        return {}

    for param, _, value in re.findall('([^;=]+)(=([^;]+))?', values):
        param = param.strip()
        value = value.strip()
        if param:
            if value:
                # values are passed inside string from CLI, so we must retype them accordingly
                try:
                    results[param] = ast.literal_eval(value)
                except ValueError:
                    # for backward compatibility, we have to accept strings without quotes
                    _LOGGER.warning("Adding missing quotes around string value: %s = %s",
                                    param, str(value))
                    results[param] = str(value)
            else:
                results[param] = True
    return results


def parse_arguments():
    """
    Parse command line arguments.
    """
    class _SplitTestParamsAction(argparse.Action):
        """
        Parse and split '--test-params' arguments.

        This expects either a single list of ; separated overrides
        as 'x=y', 'x=y,z' or 'x' (implicit true) values.
        e.g. --test-params 'x=z; y=(a,b)'
        Or a list of these ; separated lists with overrides for
        multiple tests.
        e.g. --test-params "['x=z; y=(a,b)','x=z']"
        """
        def __call__(self, parser, namespace, values, option_string=None):
            if values[0] == '[':
                input_list = ast.literal_eval(values)
                parameter_list = []
                for test_params in input_list:
                    parameter_list.append(parse_param_string(test_params))
            else:
                parameter_list = parse_param_string(values)
            results = {'_PARAMS_LIST':parameter_list}
            setattr(namespace, self.dest, results)

    class _ValidateFileAction(argparse.Action):
        """Validate a file can be read from before using it.
        """
        def __call__(self, parser, namespace, values, option_string=None):
            if not os.path.isfile(values):
                raise argparse.ArgumentTypeError(
                    'the path \'%s\' is not a valid path' % values)
            elif not os.access(values, os.R_OK):
                raise argparse.ArgumentTypeError(
                    'the path \'%s\' is not accessible' % values)

            setattr(namespace, self.dest, values)

    class _ValidateDirAction(argparse.Action):
        """Validate a directory can be written to before using it.
        """
        def __call__(self, parser, namespace, values, option_string=None):
            if not os.path.isdir(values):
                raise argparse.ArgumentTypeError(
                    'the path \'%s\' is not a valid path' % values)
            elif not os.access(values, os.W_OK):
                raise argparse.ArgumentTypeError(
                    'the path \'%s\' is not accessible' % values)

            setattr(namespace, self.dest, values)

    def list_logging_levels():
        """Give a summary of all available logging levels.

        :return: List of verbosity level names in decreasing order of
            verbosity
        """
        return sorted(VERBOSITY_LEVELS.keys(),
                      key=lambda x: VERBOSITY_LEVELS[x])

    parser = argparse.ArgumentParser(prog=__file__, formatter_class=
                                     argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--version', action='version', version='%(prog)s 0.2')
    group.add_argument('--k8s', action='store_true', help='execute Kubernetes tests')
    group.add_argument('--openstack', action='store_true', help='Run VSPERF with openstack')
    args = vars(parser.parse_args())

    return args

def main():
    """Main function.
    """
    args = parse_arguments()

    # configure settings

    settings.load_from_dir(os.path.join(_CURR_DIR, 'conf'))

    # define the timestamp to be used by logs and results
    date = datetime.datetime.fromtimestamp(time.time())
    timestamp = date.strftime('%Y-%m-%d_%H-%M-%S')
    settings.setValue('LOG_TIMESTAMP', timestamp)

    results_dir = "results_" + timestamp
    results_path = os.path.join(settings.getValue('LOG_DIR'), results_dir)
    settings.setValue('RESULTS_PATH', results_path)

    # create results directory
    if not os.path.exists(results_path):
        os.makedirs(results_path)


if __name__ == "__main__":
    main()
