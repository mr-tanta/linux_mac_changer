# Custom MAC Address Changer

Custom MAC address Changer, with complete control on the list of mac addresses.

![](macchanger.png?raw=true)

# Installation



# Usage


## Usage

Type `python3 mac_changer.py [option] [interface] [option] [mac]`:
```
Usage: python3 mac_changer.py [option] [interface] [option] [mac]
Options:
 -h, --help          Show this help message and exit
 -i  --interface     Set the interface to change it's MAC Address
 -m, --mac MAC       Set a custom MAC address, e.g. -m aa:bb:cc:dd:ee:ff 
```
NOTE: Make sure to run as root

### Set custom MAC
`python3 mac_changer.py -i wlan0 -m aa:bb:cc:dd:ee:ff`


