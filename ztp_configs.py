import csv
import sys
from jinja2 import Template

# Read device_data.csv from the current directory
device_data = csv.DictReader(open("device_data.csv"))

# Parse each row and store the contents as a "hash" into data
for row in device_data:
	data = row
	conffilename =  row["hostname"] + ".conf";

# option to use yaml data source
#		with open(yamlfilename) as fh:
#		    data = yaml.load(fh.read())
# end option to use yaml data source


	# Read the Junos config Jinja2 template file.
	with open("junos_conf_template.j2") as t_fh:
	    t_format = t_fh.read()

	template = Template(t_format)

	# Create the .conf file
	fout = open(conffilename, 'w')
	print fout

	# Write the conf file with the template and data from the row
	fout.write((template.render(data)))
	fout.close()

	# Create the ISC-DHCPd config for this node
	# Read the ISC-DHCPd Jinja2 template file.
	with open("isc-dhcpd_template.j2") as t2_fh:
	    t2_format = t2_fh.read()

	template2 = Template(t2_format)

	# Print to SDOUT	
	#print (template2.render(data))

	# Need to append to dhcpd.conf file
	with open("dhcpd.conf", "a") as dhcpdconf:
		dhcpdconf.write(template2.render(data))
	

print "Good bye!"
