  
import os
from pyats.easypy import run
from genie import testbed
import yaml
#from genie.harness.main import gRun

def main(runtime):
   
    run(testscript = './ut.py', testbed=testbed.load(os.path.join('./ci_testbed.yaml')), datafile=yaml.safe_load('./connectivity_tests.yaml'))