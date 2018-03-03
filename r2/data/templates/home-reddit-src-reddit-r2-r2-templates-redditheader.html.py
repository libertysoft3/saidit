# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505002596.173328
_enable_loop = True
_template_filename = u'/home/reddit/src/reddit/r2/r2/templates/redditheader.html'
_template_uri = u'/redditheader.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23

from pylons import request
from r2.config import feature
from r2.lib.template_helpers import (
    add_sr,
    display_link_karma,
    format_number,
    header_url,
)
from r2.models import FakeSubreddit
from r2.models.subreddit import DefaultSR
from r2.lib.pages import SearchForm


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 36
    ns = runtime.TemplateNamespace('__anon_0x7fde6026a290', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fde6026a290')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fde6026a290')._populate(_import_ns, [u'plain_link', u'img_link', u'text_with_links', u'separator', u'logout'])
        img_link = _import_ns.get('img_link', context.get('img_link', UNDEFINED))
        text_with_links = _import_ns.get('text_with_links', context.get('text_with_links', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        separator = _import_ns.get('separator', context.get('separator', UNDEFINED))
        logout = _import_ns.get('logout', context.get('logout', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 35
        __M_writer(u'\n')
        # SOURCE LINE 36
        __M_writer(u'\n\n<div id="header" role="banner">\n  <a tabindex="1" href="#content" id="jumpToContent">')
        # SOURCE LINE 39
        __M_writer(conditional_websafe(_('jump to content')))
        __M_writer(u'</a>\n  ')
        # SOURCE LINE 40
        __M_writer(conditional_websafe(thing.srtopbar))
        __M_writer(u'\n  <div id="header-bottom-left">\n    ')
        # SOURCE LINE 42

        header_title = c.site.header_title
        d = thing.default_theme_sr
        
        if c.site.header and c.can_apply_styles and c.allow_styles and not (thing.no_sr_styles or c.site.quarantine):
            header_img = c.site.header
            header_size = c.site.header_size
        else:
            header_img = d.header
            header_size = d.header_size
            header_title = d.header_title
            
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['header_title','d','header_size','header_img'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 53
        __M_writer(u'\n    \n')
        # SOURCE LINE 55
        if header_img != g.default_header_url:
            # SOURCE LINE 56
            __M_writer(u'        ')
            __M_writer(conditional_websafe(img_link(c.site.name, header_url(header_img),
            '/', _id="header-img-a", img_id='header-img',
            title=header_title, size=header_size)))
            # SOURCE LINE 58
            __M_writer(u'\n')
            # SOURCE LINE 59
        else:
            # SOURCE LINE 60
            __M_writer(u'        <a href="/" id="header-img" class="default-header" title="')
            __M_writer(conditional_websafe(header_title))
            __M_writer(u'">')
            __M_writer(conditional_websafe(g.domain))
            __M_writer(u'</a>\n')
        # SOURCE LINE 62
        __M_writer(u'    \n')
        # SOURCE LINE 64
        __M_writer(u'    &nbsp;\n\n')
        # SOURCE LINE 66
        for toolbar in thing.toolbars:
            # SOURCE LINE 67
            __M_writer(u'      ')
            __M_writer(conditional_websafe(toolbar))
            __M_writer(u'\n')
        # SOURCE LINE 69
        __M_writer(u'  </div>\n\n  <div id="header-bottom-right">\n')
        # SOURCE LINE 72
        if not c.user_is_loggedin:
            # SOURCE LINE 73
            if thing.enable_login_cover and not g.read_only_mode:
                # SOURCE LINE 74
                __M_writer(u'      <span class="user">\n        ')
                # SOURCE LINE 75

                base = g.https_endpoint
                login_url = add_sr(base + "/login", sr_path=False)
                        
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['base','login_url'] if __M_key in __M_locals_builtin_stored]))
                # SOURCE LINE 78
                __M_writer(u'\n        ')
                # SOURCE LINE 79
                __M_writer(conditional_websafe(text_with_links(_("Want to join? %(login_or_register)s in seconds."),
            login_or_register = dict(link_text=_("Log in or sign up"), path=login_url, _class="login-required"))))
                # SOURCE LINE 80
                __M_writer(u'\n      </span>\n      ')
                # SOURCE LINE 82
                __M_writer(conditional_websafe(separator("|")))
                __M_writer(u'\n')
            # SOURCE LINE 84
        else:
            # SOURCE LINE 85
            if feature.is_enabled('beta_opt_in') and c.user.pref_beta:
                # SOURCE LINE 86
                __M_writer(u'        <div class="beta-hint help help-hoverable">\n          <a class="beta-link" href="/r/')
                # SOURCE LINE 87
                __M_writer(conditional_websafe(g.beta_sr))
                __M_writer(u'">beta</a>\n          <div id="beta-help" class="hover-bubble help-bubble anchor-top">\n            <div class="help-section">\n              <p>')
                # SOURCE LINE 90
                __M_writer(conditional_websafe(_("You're in beta mode! Thanks for helping to test reddit.")))
                __M_writer(u'</p>\n              <p>\n              ')
                # SOURCE LINE 92
                __M_writer(conditional_websafe(text_with_links(_("Please give feedback at %(beta_link)s, or %(learn_more_link)s."),
                  beta_link = dict(link_text="/r/" + g.beta_sr, path="/r/" + g.beta_sr),
                  learn_more_link = dict(link_text=_("learn more on the wiki"), path="/r/" + g.beta_sr + "/wiki")
                )))
                # SOURCE LINE 95
                __M_writer(u'\n              </p>\n            </div>\n          </div>\n        </div>\n')
            # SOURCE LINE 101
            __M_writer(u'      <span class="user">\n         ')
            # SOURCE LINE 102
            __M_writer(conditional_websafe(plain_link(c.user.name, "/user/%s/" % c.user.name, _sr_path=False)))
            __M_writer(u'\n         &nbsp;(<span class="userkarma" title="')
            # SOURCE LINE 103
            __M_writer(conditional_websafe(_("post karma")))
            __M_writer(u'">')
            __M_writer(conditional_websafe(format_number(display_link_karma(c.user.link_karma))))
            __M_writer(u'</span>)\n      </span>\n\n      ')
            # SOURCE LINE 106
            __M_writer(conditional_websafe(separator("|")))
            __M_writer(u'\n\n\n')
            # SOURCE LINE 109
            if c.have_messages:
                # SOURCE LINE 110
                __M_writer(u'        ')
                __M_writer(conditional_websafe(plain_link(_("messages"), path="/message/unread/", title=_("new mail!"), _class="havemail", _sr_path=False, _id="mail")))
                __M_writer(u'\n')
                # SOURCE LINE 111
                if c.user.inbox_count > 0:
                    # SOURCE LINE 112
                    __M_writer(u'          ')
                    __M_writer(conditional_websafe(plain_link(c.user.inbox_count, path="/message/unread/", _class="message-count", _sr_path=False)))
                    __M_writer(u'\n')
                # SOURCE LINE 114
            else:
                # SOURCE LINE 115
                __M_writer(u'        ')
                __M_writer(conditional_websafe(plain_link(_("messages"), path="/message/inbox/", title=_("no new mail"), _class="nohavemail", _sr_path=False, _id="mail")))
                __M_writer(u'\n')
            # SOURCE LINE 117
            __M_writer(u'      ')
            __M_writer(conditional_websafe(separator("|")))
            __M_writer(u'\n')
            # SOURCE LINE 118
            if c.user_is_loggedin and c.user.is_moderator_somewhere:
                # SOURCE LINE 119
                __M_writer(u'         ')

                if c.have_mod_messages:
                  mail_img_class = 'havemail'
                  mail_img_title = "new mod mail!"
                  mail_path = "/message/moderator/"
                else:
                  mail_img_class = 'nohavemail'
                  mail_img_title = "no new mod mail"
                  mail_path = "/message/moderator/"
                
                css_class = "%s access-required" % mail_img_class
                data_attrs = {'event-action': 'pageview', 'event-detail': 'modmail'}
                          
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['mail_path','data_attrs','mail_img_title','mail_img_class','css_class'] if __M_key in __M_locals_builtin_stored]))
                # SOURCE LINE 131
                __M_writer(u'\n         ')
                # SOURCE LINE 132
                __M_writer(conditional_websafe(plain_link(_("mod messages"), path=mail_path,
                    title = mail_img_title, _sr_path = False,
                    _id = "modmail", _class=css_class, data=data_attrs)))
                # SOURCE LINE 134
                __M_writer(u'\n         ')
                # SOURCE LINE 135
                __M_writer(conditional_websafe(separator("|")))
                __M_writer(u'\n')
        # SOURCE LINE 138
        __M_writer(u'    ')
        __M_writer(conditional_websafe(thing.corner_buttons()))
        __M_writer(u'\n')
        # SOURCE LINE 139
        if c.user_is_loggedin and g.auth_provider.is_logout_allowed():
            # SOURCE LINE 140
            __M_writer(u'      ')
            __M_writer(conditional_websafe(separator("|")))
            __M_writer(u'\n      ')
            # SOURCE LINE 141
            __M_writer(conditional_websafe(logout(dest=request.fullpath)))
            __M_writer(u'\n')
        # SOURCE LINE 143
        __M_writer(u'  </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


