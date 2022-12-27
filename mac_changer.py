import re
import subprocess
import argparse


def get_argument():
    parser = optparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Interface to change it's MAC address.")
    parser.add_argument("-m", "--mac", dest="new_mac", help="New MAC address.")
    options = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more information")
    elif not options.new_mac:
        parser.error("[-] Please specify a new MAC address, use --help for more information")
    return options


def change_mac(interface, new_mac):
    print(f"[+] Changing the MAC address for {interface} to {new_mac}")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", f"{ifconfig_result}")
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print(f"[-] Sorry couldn't get a MAC address from {options.interface}")


options = get_argument()
current_mac = get_current_mac(options.interface)
print(f"[+] Current MAC = {current_mac}")

change_mac(options.interface, options.new_mac)
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print(f"[+] MAC address was changed successfully to {current_mac}")
else:
    print("[-] MAC address was not changed. Try again")
