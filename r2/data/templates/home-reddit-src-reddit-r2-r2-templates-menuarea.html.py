# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505003484.69242
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/menuarea.html'
_template_uri = '/menuarea.html'
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
        __M_writer(u'\n<div class="menuarea">\n')
        # SOURCE LINE 24
        for menu in thing.menus:
            # SOURCE LINE 25
            __M_writer(u'    <div class="spacer">\n      ')
            # SOURCE LINE 26
            __M_writer(conditional_websafe(menu))
            __M_writer(u'\n    </div>\n')
        # SOURCE LINE 29
        __M_writer(u'</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


