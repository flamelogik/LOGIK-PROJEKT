#!/bin/bash

# Create the /etc/synthetic.conf file
sudo touch /etc/synthetic.conf

# Enter the string 'JOBS Volumes/logik/salt/JOBS' into the file
sudo bash -c "echo 'JOBS    Volumes/logik/salt/JOBS' >> /etc/synthetic.conf"
