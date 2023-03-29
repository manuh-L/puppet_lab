#!/usr/bin/env python3
import socket

# Get the hostname
hostname = socket.gethostname()

# Get the site substring from the hostname
site = hostname[8:10]

# Check if site is equal to "dc" and print "Site=DC" if true
if site == "dc":
    print("Site=DC")

# Check if site is equal to "dr" and print "Site=DR" if true
elif site == "dr":
    print("Site=DR")

# If both conditions fail, print "Site=Unknown"
else:
    print("Site=Unknown")

