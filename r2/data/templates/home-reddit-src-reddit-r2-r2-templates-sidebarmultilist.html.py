# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1508369596.203763
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/sidebarmultilist.html'
_template_uri = '/sidebarmultilist.html'
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
        __M_writer(u'\n<ul id="side-multi-list">\n')
        # SOURCE LINE 24
        for multi in thing.multis:
            # SOURCE LINE 25
            __M_writer(u'  <li><a href="')
            __M_writer(conditional_websafe(multi.path))
            __M_writer(u'" title="')
            __M_writer(conditional_websafe(multi.name))
            __M_writer(u'">')
            __M_writer(conditional_websafe(multi.name))
            __M_writer(u'</a></li>\n')
        # SOURCE LINE 27
        __M_writer(u"</ul>\n\n<script>new r.ui.Summarize($('#side-multi-list'), 15)</script>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


