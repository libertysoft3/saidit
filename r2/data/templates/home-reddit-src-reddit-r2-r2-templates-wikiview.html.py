# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505982964.664234
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/wikiview.html'
_template_uri = '/wikiview.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 25

from r2.lib.pages import WrappedUser
from r2.lib.filters import SC_OFF, SC_ON
from r2.lib.template_helpers import _wsf


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7f20bc6b0490', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f20bc6b0490')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f20bc6b0490')._populate(_import_ns, [u'timestamp'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        timestamp = _import_ns.get('timestamp', context.get('timestamp', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n')
        # SOURCE LINE 29
        __M_writer(u'\n\n')
        # SOURCE LINE 31
        if thing.diff:
            # SOURCE LINE 32
            __M_writer(u'    <p>\n        ')
            # SOURCE LINE 33
            __M_writer(conditional_websafe(unsafe(thing.diff)))
            __M_writer(u'\n    </p>\n')
        # SOURCE LINE 36
        __M_writer(u'<p>\n')
        # SOURCE LINE 37
        if not thing.page_content_md:
            # SOURCE LINE 38
            __M_writer(u'        <em>')
            __M_writer(conditional_websafe(_("this page is empty")))
            __M_writer(u'</em>\n')
            # SOURCE LINE 39
        else:
            # SOURCE LINE 40
            __M_writer(u'        ')
            __M_writer(conditional_websafe(unsafe(thing.page_content)))
            __M_writer(u'\n')
        # SOURCE LINE 42
        __M_writer(u'    ')
        __M_writer(conditional_websafe(unsafe(SC_OFF)))
        __M_writer(u'\n    <textarea readonly class="source" rows="20" cols="20">')
        # SOURCE LINE 43
        __M_writer(conditional_websafe(thing.page_content_md))
        __M_writer(u'</textarea>\n    ')
        # SOURCE LINE 44
        __M_writer(conditional_websafe(unsafe(SC_ON)))
        __M_writer(u'\n</p>\n<hr/>\n<em>\n')
        # SOURCE LINE 48
        if thing.edit_date:
            # SOURCE LINE 49
            if thing.edit_by:
                # SOURCE LINE 50
                __M_writer(u'         ')
                __M_writer(conditional_websafe(_wsf("revision by %(user)s", user=WrappedUser(thing.edit_by))))
                __M_writer(u'\n         &mdash;&nbsp;\n')
            # SOURCE LINE 53
            __M_writer(u'    ')
            __M_writer(conditional_websafe(timestamp(thing.edit_date, include_tense=True)))
            __M_writer(u'\n')
        # SOURCE LINE 55
        __M_writer(u'<a href="#" class="toggle-source">')
        __M_writer(conditional_websafe(_("view source")))
        __M_writer(u'</a>\n</em>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


