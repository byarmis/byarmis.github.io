#!/usr/bin/env python
from datetime import datetime

AUTHOR = 'Ben Yarmis'
SITENAME = 'BLOG'
SITESUBTITLE = 'By Ben Yarmis'
SITEURL = ''
THEME = './pelican-simplegrey/'

CURRENT_YEAR = datetime.now().year

STATIC_PATHS = [
        'extra'
        , 'images'
        , 'pdfs'
      ]

EXTRA_PATH_METADATA = {
          'extra/favicon.ico': {'path': 'favicon.ico'}
        , 'extra/robots.txt': {'path':'robots.txt'}
        }

PATH = 'content'
CV_PATH = 'pdfs/YarmisResume.pdf'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['render_math']
MATH_JAX = {
        'tex_extensions' : ['AMSmath.js', 'color.js']
        }

TIMEZONE = 'US/Central'
DEFAULT_DATE_FORMAT = '%a %B %-d, %Y'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
        ('email me', ('mailto:ben@yarm.is'))
        , ("this site's repo", ('https://gitlab.com/byarmis/byarmis.gitlab.io'))
        )

# Social widget
SOCIAL = (
        ('gitlab', 'https://gitlab.com/byarmis/')
      , ('github', 'https://github.com/byarmis/')
      , ('twitter', 'https://twitter.com/byarmis/')
      , ('linkedin', 'https://www.linkedin.com/in/byarmis/')
         )


DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
