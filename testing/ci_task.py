  
import os
from pyats.easypy import run
from genie import testbed
import yaml

def main(runtime):
    
    run(testscript = './ut.py', testbed=testbed.load(os.path.join('./ci_testbed.yaml')), datafile=yaml.safe_load('./sanity_tests.yaml'))