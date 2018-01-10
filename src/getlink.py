#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#
import re
import gethtml
re_str = re.compile('<tr> <td>(.*?)</td><td')
API = 'http://viewdns.info/reverseip/?host=%s&t=1'
def reverseip(url):
  html = gethtml.getHTML(API % url)
  return re.findall(re_str, html)
