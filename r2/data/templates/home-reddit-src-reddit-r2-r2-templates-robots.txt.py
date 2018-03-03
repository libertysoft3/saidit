# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505002622.435726
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/robots.txt'
_template_uri = '/robots.txt'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 22

from r2.lib.template_helpers import add_sr


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        thing = context.get('thing', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 24
        __M_writer(u"\n# 80legs\nUser-agent: 008\nDisallow: /\n\n# 80legs' new crawler\nUser-agent: voltron\nDisallow: /\n\nUser-Agent: bender\nDisallow: /my_shiny_metal_ass\n\nUser-Agent: Gort\nDisallow: /earth\n\nUser-Agent: *\nDisallow: /*.json\nDisallow: /*.json-compact\nDisallow: /*.json-html\nDisallow: /*.xml\nDisallow: /*.rss\nDisallow: /*.i\nDisallow: /*.embed\nDisallow: /*/comments/*?*sort=\nDisallow: /r/*/comments/*/*/c*\nDisallow: /comments/*/*/c*\nDisallow: /r/*/submit\nDisallow: /message/compose*\nDisallow: /api\nDisallow: /post\nDisallow: /submit\nDisallow: /goto\nDisallow: /*after=\nDisallow: /*before=\nDisallow: /domain/*t=\nDisallow: /login\nDisallow: /reddits/search\nDisallow: /search\nDisallow: /r/*/search\nAllow: /\n\nSitemap: ")
        # SOURCE LINE 65
        __M_writer(conditional_websafe(thing.subreddit_sitemap))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


