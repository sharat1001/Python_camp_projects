def is_valid_ipv4(ipv4):
    lst = ipv4.split('.')
    if len(lst) == 4:
        for key in lst:
            if not key:
                return False
            if len(key) > 1 and key[0] == '0':
                return False
            if not (0 <= int(key) <= 255):
                return False
            if not str.isnumeric(key):
                return False  
        return True
    else:
        return False
    
print(is_valid_ipv4("192.168.1."))
    


