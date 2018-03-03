# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505025467.392562
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/subredditfacets.html'
_template_uri = '/subredditfacets.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23

from r2.lib.template_helpers import search_url


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        thing = context.get('thing', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'\n\n')
        # SOURCE LINE 27
        if thing.facets and len(thing.facets) > 1:
            # SOURCE LINE 28
            __M_writer(u'<div class="searchfacets">\n  <h4 class="title">')
            # SOURCE LINE 29
            __M_writer(conditional_websafe(_("too many results? narrow it down to a subreddit!")))
            __M_writer(u'</h4>\n  <ol class="list">\n')
            # SOURCE LINE 31
            for subreddit, count in thing.facets:
                # SOURCE LINE 32
                __M_writer(u'    <li class="searchfacet reddit">\n      <a class="facet title word" href="')
                # SOURCE LINE 33
                __M_writer(conditional_websafe(search_url(thing.prev_search, subreddit.name, restrict_sr='on', sort=thing.sort, recent=thing.recent, ref='search_facets')))
                __M_writer(u'">/r/')
                __M_writer(conditional_websafe(subreddit.name))
                __M_writer(u'</a>&nbsp;\n      <span class="facet count number">(')
                # SOURCE LINE 34
                __M_writer(conditional_websafe(count))
                __M_writer(u')</span>\n    </li>&nbsp;\n')
            # SOURCE LINE 37
            __M_writer(u'  </ol>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


