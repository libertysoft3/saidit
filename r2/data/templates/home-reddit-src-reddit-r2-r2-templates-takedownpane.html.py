# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505008089.785571
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/takedownpane.html'
_template_uri = '/takedownpane.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23

from r2.lib.filters import unsafe, safemarkdown, keep_space
from r2.lib.template_helpers import static


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        thing = context.get('thing', UNDEFINED)
        getattr = context.get('getattr', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 26
        __M_writer(u'\n\n<div class="infobar red">\n')
        # SOURCE LINE 29
        if getattr(thing.link, "takedown_img", True):
            # SOURCE LINE 30
            __M_writer(u'  <img src="')
            __M_writer(conditional_websafe(static('gagged-alien.png')))
            __M_writer(u'"/>\n')
            # SOURCE LINE 31
        else:
            # SOURCE LINE 32
            __M_writer(u'  <img src="')
            __M_writer(conditional_websafe(static('noimage.png')))
            __M_writer(u'"/>\n')
        # SOURCE LINE 34
        __M_writer(conditional_websafe(unsafe(safemarkdown(thing.explanation, nofollow=True))))
        __M_writer(u'\n<div class="clearleft"></div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


