nbu-cmd-opscenter-add-master
============================

# Description

A sample Ansible role for integrating a NetBackup Server with OpsCenter

# Requirements

This role has the following requirements:

  - Ansible 2.9+
  - NetBackup 9.0+
  - Linux Based Master Server 
  - SSH keyless access between Ansible host and the NetBackup servers
  - Credentials to login to the NetBackup CLI ("Username" + Password) 
  - Active Directory Domain Information and credentials to login to the NetBackup CLI ("Username" + Password)
  - API Key for Administrative NetBackup user

# Assumptions

To utilize this role, in-depth knowledge of both Veritas NetBackup and Ansible is required

# How to use the role

This role is part of a collection of roles available in netbackup-ansible project. To use the role:

  1. Clone the repository from GitHub and move to your Ansible Control Host:

           git clone https://github.com/VeritasOS/netbackup-ansible.git

  2. Update the role variables: 

           - playbook.yml

               NBU_MASTER_SERVER - Hostname of the NetBackup Master Server
               NBU_API_KEY - User's API key for authenticating with NetBackup API
               nbu_admin_User - Username to login to the NetBackup API (*)
               nbu_admin_password - Password for user to login to the NetBackup API (*)
               opscenter_hostname - Hostname for OpsCenter Server

           (*) Its recommended to migrate these secrets into an encrypted vars file or to a secrets management platform

  3. Create a playbook and Inventory file

            Examples are provided below in the next section

  4. Provide an inventory and execute the playbook on the master server or Linux server with access HTTPS access to the NetBackup master server:

           "ansible-playbook <playbook_name> -i <inventory_file> "

# Example Playbook / Inventory

A sample playbook and invetory file is provided below:

  1. Example "playbook.yml" file

           - name: Veritas -> Add Master Server to OpsCenter
             hosts: master
             gather_facts: no
             roles:
               - nbu-cmd-ad-integration
             vars:
               NBU_MASTER_SERVER - Hostname of the NetBackup Master Server
               NBU_API_KEY - User's API key for authenticating with NetBackup API
               nbu_admin_User - Username to login to the NetBackup API (*)
               nbu_admin_password - Password for user to login to the NetBackup API (*)
               opscenter_hostname - Hostname for OpsCenter Server

  2. Example "inventory.yml" file

	        [localhost]
	        locahost ansible_host=localhost

	        [master]
	        <fqdn1> ansible_host=<ip_address>

# Version

| Directory Name | Version | Description | 
| :--- | :--- |:--- |
| nbu-cmd-opscenter-add-master | 1.0 | Inital release |

# License

