ZTPag: Zero Touch Provisioning Auto-config Generator
===========

Why does this exist? - This addresses some of the manual configuration generation holes not filled by native ZTP on JunOS devices. 

ZTP - Boots a fresh (new, out of the box) device, updates JunOS code, adds a config (usually a static configuration for all nodes that boot into ZTP).

ZTPag - is a python script that generates configurations and static dhcpd reservations for each device. 

What does it do:
-----

1) Auto generation of static dhcp reservations (as an alternative to the randomized/pool model).

2) Customized JunOS configuration per switch (versus traditional ZTP sending a single static configuration for all junos devices).

3) specific JunOS operating system per switch. - Main benefit here is if you have several device models that require different JunOS images or versions.

Work Flow
-----

1) Inventory your devices
	a) Gather, mac address at a minimum from the outside of the box via a bar-code scanner
	b) populate the device_data.csv

Hint: The actual mac address of your management interface can be calculated from the mac on the bar code.
Example: 

```sh
Bar code mac is:  aa:11:22:33:44:00
  vlan.0 mac is:  aa:11:22:33:44:01
     me0 mac is:  aa:11:22:33:44:3f
```

2) Fill in the other fields in the device_data.csv.

3) Edit the paths at the beginning of the python script.  One for the dhcpd file, and one for the config file path.

 a) If you put the path to your server's real dhcpd.conf (On Debian, and Debain based distributions, this is located at: /etc/dhcp/dhcpd.conf) and the script will append the host reservations.  You will just need to restart your dhcp daemon.
 b) Setting the config file path to the web server [document-root]/config/ will also save you the hassle of moving files later.
 c) just remember to run the script with sudo.

4) You will also notice that any options you specify in DHCP will be committed to the configuration, like: Hostname, IP address, DNS Server, NTP, Syslog, etc.  These can be overridden later by your jinja template configuration file.  The default example in this script append a "-dhcp" to the hostname reservation and change the host name again in the configuration file.  This way you can easily tell what stage a switch is in during the upgrade process for troubleshooting purposes.

5) Run the script! (with sudo if you changed the paths).  Start dhcpd and apache.

6) Power on an amnesiac switch (or request system zeroize one that isn't new) to test.

7) Monitor via console.  At a shell prompt tail the messages log to watch the ZTP progress and see any error messages.

```sh
tail -f /var/log/messages
```

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
Thanks to Sachin for your help working through the flow.

This is an extension to Juniper's basic ZTP. 
http://www.juniper.net/techpubs/en_US/junos13.3/topics/task/configuration/software-image-and-configuration-automatic-provisioning-confguring.html

Native ZTP allows you to apply a configuration to a new amnesiac device.  This extension creates ISC dhcpd.conf configurations as well as the JunOS configurations for an "unlimited" number of devices.

Hackers:
-----
Feel free to modify for your purposes.  The python script will use your csv headers as variables to be replaced in the Jinja2 template; adding a variable is as simple as adding a column (and header) in the csv and referencing the header in your jinja template.  

Example: 
1) Add a column to the csv called: bgp_peer
2) fill in some data
3) Add some BGP config to the template and use {{ bgp_peer }} to replace the values from the csv

-Enjoy


