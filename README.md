# Custom MAC Address Changer

Custom MAC address Changer, with complete control on the list of mac addresses.

![Screenshot 2022-12-27 at 8.44.03 AM.png](..%2F..%2F..%2F..%2Fvar%2Ffolders%2F_w%2Fmfz41pwd3xd0g8n44_k0zn080000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_jRIigT%2FScreenshot%202022-12-27%20at%208.44.03%20AM.png?raw=true)

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


