#!/bin/bash

# Generate a timestamp
timestamp=$(date +"%Y-%m-%d_%H-%M-%S")

# Define the base directory
base_dir="/Users/phil_man/workspace/GitHub/LOGIK-PROJEKT/resources/utilities/"

# Define the log files directory
log_files_dir="$base_dir/test_logs/"

# Define the log file path
log_file="$log_files_dir/rsync_log_$timestamp.log"

# Define the source and destination paths
source_path="$base_dir/test_src/"
destination_path="$base_dir/test_dst/"

# Run rsync with the log file option
rsync -av --log-file="$log_file" $source_path $destination_path
