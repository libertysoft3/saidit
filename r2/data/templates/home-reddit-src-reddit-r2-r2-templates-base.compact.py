# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1508303897.762454
_enable_loop = True
_template_filename = u'/home/reddit/src/reddit/r2/r2/templates/base.compact'
_template_uri = u'/base.compact'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['bodyContent', 'robots', 'Title']


# SOURCE LINE 24

from r2.lib.template_helpers import static
from r2.lib import js


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 28
    ns = runtime.TemplateNamespace('__anon_0x7f4de7b88e90', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f4de7b88e90')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f4de7b88e90')._populate(_import_ns, [u'js_setup', u'googleanalytics', u'classes'])
        googleanalytics = _import_ns.get('googleanalytics', context.get('googleanalytics', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        classes = _import_ns.get('classes', context.get('classes', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        js_setup = _import_ns.get('js_setup', context.get('js_setup', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n')
        # SOURCE LINE 27
        __M_writer(u'\n')
        # SOURCE LINE 28
        __M_writer(u'\n<html xmlns="http://www.w3.org/1999/xhtml" lang="')
        # SOURCE LINE 29
        __M_writer(conditional_websafe(c.lang))
        __M_writer(u'">\n  <head>\n    <link rel="apple-touch-icon" \n          href="/static/compact/reddit-apple-mobile-device.png"/>\n    <link rel="apple-touch-startup-image" \n          href="/static/compact/reddit_startimg.png" />\n    <link rel="canonical" href="')
        # SOURCE LINE 35
        __M_writer(conditional_websafe(thing.canonical_link))
        __M_writer(u'" />\n')
        # SOURCE LINE 36
        if hasattr(thing, "shortlink"):
            # SOURCE LINE 37
            __M_writer(u'      <link rel="shorturl" href="https://')
            __M_writer(conditional_websafe(thing.shortlink))
            __M_writer(u'" />\n')
        # SOURCE LINE 39
        __M_writer(u'    <meta name="apple-mobile-web-app-status-bar-style" content="black" />\n    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"/>\n    <title>')
        # SOURCE LINE 41
        __M_writer(conditional_websafe(self.Title()))
        __M_writer(u'</title>\n    <meta name="title" content="')
        # SOURCE LINE 42
        __M_writer(conditional_websafe(self.Title()))
        __M_writer(u'" />\n    <meta name="description" content="')
        # SOURCE LINE 43
        __M_writer(conditional_websafe(thing.short_description or g.short_description))
        __M_writer(u'" />\n    <meta name="referrer" content="')
        # SOURCE LINE 44
        __M_writer(conditional_websafe(c.referrer_policy))
        __M_writer(u'" />\n    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\n    ')
        # SOURCE LINE 46
        __M_writer(conditional_websafe(self.robots()))
        __M_writer(u'\n    <link rel="stylesheet" href="')
        # SOURCE LINE 47
        __M_writer(conditional_websafe(static('compact.css')))
        __M_writer(u'" type="text/css" media="screen" />\n\n    <!--[if gte IE 9]> <!-->\n      ')
        # SOURCE LINE 50
        __M_writer(conditional_websafe(unsafe(js.use('reddit-init'))))
        __M_writer(u'\n    <!-- <![endif]-->\n\n    <!--[if lt IE 9]>\n      ')
        # SOURCE LINE 54
        __M_writer(conditional_websafe(unsafe(js.use('reddit-init-legacy'))))
        __M_writer(u'\n    <![endif]-->\n\n    ')
        # SOURCE LINE 57
        __M_writer(conditional_websafe(js_setup(thing.extra_js_config)))
        __M_writer(u'\n    ')
        # SOURCE LINE 58
        __M_writer(conditional_websafe(googleanalytics('mobile')))
        __M_writer(u'\n  </head>\n  <body ')
        # SOURCE LINE 60
        __M_writer(conditional_websafe(classes(*thing.page_classes())))
        __M_writer(u'>\n    ')
        # SOURCE LINE 61
        __M_writer(conditional_websafe(self.bodyContent()))
        __M_writer(u'\n    ')
        # SOURCE LINE 62
        __M_writer(conditional_websafe(unsafe(js.use('mobile'))))
        __M_writer(u'\n  </body>\n</html>\n\n')
        # SOURCE LINE 67
        __M_writer(u'\n\n')
        # SOURCE LINE 71
        __M_writer(u'\n\n')
        # SOURCE LINE 77
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bodyContent(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f4de7b88e90')._populate(_import_ns, [u'js_setup', u'googleanalytics', u'classes'])
        __M_writer = context.writer()
        # SOURCE LINE 66
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_robots(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f4de7b88e90')._populate(_import_ns, [u'js_setup', u'googleanalytics', u'classes'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 73
        __M_writer(u'\n')
        # SOURCE LINE 74
        if hasattr(thing, 'robots') and thing.robots:
            # SOURCE LINE 75
            __M_writer(u'     <meta name="robots" content="')
            __M_writer(conditional_websafe(thing.robots))
            __M_writer(u'" />\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_Title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f4de7b88e90')._populate(_import_ns, [u'js_setup', u'googleanalytics', u'classes'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 69
        __M_writer(u'\n')
        # SOURCE LINE 70
        __M_writer(conditional_websafe(thing.title))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


