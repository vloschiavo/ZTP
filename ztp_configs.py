#!/usr/bin/python

# Import the necessary modules
import csv
import sys
from jinja2 import Template


##################################################
# Begin: User defined variables
##################################################
# For these two variables below to work you'll need to run the script as the appropriate user / credentials.  sudo should work fine.  If the script boms, check your paths and permissions.

# Set this variable to your dhcpd.conf path. In the example below, the system dhcpd.conf would appended with the specific host reservations.  You may want to backup your original first.  :)
# e.g.  dhcpd_file="/etc/dhcp/dhcpd.conf"
dhcpd_file="dhcpd.conf"

# Set this variable to your web server path. In the example below, the configurations would be located at http://server_ip/config/ on Ubuntu 14.04 with Apache2
# e.g.  conf_path="/var/www/config/"
conf_path=""

# File name of your csv file
csv_filename="device_data.csv"

# Command to restart your DHCP daemon - unremark the next line 
dhcpd_restart_command="sudo /etc/init.d/isc-dhcp-server restart"

##################################################
# End: User defined variables
# Beyond here be dragons
##################################################

# Read device_data.csv from the current directory
# csv.DictReader reads the first row as a header row and stores the column headings as keys
device_data = csv.DictReader(open(csv_filename))

# Loops through the device_data csv so we can perform actions for each row
for row in device_data:
	# Stores the contents of each "cell" as the value for the column header
	# key : value pair

	# The below example will print the value of the management IP column for the current row.
	# print row["mgmt_ip"] 
	data = row
	
	# creates a filename variable for the JunOS configuration based on the hostname in the CSV
	conffilename =  conf_path + row["hostname"] + ".conf";

	# Open the Junos config Jinja2 template file.
	with open("junos_conf_template.j2") as t_fh:
	    t_format = t_fh.read()

	# Set it up as a template
	template = Template(t_format)

	# Create the .conf file
	fout = open(conffilename, 'w')
	print fout

	# Write the conf file with the template and data from the current row
	# Performs a "search and replace"
	fout.write((template.render(data)))
	fout.close()

	# Create the ISC-DHCPd config for this node
	# Read the ISC-DHCPd Jinja2 template file.
	with open("isc-dhcpd_template.j2") as t2_fh:
	    t2_format = t2_fh.read()

	# Set it up as a template
	template2 = Template(t2_format)

	# Print to SDOUT	
	#print (template2.render(data))

	# Append our host definition to the dhcpd.conf
	with open(dhcpd_file, "a") as dhcpdconf:
		dhcpdconf.write(template2.render(data))

# Restart dhcpd
from subprocess import call
dhcpd_return_code = call(dhcpd_restart_command, shell=True)

print "Good bye!"
