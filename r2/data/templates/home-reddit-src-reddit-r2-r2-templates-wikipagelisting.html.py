# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1506018929.666098
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/wikipagelisting.html'
_template_uri = '/wikipagelisting.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['listing']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        thing = context.get('thing', UNDEFINED)
        def listing(pages):
            return render_listing(context._locals(__M_locals),pages)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        from r2.models.wiki import WikiPage 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['WikiPage'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')
        # SOURCE LINE 38
        __M_writer(u'\n\n<div class="pagelisting">\n')
        # SOURCE LINE 41
        __M_writer(conditional_websafe(listing(thing.pages)))
        __M_writer(u'\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_listing(context,pages):
    __M_caller = context.caller_stack._push_frame()
    try:
        def listing(pages):
            return render_listing(context,pages)
        __M_writer = context.writer()
        # SOURCE LINE 25
        __M_writer(u'\n')
        # SOURCE LINE 26
        for name, page_info in pages.iteritems():
            # SOURCE LINE 27
            __M_writer(u'        <ul>\n        <li>\n')
            # SOURCE LINE 29
            if page_info[0]:
                # SOURCE LINE 30
                __M_writer(u'            <a href="')
                __M_writer(conditional_websafe(c.wiki_base_url))
                __M_writer(u'/')
                __M_writer(conditional_websafe(page_info[0].name))
                __M_writer(u'" target="_blank">')
                __M_writer(conditional_websafe(name))
                __M_writer(u'</a></li>\n')
                # SOURCE LINE 31
            else:
                # SOURCE LINE 32
                __M_writer(u'            ')
                __M_writer(conditional_websafe(name))
                __M_writer(u'\n        </li>\n')
            # SOURCE LINE 35
            __M_writer(u'        ')
            __M_writer(conditional_websafe(listing(page_info[1])))
            __M_writer(u'\n        </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


