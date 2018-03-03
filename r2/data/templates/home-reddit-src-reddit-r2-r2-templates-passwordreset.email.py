# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1508399854.599322
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/passwordreset.email'
_template_uri = '/passwordreset.email'
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
        __M_writer(u'\na password reset has been requested for the reddit username: ')
        # SOURCE LINE 23
        __M_writer(conditional_websafe(thing.user.name))
        __M_writer(u'\n\nif you did not make this request, you can safely ignore this email. a password reset request can be made by anyone, and it does not indicate that your account is in any danger of being accessed by someone else.\n\nif you do actually want to reset your password, visit this link:\n\n    ')
        # SOURCE LINE 29
        __M_writer(conditional_websafe(thing.passlink))
        __M_writer(u'\n\nthanks for using the site!\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


