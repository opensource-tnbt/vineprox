import os

from conf import merge_spec
from conf import settings
from jinja2 import Environment, FileSystemLoader

_CURR_DIR = os.path.dirname(os.path.realpath(__file__))
settings.load_from_dir(os.path.join(_CURR_DIR, 'conf'))

values_from_vineperf = {
    'm1_admin_ip' : settings.getValue('TRAFFICGEN_PROX_EAST_MGMT_IP'),
    'm2_admin_ip' : settings.getValue('TRAFFICGEN_PROX_WEST_MGMT_IP'),
    'local_ip1' : settings.getValue('TRAFFICGEN_PROX_EAST_IP'),
    'local_ip2' : settings.getValue('TRAFFICGEN_PROX_WEST_IP'),
    'dest_hex_mac2' : settings.getValue('TRAFFICGEN_PROX_EAST_MAC'),
    'dest_hex_mac1' : settings.getValue('TRAFFICGEN_PROX_WEST_MAC'),
    'first_w' : settings.getValue('TRAFFICGEN_PROX_EAST_PCI_ID'),
    'second_w' : settings.getValue('TRAFFICGEN_PROX_WEST_PCI_ID'),
    'mcore' : settings.getValue('TRAFFICGEN_PROX_MASTER_CORES'),
    'gencores' : settings.getValue('TRAFFICGEN_PROX_GENERATOR_CORES'),
    'latcores' : settings.getValue('TRAFFICGEN_PROX_LATENCY_CORES'),
    'config_file' : settings.getValue('TRAFFICGEN_PROX_GENERATOR_CONFIG_FILENAME'),
    'user' : settings.getValue('TRAFFICGEN_PROX_GENERATOR_USER'),
    'key' : settings.getValue('TRAFFICGEN_PROX_GENERATOR_KEYFILE')
}

file_loader = FileSystemLoader('templates')
env = Environment(loader = file_loader)

for filename in os.listdir('templates'):
    file = env.get_template(filename)
    rendered_content = file.render(data = values_from_vineperf)
    print(rendered_content)

    with open(filename, "w") as fh:
        fh.write(rendered_content)