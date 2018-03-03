# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505025479.248738
_enable_loop = True
_template_filename = u'/home/reddit/src/reddit/r2/r2/templates/searchresultbase.html'
_template_uri = u'/searchresultbase.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['search_result_icon', 'search_result_content', 'search_result_body', 'search_result_css_class', 'search_result_footer', 'search_result_header', 'search_result_meta']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        thing = context.get('thing', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n<div class="')
        # SOURCE LINE 23
        __M_writer(conditional_websafe(self.search_result_css_class()))
        __M_writer(u'" data-fullname="')
        __M_writer(conditional_websafe(thing.fullname))
        __M_writer(u'">\n  ')
        # SOURCE LINE 24
        __M_writer(conditional_websafe(self.search_result_content()))
        __M_writer(u'\n</div>\n\n')
        # SOURCE LINE 32
        __M_writer(u'\n\n')
        # SOURCE LINE 36
        __M_writer(u'\n\n')
        # SOURCE LINE 42
        __M_writer(u'\n\n')
        # SOURCE LINE 48
        __M_writer(u'\n\n')
        # SOURCE LINE 54
        __M_writer(u'\n\n')
        # SOURCE LINE 60
        __M_writer(u'\n\n')
        # SOURCE LINE 64
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_search_result_icon(context,name):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 62
        __M_writer(u'\n  <span class="search-result-icon search-result-icon-')
        # SOURCE LINE 63
        __M_writer(conditional_websafe(name))
        __M_writer(u'"></span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_search_result_content(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 27
        __M_writer(u'\n  ')
        # SOURCE LINE 28
        __M_writer(conditional_websafe(self.search_result_header()))
        __M_writer(u'\n  ')
        # SOURCE LINE 29
        __M_writer(conditional_websafe(self.search_result_meta()))
        __M_writer(u'\n  ')
        # SOURCE LINE 30
        __M_writer(conditional_websafe(self.search_result_body()))
        __M_writer(u'\n  ')
        # SOURCE LINE 31
        __M_writer(conditional_websafe(self.search_result_footer()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_search_result_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        caller = context.get('caller', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 50
        __M_writer(u'\n  <div class="search-result-body">\n    ')
        # SOURCE LINE 52
        __M_writer(conditional_websafe(caller.body()))
        __M_writer(u'\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_search_result_css_class(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 34
        __M_writer(u'\n  search-result\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_search_result_footer(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        caller = context.get('caller', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 56
        __M_writer(u'\n  <div class="search-result-footer">\n    ')
        # SOURCE LINE 58
        __M_writer(conditional_websafe(caller.body()))
        __M_writer(u'\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_search_result_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        caller = context.get('caller', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 38
        __M_writer(u'\n  <header class="search-result-header">\n    ')
        # SOURCE LINE 40
        __M_writer(conditional_websafe(caller.body()))
        __M_writer(u'\n  </header>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_search_result_meta(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        caller = context.get('caller', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 44
        __M_writer(u'\n  <div class="search-result-meta">\n    ')
        # SOURCE LINE 46
        __M_writer(conditional_websafe(caller.body()))
        __M_writer(u'\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


