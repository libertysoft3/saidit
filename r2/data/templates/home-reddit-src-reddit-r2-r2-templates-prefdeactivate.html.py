# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1508436224.954444
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/prefdeactivate.html'
_template_uri = '/prefdeactivate.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23

from r2.lib.filters import safemarkdown, jssafe


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 26
    ns = runtime.TemplateNamespace('__anon_0x7f99e7140ad0', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f99e7140ad0')] = ns

    # SOURCE LINE 27
    ns = runtime.TemplateNamespace(u'utils', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'utils')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f99e7140ad0')._populate(_import_ns, [u'error_field', u'text_with_links'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        utils = _mako_get_namespace(context, 'utils')
        error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'\n')
        # SOURCE LINE 26
        __M_writer(u'\n')
        # SOURCE LINE 27
        __M_writer(u'\n\n<h1>')
        # SOURCE LINE 29
        __M_writer(conditional_websafe(_("deactivate your reddit account")))
        __M_writer(u'</h1>\n\n<form action="javascript:;" method="post"\n  onsubmit="')
        # SOURCE LINE 32
        __M_writer(conditional_websafe("return post_form(this, 'deactivate_user', function(x) {return '%s'})" % jssafe(_("deactivating..."))))
        __M_writer(u'" id="pref-deactivate">\n\n<div class="spacer">\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                # SOURCE LINE 35
                __M_writer(u'\n    <div class="rounded white-field">\n      ')
                # SOURCE LINE 37
                __M_writer(conditional_websafe(unsafe(safemarkdown(_(
        " * if you're having a problem on reddit, please consider [contacting us](/message/compose?to=%2Fr%2Freddit.com) about it before deactivating your account.\n"
        " * deactivating your account will not delete the content of posts and comments you've made on reddit. to do so, please delete them individually."
      )))))
                # SOURCE LINE 40
                __M_writer(u'\n    </div>\n  ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 35
            __M_writer(conditional_websafe(utils.round_field(title=(_('sorry to see you go!')))))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 42
        __M_writer(u'\n</div>\n\n')
        # SOURCE LINE 45
        if thing.has_paypal_subscription:
            # SOURCE LINE 46
            __M_writer(u'  <div class="spacer">\n    ')
            def ccall(caller):
                def body():
                    dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
                    text_with_links = _import_ns.get('text_with_links', context.get('text_with_links', UNDEFINED))
                    __M_writer = context.writer()
                    # SOURCE LINE 47
                    __M_writer(u'\n      <div class="rounded white-field">\n        <div class="gold-subscription">\n          ')
                    # SOURCE LINE 50
                    __M_writer(conditional_websafe(text_with_links(
            _("log in to %%(paypal_link)s to cancel your subscription (%(subscr_id)s).") % dict(subscr_id=thing.paypal_subscr_id),
            paypal_link=dict(link_text="paypal", path=thing.paypal_url)
          )))
                    # SOURCE LINE 53
                    __M_writer(u'\n        </div>\n      </div>\n    ')
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 47
                __M_writer(conditional_websafe(utils.round_field(title=(_('please cancel your gold subscription!')))))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 56
            __M_writer(u'\n  </div>\n')
        # SOURCE LINE 59
        __M_writer(u'\n<div class="spacer">\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                # SOURCE LINE 61
                __M_writer(u'\n    <textarea name="deactivate_message" id="deactivate-message"></textarea>\n    ')
                # SOURCE LINE 63
                __M_writer(conditional_websafe(error_field("TOO_LONG", "deactivate_message")))
                __M_writer(u'\n  ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 61
            __M_writer(conditional_websafe(utils.round_field(description=u'(' + (_('optional')) + u')',title=(_('why are you deactivating this account?')))))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 64
        __M_writer(u'\n</div>\n\n<div class="spacer">\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                # SOURCE LINE 68
                __M_writer(u'\n    <label for="deactivate-user">')
                # SOURCE LINE 69
                __M_writer(conditional_websafe(_("username")))
                __M_writer(u'</label>\n    ')
                # SOURCE LINE 70
                __M_writer(conditional_websafe(error_field("NOT_USER", "user")))
                __M_writer(u'\n    <input name="user" id="deactivate-user" type="text" />\n    <label for="deactivate-password">')
                # SOURCE LINE 72
                __M_writer(conditional_websafe(_("password")))
                __M_writer(u'</label>\n    ')
                # SOURCE LINE 73
                __M_writer(conditional_websafe(error_field("WRONG_PASSWORD", "passwd")))
                __M_writer(u'\n    <input name="passwd" id="deactivate-password" type="password" />\n  ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 68
            __M_writer(conditional_websafe(utils.round_field(css_class=u'credentials',description=u'(' + (_('for security purposes')) + u')',title=(_('account credentials')))))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 75
        __M_writer(u'\n</div>  \n\n<div class="spacer">\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                # SOURCE LINE 79
                __M_writer(u'\n    <div class="rounded white-field">\n      <input name="confirm" id="confirm-deactivate" type="checkbox"/>\n      <label for="confirm-deactivate">')
                # SOURCE LINE 82
                __M_writer(conditional_websafe(_("I understand that deactivated accounts are not recoverable.")))
                __M_writer(u'</label>\n    </div>\n    ')
                # SOURCE LINE 84
                __M_writer(conditional_websafe(error_field("CONFIRM", "confirm")))
                __M_writer(u'\n  ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 79
            __M_writer(conditional_websafe(utils.round_field(title=(_('confirmation')))))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 85
        __M_writer(u'\n</div>\n\n<div class="spacer">\n  <button type="submit" class="btn">')
        # SOURCE LINE 89
        __M_writer(conditional_websafe(_("deactivate account")))
        __M_writer(u'</button>\n  <span class="status"></span>\n  ')
        # SOURCE LINE 91
        __M_writer(conditional_websafe(error_field("RATELIMIT", "vdelay")))
        __M_writer(u'\n</div>\n</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


