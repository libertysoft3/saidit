# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1520060829.036713
_enable_loop = True
_template_filename = u'/home/reddit/src/reddit/r2/r2/templates/base.html'
_template_uri = u'/base.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['head', 'javascript_bottom', 'Title', 'javascript', 'robots', 'keywords', 'stylesheet', 'bodyContent', 'pagemeta', 'viewport']


# SOURCE LINE 24

from r2.lib.template_helpers import static
from r2.models import Link, Comment, Subreddit
from r2.lib import tracking


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 29
    ns = runtime.TemplateNamespace('__anon_0x7fc7c78e2710', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fc7c78e2710')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c78e2710')._populate(_import_ns, [u'js_setup', u'googleanalytics', u'googletagmanager', u'classes'])
        googletagmanager = _import_ns.get('googletagmanager', context.get('googletagmanager', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        classes = _import_ns.get('classes', context.get('classes', UNDEFINED))
        js_setup = _import_ns.get('js_setup', context.get('js_setup', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n<!doctype html>\n')
        # SOURCE LINE 28
        __M_writer(u'\n')
        # SOURCE LINE 29
        __M_writer(u'\n<html xmlns="http://www.w3.org/1999/xhtml" lang="')
        # SOURCE LINE 30
        __M_writer(conditional_websafe(c.lang))
        __M_writer(u'"\n      xml:lang="')
        # SOURCE LINE 31
        __M_writer(conditional_websafe(c.lang))
        __M_writer(u'">\n  <head>\n    <title>')
        # SOURCE LINE 33
        __M_writer(conditional_websafe(self.Title()))
        __M_writer(u'</title>\n    <meta name="keywords" content="')
        # SOURCE LINE 34
        __M_writer(conditional_websafe(self.keywords()))
        __M_writer(u'" />\n    <meta name="description" content="')
        # SOURCE LINE 35
        __M_writer(conditional_websafe(getattr(thing, 'short_description', None) or g.short_description))
        __M_writer(u'" />\n    <meta name="referrer" content="')
        # SOURCE LINE 36
        __M_writer(conditional_websafe(c.referrer_policy))
        __M_writer(u'">\n    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\n    <link type="application/opensearchdescription+xml" rel="search" href="/static/opensearch.xml"/>\n    <link rel="canonical" href="')
        # SOURCE LINE 39
        __M_writer(conditional_websafe(thing.canonical_link))
        __M_writer(u'" />\n    ')
        # SOURCE LINE 40
        __M_writer(conditional_websafe(self.viewport()))
        __M_writer(u'\n    ')
        # SOURCE LINE 41
        __M_writer(conditional_websafe(self.robots()))
        __M_writer(u'\n    ')
        # SOURCE LINE 42
        __M_writer(conditional_websafe(self.pagemeta()))
        __M_writer(u'\n    ')
        # SOURCE LINE 43
        __M_writer(conditional_websafe(self.stylesheet()))
        __M_writer(u'\n    ')
        # SOURCE LINE 44
        __M_writer(conditional_websafe(self.javascript()))
        __M_writer(u'\n    ')
        # SOURCE LINE 45
        __M_writer(conditional_websafe(js_setup(getattr(thing, "extra_js_config", None))))
        __M_writer(u'\n\n')
        # SOURCE LINE 48
        __M_writer(u'    <style type="text/css">\n')
        # SOURCE LINE 52
        __M_writer(u'      ')
        __M_writer(conditional_websafe(unsafe(_("/* Custom css: use this block to insert special translation-dependent css in the page header */").replace("</", ""))))
        __M_writer(u'\n    </style>\n\n    ')
        # SOURCE LINE 55
        __M_writer(conditional_websafe(self.head()))
        __M_writer(u'\n  </head>\n\n  <body ')
        # SOURCE LINE 58
        __M_writer(conditional_websafe(classes(*thing.page_classes())))
        __M_writer(u'>\n    ')
        # SOURCE LINE 59
        __M_writer(conditional_websafe(googletagmanager()))
        __M_writer(u'\n    ')
        # SOURCE LINE 60
        __M_writer(conditional_websafe(self.bodyContent()))
        __M_writer(u'\n    ')
        # SOURCE LINE 61
        __M_writer(conditional_websafe(self.javascript_bottom()))
        __M_writer(u'\n  </body>\n</html>\n\n')
        # SOURCE LINE 66
        __M_writer(u'\n\n')
        # SOURCE LINE 70
        __M_writer(u'\n\n')
        # SOURCE LINE 75
        __M_writer(u'\n\n')
        # SOURCE LINE 79
        __M_writer(u'\n\n')
        # SOURCE LINE 85
        __M_writer(u'\n\n')
        # SOURCE LINE 89
        __M_writer(u'\n\n')
        # SOURCE LINE 92
        __M_writer(u'\n\n')
        # SOURCE LINE 95
        __M_writer(u'\n\n')
        # SOURCE LINE 98
        __M_writer(u'\n\n')
        # SOURCE LINE 101
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c78e2710')._populate(_import_ns, [u'js_setup', u'googleanalytics', u'googletagmanager', u'classes'])
        googleanalytics = _import_ns.get('googleanalytics', context.get('googleanalytics', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 87
        __M_writer(u'\n')
        # SOURCE LINE 88
        __M_writer(conditional_websafe(googleanalytics('web', thing.is_gold_page() if hasattr(thing, 'is_gold_page') else False)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascript_bottom(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c78e2710')._populate(_import_ns, [u'js_setup', u'googleanalytics', u'googletagmanager', u'classes'])
        __M_writer = context.writer()
        # SOURCE LINE 100
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_Title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c78e2710')._populate(_import_ns, [u'js_setup', u'googleanalytics', u'googletagmanager', u'classes'])
        __M_writer = context.writer()
        # SOURCE LINE 68
        __M_writer(u'\n')
        # SOURCE LINE 69
        __M_writer(conditional_websafe(c.site.title))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascript(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c78e2710')._populate(_import_ns, [u'js_setup', u'googleanalytics', u'googletagmanager', u'classes'])
        __M_writer = context.writer()
        # SOURCE LINE 97
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_robots(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c78e2710')._populate(_import_ns, [u'js_setup', u'googleanalytics', u'googletagmanager', u'classes'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 81
        __M_writer(u'\n')
        # SOURCE LINE 82
        if hasattr(thing, 'robots') and thing.robots:
            # SOURCE LINE 83
            __M_writer(u'     <meta name="robots" content="')
            __M_writer(conditional_websafe(thing.robots))
            __M_writer(u'" />\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_keywords(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c78e2710')._populate(_import_ns, [u'js_setup', u'googleanalytics', u'googletagmanager', u'classes'])
        __M_writer = context.writer()
        # SOURCE LINE 73
        __M_writer(u'\nantiextremes, anti extremes, antiextremes.com, saidit, saidit.net, said it, vote, voting, comment, reddit, reddit replacement, new reddit, besides reddit, other than reddit, other reddit, saiditnet, anonymous, anonymous social media, comments, links, social media, posts, submit links\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheet(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c78e2710')._populate(_import_ns, [u'js_setup', u'googleanalytics', u'googletagmanager', u'classes'])
        __M_writer = context.writer()
        # SOURCE LINE 94
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bodyContent(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c78e2710')._populate(_import_ns, [u'js_setup', u'googleanalytics', u'googletagmanager', u'classes'])
        __M_writer = context.writer()
        # SOURCE LINE 65
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_pagemeta(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c78e2710')._populate(_import_ns, [u'js_setup', u'googleanalytics', u'googletagmanager', u'classes'])
        __M_writer = context.writer()
        # SOURCE LINE 91
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_viewport(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c78e2710')._populate(_import_ns, [u'js_setup', u'googleanalytics', u'googletagmanager', u'classes'])
        __M_writer = context.writer()
        # SOURCE LINE 77
        __M_writer(u'\n<meta name="viewport" content="width=1024">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


