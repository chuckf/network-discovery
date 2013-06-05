#!/usr/bin/python 
# ping_sweep.py - ping sweep a range of IPs or network block.
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; Applies version 2 of the License.
#
# reverse_lookup.py -r <first-ip>-<lastip> | -c <ip/mask> 
# 
# -r range of IPs
# -c CIDR notation
#
# 6/4/2013 - initial code
#


import os
import re
import optparse
import netaddr
import socket

from netaddr import *
from subprocess import Popen, PIPE, STDOUT

def main():

  parser = optparse.OptionParser()

  parser.add_option("--range","-r", help="define the IP range", nargs=1)
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

  for ip in iprange:
     netaddress = re.compile("^\d{1,3}.\d{1,3}.\d{1,3}.0")
     test = netaddress.match(str(ip))
     if not test:
       name,alias,address = socket.gethostbyaddr(str(ip)) 
       
       # If the IP Address answers, print it
       if name:
          print "Name: " + name
          print "Address: " + str(ip) + "\n"


if __name__ == "__main__":
    main()
