# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1508300012.186135
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/verifyemail.email'
_template_uri = '/verifyemail.email'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        thing = context.get('thing', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\nyour username is:\n\n    ')
        # SOURCE LINE 25
        __M_writer(conditional_websafe(thing.user.name))
        __M_writer(u'\n\nvisit this link to verify your email address:\n\n    ')
        # SOURCE LINE 29
        __M_writer(conditional_websafe(thing.emaillink))
        __M_writer(u'\n\nthanks for using the site!\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


