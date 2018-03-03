# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505982992.057555
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/wikipagerevisions.html'
_template_uri = '/wikipagerevisions.html'
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
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(conditional_websafe(thing.listing))
        __M_writer(u'\n')
        # SOURCE LINE 24
        if thing.page and thing.listing.things:
            # SOURCE LINE 25
            __M_writer(u'    <button onclick="r.wiki.goCompare()">')
            __M_writer(conditional_websafe(_("compare selected")))
            __M_writer(u'</button>\n')
        # SOURCE LINE 27
        __M_writer(u'<br/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


