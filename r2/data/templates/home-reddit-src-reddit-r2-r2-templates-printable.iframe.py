# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1511947254.220483
_enable_loop = True
_template_filename = u'/home/reddit/src/reddit/r2/r2/templates/printable.iframe'
_template_uri = u'/printable.iframe'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['entry', 'parent', 'Child']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(conditional_websafe(self.parent()))
        __M_writer(u'\n')
        # SOURCE LINE 24
        __M_writer(conditional_websafe(self.entry()))
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(conditional_websafe(self.Child()))
        __M_writer(u'\n\n\n')
        # SOURCE LINE 29
        __M_writer(u'\n\n')
        # SOURCE LINE 32
        __M_writer(u'\n\n')
        # SOURCE LINE 36
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_entry(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 31
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_parent(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 28
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_Child(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        thing = context.get('thing', UNDEFINED)
        getattr = context.get('getattr', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 34
        __M_writer(u'\n  ')
        # SOURCE LINE 35
        __M_writer(conditional_websafe(getattr(thing, "child", "")))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


