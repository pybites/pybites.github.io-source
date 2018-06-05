#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'pybites'
SITENAME = 'PyBites'
SITETITLE = 'PyBites'
SITESUBTITLE = 'Python Code Challenges, Articles and News - One Bite a Day'
SITEDESCRIPTION = SITESUBTITLE
SITEURL = 'https://pybit.es'
SITELOGO = 'https://pybit.es/theme/img/profile.png'
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

PATH = 'content'
THEME = 'Flex'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

FEED_ALL_RSS = 'feeds/all.rss.xml'  # this is the constant used in flex
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
INDEX_SAVE_AS = 'blog_index.html'

TWITTER_USERNAME = "pybites"
GITHUB_USERNAME = "pybites"

DEFAULT_PAGINATION = 10

ADD_THIS_ID = 'ra-5859c6a67eb6254d'
DISQUS_SITENAME = 'http-pybit-es'
GOOGLE_ANALYTICS = 'UA-89294245-1'

STATIC_PATHS = [
    'images',
    'extra/CNAME',
    'extra/favicon.ico',
]
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
FAVICON = 'favicon.ico'

# using links to have more control over order and naming of navbar items
# it also seems the only way to link to external resources (cc.es), see
# https://appliedcaffeine.org/navbaritems.html
LINKS = (
  ('About', '/pages/about.html'),
  ('Articles', '/pages/articles.html'),
  ('CodeChalleng.es', 'https://codechalleng.es'),
  ('#100DaysOfCode', '/pages/courses.html'),
  ('Python News', '/pages/news.html'),
  ('Search', '/pages/search.html'),
)

# embed jupyter notebooks and post stats
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup', 'post_stats']
IPYNB_USE_META_SUMMARY = True
IGNORE_FILES = ['.ipynb_checkpoints']
