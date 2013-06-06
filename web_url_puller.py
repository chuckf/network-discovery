#!/usr/bin/python 
# web_url_puller.py - pull the links out of a web page
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; Applies version 2 of the License.
#
# web_url_puller.py -u ip [-s]
# 
# -u url
# -s uses HTTP over SSL
# -p port number
#
# 6/5/2013 - initial code
#


import os
import re
import optparse
import netaddr
import socket

from netaddr import *
from subprocess import Popen, PIPE, STDOUT
from optparse import OptionParser

def main():

  parser = optparse.OptionParser()

  parser.add_option("--url","-u", help="the IP address of the URL", nargs=1)
  parser.add_option("--port","-p", help="port for the URL, defaults to port 80", nargs=1, default=80)
  parser.add_option("-s", action="store_true", dest="ssl", help="Use SSL over HTTP")

  (opts, args) = parser.parse_args()

  if opts.url and opts.ssl:
    url = "https://" + str(opts.url)
  elif opts.url and not opts.ssl:
    url = "http://" + str(opts.url)
  else:
    print "You need to provide the URL."
    exit(1)

  if opts.port is not 80:
    port = opts.port
  else:
    port = 80

# open a socket to port 80


if __name__ == "__main__":
    main()
