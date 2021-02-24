# DEPLOYMENT

## Contains ansible playbook for deployment automation

**./host_vars/**
Contains variables for each host

**./host_group/**
Contains variables for each group of hosts

**./roles/**
Contains deployment roles

**./ansible.cfg**
Local ansible configuration file

**./dev_inventory.yaml**
Ansible inventory for DEV/PROD simulation instance

**./ci_inventory.yaml**
Ansible inventory for CI simulation instance

**./ci.yaml**
Example configuration to deploy:
L3 interfaces, ACLs and respective NAT statement for internal network, HSRP tracked by IP SLA also for internal network, dual-hub DMVPN with EIGRP routing over it, banner configuration