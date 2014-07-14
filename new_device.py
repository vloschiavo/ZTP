import csv

# possibly use xls(x)?  would require additional module (sudo pip install xlrd)
#import xlrd

import yaml
import sys
from glob import glob
from jinja2 import Template

with open('device_data.csv') as csvfile:
	device_data = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in device_data:
		print ', '.join(row)


# Number of rows in CSV file
y = 2

# YAML file.
for x in range(1,y+1):
	yamlfilename = 'ex4200-0' + `x` + ".yml";
	conffilename = 'ex4200-0' + `x` + ".conf";

	print x
	print conffilename

	with open(yamlfilename) as fh:
	    data = yaml.load(fh.read())

	# Jinja2 template file.
	with open(glob('*.j2')[0]) as t_fh:
	    t_format = t_fh.read()

	template = Template(t_format)

	fout = open(conffilename, 'w')
	print fout
	fout.write((template.render(data)))
	fout.close()

print "Good bye!"
