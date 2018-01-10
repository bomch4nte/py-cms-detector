#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#
import urllib2
def getHTML(url, data=None, user_agent=None, timeout=3):
  request = urllib2.Request(url, data=data, headers={'User-Agent': user_agent})
  return urllib2.urlopen(request, timeout=timeout)
