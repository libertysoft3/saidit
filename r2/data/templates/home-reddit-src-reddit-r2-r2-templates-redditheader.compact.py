# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1508303897.791171
_enable_loop = True
_template_filename = u'/home/reddit/src/reddit/r2/r2/templates/redditheader.compact'
_template_uri = u'/redditheader.compact'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23

from r2.lib.template_helpers import display_link_karma, header_url
from r2.models.subreddit import DefaultSR, FakeSubreddit

 

def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 28
    ns = runtime.TemplateNamespace('__anon_0x7f4dec5a5a90', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f4dec5a5a90')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f4dec5a5a90')._populate(_import_ns, [u'plain_link', u'img_link', u'separator', u'logout'])
        img_link = _import_ns.get('img_link', context.get('img_link', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        logout = _import_ns.get('logout', context.get('logout', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 27
        __M_writer(u'\n')
        # SOURCE LINE 28
        __M_writer(u'\n\n')
        # SOURCE LINE 30

        from r2.lib.menus import PageNameNav
        toolbars = thing.toolbars
        nav = "mobile"
        if toolbars and isinstance(toolbars[0], PageNameNav):
            nav = toolbars[0]
            toolbars = toolbars[1:]
        nav = thing.short_title or nav
         
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['toolbars','nav','PageNameNav'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 38
        __M_writer(u'\n<div id="preload">\n    <div class="commentcount"><div class="comments"></div><div class="comments preloaded"></div></div>\n</div>\n<div id="topbar">\n  <div class="left">\n   ')
        # SOURCE LINE 44

        d = DefaultSR()
        if c.site.header and c.allow_styles and not c.site.quarantine:
            header_img = header_url(c.site.header)
            header_size = c.site.header_size
            header_title = c.site.header_title
        else:
            header_img = header_url(d.header)
            header_size = None
            header_title = d.header_title
            
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['header_title','d','header_size','header_img'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 54
        __M_writer(u'\n    ')
        # SOURCE LINE 55
        __M_writer(conditional_websafe(img_link(c.site.name, header_img, '/', _id = "header-img-a", img_id = 'header-img', title = header_title, size = header_size)))
        __M_writer(u'\n  </div>\n  <h1>')
        # SOURCE LINE 57
        __M_writer(conditional_websafe(nav))
        __M_writer(u'</h1>\n  <div class="right">\n')
        # SOURCE LINE 59
        if c.user_is_loggedin:
            # SOURCE LINE 60
            __M_writer(u'      ')

            if c.have_messages:
              mail_img_class = 'havemail'
              mail_path = '/message/unread/'
            else:
              mail_img_class = 'nohavemail'
              mail_path = '/message/inbox/'
                  
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['mail_path','mail_img_class'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 67
            __M_writer(u'\n      ')
            # SOURCE LINE 68
            __M_writer(conditional_websafe(plain_link('', mail_path, _sr_path=False, _class=mail_img_class, _id='mail')))
            __M_writer(u'\n')
            # SOURCE LINE 69
            if c.user_is_loggedin and c.user.is_moderator_somewhere:
                # SOURCE LINE 70
                __M_writer(u'        ')

                mail_path = '/message/moderator/'
                if c.have_mod_messages:
                    mail_img_class = 'havemail'
                else:
                    mail_img_class = 'nohavemail'
                        
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['mail_path','mail_img_class'] if __M_key in __M_locals_builtin_stored]))
                # SOURCE LINE 76
                __M_writer(u'\n        ')
                # SOURCE LINE 77
                __M_writer(conditional_websafe(plain_link('', mail_path, _sr_path=False, _class=mail_img_class, _id='modmail')))
                __M_writer(u'\n')
        # SOURCE LINE 80
        __M_writer(u'    <a class="topbar-options" href="#" id="topmenu_toggle"></a>\n  </div>\n  <div id="top_menu">\n')
        # SOURCE LINE 83
        if c.user_is_loggedin:
            # SOURCE LINE 84
            __M_writer(u'    <div class="menuitem">\n      ')
            # SOURCE LINE 85
            __M_writer(conditional_websafe(plain_link(c.user.name, "/user/%s/" % c.user.name, _sr_path=False)))
            __M_writer(u'\n      &nbsp;(<b>')
            # SOURCE LINE 86
            __M_writer(conditional_websafe(display_link_karma(c.user.link_karma)))
            __M_writer(u'</b>)\n    </div>\n    <div class="menuitem">\n      ')
            # SOURCE LINE 89
            __M_writer(conditional_websafe(plain_link("subreddits", "/subreddits/mine", _sr_path=False)))
            __M_writer(u'\n    </div>\n    <div class="menuitem">\n      ')
            # SOURCE LINE 92
            __M_writer(conditional_websafe(plain_link("submit", "/submit", _sr_path=False)))
            __M_writer(u'\n    </div>\n')
            # SOURCE LINE 94
            if g.auth_provider.is_logout_allowed():
                # SOURCE LINE 95
                __M_writer(u'    <div class="menuitem bottm-bar">\n      ')
                # SOURCE LINE 96
                __M_writer(conditional_websafe(logout(dest=request.fullpath)))
                __M_writer(u'\n    </div>\n')
            # SOURCE LINE 99
        else:
            # SOURCE LINE 100
            __M_writer(u'    <div class="menuitem">\n      ')
            # SOURCE LINE 101
            __M_writer(conditional_websafe(plain_link("log in", "/login", _sr_path=False)))
            __M_writer(u'\n    </div>\n    <div class="menuitem bottm-bar">\n      ')
            # SOURCE LINE 104
            __M_writer(conditional_websafe(plain_link("sign up", "/register", _sr_path=False)))
            __M_writer(u'\n    </div>\n    <div class="menuitem">\n      ')
            # SOURCE LINE 107
            __M_writer(conditional_websafe(plain_link("subreddits", "/subreddits/", _sr_path=False)))
            __M_writer(u'\n    </div>\n')
        # SOURCE LINE 110
        __M_writer(u'    <div class="menuitem">\n      ')
        # SOURCE LINE 111
        __M_writer(conditional_websafe(plain_link("search", "/search")))
        __M_writer(u'\n    </div>\n')
        # SOURCE LINE 113
        if not isinstance(c.site, FakeSubreddit):
            # SOURCE LINE 114
            __M_writer(u'    <div class="menuitem">\n      ')
            # SOURCE LINE 115
            __M_writer(conditional_websafe(plain_link("sidebar", "/about/sidebar")))
            __M_writer(u'\n    </div>\n')
        # SOURCE LINE 118
        __M_writer(u'  </div>\n</div>\n')
        # SOURCE LINE 120
        if toolbars:
            # SOURCE LINE 121
            __M_writer(u'  <div class="subtoolbar">\n')
            # SOURCE LINE 122
            for toolbar in toolbars:
                # SOURCE LINE 123
                __M_writer(u'      ')
                __M_writer(conditional_websafe(toolbar))
                __M_writer(u'\n')
            # SOURCE LINE 125
            __M_writer(u'  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


