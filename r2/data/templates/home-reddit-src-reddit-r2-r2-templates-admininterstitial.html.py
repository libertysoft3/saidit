# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505799307.31921
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/admininterstitial.html'
_template_uri = '/admininterstitial.html'
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
    ns = runtime.TemplateNamespace(u'utils', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'utils')] = ns

    # SOURCE LINE 28
    ns = runtime.TemplateNamespace('__anon_0x7ff76fa624d0', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7ff76fa624d0')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'interstitial.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7ff76fa624d0')._populate(_import_ns, [u'error_field'])
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
        # SOURCE LINE 42
        __M_writer(u'\n\n')
        # SOURCE LINE 87
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_interstitial_image_attrs(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7ff76fa624d0')._populate(_import_ns, [u'error_field'])
        __M_writer = context.writer()
        # SOURCE LINE 32
        __M_writer(u'\n  src="')
        # SOURCE LINE 33
        __M_writer(conditional_websafe(static('interstitial-image-admin.png')))
        __M_writer(u'"\n  title="')
        # SOURCE LINE 34
        __M_writer(conditional_websafe(_('Are you one of us?')))
        __M_writer(u'"\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_interstitial_message(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7ff76fa624d0')._populate(_import_ns, [u'error_field'])
        __M_writer = context.writer()
        # SOURCE LINE 41
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_interstitial_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7ff76fa624d0')._populate(_import_ns, [u'error_field'])
        __M_writer = context.writer()
        # SOURCE LINE 37
        __M_writer(u'\n  ')
        # SOURCE LINE 38
        __M_writer(conditional_websafe(_('Enter your password and one-time code')))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_interstitial_buttons(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7ff76fa624d0')._populate(_import_ns, [u'error_field'])
        utils = _mako_get_namespace(context, 'utils')
        __M_writer = context.writer()
        # SOURCE LINE 44
        __M_writer(u'\n  <form action="/post/adminon" method="post"\n      onsubmit="return post_form(this, \'adminon\')" id="adminon">\n    <div class="spacer">\n      ')
        def ccall(caller):
            def body():
                thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
                error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
                __M_writer = context.writer()
                # SOURCE LINE 48
                __M_writer(u'\n')
                # SOURCE LINE 49
                if thing.dest:
                    # SOURCE LINE 50
                    __M_writer(u'          <input type="hidden" name="dest" value="')
                    __M_writer(conditional_websafe(thing.dest))
                    __M_writer(u'" />\n')
                # SOURCE LINE 52
                __M_writer(u'      <input type="password" name="password" tabindex="1" autofocus />\n      ')
                # SOURCE LINE 53
                __M_writer(conditional_websafe(error_field("WRONG_PASSWORD", "password")))
                __M_writer(u'\n      ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 48
            __M_writer(conditional_websafe(utils.round_field(css_class=u'adminpasswordform',description=(_('(required)')),title=(_('password')))))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 54
        __M_writer(u'\n\n')
        # SOURCE LINE 56
        if not g.disable_require_admin_otp or c.user.otp_secret:
            # SOURCE LINE 57
            __M_writer(u'      ')
            def ccall(caller):
                def body():
                    error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
                    __M_writer = context.writer()
                    __M_writer(u'\n      <input type="text" name="otp" maxlength="6" tabindex="1" required pattern="[0-9]{6}" autocomplete="off"\n')
                    # SOURCE LINE 59
                    if c.otp_cached:
                        # SOURCE LINE 60
                        __M_writer(u'      disabled\n')
                    # SOURCE LINE 62
                    __M_writer(u'      />\n      ')
                    # SOURCE LINE 63
                    __M_writer(conditional_websafe(error_field("WRONG_PASSWORD", "otp")))
                    __M_writer(u'\n      ')
                    # SOURCE LINE 64
                    __M_writer(conditional_websafe(error_field("NO_OTP_SECRET", "otp")))
                    __M_writer(u'\n      ')
                    # SOURCE LINE 65
                    __M_writer(conditional_websafe(error_field("RATELIMIT", "otp")))
                    __M_writer(u'\n\n      <label>\n          <input type="checkbox" name="remember" tabindex="1"\n')
                    # SOURCE LINE 69
                    if c.otp_cached:
                        # SOURCE LINE 70
                        __M_writer(u'            disabled\n            checked\n')
                    # SOURCE LINE 73
                    __M_writer(u'          > ')
                    __M_writer(conditional_websafe(_("remember this computer")))
                    __M_writer(u'</label>\n      ')
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 57
                __M_writer(conditional_websafe(utils.round_field(css_class=u'adminpasswordform',description=(_('(required)')),title=(_('one-time verification code')))))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 74
            __M_writer(u'\n')
        # SOURCE LINE 76
        __M_writer(u'\n      <div class="buttons">\n        <button class="c-btn c-btn-primary" type="submit">\n          ')
        # SOURCE LINE 79
        __M_writer(conditional_websafe(_('turn admin on')))
        __M_writer(u'\n        </button>\n      </div>\n\n      <p class="status error"></p>\n\n    </div>\n  </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


