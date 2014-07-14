Adding a New Juniper Device to Your Network via ZTP
===========

This example is described in detail in the following document:
http://www.juniper.net/techpubs/en_US/release-independent/nce/information-products/topic-collections/nce/new-rtg-device/adding-a-new-network-device.pdf

It specifically applies to the section "Configuring New Routing
Devices".

Based on Jeremy Schulman's work:
https://github.com/jeremyschulman/NCE

This is an extension to Juniper's basic ZTP. 
http://www.juniper.net/techpubs/en_US/junos13.3/topics/task/configuration/software-image-and-configuration-automatic-provisioning-confguring.html

Native ZTP allows you to apply a configuration to a new amnesiac device.  This extension creates ISC dhcpd.conf configurations as well as the JunOS configurations for an "unlimited" number of devices.

The script looks for a csv file named 'device_data.csv' with the headers as follows:
hostname,mgmt_ip,mac_address,serial_number,domain_name,root_encrypted_password


Usage
-----

```sh
python new_device.py
```
