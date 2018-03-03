# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1509788465.909998
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/prefsecurity.html'
_template_uri = '/prefsecurity.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23

from r2.lib import js
from r2.lib.strings import strings


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 28
    ns = runtime.TemplateNamespace('__anon_0x7fc6ac1d0d50', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fc6ac1d0d50')] = ns

    # SOURCE LINE 29
    ns = runtime.TemplateNamespace(u'utils', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'utils')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc6ac1d0d50')._populate(_import_ns, [u'error_field', u'_md'])
        utils = _mako_get_namespace(context, 'utils')
        _md = _import_ns.get('_md', context.get('_md', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 26
        __M_writer(u'\n\n')
        # SOURCE LINE 28
        __M_writer(u'\n')
        # SOURCE LINE 29
        __M_writer(u'\n\n\n')
        # SOURCE LINE 32
        if c.user_is_loggedin and c.user.name in g.admins:
            # SOURCE LINE 33
            __M_writer(u'<h1>')
            __M_writer(conditional_websafe(_("two-factor authentication")))
            __M_writer(u'</h1>\n\n')
            # SOURCE LINE 35
            if c.user.otp_secret:
                # SOURCE LINE 36
                __M_writer(u'    <form action="/post/disable_otp" method="post" onsubmit="return post_form(this, \'disable_otp\')" id="pref-otp">\n\n    ')
                # SOURCE LINE 38
                __M_writer(conditional_websafe(_md("two-factor authentication is currently **enabled**. fill out the form below if you would like to disable it.", wrap=True)))
                __M_writer(u'\n\n    ')
                def ccall(caller):
                    def body():
                        error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
                        __M_writer = context.writer()
                        # SOURCE LINE 40
                        __M_writer(u'\n      <input type="password" name="password" />\n      ')
                        # SOURCE LINE 42
                        __M_writer(conditional_websafe(error_field("WRONG_PASSWORD", "password")))
                        __M_writer(u'\n    ')
                        return ''
                    return [body]
                context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
                try:
                    # SOURCE LINE 40
                    __M_writer(conditional_websafe(utils.round_field(description=(_('(required)')),title=(_('password')))))
                finally:
                    context.caller_stack.nextcaller = None
                # SOURCE LINE 43
                __M_writer(u'\n\n    ')
                def ccall(caller):
                    def body():
                        error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
                        __M_writer = context.writer()
                        # SOURCE LINE 45
                        __M_writer(u'\n      <input type="number" name="otp" maxlength="6" />\n      ')
                        # SOURCE LINE 47
                        __M_writer(conditional_websafe(error_field("WRONG_PASSWORD", "otp")))
                        __M_writer(u'\n      ')
                        # SOURCE LINE 48
                        __M_writer(conditional_websafe(error_field("NO_OTP_SECRET", "otp")))
                        __M_writer(u'\n      ')
                        # SOURCE LINE 49
                        __M_writer(conditional_websafe(error_field("RATELIMIT", "otp")))
                        __M_writer(u'\n    ')
                        return ''
                    return [body]
                context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
                try:
                    # SOURCE LINE 45
                    __M_writer(conditional_websafe(utils.round_field(description=(_('(required)')),title=(_('one-time password')))))
                finally:
                    context.caller_stack.nextcaller = None
                # SOURCE LINE 50
                __M_writer(u'\n\n    <input type="submit" value="')
                # SOURCE LINE 52
                __M_writer(conditional_websafe(_("disable")))
                __M_writer(u'">\n    </form>\n')
                # SOURCE LINE 54
            else:
                # SOURCE LINE 55
                __M_writer(u'    <form action="/post/generate_otp_secret" method="post" onsubmit="return post_form(this, \'generate_otp_secret\')" id="pref-otp">\n\n    ')
                # SOURCE LINE 57
                __M_writer(conditional_websafe(_md("enter your current password below to start the activation process for two-factor authentication.", wrap=True)))
                __M_writer(u'\n\n    ')
                def ccall(caller):
                    def body():
                        error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
                        __M_writer = context.writer()
                        # SOURCE LINE 59
                        __M_writer(u'\n      <input type="password" name="password" />\n      ')
                        # SOURCE LINE 61
                        __M_writer(conditional_websafe(error_field("WRONG_PASSWORD", "password")))
                        __M_writer(u'\n    ')
                        return ''
                    return [body]
                context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
                try:
                    # SOURCE LINE 59
                    __M_writer(conditional_websafe(utils.round_field(description=(_('(required)')),title=(_('password')))))
                finally:
                    context.caller_stack.nextcaller = None
                # SOURCE LINE 62
                __M_writer(u'\n\n    <input type="submit" value="')
                # SOURCE LINE 64
                __M_writer(conditional_websafe(_("activate")))
                __M_writer(u'">\n\n    </form>\n\n    <form action="/post/enable_otp" method="post" onsubmit="return post_form(this, \'enable_otp\')" id="pref-otp-qr">\n\n    <div id="otp-secret-info">\n        ')
                # SOURCE LINE 71
                __M_writer(conditional_websafe(_md("below is your two-factor authentication secret. you can scan the QR code with Google Authenticator or enter the key below manually. you WILL NOT have another chance to see this secret.")))
                __M_writer(u'\n    </div>\n\n    ')
                def ccall(caller):
                    def body():
                        error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
                        __M_writer = context.writer()
                        # SOURCE LINE 74
                        __M_writer(u'\n      <input type="number" name="otp" maxlength="6" />\n      ')
                        # SOURCE LINE 76
                        __M_writer(conditional_websafe(error_field("WRONG_PASSWORD", "otp")))
                        __M_writer(u'\n      ')
                        # SOURCE LINE 77
                        __M_writer(conditional_websafe(error_field("EXPIRED", "otp")))
                        __M_writer(u'\n    ')
                        return ''
                    return [body]
                context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
                try:
                    # SOURCE LINE 74
                    __M_writer(conditional_websafe(utils.round_field(description=(_('(required)')),title=(_('one-time password')))))
                finally:
                    context.caller_stack.nextcaller = None
                # SOURCE LINE 78
                __M_writer(u'\n\n    <input type="submit" value="')
                # SOURCE LINE 80
                __M_writer(conditional_websafe(_("enable")))
                __M_writer(u'">\n\n    </form>\n')
        # SOURCE LINE 85
        __M_writer(u'\n')
        # SOURCE LINE 86
        __M_writer(conditional_websafe(unsafe(js.use("qrcode"))))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


