# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505029547.650417
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/password.html'
_template_uri = '/password.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 24
    ns = runtime.TemplateNamespace(u'utils', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'utils')] = ns

    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7fb219dfe1d0', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fb219dfe1d0')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fb219dfe1d0')._populate(_import_ns, [u'error_field'])
        utils = _mako_get_namespace(context, 'utils')
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n')
        # SOURCE LINE 24
        __M_writer(u'\n\n<form id="passform" action="/api/password" method="post"\n      class="content"\n      onsubmit="return post_form(this, \'password\');">\n  <h1>')
        # SOURCE LINE 29
        __M_writer(conditional_websafe(_("reset your password")))
        __M_writer(u'</h1>\n  <p>')
        # SOURCE LINE 30
        __M_writer(conditional_websafe(_("enter your username below and we'll email you a link to reset your password")))
        __M_writer(u'</p>\n')
        # SOURCE LINE 31
        if request.params.get('expired'):
            # SOURCE LINE 32
            __M_writer(u'    <span class="error">\n      ')
            # SOURCE LINE 33
            __M_writer(conditional_websafe(_("password reset link expired. please try again")))
            __M_writer(u'\n    </span>\n')
        # SOURCE LINE 36
        __M_writer(u'\n<div class="spacer">\n  ')
        def ccall(caller):
            def body():
                error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
                __M_writer = context.writer()
                # SOURCE LINE 38
                __M_writer(u'\n    <input type="text" name="name" maxlength="20"/>\n    ')
                # SOURCE LINE 40
                __M_writer(conditional_websafe(error_field("USER_DOESNT_EXIST", "name")))
                __M_writer(u'\n    ')
                # SOURCE LINE 41
                __M_writer(conditional_websafe(error_field("NO_EMAIL_FOR_USER", "name")))
                __M_writer(u'\n    ')
                # SOURCE LINE 42
                __M_writer(conditional_websafe(error_field("RATELIMIT", "ratelimit")))
                __M_writer(u'\n  ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 38
            __M_writer(conditional_websafe(utils.round_field(title=(_('username')))))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 43
        __M_writer(u'\n</div>\n\n<button type="submit" class="btn">')
        # SOURCE LINE 46
        __M_writer(conditional_websafe(_("email me")))
        __M_writer(u'</button>\n<span class="status"></span>\n\n</form>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


