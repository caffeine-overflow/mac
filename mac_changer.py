#!usr/bin/env python
import subprocess
import optparse
import re
# ffdgdg

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m", "--mac", dest="mac", help="New MAC address")
    (options, arguments) =  parser.parse_args()
    if not options.interface:
        parser.error(("[-] Please specify an interface, use --help for more info"))
    elif not options.mac:
        parser.error(("[-] Please specify an mac address, use --help for more info"))
    return options

def change_mac(interfaceparm, new_macparm):
    print("[+]Changing MAC address for " + interfaceparm + " to " + new_macparm)
    subprocess.call(["ifconfig", interfaceparm, "down"])
    subprocess.call(["ifconfig", interfaceparm, "hw", "ether", new_macparm])
    subprocess.call(["ifconfig", interfaceparm, "up"])

def get_mac_address(interfaceparm):
    ifconfig_result = subprocess.check_output(["ifconfig", interfaceparm])
    mac_regex = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_regex:
        return mac_regex.group(0)
    else:
        print("Could not find a MAC address")


options= get_arguments()
current_mac = get_mac_address(options.interface)
print("Current MAC : "+ str(current_mac))
change_mac(options.interface, options.mac)
current_mac = get_mac_address(options.interface)
if current_mac == options.mac:
    print("[+] MAC address was successfully changed to "+ current_mac)
else:
    print("[-] MAC address did not get changed")
