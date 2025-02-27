nbu-tuning-linux
================

# Description

A sample Ansible role for defining NetBackup tuning touch files

# Requirements

This role has the following requirements:

  - Ansible 2.9+
  - NetBackup 9.0+
  - Linux Based NetBackup Server 
  - SSH keyless access between Ansible host and the NetBackup servers

Notes:

# Assumptions

To utilize this role, in-depth knowledge of both Veritas NetBackup and Ansible is required

# How to use the role

This role is part of a collection of roles available in netbackup-ansible project. To use the role:

  1. Clone the repository from GitHub and move to your Ansible Control Host:

           git clone https://github.com/VeritasOS/netbackup-ansible.git

  2. Update the role variables: 

           - playbook

               nbu_role - The NetBackup role running on the host "master", "media" or "client_linux"

  3. Create a playbook and Inventory file

            Examples are provided below in the next section

  4. Provide an inventory and execute the playbook on the master server or Linux server with access HTTPS access to the NetBackup master server:

           "ansible-playbook <playbook_name> -i <inventory_file> "

# Example Playbook / Inventory

A sample playbook and invetory file is provided below:

  1. Example "playbook.yml" file(s)

           - name: Veritas -> Set NetBackup tuning parameters
             hosts: master
             gather_facts: no
             roles:
               - nbu-tuning-linux
             vars:    
                nbu_role: "master"

           - name: Veritas -> Set NetBackup tuning parameters
             hosts: media
             gather_facts: no
             roles:
               - nbu-tuning-linux
             vars:    
                nbu_role: "media"

           - name: Veritas -> Set NetBackup tuning parameters
             hosts: client_linux
             gather_facts: no
             roles:
               - nbu-tuning-linux
             vars:    
                nbu_role: "client_linux"

  2. Example "inventory.yml" file

	        [localhost]
	        locahost ansible_host=localhost

	        [master]
	        <fqdn1> ansible_host=<ip_address>

	        [media]
	        <fqdn1> ansible_host=<ip_address>

	        [client_linux]
	        <fqdn1> ansible_host=<ip_address>

# Version

| Directory Name | Version | Description | 
| :--- | :--- |:--- |
| nbu-tuning-linux | 1.0 | Inital release |

# License

