# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Eric Van Steenbergen'
SITENAME = u'Eric V. Braindumps'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Manila'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('A world without Linux', 'http://www.linuxfoundation.org/world-without-linux'),)

# Social widget
SOCIAL = (('LinkedIn profile', 'https://www.linkedin.com/in/ericvansteenbergen'),
          ('GitHub Page', 'http://ericvs.github.io'),)

DEFAULT_PAGINATION = 10

THEME = "/Users/ericvs/.virtualenvs/pelican/lib/python2.7/site-packages/pelican/themes/bootstrap2-dark"

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
