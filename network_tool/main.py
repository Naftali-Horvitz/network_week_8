from core.utils import *
from core.validation import *
from core.output_string import *
from core.write_to_file import *

def main():
    
    ip = input("enter the ip.")
    while not validate_ip(ip):
        ip = input("enter the ip.")
    
    mask = input("enter the mask.")
    while not validate_ip(mask) or not is_mask_built_correctly(mask):
        mask = input("enter the mask.")
        
    cidr = find_cidr(mask)
    host_bit = 2 ** ( 8- (cidr % 8))
    correct_byte = cidr // 8
    
    int_network = find_network_by_cidr(ip, correct_byte, host_bit)
    network = int_to_str_ip(int_network)
    int_broadcast = find_broadcast(int_network, correct_byte, host_bit)
    broadcast = int_to_str_ip(int_broadcast)
    num_hosts = num_of_hosts(cidr)
    mask_class = class_identification(mask)
    id = '315605808'
    
    write_subnet_info(ip, id, mask, network, broadcast, num_hosts, mask_class, cidr)
    

if __name__ == "__main__":
    main()