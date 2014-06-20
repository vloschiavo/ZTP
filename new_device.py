import yaml
import sys
from glob import glob
from jinja2 import Template

# YAML file.
with open(glob('*.yml')[0]) as fh:
    data = yaml.load(fh.read())

# Jinja2 template file.
with open(glob('*.j2')[0]) as t_fh:
    t_format = t_fh.read()

template = Template(t_format)
print (template.render(data))