#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'SS'
SITENAME = u'Networked Systems'
SITEURL = 'http://localhost:8000'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

USE_FOLDER_AS_CATEGORY = True

# Plugins
PLUGIN_PATH = '../pelican-plugins'
PLUGINS = ['tipue_search']


# Theme
THEME = '../my_theme/pelican-elegant'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('All Things Distributed', 'http://www.allthingsdistributed.com'),
          ('Network Static', 'http://networkstatic.net'),
          ('High Scalability', 'http://highscalability.com'),
          ('Scaling Systems', 'http://scalingsystems.com'),
	  ('Network Heresy', 'http://networkheresy.com'),
          ('Ethereal Mind', 'http://etherealmind.com'),
          ('Perspectives', 'http://perspectives.mvdirona.com'),
          ('The Paper Trail', 'http://the-paper-trail.org'),
          ('Brain Food for Hackers', 'http://duartes.org/gustavo/blog/'),
          ('Some really good blogs', 'http://highscalability.com/blog/category/blog'))

# Social widget
SOCIAL = (('GitHub', 'https://github.com/essessv'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
