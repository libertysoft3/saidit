# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505799486.363361
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/tablelisting.html'
_template_uri = '/tablelisting.html'
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
    # SOURCE LINE 26
    ns = runtime.TemplateNamespace('__anon_0x7ff76fc3a550', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7ff76fc3a550')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7ff76fc3a550')._populate(_import_ns, [u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'\n')
        # SOURCE LINE 26
        __M_writer(u'\n\n')
        # SOURCE LINE 28

        _id = ("_%s" % thing.parent_name) if hasattr(thing, 'parent_name') else ''
        cls = thing.lookups[0].__class__.__name__.lower()
         
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['_id','cls'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 31
        __M_writer(u'\n\n<style type="text/css">\n  .generic-table {\n    font-size: small;\n    color: black;\n    margin-left: 5px;}\n</style>\n\n<div id="siteTable')
        # SOURCE LINE 40
        __M_writer(conditional_websafe(_id))
        __M_writer(u'" class="sitetable ')
        __M_writer(conditional_websafe(cls))
        __M_writer(u'">\n  <table class="generic-table">\n')
        # SOURCE LINE 42
        for a in thing.things:
            # SOURCE LINE 43
            __M_writer(u'      ')
            __M_writer(conditional_websafe(a))
            __M_writer(u'\n')
        # SOURCE LINE 45
        __M_writer(u'  </table>\n</div>\n\n')
        # SOURCE LINE 48
        if thing.nextprev and (thing.prev or thing.next):
            # SOURCE LINE 49
            __M_writer(u'  <p class="nextprev"> ')
            __M_writer(conditional_websafe(_("view more:")))
            __M_writer(u'&#32;\n')
            # SOURCE LINE 50
            if thing.prev:
                # SOURCE LINE 51
                __M_writer(u'    ')
                __M_writer(conditional_websafe(plain_link(_("first"), thing.first, rel="nofollow first")))
                __M_writer(u'\n    <span class="separator"></span>\n    ')
                # SOURCE LINE 53
                __M_writer(conditional_websafe(plain_link(format_html("&lsaquo; %s", _("prev")), thing.prev, rel="nofollow prev")))
                __M_writer(u'\n')
            # SOURCE LINE 55
            if thing.prev and thing.next:
                # SOURCE LINE 56
                __M_writer(u'    <span class="separator"></span>\n')
            # SOURCE LINE 58
            if thing.next:
                # SOURCE LINE 59
                __M_writer(u'  ')
                __M_writer(conditional_websafe(plain_link(format_html("%s &rsaquo;", _("next")), thing.next, rel="nofollow next")))
                __M_writer(u'\n')
            # SOURCE LINE 61
            __M_writer(u'  </p>\n')
        # SOURCE LINE 63
        if not thing.things:
            # SOURCE LINE 64
            __M_writer(u'  <p id="noresults" class="error">')
            __M_writer(conditional_websafe(_("there doesn't seem to be anything here")))
            __M_writer(u'</p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


