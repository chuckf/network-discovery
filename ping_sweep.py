#!/usr/bin/python

# ping_sweep.py - ping sweep a range of IPs or network block.
#
# ping_sweep.py -r <first-ip>-<lastip> | -c <ip/mask> [-t timeout]
# 
# -r range of IPs
# -c CIDR notation
# -t default is 500 (milliseconds?)


import os
import optparse
import netaddr

from netaddr import *

parser = optparse.OptionParser()

parser.add_option("--timeout","-t", help="define the timeout value",type=int)
parser.add_option("--range","-r", help="define the IP range", nargs=1)
parser.add_option("--cidr","-c", help="define the network in CIDR notation")

(opts, args) = parser.parse_args()

if not opts.range and not opts.cidr:
   print "You need to provide either the range or CIDR notation."
   exit(1)
elif opts.range:
   ips = opts.range.split("-")
   iprange = IPRange(ips[0], ips[1])
   #print ips[0]
   #print ips[1]

if opts.timeout is not None:
   timeout = opts.timeout
   print timeout

for ip in iprange:
   os.system("ping -c 1 " + str(ip))
    
