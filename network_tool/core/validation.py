from core.utils import *

def validate_ip(ip: str):    
    octatas = str_ip_to_int(ip)
    for i in octatas:
        if i < 0 or i > 255:                    
            print(f"The {ip} entered is invalid.")
            return False
    return len(octatas) == 4

def is_mask_built_correctly(mask: str):
    octatas = str_ip_to_int(mask)
    result = "".join(decimal_to_binary(i) for i in octatas)
    if "01" in result:
        print("The mask is not constructed correctly.")
        return False
    return True

