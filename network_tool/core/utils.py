
def find_correct_byte(subnet_mask: str):
    
    cidr = find_cidr(subnet_mask)
    host_bit = 2 ** ( 8- (cidr % 8))
    correct_byte = cidr // 8
    return host_bit, correct_byte
    
def find_network_by_cidr(ip: str, correct_byte: int, host_bit: int) -> list[int]:
    list_ip = str_ip_to_int(ip)
    network = list_ip[::]
    network[correct_byte] = list_ip[correct_byte] // host_bit * host_bit
    network[correct_byte + 1:] = [0 for _ in network[correct_byte + 1:]]
    return network

def find_broadcast(network: list, correct_byte: int, host_bit: int) -> list[int]:
    broadcast = network[::]
    broadcast[correct_byte] += host_bit - 1 
    broadcast[correct_byte + 1:] = [255 for _ in broadcast[correct_byte + 1:]]
    print(network)
    return network

def num_of_hosts(cidr: int) -> int:
    return 2 ** (32 - cidr) - 2

def find_cidr(subnet_mask: str) -> int:
    octatas = str_ip_to_int(subnet_mask)
    bin_subnet_mask = "".join(decimal_to_binary(i) for i in octatas)    
    cidr = bin_subnet_mask.split('0', 1)[0]
    print(len(cidr))
    return len(cidr)

def class_identification(mask: str) -> str:
    
    cidr = find_cidr(mask)
    
    if cidr % 8 != 0:
        return "Classless"
    elif cidr // 8 == 1:
        return "Class A"
    elif cidr // 8 == 2:
        return "Class B"
    elif cidr // 8 == 3:
        return "Class C"
     
def decimal_to_binary(dec_num: int, bits_len = 8) -> str:
    result = ""
    max_num = 2**bits_len - 1
    for i in range(bits_len - 1, -1, -1):
        if dec_num >= 2**i:
            result += "1"
            dec_num -= 2**i
        else:
            result += "0"

    return result

def int_to_str_ip(int_list) -> str:
    list_ip = list(map(str, int_list))
    return '.'.join(list_ip)

def str_ip_to_int(ip) -> list[int]:
    ip_oct = ip.split(".")
    return [int(i) for i in ip_oct if i != "" and i.isdigit()]


