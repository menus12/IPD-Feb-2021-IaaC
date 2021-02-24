# Network as code 
## Demo repository for Cisco Netacad IPD Week (Febraury 2021)

Using this repository you can will find:
- Example of how to programmaticaly access Cisco Modeling Labs using virl2_client SDK
- Example of basic Ansible playbook for network configuration deployment
- Example of pyATS script and datafile to assure deployed configuration
- Example of CI/CD pipeline using GitHub Actions

## REPOSITORY STRUCTURE
**./deployment/**
Contains Ansible playbook and inventories

**./testing/**
Contains pyATS testing scripts

**./.github/workflows/**
Contains GitHub Actions workflows for CI/CD pipelines

**./cml_dev_topology.yaml**
CML2 topology instance for DEV cycle or PROD emulation, accessed via external bridge and NAT on ISP 

**./cml_ci_topology.yaml**
CML2 topology instance for CI process, has different NAT statements to allow concurent run with DEV/PROD instance

**./cml_wrapper.py**
Script to kickstart CML topology during CI workflow and shutdown it after using CML2 SDK
