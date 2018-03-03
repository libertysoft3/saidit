# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505799566.456359
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/subreddittraffic.html'
_template_uri = '/subreddittraffic.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['preamble']


# SOURCE LINE 27

from r2.lib.filters import safemarkdown
from r2.lib.strings import strings


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 25
    ns = runtime.TemplateNamespace('__anon_0x7ff76ed1c590', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7ff76ed1c590')] = ns

    # SOURCE LINE 24
    ns = runtime.TemplateNamespace('__anon_0x7ff76ed1c790', context._clean_inheritance_tokens(), templateuri=u'reddittraffic.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7ff76ed1c790')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'reddittraffic.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7ff76ed1c590')._populate(_import_ns, [u'_md'])
        _mako_get_namespace(context, '__anon_0x7ff76ed1c790')._populate(_import_ns, [u'load_timeseries_js'])
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n')
        # SOURCE LINE 24
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'\n\n')
        # SOURCE LINE 30
        __M_writer(u'\n\n')
        # SOURCE LINE 37
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_preamble(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7ff76ed1c590')._populate(_import_ns, [u'_md'])
        _mako_get_namespace(context, '__anon_0x7ff76ed1c790')._populate(_import_ns, [u'load_timeseries_js'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        load_timeseries_js = _import_ns.get('load_timeseries_js', context.get('load_timeseries_js', UNDEFINED))
        _md = _import_ns.get('_md', context.get('_md', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 32
        __M_writer(u'\n  ')
        # SOURCE LINE 33
        __M_writer(conditional_websafe(unsafe(safemarkdown(strings.traffic_subreddit_explanation % dict(subreddit=thing.place)))))
        __M_writer(u'\n  <p>')
        # SOURCE LINE 34
        __M_writer(conditional_websafe(_md("All times are in [UTC](http://en.wikipedia.org/wiki/UTC).", wrap=True)))
        __M_writer(u'</p>\n\n  ')
        # SOURCE LINE 36
        __M_writer(conditional_websafe(load_timeseries_js()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


