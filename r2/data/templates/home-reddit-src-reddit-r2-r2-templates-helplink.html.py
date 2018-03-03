# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1520060829.538466
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/helplink.html'
_template_uri = '/helplink.html'
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
    ns = runtime.TemplateNamespace('__anon_0x7fc7c782ce10', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fc7c782ce10')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c782ce10')._populate(_import_ns, [u'data'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        data = _import_ns.get('data', context.get('data', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n<a class="helplink ')
        # SOURCE LINE 25
        __M_writer(conditional_websafe('access-required' if thing.access_required else ''))
        __M_writer(u'"\n   href="')
        # SOURCE LINE 26
        __M_writer(conditional_websafe(thing.url))
        __M_writer(u'"\n   ')
        # SOURCE LINE 27
        __M_writer(conditional_websafe(data(**thing.data_attrs)))
        __M_writer(u'\n>\n  ')
        # SOURCE LINE 29
        __M_writer(conditional_websafe(thing.label))
        __M_writer(u'\n</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


