# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505844486.617504
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/useriphistory.html'
_template_uri = '/useriphistory.html'
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
    ns = runtime.TemplateNamespace('__anon_0x7f211af895d0', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f211af895d0')] = ns

    # SOURCE LINE 25
    ns = runtime.TemplateNamespace(u'utils', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'utils')] = ns

    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7f211af896d0', context._clean_inheritance_tokens(), templateuri=u'prefapps.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f211af896d0')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f211af895d0')._populate(_import_ns, [u'error_field', u'timestamp'])
        _mako_get_namespace(context, '__anon_0x7f211af896d0')._populate(_import_ns, [u'authorized_app'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        utils = _mako_get_namespace(context, 'utils')
        authorized_app = _import_ns.get('authorized_app', context.get('authorized_app', UNDEFINED))
        timestamp = _import_ns.get('timestamp', context.get('timestamp', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n')
        # SOURCE LINE 24
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'\n\n')
        # SOURCE LINE 27

        from r2.lib.strings import strings
        ip_format = {'address': request.ip}
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['ip_format','strings'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 30
        __M_writer(u'\n\n<div id="account-activity" class="instructions">\n<h1>')
        # SOURCE LINE 33
        __M_writer(conditional_websafe(_("Recent activity on your account")))
        __M_writer(u'</h1>\n\n<p>')
        # SOURCE LINE 35
        __M_writer(conditional_websafe(strings.account_activity_blurb))
        __M_writer(u'</p>\n\n<p>')
        # SOURCE LINE 37
        __M_writer(conditional_websafe(strings.your_current_ip_is % ip_format))
        __M_writer(u'</p>\n<table>\n    <thead>\n        <tr>\n            <th>')
        # SOURCE LINE 41
        __M_writer(conditional_websafe(_("IP address")))
        __M_writer(u'</th>\n            <th>')
        # SOURCE LINE 42
        __M_writer(conditional_websafe(_("Location")))
        __M_writer(u'</th>\n            <th>')
        # SOURCE LINE 43
        __M_writer(conditional_websafe(_("Last Visit")))
        __M_writer(u'</th>\n            <th>')
        # SOURCE LINE 44
        __M_writer(conditional_websafe(_("Organization")))
        __M_writer(u'</th>\n        </tr>\n    </thead>\n    <tbody>\n')
        # SOURCE LINE 48
        for ip_data in thing.ips[:10]:
            # SOURCE LINE 49
            __M_writer(u'        ')
 
            ip, last_visit, location, org = ip_data[:4]
                    
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['ip','location','last_visit','org'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 51
            __M_writer(u'\n        <tr>\n            <td>')
            # SOURCE LINE 53
            __M_writer(conditional_websafe(ip))
            __M_writer(u'</td>\n            <td>')
            # SOURCE LINE 54
            __M_writer(conditional_websafe(location.get('country_name', '')))
            __M_writer(u'</td>\n            <td>')
            # SOURCE LINE 55
            __M_writer(conditional_websafe(timestamp(last_visit, live=True, include_tense=True)))
            __M_writer(u'</td>\n            <td>')
            # SOURCE LINE 56
            __M_writer(conditional_websafe(org))
            __M_writer(u'</td>\n        </tr>\n')
        # SOURCE LINE 59
        __M_writer(u'    </tbody>\n</table>\n</div>\n\n<hr/>\n\n<h1>')
        # SOURCE LINE 65
        __M_writer(conditional_websafe(_("Log out of all other sessions")))
        __M_writer(u'</h1>\n\n<form action="/post/clear_sessions" method="post"\n      onsubmit="return post_form(this, \'clear_sessions\')" id="clear_sessions">\n\n<div class="spacer">\n  ')
        def ccall(caller):
            def body():
                error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
                __M_writer = context.writer()
                # SOURCE LINE 71
                __M_writer(u'\n  <input type="password" name="curpass" />\n  ')
                # SOURCE LINE 73
                __M_writer(conditional_websafe(error_field("WRONG_PASSWORD", "curpass")))
                __M_writer(u'\n  ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 71
            __M_writer(conditional_websafe(utils.round_field(description=(_('(required)')),title=(_('current password')))))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 74
        __M_writer(u'\n</div>\n<button type="submit" class="btn">')
        # SOURCE LINE 76
        __M_writer(conditional_websafe(_('clear sessions')))
        __M_writer(u'</button>\n<span class="status error"></span>\n\n</form>\n\n')
        # SOURCE LINE 81
        if thing.my_apps:
            # SOURCE LINE 82
            __M_writer(u'  <hr/>\n  <div id="account-activity-apps" class="instructions">\n    <h1>')
            # SOURCE LINE 84
            __M_writer(conditional_websafe(_("Apps you have authorized")))
            __M_writer(u'</h1>\n    <p>')
            # SOURCE LINE 85
            __M_writer(conditional_websafe(strings.account_activity_apps_blurb))
            __M_writer(u'</p>\n')
            # SOURCE LINE 86
            for app_data in thing.my_apps.values():
                # SOURCE LINE 87
                __M_writer(u'      ')
                __M_writer(conditional_websafe(authorized_app(app_data)))
                __M_writer(u'\n')
            # SOURCE LINE 89
            __M_writer(u'  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


