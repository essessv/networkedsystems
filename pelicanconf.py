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
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid',
                'toc(permalink=true)']
PLUGIN_PATH = '../pelican-plugins'
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search', 'liquid_tags.img',
           'neighbors', 'latex', 'related_posts', 'share_post',
           'multi_part']
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Theme
THEME = '../my_theme/pelican-elegant'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Elegant theme
STATIC_PATHS = ['theme/images', 'images']
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search', '404'))
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
USE_SHORTCUT_ICONS = True

# Elegant Labels
SOCIAL_PROFILE_LABEL = u'Stay in Touch'
RELATED_POSTS_LABEL = 'Keep Reading'
SHARE_POST_INTRO = 'Like this post? Share on:'
COMMENTS_INTRO = u'So what do you think? Please leave your comments below.'

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
