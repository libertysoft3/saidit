# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505002596.235313
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/loginformwide.html'
_template_uri = '/loginformwide.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23

from r2.lib.template_helpers import add_sr
from r2.lib.utils import UrlParser
import random


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 29
    ns = runtime.TemplateNamespace('__anon_0x7fde603adc10', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fde603adc10')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fde603adc10')._populate(_import_ns, [u'error_field'])
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 27
        __M_writer(u'\n\n')
        # SOURCE LINE 29
        __M_writer(u'\n\n')
        # SOURCE LINE 31

        op = "login-main"
        base = g.https_endpoint
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['base','op'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 34
        __M_writer(u'\n<form method="post"\n      action="')
        # SOURCE LINE 36
        __M_writer(conditional_websafe(add_sr(base + '/post/login')))
        __M_writer(u'"\n      id="login_')
        # SOURCE LINE 37
        __M_writer(conditional_websafe(op))
        __M_writer(u'"\n      class="login-form login-form-side">\n  <input type="hidden" name="op" value="')
        # SOURCE LINE 39
        __M_writer(conditional_websafe(op))
        __M_writer(u'" />\n  <input name="user" placeholder="')
        # SOURCE LINE 40
        __M_writer(conditional_websafe(_('username')))
        __M_writer(u'" type="text" maxlength="20" tabindex="1"/>\n  <input name="passwd" placeholder="')
        # SOURCE LINE 41
        __M_writer(conditional_websafe(_('password')))
        __M_writer(u'" type="password" tabindex="1"/>\n\n  <div class="status"></div>\n\n  <div id="remember-me">\n    <input type="checkbox" name="rem" id="rem-')
        # SOURCE LINE 46
        __M_writer(conditional_websafe(op))
        __M_writer(u'" tabindex="1" />\n    <label for="rem-')
        # SOURCE LINE 47
        __M_writer(conditional_websafe(op))
        __M_writer(u'">')
        __M_writer(conditional_websafe(_("remember me")))
        __M_writer(u'</label>\n    <a class="recover-password" href="/password">')
        # SOURCE LINE 48
        __M_writer(conditional_websafe(_("reset password")))
        __M_writer(u'</a>\n  </div>\n\n  <div class="submit">\n    <span class="throbber"></span>\n    <button class="btn" type="submit" tabindex="1">')
        # SOURCE LINE 53
        __M_writer(conditional_websafe(_("login")))
        __M_writer(u'</button>\n  </div>\n  \n  <div class="clear"></div>\n</form>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


