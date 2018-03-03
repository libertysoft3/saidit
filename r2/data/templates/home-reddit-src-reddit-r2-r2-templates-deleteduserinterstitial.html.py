# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1509280490.748944
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/deleteduserinterstitial.html'
_template_uri = '/deleteduserinterstitial.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['interstitial_image_attrs', 'interstitial_title']


# SOURCE LINE 23

from r2.lib.template_helpers import static 


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
    return runtime._inherit_from(context, u'interstitial.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'\n\n')
        # SOURCE LINE 27
        __M_writer(u'\n\n')
        # SOURCE LINE 32
        __M_writer(u'\n\n')
        # SOURCE LINE 36
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_interstitial_image_attrs(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 29
        __M_writer(u'\n  src="')
        # SOURCE LINE 30
        __M_writer(conditional_websafe(static('interstitial-image-deleted-user.png')))
        __M_writer(u'"\n  alt="')
        # SOURCE LINE 31
        __M_writer(conditional_websafe(_('deleted')))
        __M_writer(u'"\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_interstitial_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 34
        __M_writer(u'\n  ')
        # SOURCE LINE 35
        __M_writer(conditional_websafe(_("This user has deleted their account.")))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


