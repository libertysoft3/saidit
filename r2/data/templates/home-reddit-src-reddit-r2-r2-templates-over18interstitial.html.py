# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1517702796.44583
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/over18interstitial.html'
_template_uri = '/over18interstitial.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['interstitial_image_attrs', 'interstitial_message', 'interstitial_title', 'interstitial_buttons']


# SOURCE LINE 23

from r2.lib.template_helpers import static 


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 27
    ns = runtime.TemplateNamespace('__anon_0x7f5980b7f210', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f5980b7f210')] = ns

    # SOURCE LINE 28
    ns = runtime.TemplateNamespace(u'utils', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'utils')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'interstitial.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f5980b7f210')._populate(_import_ns, [u'submit_form'])
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'\n\n')
        # SOURCE LINE 27
        __M_writer(u'\n')
        # SOURCE LINE 28
        __M_writer(u'\n\n')
        # SOURCE LINE 30
        __M_writer(u'\n\n')
        # SOURCE LINE 35
        __M_writer(u'\n\n')
        # SOURCE LINE 39
        __M_writer(u'\n\n')
        # SOURCE LINE 45
        __M_writer(u'\n\n')
        # SOURCE LINE 58
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_interstitial_image_attrs(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f5980b7f210')._populate(_import_ns, [u'submit_form'])
        __M_writer = context.writer()
        # SOURCE LINE 32
        __M_writer(u'\n  src="')
        # SOURCE LINE 33
        __M_writer(conditional_websafe(static('interstitial-image-over18.png')))
        __M_writer(u'"\n  alt="')
        # SOURCE LINE 34
        __M_writer(conditional_websafe(_('over 18')))
        __M_writer(u'"\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_interstitial_message(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f5980b7f210')._populate(_import_ns, [u'submit_form'])
        __M_writer = context.writer()
        # SOURCE LINE 41
        __M_writer(u'\n  <p>\n    ')
        # SOURCE LINE 43
        __M_writer(conditional_websafe(_("You must be at least eighteen years old to view this content. Are you over eighteen and willing to see adult content?")))
        __M_writer(u'\n  </p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_interstitial_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f5980b7f210')._populate(_import_ns, [u'submit_form'])
        __M_writer = context.writer()
        # SOURCE LINE 37
        __M_writer(u'\n  ')
        # SOURCE LINE 38
        __M_writer(conditional_websafe(_("You must be 18+ to view this community")))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_interstitial_buttons(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f5980b7f210')._populate(_import_ns, [u'submit_form'])
        utils = _mako_get_namespace(context, 'utils')
        __M_writer = context.writer()
        # SOURCE LINE 47
        __M_writer(u'\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                # SOURCE LINE 48
                __M_writer(u'\n    <div class="buttons">\n      <button class="c-btn c-btn-primary" type="submit" name="over18" value="no">\n        ')
                # SOURCE LINE 51
                __M_writer(conditional_websafe(_("no thank you")))
                __M_writer(u'\n      </button>\n      <button class="c-btn c-btn-primary" type="submit" name="over18" value="yes">\n        ')
                # SOURCE LINE 54
                __M_writer(conditional_websafe(_("continue")))
                __M_writer(u'\n      </button>\n    </div>\n  ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 48
            __M_writer(conditional_websafe(utils.submit_form(_class=u'pretty-form')))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 57
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


