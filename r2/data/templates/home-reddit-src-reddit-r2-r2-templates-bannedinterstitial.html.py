# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1508452693.288041
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/bannedinterstitial.html'
_template_uri = '/bannedinterstitial.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['interstitial_image_attrs', 'interstitial_message', 'interstitial_title']


# SOURCE LINE 23

from r2.lib.template_helpers import _wsf, static


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 27
    ns = runtime.TemplateNamespace('__anon_0x7f7227efaa10', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f7227efaa10')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'interstitial.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f7227efaa10')._populate(_import_ns, [u'_md', u'buffered_timestamp'])
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'\n\n')
        # SOURCE LINE 27
        __M_writer(u'\n\n')
        # SOURCE LINE 29
        __M_writer(u'\n\n')
        # SOURCE LINE 34
        __M_writer(u'\n\n')
        # SOURCE LINE 38
        __M_writer(u'\n\n')
        # SOURCE LINE 52
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_interstitial_image_attrs(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f7227efaa10')._populate(_import_ns, [u'_md', u'buffered_timestamp'])
        __M_writer = context.writer()
        # SOURCE LINE 31
        __M_writer(u'\n  src="')
        # SOURCE LINE 32
        __M_writer(conditional_websafe(static('interstitial-image-banned.png')))
        __M_writer(u'"\n  alt="')
        # SOURCE LINE 33
        __M_writer(conditional_websafe(_('banned')))
        __M_writer(u'"\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_interstitial_message(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f7227efaa10')._populate(_import_ns, [u'_md', u'buffered_timestamp'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        buffered_timestamp = _import_ns.get('buffered_timestamp', context.get('buffered_timestamp', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        _md = _import_ns.get('_md', context.get('_md', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 40
        __M_writer(u'\n')
        # SOURCE LINE 41
        if thing.message:
            # SOURCE LINE 42
            __M_writer(u'    ')
            __M_writer(conditional_websafe(parent.interstitial_message()))
            __M_writer(u'\n')
            # SOURCE LINE 43
        else:
            # SOURCE LINE 44
            __M_writer(u'    ')
            __M_writer(conditional_websafe(_md("This community has been banned for violating the [SaidIt rules](/r/AntiExtremes/comments/63/antiextremescom_content_policy/).")))
            __M_writer(u'\n')
        # SOURCE LINE 46
        __M_writer(u'\n')
        # SOURCE LINE 47
        if thing.ban_time:
            # SOURCE LINE 48
            __M_writer(u'    <div class="note">\n      ')
            # SOURCE LINE 49
            __M_writer(conditional_websafe(_wsf("Banned %(time_ago)s.", time_ago=unsafe(buffered_timestamp(thing.ban_time, include_tense=True)))))
            __M_writer(u'\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_interstitial_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f7227efaa10')._populate(_import_ns, [u'_md', u'buffered_timestamp'])
        __M_writer = context.writer()
        # SOURCE LINE 36
        __M_writer(u'\n  ')
        # SOURCE LINE 37
        __M_writer(conditional_websafe(_("This community has been banned")))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


