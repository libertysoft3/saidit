# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1520060829.843861
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/debugfooter.html'
_template_uri = '/debugfooter.html'
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
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n<p class="bottommenu debuginfo"><span class="icon">&pi;</span>&nbsp;<span class="content">Rendered by PID ')
        # SOURCE LINE 23
        __M_writer(conditional_websafe(g.reddit_pid))
        __M_writer(u' on ')
        __M_writer(conditional_websafe(g.reddit_host))
        __M_writer(u' at ')
        __M_writer(conditional_websafe(c.start_time))
        __M_writer(u' running ')
        __M_writer(conditional_websafe(g.short_version))
        __M_writer(u' ')
        __M_writer(conditional_websafe(c.location_info))
        __M_writer(u'.</span></p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


