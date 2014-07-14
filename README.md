ZTPag 
Zero Touch Provisioning Auto-config Generator
===========

Why does this exist? - This addresses some of the manual configuration generation holes not filled by native ZTP on JunOS devices. 

ZTP - Boots a fresh (new, out of the box) device, updates JunOS code, adds a config (usually a static configuration for all nodes that boot into ZTP).

ZTPag - is a python script that generates configurations and static dhcpd reservations for each device. 

Work Flow
-----

1) Inventory your devices
	a) Gather, mac address at a minimum from the outside of the box via a bar-code scanner
	b) populate the device_data.csv

2) Fill in the other fields in the device_data.csv.

3) Run the script

Usage
-----
```sh
./ztp_configs.py
```
or
```sh
python ztp_configs.py
```

Notes and ack(s):
-----

Juniper doc:
http://www.juniper.net/techpubs/en_US/release-independent/nce/information-products/topic-collections/nce/new-rtg-device/adding-a-new-network-device.pdf

It specifically applies to the section "Configuring New Routing
Devices".

Thank you Jeremy Schulman for the inspiration.  See his work here: https://github.com/jeremyschulman/NCE

This is an extension to Juniper's basic ZTP. 
http://www.juniper.net/techpubs/en_US/junos13.3/topics/task/configuration/software-image-and-configuration-automatic-provisioning-confguring.html

Native ZTP allows you to apply a configuration to a new amnesiac device.  This extension creates ISC dhcpd.conf configurations as well as the JunOS configurations for an "unlimited" number of devices.

Hackers:
-----
Feel free to modify for your purposes.  They python will use your csv headers as variables to be replaced in the Jinja2 template; adding a variable is as simple as adding a column (and header) in the csv and referencing the header in your jinja template.  

Example: 
1) Add a column to the csv called: bgp_peer
2) fill in some data
3) Add some BGP config to the template and use {{ bgp_peer }} to replace the values from the csv

-Enjoy


