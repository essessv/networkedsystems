#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Site Basic Settings
AUTHOR = u'SS'
SITEURL = 'http://localhost:8000'
SITENAME = u"""<span style="color:#AA1032;">Networked Systems</span>"""
FEATURED_IMAGE = SITEURL + '/theme/images/apple-touch-icon-152x152.png'
DATE_FORMATS = {'en': '%a, %d %b %Y'}
LOCALE = ('en_US')
DEFAULT_LANG = u'en'
TIMEZONE = "US/Pacific"

USE_FOLDER_AS_CATEGORY = True

# Theme
THEME = '../my_theme/pelican-elegant'
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search', '404'))
TYPOGRIFY = True
DEFAULT_PAGINATION = 10
RECENT_ARTICLES_COUNT = 10
# Plugins
MD_EXTENSIONS = ['codehilite(linenums = True)', 'extra', 'headerid', 'toc(permalink=true)']


PLUGIN_PATH = '../pelican-plugins'
PLUGINS = ['code_include', 'summary', 'clean_summary']
PLUGINS.extend(['tipue_search', 'neighbors', 'related_posts'])
PLUGINS.extend(['share_post', 'multi_part', 'extract_toc'])
PLUGINS.extend(['sitemap', 'assets', 'feed_summary'])
PLUGINS.extend(['pelican_youtube', 'simple_footnotes'])

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

# Summary plugin
CLEAN_SUMMARY_MAXIMUM = 1
CLEAN_SUMMARY_MINIMUM_ONE = True
FEED_USE_SUMMARY = True
RELATED_POSTS_MAX = 10

# Code
#PYGMENTS_RST_OPTIONS = {'classprefix': 'pgcss', 'linenos': 'table'}


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Elegant theme
STATIC_PATHS = ['theme/images', 'images']
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
USE_SHORTCUT_ICONS = True
ARTICLE_URL = u'{slug}'
PAGE_URL = u'{slug}'
PAGE_SAVE_AS = u'{slug}.html'

# Elegant Labels
SOCIAL_PROFILE_LABEL = u'Connect with SS:'
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
SOCIAL = (('GitHub', 'https://github.com/essessv'),
          ('Email', 'mailto:essessv@gmail.com'),
          ('RSS', 'http://networkedsystems.in/feeds/all.atom.xml'),)

# Mailchimp
EMAIL_SUBSCRIPTION_LABEL = u'Get Monthly Updates'
EMAIL_FIELD_PLACEHOLDER = u'Enter your email.'
SUBSCRIBE_BUTTON_TITLE = u'Send me Free updates'
MAILCHIMP_FORM_ACTION = u'empty'


