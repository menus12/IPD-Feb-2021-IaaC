import argparse
import os
from virl2_client import ClientLibrary 
from datetime import datetime

def import_lab(client, path):
    lab_name = "ci-test-" + datetime.now().strftime("%Y%m%d"+"-%H%M%S")
    print('Importing test topology...')
    lab = client.import_lab_from_path(path, title=lab_name)
    print('Lab ' + lab_name + ' successfully imported. Lab ID is ' + lab.id)
    return lab

parser = argparse.ArgumentParser(description='CI test CML wrapper')    
parser.add_argument('--url', type=str, help='CML host URL (default from env)')
parser.add_argument('--user', type=str, help='CML username (default from env)')
parser.add_argument('--passwd', type=str, help='CML password (default from env)')
parser.add_argument('--topology', type=str, help='CML topology pass (default is ./cml_ci_topology.yaml)')
parser.add_argument('--action', type=str, help='create or destroy (default create)')
args = parser.parse_args()

if args.url == None:
    args.url = os.environ['VIRL2_URL']
if args.user == None:
    args.user = os.environ['VIRL2_USER']
if args.passwd == None:
    args.passwd = os.environ['VIRL2_PASS']
if args.action == None:
    args.action = 'create'
if args.topology == None:
    args.topology = './cml_ci_topology.yaml'

if args.url == None or args.user == None or args.passwd == None:
    print (parser.print_help())
    exit(1)

client_library = ClientLibrary(args.url, args.user, args.passwd, ssl_verify=False)
print('Successfully authenticated with CML controller')

if args.action == 'create':
    lab = import_lab(client_library, args.topology)
    
    f = open(".lab_id", "w")
    f.write(lab.id)
    f.close()
    
    print('Starting ' + lab.title + '...')
    lab.start(wait=True)
    
    print('Done!')
    
if args.action == 'destroy':
    f = open(".lab_id", "r")
    lab_id = f.read()
    f.close()
    
    print('Lab ID is ' + lab_id)
    lab = client_library.join_existing_lab(lab_id)
    
    print('Stoping lab' + lab_id)
    lab.stop()
    
    print('Wiping lab' + lab_id + ' out')
    lab.wipe()
    
    print('Removing lab' + lab_id)
    client_library.remove_lab(lab_id)
    
    print('Done!')
