# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505019877.527421
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/morerecursion.html'
_template_uri = '/morerecursion.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['commentBody', 'midcol']


# SOURCE LINE 24

from r2.models import Link


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'comment_skeleton.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n')
        # SOURCE LINE 26
        __M_writer(u'\n\n\n')
        # SOURCE LINE 41
        __M_writer(u'\n\n')
        # SOURCE LINE 44
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_commentBody(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        thing = context.get('thing', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 29
        __M_writer(u'\n')
        # SOURCE LINE 30

        url = thing.parent_permalink
        inbound_tracking_url = Link.tracking_link(thing.parent_permalink, thing, context='continue_thread')
        
        
        # SOURCE LINE 33
        __M_writer(u'\n<span class="deepthread"><a\n    href="')
        # SOURCE LINE 35
        __M_writer(conditional_websafe(url))
        __M_writer(u'"\n')
        # SOURCE LINE 36
        if inbound_tracking_url != url:
            # SOURCE LINE 37
            __M_writer(u'      data-href-url="')
            __M_writer(conditional_websafe(url))
            __M_writer(u'"\n      data-inbound-url="')
            # SOURCE LINE 38
            __M_writer(conditional_websafe(inbound_tracking_url))
            __M_writer(u'"\n')
        # SOURCE LINE 40
        __M_writer(u'    >')
        __M_writer(conditional_websafe(_("continue this thread")))
        __M_writer(u'</a></span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_midcol(context,cls=''):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 43
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


