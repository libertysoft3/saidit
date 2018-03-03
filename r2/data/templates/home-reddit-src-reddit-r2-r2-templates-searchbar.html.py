# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505003389.794396
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/searchbar.html'
_template_uri = '/searchbar.html'
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
        if thing.prev_search and thing.converted_data:
            # SOURCE LINE 24
            __M_writer(u'  <div class="search-summary">\n    <div>\n    <p class="debuginfo">\n      <span class="icon">&delta;</span>&nbsp;\n      <span class="content">')
            # SOURCE LINE 28
            __M_writer(conditional_websafe(_('converted query to %(syntax)s syntax: %(converted)s') % thing.converted_data))
            __M_writer(u'</span>\n    </p>\n    </div>\n  </div>\n')
        # SOURCE LINE 33
        __M_writer(u'\n<div class="searchpane raisedbox">\n  <h4 style="color:gray">')
        # SOURCE LINE 35
        __M_writer(conditional_websafe(thing.header))
        __M_writer(u'</h4>\n\n  <div id="previoussearch">\n    ')
        # SOURCE LINE 38
        __M_writer(conditional_websafe(thing.search_form))
        __M_writer(u'\n  </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


