# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505002596.476016
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/login.html'
_template_uri = '/login.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['login_form', 'login_panel']


# SOURCE LINE 23

from r2.config import feature
from r2.lib.template_helpers import add_sr
from r2.lib.template_helpers import static
from r2.lib.strings import strings
from r2.lib.utils import UrlParser
import random
 

def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 32
    ns = runtime.TemplateNamespace('__anon_0x7fde5fe6ba90', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fde5fe6ba90')] = ns

    # SOURCE LINE 31
    ns = runtime.TemplateNamespace('__anon_0x7fde5fe6b9d0', context._clean_inheritance_tokens(), templateuri=u'captcha.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fde5fe6b9d0')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fde5fe6ba90')._populate(_import_ns, [u'error_field', u'img_link', u'form_group', u'text_with_links'])
        _mako_get_namespace(context, '__anon_0x7fde5fe6b9d0')._populate(_import_ns, [u'captchagen'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        def login_form(register=False,user='',dest='',compact=False,autofocus=True):
            return render_login_form(context._locals(__M_locals),register,user,dest,compact,autofocus)
        def login_panel(lf,user_reg='',user_login='',dest='',registration_info=None):
            return render_login_panel(context._locals(__M_locals),lf,user_reg,user_login,dest,registration_info)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 30
        __M_writer(u'\n')
        # SOURCE LINE 31
        __M_writer(u'\n')
        # SOURCE LINE 32
        __M_writer(u'\n\n')
        # SOURCE LINE 35
        if c.user_is_loggedin:
            # SOURCE LINE 36
            __M_writer(u'  <p class="error">')
            __M_writer(conditional_websafe(_("You are logged in. Go use the site!")))
            __M_writer(u'</p>\n')
            # SOURCE LINE 37
        else:
            # SOURCE LINE 38
            if thing.is_popup:
                # SOURCE LINE 39
                __M_writer(u'    <h3 id="cover-msg" class="modal-title">\n      ')
                # SOURCE LINE 40
                __M_writer(conditional_websafe(_('You need to login to do that.')))
                __M_writer(u'\n    </h3>\n')
            # SOURCE LINE 43
            __M_writer(u'  <div id="login">\n    ')
            # SOURCE LINE 44
            __M_writer(conditional_websafe(login_panel(login_form, 
                  user_reg = thing.user_reg, user_login = thing.user_login, 
                  dest=thing.dest,
                  registration_info=thing.registration_info)))
            # SOURCE LINE 47
            __M_writer(u'\n  </div>\n')
        # SOURCE LINE 50
        __M_writer(u'\n')
        # SOURCE LINE 240
        __M_writer(u'\n\n\n')
        # SOURCE LINE 263
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_login_form(context,register=False,user='',dest='',compact=False,autofocus=True):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fde5fe6ba90')._populate(_import_ns, [u'error_field', u'img_link', u'form_group', u'text_with_links'])
        _mako_get_namespace(context, '__anon_0x7fde5fe6b9d0')._populate(_import_ns, [u'captchagen'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        captchagen = _import_ns.get('captchagen', context.get('captchagen', UNDEFINED))
        form_group = _import_ns.get('form_group', context.get('form_group', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 51
        __M_writer(u'\n')
        # SOURCE LINE 52
        if not compact:
            # SOURCE LINE 53
            __M_writer(u'    ')

            op = "reg" if register else "login"
            base = g.https_endpoint
            tabindex = 2 if register else 3
                
            
            # SOURCE LINE 57
            __M_writer(u'\n    <form id="')
            # SOURCE LINE 58
            __M_writer(conditional_websafe('register' if register else 'login'))
            __M_writer(u'-form" method="post" \n          action="')
            # SOURCE LINE 59
            __M_writer(conditional_websafe(add_sr(base + '/post/' + op)))
            __M_writer(u'"\n          class="form-v2">\n      <input type="hidden" name="op" value="')
            # SOURCE LINE 61
            __M_writer(conditional_websafe(op))
            __M_writer(u'">\n')
            # SOURCE LINE 62
            if dest:
                # SOURCE LINE 63
                __M_writer(u'        <input type="hidden" name="dest" value="')
                __M_writer(conditional_websafe(dest))
                __M_writer(u'">\n')
            # SOURCE LINE 65
            __M_writer(u'      ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    # SOURCE LINE 70
                    __M_writer(u'\n        <label for="user_')
                    # SOURCE LINE 71
                    __M_writer(conditional_websafe(op))
                    __M_writer(u'" class="screenreader-only">')
                    __M_writer(conditional_websafe(_('username')))
                    __M_writer(u':</label>\n        <input value="')
                    # SOURCE LINE 72
                    __M_writer(conditional_websafe(user))
                    __M_writer(u'" name="user" id="user_')
                    __M_writer(conditional_websafe(op))
                    __M_writer(u'" class="c-form-control"\n               type="text" maxlength="20" tabindex="')
                    # SOURCE LINE 73
                    __M_writer(conditional_websafe(tabindex))
                    __M_writer(u'"\n')
                    # SOURCE LINE 74
                    if register:
                        # SOURCE LINE 75
                        __M_writer(u'                placeholder="')
                        __M_writer(conditional_websafe(_('choose a username')))
                        __M_writer(u'"\n                data-validate-url="/api/check_username.json"\n                data-validate-min="3"\n                autocomplete="off"\n')
                        # SOURCE LINE 79
                    else:
                        # SOURCE LINE 80
                        __M_writer(u'                placeholder="')
                        __M_writer(conditional_websafe(_('username')))
                        __M_writer(u'"\n')
                        # SOURCE LINE 81
                        if autofocus:
                            # SOURCE LINE 82
                            __M_writer(u'                  autofocus\n')
                    # SOURCE LINE 85
                    __M_writer(u'               >\n      ')
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 65
                __M_writer(conditional_websafe(form_group(
                    'user',
                    'USERNAME_TOO_SHORT',
                    'USERNAME_INVALID_CHARACTERS',
                    'USERNAME_TAKEN',
                    show_errors=register)))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 86
            __M_writer(u'\n      ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    # SOURCE LINE 87
                    __M_writer(u'\n        <label for="passwd_')
                    # SOURCE LINE 88
                    __M_writer(conditional_websafe(op))
                    __M_writer(u'" class="screenreader-only">')
                    __M_writer(conditional_websafe(_('password')))
                    __M_writer(u':</label>\n        <input id="passwd_')
                    # SOURCE LINE 89
                    __M_writer(conditional_websafe(op))
                    __M_writer(u'" class="c-form-control" name="passwd" type="password"\n               tabindex="')
                    # SOURCE LINE 90
                    __M_writer(conditional_websafe(tabindex))
                    __M_writer(u'" placeholder="')
                    __M_writer(conditional_websafe(_('password')))
                    __M_writer(u'"\n               ')
                    # SOURCE LINE 91
                    __M_writer(conditional_websafe("data-validate-url='/api/check_password.json'" if register else ''))
                    __M_writer(u'>\n      ')
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 87
                __M_writer(conditional_websafe(form_group('passwd', 'BAD_PASSWORD', 'WRONG_PASSWORD', show_errors=True)))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 92
            __M_writer(u'\n')
            # SOURCE LINE 93
            if register:
                # SOURCE LINE 94
                __M_writer(u'        ')
                def ccall(caller):
                    def body():
                        __M_writer = context.writer()
                        __M_writer(u'\n          <label for="passwd2_')
                        # SOURCE LINE 95
                        __M_writer(conditional_websafe(op))
                        __M_writer(u'" class="screenreader-only">')
                        __M_writer(conditional_websafe(_('verify password')))
                        __M_writer(u':</label>\n          <input name="passwd2" id="passwd2_')
                        # SOURCE LINE 96
                        __M_writer(conditional_websafe(op))
                        __M_writer(u'" class="c-form-control"\n                 type="password" tabindex="')
                        # SOURCE LINE 97
                        __M_writer(conditional_websafe(tabindex))
                        __M_writer(u'"\n                 placeholder="')
                        # SOURCE LINE 98
                        __M_writer(conditional_websafe(_('verify password')))
                        __M_writer(u'">\n        ')
                        return ''
                    return [body]
                context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
                try:
                    # SOURCE LINE 94
                    __M_writer(conditional_websafe(form_group('passwd2', 'BAD_PASSWORD_MATCH', show_errors=register)))
                finally:
                    context.caller_stack.nextcaller = None
                # SOURCE LINE 99
                __M_writer(u'\n        ')
                def ccall(caller):
                    def body():
                        __M_writer = context.writer()
                        # SOURCE LINE 100
                        __M_writer(u'\n          <label for="email_')
                        # SOURCE LINE 101
                        __M_writer(conditional_websafe(op))
                        __M_writer(u'" class="screenreader-only">\n            ')
                        # SOURCE LINE 102
                        __M_writer(conditional_websafe(_('email')))
                        __M_writer(u': &nbsp;<i>(')
                        __M_writer(conditional_websafe(_('optional')))
                        __M_writer(u')\n          </i></label>\n          <input value="" name="email" id="email_')
                        # SOURCE LINE 104
                        __M_writer(conditional_websafe(op))
                        __M_writer(u'" class="c-form-control"\n                 type="text" tabindex="')
                        # SOURCE LINE 105
                        __M_writer(conditional_websafe(tabindex))
                        __M_writer(u'"\n                 placeholder="')
                        # SOURCE LINE 106
                        __M_writer(conditional_websafe(_('email (optional)')))
                        __M_writer(u'"\n                 data-validate-url="/api/check_email.json"\n                 data-validate-on="change blur">\n        ')
                        return ''
                    return [body]
                context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
                try:
                    # SOURCE LINE 100
                    __M_writer(conditional_websafe(form_group('email', 'BAD_EMAIL', show_errors=register)))
                finally:
                    context.caller_stack.nextcaller = None
                # SOURCE LINE 109
                __M_writer(u'\n')
            # SOURCE LINE 111
            __M_writer(u'      <div class="c-checkbox">\n        <input type="checkbox" name="rem" id="rem_')
            # SOURCE LINE 112
            __M_writer(conditional_websafe(op))
            __M_writer(u'" tabindex="')
            __M_writer(conditional_websafe(tabindex))
            __M_writer(u'">\n        <label for="rem_')
            # SOURCE LINE 113
            __M_writer(conditional_websafe(op))
            __M_writer(u'">\n          ')
            # SOURCE LINE 114
            __M_writer(conditional_websafe(_('remember me')))
            __M_writer(u'\n        </label>\n')
            # SOURCE LINE 116
            if not register:
                # SOURCE LINE 117
                __M_writer(u'          <a href="/password" class="c-pull-right">')
                __M_writer(conditional_websafe(_('reset password')))
                __M_writer(u'</a>\n')
            # SOURCE LINE 119
            __M_writer(u'      </div>\n')
            
            # SOURCE LINE 133
            __M_writer(u'      <div class="c-clearfix c-submit-group">\n        <span class="c-form-throbber"></span>\n        <button type="submit" class="c-btn c-btn-primary c-pull-right" tabindex="')
            # SOURCE LINE 135
            __M_writer(conditional_websafe(tabindex))
            __M_writer(u'">\n          ')
            # SOURCE LINE 136
            __M_writer(conditional_websafe(register and _("sign up") or _("log in")))
            __M_writer(u'\n        </button>\n      </div>\n      <div>\n        <div class="c-alert c-alert-danger"></div>\n')
            # SOURCE LINE 141
            if register:
                # SOURCE LINE 142
                __M_writer(u'          ')
                __M_writer(conditional_websafe(error_field("RATELIMIT", "ratelimit")))
                __M_writer(u'\n          ')
                # SOURCE LINE 143
                __M_writer(conditional_websafe(error_field("RATELIMIT", "vdelay")))
                __M_writer(u'\n')
            # SOURCE LINE 145
            __M_writer(u'      </div>\n    </form>\n')
            # SOURCE LINE 147
        else:
            # SOURCE LINE 148
            __M_writer(u'    ')

            op = "reg" if register else "login"
            base = g.https_endpoint
            tabindex = 2 if register else 3
                
            
            # SOURCE LINE 152
            __M_writer(u'\n    <form id="login_')
            # SOURCE LINE 153
            __M_writer(conditional_websafe(op))
            __M_writer(u'" method="post" \n          action="')
            # SOURCE LINE 154
            __M_writer(conditional_websafe(add_sr(base + '/post/' + op)))
            __M_writer(u'"\n          class="user-form ')
            # SOURCE LINE 155
            __M_writer(conditional_websafe('register-form' if register else 'login-form'))
            __M_writer(u'">\n      <input type="hidden" name="op" value="')
            # SOURCE LINE 156
            __M_writer(conditional_websafe(op))
            __M_writer(u'" />\n')
            # SOURCE LINE 157
            if dest:
                # SOURCE LINE 158
                __M_writer(u'        <input type="hidden" name="dest" value="')
                __M_writer(conditional_websafe(dest))
                __M_writer(u'" />\n')
            # SOURCE LINE 160
            __M_writer(u'      <div>\n        <ul>\n          <li class="name-entry">\n            <label for="user_')
            # SOURCE LINE 163
            __M_writer(conditional_websafe(op))
            __M_writer(u'">')
            __M_writer(conditional_websafe(_('username')))
            __M_writer(u':</label>\n            <input value="')
            # SOURCE LINE 164
            __M_writer(conditional_websafe(user))
            __M_writer(u'" name="user" id="user_')
            __M_writer(conditional_websafe(op))
            __M_writer(u'" \n                   type="text" maxlength="20" tabindex="')
            # SOURCE LINE 165
            __M_writer(conditional_websafe(tabindex))
            __M_writer(u'" autofocus />\n')
            # SOURCE LINE 166
            if register:
                # SOURCE LINE 167
                __M_writer(u'              <span class="throbber"></span>\n              <span class="notice-taken">')
                # SOURCE LINE 168
                __M_writer(conditional_websafe(_('try another')))
                __M_writer(u'</span>\n              <span class="notice-available">')
                # SOURCE LINE 169
                __M_writer(conditional_websafe(_('available!')))
                __M_writer(u'</span>\n              ')
                # SOURCE LINE 170
                __M_writer(conditional_websafe(error_field("BAD_USERNAME", "user", kind="span")))
                __M_writer(u'\n              ')
                # SOURCE LINE 171
                __M_writer(conditional_websafe(error_field("USERNAME_TAKEN", "user", kind="span")))
                __M_writer(u'\n              ')
                # SOURCE LINE 172
                __M_writer(conditional_websafe(error_field("USERNAME_TAKEN_DEL", "user", kind="span")))
                __M_writer(u'\n')
            # SOURCE LINE 174
            __M_writer(u'          </li>\n')
            # SOURCE LINE 175
            if register:
                # SOURCE LINE 176
                __M_writer(u'          <li>\n            <label for="email_')
                # SOURCE LINE 177
                __M_writer(conditional_websafe(op))
                __M_writer(u'">\n              ')
                # SOURCE LINE 178
                __M_writer(conditional_websafe(_('account recovery email')))
                __M_writer(u': &nbsp;<i>(')
                __M_writer(conditional_websafe(_('optional')))
                __M_writer(u')\n            </i></label>\n            <input value="" name="email" id="email_')
                # SOURCE LINE 180
                __M_writer(conditional_websafe(op))
                __M_writer(u'" \n                   type="email" maxlength="50" tabindex="')
                # SOURCE LINE 181
                __M_writer(conditional_websafe(tabindex))
                __M_writer(u'"/>\n            <label for="email_')
                # SOURCE LINE 182
                __M_writer(conditional_websafe(op))
                __M_writer(u'" class="note">')
                __M_writer(conditional_websafe(_('we only send email at your request')))
                __M_writer(u'</label>\n')
                # SOURCE LINE 183
                if register:
                    # SOURCE LINE 184
                    __M_writer(u'              ')
                    __M_writer(conditional_websafe(error_field("BAD_EMAILS", "email", kind="span")))
                    __M_writer(u'\n')
                # SOURCE LINE 186
                __M_writer(u'          </li>\n')
            # SOURCE LINE 188
            __M_writer(u'          <li>\n            <label for="passwd_')
            # SOURCE LINE 189
            __M_writer(conditional_websafe(op))
            __M_writer(u'">')
            __M_writer(conditional_websafe(_('password')))
            __M_writer(u':</label>\n            <input id="passwd_')
            # SOURCE LINE 190
            __M_writer(conditional_websafe(op))
            __M_writer(u'" name="passwd" type="password" \n                   tabindex="')
            # SOURCE LINE 191
            __M_writer(conditional_websafe(tabindex))
            __M_writer(u'"/>\n')
            # SOURCE LINE 192
            if register:
                # SOURCE LINE 193
                __M_writer(u'              ')
                __M_writer(conditional_websafe(error_field("BAD_PASSWORD", "passwd", kind="span")))
                __M_writer(u'\n')
                # SOURCE LINE 194
            else:
                # SOURCE LINE 195
                __M_writer(u'              ')
                __M_writer(conditional_websafe(error_field("WRONG_PASSWORD", "passwd", kind="span")))
                __M_writer(u'\n')
            # SOURCE LINE 197
            __M_writer(u'          </li>\n')
            # SOURCE LINE 198
            if register:
                # SOURCE LINE 199
                __M_writer(u'          <li>\n            <label for="passwd2_')
                # SOURCE LINE 200
                __M_writer(conditional_websafe(op))
                __M_writer(u'">')
                __M_writer(conditional_websafe(_('verify password')))
                __M_writer(u':</label>\n            <input name="passwd2" id="passwd2_')
                # SOURCE LINE 201
                __M_writer(conditional_websafe(op))
                __M_writer(u'" \n                   type="password" tabindex="')
                # SOURCE LINE 202
                __M_writer(conditional_websafe(tabindex))
                __M_writer(u'"/>\n            ')
                # SOURCE LINE 203
                __M_writer(conditional_websafe(error_field("BAD_PASSWORD_MATCH", "passwd2", kind="span")))
                __M_writer(u'\n          </li>\n          <li>\n')
                # SOURCE LINE 206
                if not g.disable_captcha:
                    # SOURCE LINE 207
                    __M_writer(u'            ')
                    iden = hasattr(thing, "captcha") and thing.captcha.iden or '' 
                    
                    __M_writer(u'\n            ')
                    # SOURCE LINE 208
                    __M_writer(conditional_websafe(captchagen(iden, tabulate=True, label=False, size=30, tabindex=tabindex)))
                    __M_writer(u'\n')
                # SOURCE LINE 210
                __M_writer(u'          </li>\n')
            # SOURCE LINE 212
            __M_writer(u'        <li>\n          <input type="checkbox" name="rem" id="rem_')
            # SOURCE LINE 213
            __M_writer(conditional_websafe(op))
            __M_writer(u'" tabindex="')
            __M_writer(conditional_websafe(tabindex))
            __M_writer(u'" />\n          <label for="rem_')
            # SOURCE LINE 214
            __M_writer(conditional_websafe(op))
            __M_writer(u'" class="remember">\n            ')
            # SOURCE LINE 215
            __M_writer(conditional_websafe(_('remember me')))
            __M_writer(u'\n          </label>\n        </li>\n')
            # SOURCE LINE 218
            if not register:
                # SOURCE LINE 219
                __M_writer(u'        <li>\n          <a class="recover-password" href="/password">\n            ')
                # SOURCE LINE 221
                __M_writer(conditional_websafe(_("recover password")))
                __M_writer(u'\n          </a>\n        </li>\n')
            # SOURCE LINE 225
            __M_writer(u'      </ul>\n        <p class="submit">\n          <button type="submit" class="button" tabindex="')
            # SOURCE LINE 227
            __M_writer(conditional_websafe(tabindex))
            __M_writer(u'">\n            ')
            # SOURCE LINE 228
            __M_writer(conditional_websafe(register and _("sign up") or _("log in")))
            __M_writer(u'\n          </button>\n          <span class="throbber"></span>\n          <span class="status"></span>\n')
            # SOURCE LINE 232
            if register:
                # SOURCE LINE 233
                __M_writer(u'            ')
                __M_writer(conditional_websafe(error_field("RATELIMIT", "ratelimit")))
                __M_writer(u'\n            ')
                # SOURCE LINE 234
                __M_writer(conditional_websafe(error_field("RATELIMIT", "vdelay")))
                __M_writer(u'\n')
            # SOURCE LINE 236
            __M_writer(u'        </p>\n      </div>\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_login_panel(context,lf,user_reg='',user_login='',dest='',registration_info=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fde5fe6ba90')._populate(_import_ns, [u'error_field', u'img_link', u'form_group', u'text_with_links'])
        _mako_get_namespace(context, '__anon_0x7fde5fe6b9d0')._populate(_import_ns, [u'captchagen'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        text_with_links = _import_ns.get('text_with_links', context.get('text_with_links', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 243
        __M_writer(u'\n  ')
        # SOURCE LINE 244
        autofocus = (not thing.is_popup) 
        
        __M_writer(u'\n  <div class="split-panel">\n    <div class="split-panel-section split-panel-divider">\n      <h4 class="modal-title">')
        # SOURCE LINE 247
        __M_writer(conditional_websafe(_("create a new account")))
        __M_writer(u'</h4>\n      ')
        # SOURCE LINE 248
        __M_writer(conditional_websafe(lf(register=True, user=user_reg, dest=dest, autofocus=autofocus)))
        __M_writer(u'\n    </div>\n    <div class="split-panel-section">\n      <h4 class="modal-title">')
        # SOURCE LINE 251
        __M_writer(conditional_websafe(_("log in")))
        __M_writer(u'</h4>\n      ')
        # SOURCE LINE 252
        __M_writer(conditional_websafe(lf(user = user_login, dest = dest, autofocus=autofocus)))
        __M_writer(u'\n    </div>\n  </div>\n  <p class="login-disclaimer">\n    ')
        # SOURCE LINE 256
        __M_writer(conditional_websafe(text_with_links(
      _("By signing up, you agree to our %(policy)s."),
        policy=dict(link_text=_("Terms and Content Policy"), path="/r/SaidIt/comments/j1/the_saiditnet_terms_and_content_policy/"),    )))



        # SOURCE LINE 261
        __M_writer(u'\n  </p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


