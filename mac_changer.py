#!usr/bin/env python
import subprocess
import optparse
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


options= get_arguments()
change_mac(options.interface, options.mac)
