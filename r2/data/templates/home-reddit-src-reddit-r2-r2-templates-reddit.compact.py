# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1508303897.751785
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/reddit.compact'
_template_uri = '/reddit.compact'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['bodyContent']


# SOURCE LINE 23

from r2.lib import tracking
 

def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 27
    ns = runtime.TemplateNamespace('__anon_0x7f4de7b88f10', context._clean_inheritance_tokens(), templateuri=u'login.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f4de7b88f10')] = ns

    # SOURCE LINE 28
    ns = runtime.TemplateNamespace('__anon_0x7f4de7b88110', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f4de7b88110')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.compact', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f4de7b88f10')._populate(_import_ns, [u'login_form'])
        _mako_get_namespace(context, '__anon_0x7f4de7b88110')._populate(_import_ns, [u'tags'])
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'\n')
        # SOURCE LINE 26
        __M_writer(u'\n')
        # SOURCE LINE 27
        __M_writer(u'\n')
        # SOURCE LINE 28
        __M_writer(u'\n\n')
        # SOURCE LINE 40
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bodyContent(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f4de7b88f10')._populate(_import_ns, [u'login_form'])
        _mako_get_namespace(context, '__anon_0x7f4de7b88110')._populate(_import_ns, [u'tags'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 30
        __M_writer(u'\n  ')
        # SOURCE LINE 31
        runtime._include_file(context, u'redditheader.compact', _template_uri)
        __M_writer(u'\n')
        # SOURCE LINE 32
        if thing.content:
            # SOURCE LINE 33
            __M_writer(u'    <div class="content">\n      ')
            # SOURCE LINE 34
            __M_writer(conditional_websafe(thing.content()))
            __M_writer(u'\n    </div>\n')
        # SOURCE LINE 37
        if g.tracker_url and thing.site_tracking and not c.secure:
            # SOURCE LINE 38
            __M_writer(u'    <img alt="" src="')
            __M_writer(conditional_websafe(tracking.get_pageview_pixel_url()))
            __M_writer(u'"/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


