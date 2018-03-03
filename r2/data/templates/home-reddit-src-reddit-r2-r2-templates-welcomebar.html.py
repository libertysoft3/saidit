# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505007497.804299
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/welcomebar.html'
_template_uri = '/welcomebar.html'
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
        __M_writer(u'\n<div class="infobar welcome">\n  <h1>')
        # SOURCE LINE 24
        __M_writer(conditional_websafe(thing.message[0]))
        __M_writer(u'</h1>\n  <div class="button-row">\n    <h2>')
        # SOURCE LINE 26
        __M_writer(conditional_websafe(thing.message[1]))
        __M_writer(u'</h2>\n    <a href="/about">')
        # SOURCE LINE 27
        __M_writer(conditional_websafe(_("learn more")))
        __M_writer(u' &rsaquo;</a>\n  </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


