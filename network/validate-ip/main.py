#!/usr/bin/env python

def is_valide_ip(ip):
    '''Validate address IP4 or IP6 in any form'''
    
    import ipaddress

    try:
        ipaddress.ip_address(ip)
    except ValueError:
        return False
    
    return True


def is_valide_ip4(ip):
    '''Validate address IP4 in form a.b.c.d'''
    
    parts = ip.split(".")

    if len(parts) != 4:
        return False

    for x in parts:
        try:
            number = int(x)
        except ValueError:
            return False

        #if not (0 <= number <= 255):
        if number < 0 or number > 255:
            return False

    return True
    
    
if __name__ == '__main__':

    data = [
        '0.0.0.0',
        '127.0.0.1',
        '200',
        'a.b.c.d',
        '200::',
    ]
    
    for ip in data:
        if is_valide_ip4(ip):
            print('IP4:', ip, 'OK')
        else:
            print('IP4:', ip, 'Wrong')
        
        if is_valide_ip(ip):
            print('IPx:', ip, 'OK')
        else:
            print('IPx:', ip, 'Wrong')
