#!/usr/bin/python 
# ping_sweep.py - ping sweep a range of IPs or network block.
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; Applies version 2 of the License.
#
# ping_sweep.py -r <first-ip>-<lastip> | -c <ip/mask> [-t timeout]
# 
# -r range of IPs
# -c CIDR notation
# -t default is 500 (milliseconds?)
#
# 6/3/2013 - Range, CIDR, and timeout work now. 
#
# TODO:
# Check per OS type (Mac/Linux/Windows)
#


import os
import platform
import re
import optparse
import netaddr
import subprocess

from netaddr import *
from subprocess import Popen, PIPE, STDOUT

def main():

  out = os.popen("which ping")
  ping_cmd = out.read().strip("\n")
     

  parser = optparse.OptionParser()

  parser.add_option("--range","-r", help="define the IP range", nargs=1)
  parser.add_option("--timeout","-t", help="define the timeout value in milliseconds",type=int)
  parser.add_option("--cidr","-c", help="define the network in CIDR notation",nargs=1)

  (opts, args) = parser.parse_args()

  if not opts.range and not opts.cidr:
     print "You need to provide either the range or CIDR notation."
     exit(1)
  elif opts.cidr:
     iprange = IPNetwork(opts.cidr)
  elif opts.range:
     ips = opts.range.split("-")
     iprange = IPRange(ips[0], ips[1])

  if opts.timeout is not None:
     timeout = opts.timeout
  else:
     timeout = None
     
  for ip in iprange:
     netaddress = re.compile("^\d{1,3}.\d{1,3}.\d{1,3}.0")
     test = netaddress.match(str(ip))
     if not test:
       DEVNULL = open(os.devnull, 'wb')
       if timeout:  
         response = subprocess.call([ping_cmd, '-W', str(timeout), '-c 1', str(ip)],stdout=DEVNULL,stdin=PIPE,stderr=STDOUT)
       else:
         response = subprocess.call([ping_cmd, '-c 1', str(ip)], stdout=DEVNULL,stdin=PIPE,stderr=STDOUT)
       # If the IP Address answers, print it
       if response == 0:
         print ip


if __name__ == "__main__":
    main()
