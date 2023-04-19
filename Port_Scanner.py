#!/usr/bin/env python3
import socket
import re
import pyfiglet
from datetime import datetime

def title():
    title_name = pyfiglet.figlet_format('PORT SCANNER')
    print(title_name)
def scan(ip_add_format,port_range_format,port_min,port_max,open_ports):
    while True:
        target = input("Please enter an IP address: ")
        ip_target_valid = re.search(ip_add_format, target)
        if ip_target_valid:
            pass
        else:
            print("Not a valid IP")
            break

        port_range_start = input("Enter beginning port: ")
        port_range_end = input("\nEnter ending port: ")

        start_target_valid = re.search(port_range_format, port_range_start)
        end_target_valid = re.search(port_range_format, port_range_end)

        port_range_start = int(port_range_start)
        port_range_end = int(port_range_end)

        if start_target_valid and end_target_valid:
            if port_range_start > port_min and port_range_start <= port_max and port_range_start <= port_range_end:
                if port_range_end > port_min and port_range_end <= port_max and port_range_end >= port_range_start:
                    pass
                else:
                    exit("Not a valid port range")
            else:
                exit("Not a valid port range")
        else:
            print("Ports exceed valid range")
            break

        print('_'* 50)
        print(f"Scanning target: {target}")
        print("Scan started at: " + str(datetime.now()))
        print('_' * 50)

        for port in range(port_range_start,port_range_end + 1):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(1.00)
                    s.connect((target, port))
                    open_ports.append(port)
            except:
                print(f"Port {port}: closed")
        for port in open_ports:
            print(f"Port {port} is open on {target}.")

if __name__ == "__main__":
    ip_add_format = re.compile("^[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}$")
    port_range_format = re.compile("^[0-9]{1,5}$")

    port_min = 0
    port_max = 65535
    open_ports = []

    title()
    scan(ip_add_format,port_range_format,port_min,port_max,open_ports)