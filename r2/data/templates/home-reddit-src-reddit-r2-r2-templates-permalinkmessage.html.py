# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505278889.178917
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/permalinkmessage.html'
_template_uri = '/permalinkmessage.html'
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
        __M_writer(u'\n<div class="infobar">\n    ')
        # SOURCE LINE 24
        __M_writer(conditional_websafe(_("you are viewing a single comment's thread.")))
        __M_writer(u'\n    <p>\n      <a href="')
        # SOURCE LINE 26
        __M_writer(conditional_websafe(thing.comments_url))
        __M_writer(u'">')
        __M_writer(conditional_websafe(_("view the rest of the comments")))
        __M_writer(u'</a>\n        &nbsp;&#8594;\n    </p>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


