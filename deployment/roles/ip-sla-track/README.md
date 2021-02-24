ip-sla-tack
=========

This role is used for SLA and track configuration on IOS

Requirements
------------

Tested against IOS XE 17.03.01 on CML2

Role Variables
--------------

Variables used in host_vars:
sla_instance:
  - id: 
    type: 
    dest: 
    source: 
    frequency: 
    start: 
    life: 

track_instance:
  - id: 
    sla: 
    type: 


Example Playbook
----------------

    - hosts: routers
      roles:
         - ip-sla-tack

License
-------

BSD

Author Information
------------------

Aleksandr Gorbachev (agorbachev@nsalab.org)
