syslog-client
=========

This role is used for SLA and track configuration on IOS

Requirements
------------

Tested against IOS XE 17.03.01 on CML2

Role Variables
--------------

Variables used in host_vars:
- logging_level
- logging_hosts - list of dicts with following parameters
  - host
  - interface - interface for ASA devices


Example Playbook
----------------

    - hosts: HQ1:FW1
      roles:
         - syslog-client

License
-------

BSD

Author Information
------------------

Aleksandr Gorbachev (agorbachev@nsalab.org)
