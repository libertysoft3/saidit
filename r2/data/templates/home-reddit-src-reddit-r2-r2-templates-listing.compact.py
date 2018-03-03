# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1508303897.841914
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/listing.compact'
_template_uri = '/listing.compact'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7f4de7b88810', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f4de7b88810')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f4de7b88810')._populate(_import_ns, [u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n')
        # SOURCE LINE 25

        _id = ("_%s" % thing.parent_name) if hasattr(thing, 'parent_name') else ''
        cls = thing.lookups[0].__class__.__name__.lower()
         
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['_id','cls'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 28
        __M_writer(u'\n<div id="siteTable')
        # SOURCE LINE 29
        __M_writer(conditional_websafe(_id))
        __M_writer(u'" class="sitetable ')
        __M_writer(conditional_websafe(cls))
        __M_writer(u'">\n')
        # SOURCE LINE 30
        for a in thing.things:
            # SOURCE LINE 31
            __M_writer(u'      ')
            __M_writer(conditional_websafe(a))
            __M_writer(u'\n')
        # SOURCE LINE 33
        __M_writer(u'</div>\n\n')
        # SOURCE LINE 35
        if thing.nextprev and thing.next:
            # SOURCE LINE 36
            __M_writer(u'<script type="text/javascript">\n$($(window).scroll(function(){\n            var loading = $(".loading").length;\n            if (!loading && $(window).scrollTop() > \n              0.8*( $(document).height() - window.innerHeight) ){\n                fetch_more();\n                } \n            }))\n</script>\n')
        # SOURCE LINE 46
        __M_writer(u'\n')
        # SOURCE LINE 47
        if not thing.things:
            # SOURCE LINE 48
            __M_writer(u'  <p id="noresults" class="error">')
            __M_writer(conditional_websafe(_("there doesn't seem to be anything here")))
            __M_writer(u'</p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


