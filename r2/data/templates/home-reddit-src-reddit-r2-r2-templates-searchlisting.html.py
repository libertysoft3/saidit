# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505025467.373641
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/searchlisting.html'
_template_uri = '/searchlisting.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23

from r2.lib.template_helpers import format_html
 

def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 27
    ns = runtime.TemplateNamespace('__anon_0x7fb21a697dd0', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fb21a697dd0')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fb21a697dd0')._populate(_import_ns, [u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'\n\n')
        # SOURCE LINE 27
        __M_writer(u'\n\n<div class="listing search-result-listing">\n  <div class="search-result-group">\n')
        # SOURCE LINE 31
        if thing.heading:
            # SOURCE LINE 32
            __M_writer(u'      <header class="search-result-group-header">\n        <span class="search-header-label">')
            # SOURCE LINE 33
            __M_writer(conditional_websafe(thing.heading))
            __M_writer(u'</span>\n')
            # SOURCE LINE 34
            if thing.nav_menus:
                # SOURCE LINE 35
                __M_writer(u'          <div class="search-header-menus">\n')
                # SOURCE LINE 36
                for menu in thing.nav_menus:
                    # SOURCE LINE 37
                    __M_writer(u'              <div class="search-menu">')
                    __M_writer(conditional_websafe(menu))
                    __M_writer(u'</div>\n')
                # SOURCE LINE 39
                __M_writer(u'          </div>\n')
            # SOURCE LINE 41
            __M_writer(u'      </header>\n')
        # SOURCE LINE 43
        __M_writer(u'    <div class="contents">\n')
        # SOURCE LINE 44
        for a in thing.things:
            # SOURCE LINE 45
            __M_writer(u'        ')
            __M_writer(conditional_websafe(a))
            __M_writer(u'\n')
        # SOURCE LINE 47
        __M_writer(u'    </div>\n    <footer>\n')
        # SOURCE LINE 49
        if thing.nextprev and (thing.prev or thing.next):
            # SOURCE LINE 50
            __M_writer(u'        <div class="nav-buttons">\n          <span class="nextprev">')
            # SOURCE LINE 51
            __M_writer(conditional_websafe(_("view more:")))
            __M_writer(u'&#32;\n')
            # SOURCE LINE 52
            if thing.prev:
                # SOURCE LINE 53
                __M_writer(u'            ')
                __M_writer(conditional_websafe(plain_link(format_html("&lsaquo; %s", _("prev")), thing.prev, rel="nofollow prev")))
                __M_writer(u'\n')
            # SOURCE LINE 55
            if thing.prev and thing.next:
                # SOURCE LINE 56
                __M_writer(u'            <span class="separator"></span>\n')
            # SOURCE LINE 58
            if thing.next:
                # SOURCE LINE 59
                __M_writer(u'            ')
                __M_writer(conditional_websafe(plain_link(format_html("%s &rsaquo;", _("next")), thing.next, rel="nofollow next")))
                __M_writer(u'\n')
            # SOURCE LINE 61
            __M_writer(u'          </span>\n')
            # SOURCE LINE 62
            if thing.next_suggestions:
                # SOURCE LINE 63
                __M_writer(u'            ')
                __M_writer(conditional_websafe(thing.next_suggestions))
                __M_writer(u'\n')
            # SOURCE LINE 65
            __M_writer(u'        </div>\n')
        # SOURCE LINE 67
        if not thing.things:
            # SOURCE LINE 68
            __M_writer(u'        <p class="info">')
            __M_writer(conditional_websafe(_("there doesn't seem to be anything here")))
            __M_writer(u'</p>\n')
        # SOURCE LINE 70
        __M_writer(u'    </footer>\n  </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


