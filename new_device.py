import csv

# possibly use xls(x)?  would require additional module (sudo pip install xlrd)
#import xlrd

# yaml option 
#import yaml

import sys
from glob import glob
from jinja2 import Template


device_data = csv.DictReader(open("device_data.csv"))
for row in device_data:
	data = row
	conffilename =  row["hostname"] + ".conf";

# option to use yaml data source
#		with open(yamlfilename) as fh:
#		    data = yaml.load(fh.read())
# end option to use yaml data source

	# Jinja2 template file.
	with open(glob('*.j2')[0]) as t_fh:
	    t_format = t_fh.read()

	template = Template(t_format)
	fout = open(conffilename, 'w')
	print fout
	fout.write((template.render(data)))
	fout.close()

print "Good bye!"
