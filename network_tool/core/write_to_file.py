from core.output_string import *
from core.utils import *
from core.validation import *

def write_subnet_info(ip: str, id: str, subnet_mask:str, network: str, broadcast: str, num_hosts: int, mask_class : str, cidr: int):
    with open(f"subnet_info_{ip}_{id}", 'w') as f:
        f.write(format_input_ip(ip))
        f.write(format_subnet_mask(subnet_mask))
        f.write(format_class_full_status(mask_class))
        f.write(format_network_address(network))
        f.write(format_broadcast_address(broadcast))
        f.write(format_num_hosts(num_hosts))
        f.write(format_cidr_mask(cidr))
        