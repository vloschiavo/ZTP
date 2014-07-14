#!/usr/bin/python

# Import the necessary modules
import csv
import sys
from jinja2 import Template

# Read device_data.csv from the current directory
# csv.DictReader reads the first row as a header row and stores the column headings as keys
device_data = csv.DictReader(open("device_data.csv"))

# Loops through the device_data csv so we can perform actions for each row
for row in device_data:
	# Stores the contents of each "cell" as the value for the column header
	# key : value pair

	# The below example will print the value of the management IP column for the current row.
	# print row["mgmt_ip"] 
	data = row
	
	# creates a filename variable for the JunOS configuration based on the hostname in the CSV
	conffilename =  row["hostname"] + ".conf";

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
	with open("dhcpd.conf", "a") as dhcpdconf:
		dhcpdconf.write(template2.render(data))

print "Good bye!"
