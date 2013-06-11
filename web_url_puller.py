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
# 6/10/2013 - added more error checking.
#
# TODO:
# Get SSL encoding working
# Get regex parsing working 



import os
import re
import optparse
import netaddr
import urllib
import urllib2

from netaddr import *
from subprocess import Popen, PIPE, STDOUT
from optparse import OptionParser
from urllib2 import Request, urlopen, URLError

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
  
  request = urllib2.Request(url)
  try: 
    urllib2.urlopen(request)
  except URLError as e:
    print "Nothing to parse: Error code " + str(e.code) + " " + e.reason  
    exit(1)

  response = urllib2.urlopen(request)
  html = response.read()
  print html

if __name__ == "__main__":
    main()
