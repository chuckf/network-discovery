#!/usr/bin/python 
#
# web_url_puller.py - pull the links out of a web page
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; Applies version 2 of the License.
#
# web_url_puller.py -u ip [-s]
# 
# -u url
# -p port number
# -s 
#
# 6/5/2013 - initial code
# 6/10/2013 - added more error checking.
# 6/21/2013 - working with regex
#
# TODO:
# -Add SSL support


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

  (opts, args) = parser.parse_args()

  if opts.url:
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

  #counter for how many links in the HTML
  linkvalue = 0 

  page = urllib2.urlopen(url)
  html = page.read()
  links = re.findall(r"<a.*?\s*href=\"(.*?)\".*?>(.*?)</a>", html)

  for link in links:
    print('link: ' + link[0])
    linkvalue = linkvalue+1

  if linkvalue == 0:
    print "No links in this HTML file."

if __name__ == "__main__":
    main()
