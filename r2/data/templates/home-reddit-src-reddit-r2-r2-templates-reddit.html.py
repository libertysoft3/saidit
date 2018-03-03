# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1520060828.964822
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/reddit.html'
_template_uri = '/reddit.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['global_stylesheets', 'javascript_bottom', 'Title', 'javascript', 'sr_stylesheets', 'stylesheet', 'bodyContent', 'pagemeta', 'sidebar', 'extra_stylesheets']


# SOURCE LINE 23

from r2.config import feature
from r2.lib.template_helpers import add_sr, static, join_urls, class_dict, get_domain
from r2.lib.filters import unsafe, scriptsafe_dumps
from r2.lib.pages import (
   SearchForm,
   ClickGadget,
   SideContentBox,
   Login,
   ListingChooser,
   InTimeoutInterstitial,
)
from r2.lib import tracking
from pylons import request
from r2.lib.strings import strings
from r2.models import make_feedurl


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 41
    ns = runtime.TemplateNamespace('__anon_0x7fc7c7a45ad0', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fc7c7a45ad0')] = ns

    # SOURCE LINE 42
    ns = runtime.TemplateNamespace('__anon_0x7fc7c7b5f950', context._clean_inheritance_tokens(), templateuri=u'adminbar.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fc7c7b5f950')] = ns

    # SOURCE LINE 40
    ns = runtime.TemplateNamespace('__anon_0x7fc7c7a45d50', context._clean_inheritance_tokens(), templateuri=u'less.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fc7c7a45d50')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7a45ad0')._populate(_import_ns, [u'tags', u'classes'])
        _mako_get_namespace(context, '__anon_0x7fc7c7b5f950')._populate(_import_ns, [u'adminbar_stylesheet'])
        _mako_get_namespace(context, '__anon_0x7fc7c7a45d50')._populate(_import_ns, [u'less_js', u'less_stylesheet'])
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 39
        __M_writer(u'\n')
        # SOURCE LINE 40
        __M_writer(u'\n')
        # SOURCE LINE 41
        __M_writer(u'\n')
        # SOURCE LINE 42
        __M_writer(u'\n')
        # SOURCE LINE 43
        __M_writer(u'\n\n')
        # SOURCE LINE 51
        __M_writer(u'\n\n')
        # SOURCE LINE 64
        __M_writer(u'\n\n')
        # SOURCE LINE 75
        __M_writer(u'\n\n')
        # SOURCE LINE 82
        __M_writer(u'\n\n')
        # SOURCE LINE 113
        __M_writer(u'\n\n')
        # SOURCE LINE 119
        __M_writer(u'\n\n')
        # SOURCE LINE 131
        __M_writer(u'\n\n')
        # SOURCE LINE 140
        __M_writer(u'\n\n')
        # SOURCE LINE 222
        __M_writer(u'\n\n')
        # SOURCE LINE 226
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_global_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7a45ad0')._populate(_import_ns, [u'tags', u'classes'])
        _mako_get_namespace(context, '__anon_0x7fc7c7b5f950')._populate(_import_ns, [u'adminbar_stylesheet'])
        _mako_get_namespace(context, '__anon_0x7fc7c7a45d50')._populate(_import_ns, [u'less_js', u'less_stylesheet'])
        less_stylesheet = _import_ns.get('less_stylesheet', context.get('less_stylesheet', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 53
        __M_writer(u'\n  ')
        # SOURCE LINE 54
        __M_writer(conditional_websafe(less_stylesheet("reddit.less")))
        __M_writer(u'\n')
        # SOURCE LINE 55
        if getattr(thing, "feature_new_expando_icons", False):
            # SOURCE LINE 56
            __M_writer(u'    ')
            __M_writer(conditional_websafe(less_stylesheet("expando.less")))
            __M_writer(u'\n')
        # SOURCE LINE 58
        __M_writer(u'\n')
        # SOURCE LINE 60
        __M_writer(u'  ')
        __M_writer(conditional_websafe(less_stylesheet("theme-custom.less")))
        __M_writer(u'\n')
        # SOURCE LINE 61
        if getattr(thing, "chat_include_css", False):
            # SOURCE LINE 62
            __M_writer(u'    ')
            __M_writer(conditional_websafe(less_stylesheet("feature-chat.less")))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascript_bottom(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7a45ad0')._populate(_import_ns, [u'tags', u'classes'])
        _mako_get_namespace(context, '__anon_0x7fc7c7b5f950')._populate(_import_ns, [u'adminbar_stylesheet'])
        _mako_get_namespace(context, '__anon_0x7fc7c7a45d50')._populate(_import_ns, [u'less_js', u'less_stylesheet'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 133
        __M_writer(u'\n  ')
        # SOURCE LINE 134
        from r2.lib import js 
        
        __M_writer(u'\n  ')
        # SOURCE LINE 135
        __M_writer(conditional_websafe(unsafe(js.use('reddit'))))
        __M_writer(u'\n')
        # SOURCE LINE 136
        if getattr(thing, "feature_expando_nsfw_flow", False):
            # SOURCE LINE 137
            __M_writer(u'    ')
            __M_writer(conditional_websafe(unsafe(js.use("expando-nsfw-flow"))))
            __M_writer(u'\n')
        # SOURCE LINE 139
        __M_writer(u'  ')
        __M_writer(conditional_websafe(unsafe(c.js_preload.use())))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_Title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7a45ad0')._populate(_import_ns, [u'tags', u'classes'])
        _mako_get_namespace(context, '__anon_0x7fc7c7b5f950')._populate(_import_ns, [u'adminbar_stylesheet'])
        _mako_get_namespace(context, '__anon_0x7fc7c7a45d50')._populate(_import_ns, [u'less_js', u'less_stylesheet'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 45
        __M_writer(u'\n')
        # SOURCE LINE 46
        if thing.title:
            # SOURCE LINE 47
            __M_writer(u'    ')
            __M_writer(conditional_websafe(thing.title))
            __M_writer(u'\n')
            # SOURCE LINE 48
        else:
            # SOURCE LINE 49
            __M_writer(u'    ')
            __M_writer(conditional_websafe(parent.Title()))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascript(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7a45ad0')._populate(_import_ns, [u'tags', u'classes'])
        _mako_get_namespace(context, '__anon_0x7fc7c7b5f950')._populate(_import_ns, [u'adminbar_stylesheet'])
        _mako_get_namespace(context, '__anon_0x7fc7c7a45d50')._populate(_import_ns, [u'less_js', u'less_stylesheet'])
        less_js = _import_ns.get('less_js', context.get('less_js', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 121
        __M_writer(u'\n  ')
        # SOURCE LINE 122
        from r2.lib import js 
        
        __M_writer(u'\n  <!--[if gte IE 9]> <!-->\n    ')
        # SOURCE LINE 124
        __M_writer(conditional_websafe(unsafe(js.use('reddit-init'))))
        __M_writer(u'\n  <!-- <![endif]-->\n\n  <!--[if lt IE 9]>\n    ')
        # SOURCE LINE 128
        __M_writer(conditional_websafe(unsafe(js.use('reddit-init-legacy'))))
        __M_writer(u'\n  <![endif]-->\n  ')
        # SOURCE LINE 130
        __M_writer(conditional_websafe(less_js()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sr_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7a45ad0')._populate(_import_ns, [u'tags', u'classes'])
        _mako_get_namespace(context, '__anon_0x7fc7c7b5f950')._populate(_import_ns, [u'adminbar_stylesheet'])
        _mako_get_namespace(context, '__anon_0x7fc7c7a45d50')._populate(_import_ns, [u'less_js', u'less_stylesheet'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 66
        __M_writer(u'\n')
        # SOURCE LINE 67
        if thing.subreddit_stylesheet_url:
            # SOURCE LINE 68
            __M_writer(u'    <!--[if gte IE 8]> <!-->\n    <link rel="stylesheet"\n          href="')
            # SOURCE LINE 70
            __M_writer(conditional_websafe(thing.subreddit_stylesheet_url))
            __M_writer(u'"\n          title="applied_subreddit_stylesheet"\n          type="text/css">\n    <!-- <![endif]-->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheet(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7a45ad0')._populate(_import_ns, [u'tags', u'classes'])
        _mako_get_namespace(context, '__anon_0x7fc7c7b5f950')._populate(_import_ns, [u'adminbar_stylesheet'])
        _mako_get_namespace(context, '__anon_0x7fc7c7a45d50')._populate(_import_ns, [u'less_js', u'less_stylesheet'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 115
        __M_writer(u'\n  ')
        # SOURCE LINE 116
        __M_writer(conditional_websafe(self.global_stylesheets()))
        __M_writer(u'\n  ')
        # SOURCE LINE 117
        __M_writer(conditional_websafe(self.sr_stylesheets()))
        __M_writer(u'\n  ')
        # SOURCE LINE 118
        __M_writer(conditional_websafe(self.extra_stylesheets()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bodyContent(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7a45ad0')._populate(_import_ns, [u'tags', u'classes'])
        _mako_get_namespace(context, '__anon_0x7fc7c7b5f950')._populate(_import_ns, [u'adminbar_stylesheet'])
        _mako_get_namespace(context, '__anon_0x7fc7c7a45d50')._populate(_import_ns, [u'less_js', u'less_stylesheet'])
        tags = _import_ns.get('tags', context.get('tags', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        classes = _import_ns.get('classes', context.get('classes', UNDEFINED))
        def sidebar(content=None):
            return render_sidebar(context,content)
        __M_writer = context.writer()
        # SOURCE LINE 142
        __M_writer(u'\n')
        # SOURCE LINE 143
        if thing.header:
            # SOURCE LINE 144
            __M_writer(u'    ')
            runtime._include_file(context, u'adminbar.html', _template_uri)
            __M_writer(u'\n    ')
            # SOURCE LINE 145
            runtime._include_file(context, u'redditheader.html', _template_uri)
            __M_writer(u'\n')
        # SOURCE LINE 147
        __M_writer(u'\n')
        # SOURCE LINE 148
        if thing.show_sidebar:
            # SOURCE LINE 149
            __M_writer(u'    <div class="side')
            __M_writer(conditional_websafe(" side-chat" if thing.show_sidebar_chat else ""))
            __M_writer(u' ')
            __M_writer(conditional_websafe(c.user.pref_chat_sidebar_size if thing.show_sidebar_chat else ""))
            __M_writer(u'">\n      ')
            # SOURCE LINE 150
            __M_writer(conditional_websafe(sidebar(content = thing.rightbox())))
            __M_writer(u'\n    </div>\n')
        # SOURCE LINE 153
        __M_writer(u'\n')
        # SOURCE LINE 154
        if thing.show_chooser:
            # SOURCE LINE 155
            __M_writer(u'    ')
            __M_writer(conditional_websafe(ListingChooser()))
            __M_writer(u'\n')
        # SOURCE LINE 157
        __M_writer(u'\n')
        # SOURCE LINE 158
        if thing.auction_announcement:
            # SOURCE LINE 159
            __M_writer(u'    <div id="auction-announcement-container">\n      <div id="auction-announcement">\n        <h1>\n          ad auctions are launching monday 2/8\n        </h1>\n        <p>\n          for more details, see our&nbsp;<a href="https://www.reddit.com/r/selfserve/comments/434c0x/the_auction_is_coming/" target="_blank">announcement in /r/selfserve</a>\n        </p>\n      </div>\n    </div>\n')
        # SOURCE LINE 170
        __M_writer(u'\n  ')
        # SOURCE LINE 171
        content = getattr(self, "content", None) or thing.content 
        
        __M_writer(u'\n')
        # SOURCE LINE 172
        if content:
            # SOURCE LINE 175
            __M_writer(u'    <a name="content"></a>\n    <div ')
            # SOURCE LINE 176
            __M_writer(conditional_websafe(tags(id=thing.content_id)))
            __M_writer(u' ')
            __M_writer(conditional_websafe(classes("content", thing.css_class)))
            __M_writer(u' role="main">\n      ')
            # SOURCE LINE 177
            __M_writer(conditional_websafe(content()))
            __M_writer(u'\n    </div>\n')
        # SOURCE LINE 180
        __M_writer(u'\n  ')
        # SOURCE LINE 181
        __M_writer(conditional_websafe(thing.footer))
        __M_writer(u'\n\n')
        # SOURCE LINE 183
        if not c.user_is_loggedin and not g.read_only_mode:
            # SOURCE LINE 184
            if thing.enable_login_cover:
                # SOURCE LINE 185
                __M_writer(u'      <script>\n        var BETA_HOST = \'beta.reddit.com\';\n        if (location.host === BETA_HOST) {\n          r.config.https_endpoint = \'https://\' + BETA_HOST;\n        }\n      </script>\n      <script id="login-popup" type="text/template">\n        ')
                # SOURCE LINE 192
                __M_writer(conditional_websafe(Login(is_popup=True)))
                __M_writer(u'\n      </script>\n')
            # SOURCE LINE 195
            __M_writer(u'    <script id="lang-popup" type="text/template">\n      ')
            # SOURCE LINE 196
            runtime._include_file(context, u'prefoptions.html', _template_uri)
            __M_writer(u'\n    </script>\n')
        # SOURCE LINE 199
        if c.secure:
            # SOURCE LINE 201
            __M_writer(u'      <img id="hsts_pixel" src="//')
            __M_writer(conditional_websafe(g.domain))
            __M_writer(u'/static/pixel.png">\n')
        # SOURCE LINE 203
        if feature.is_enabled("test_https_certs"):
            # SOURCE LINE 204
            __M_writer(u'    ')
            from r2.lib import js 
            
            __M_writer(u'\n    ')
            # SOURCE LINE 205
            __M_writer(conditional_websafe(unsafe(js.use("https-tester"))))
            __M_writer(u'\n    ')
            # SOURCE LINE 206

            cur_proto = ("https:" if c.secure else "http:")
            https_test_config = {
                "runName": g.live_config.get("https_cert_testing_run_name"),
                "controlImg": cur_proto + g.live_config.get("https_cert_testing_img_control"),
                "testImg": g.live_config.get("https_cert_testing_img_test"),
                "logPixel": cur_proto + g.httpstracker_url,
            }
            
            
            # SOURCE LINE 214
            __M_writer(u'\n    <script type="text/javascript">\n    if(Math.random() < ')
            # SOURCE LINE 216
            __M_writer(conditional_websafe(scriptsafe_dumps(g.live_config.get("https_cert_testing_probability"))))
            __M_writer(u') {\n        runHTTPSCertTest(')
            # SOURCE LINE 217
            __M_writer(conditional_websafe(scriptsafe_dumps(https_test_config)))
            __M_writer(u');\n    }\n    </script>\n')
        # SOURCE LINE 221
        __M_writer(u'  ')
        __M_writer(conditional_websafe(thing.debug_footer))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_pagemeta(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7a45ad0')._populate(_import_ns, [u'tags', u'classes'])
        _mako_get_namespace(context, '__anon_0x7fc7c7b5f950')._populate(_import_ns, [u'adminbar_stylesheet'])
        _mako_get_namespace(context, '__anon_0x7fc7c7a45d50')._populate(_import_ns, [u'less_js', u'less_stylesheet'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 84
        __M_writer(u'\n')
        # SOURCE LINE 85
        if hasattr(thing, "shortlink"):
            # SOURCE LINE 86
            __M_writer(u'    <link rel="shorturl" href="https://')
            __M_writer(conditional_websafe(thing.shortlink))
            __M_writer(u'"/>\n')
        # SOURCE LINE 88
        __M_writer(u'\n')
        # SOURCE LINE 89
        if hasattr(thing, "og_data"):
            # SOURCE LINE 90
            for (og_property, og_value) in thing.og_data.iteritems():
                # SOURCE LINE 91
                __M_writer(u'      <meta property="og:')
                __M_writer(conditional_websafe(og_property))
                __M_writer(u'" content="')
                __M_writer(conditional_websafe(og_value))
                __M_writer(u'">\n')
        # SOURCE LINE 94
        __M_writer(u'\n')
        # SOURCE LINE 95
        if hasattr(thing, "twitter_card"):
            # SOURCE LINE 96
            for (twitter_card_property, twitter_card_value) in thing.twitter_card.iteritems():
                # SOURCE LINE 97
                __M_writer(u'      <meta property="twitter:')
                __M_writer(conditional_websafe(twitter_card_property))
                __M_writer(u'" content="')
                __M_writer(conditional_websafe(twitter_card_value))
                __M_writer(u'">\n')
        # SOURCE LINE 100
        __M_writer(u'\n  <link rel=\'icon\' href="')
        # SOURCE LINE 101
        __M_writer(conditional_websafe(static('icon.png')))
        __M_writer(u'" sizes="256x256" type="image/png" />\n  <link rel=\'shortcut icon\' href="')
        # SOURCE LINE 102
        __M_writer(conditional_websafe(static('favicon.ico')))
        __M_writer(u'" type="image/x-icon" />\n  <link rel=\'apple-touch-icon-precomposed\' href="')
        # SOURCE LINE 103
        __M_writer(conditional_websafe(static('icon-touch.png')))
        __M_writer(u'" />\n')
        # SOURCE LINE 104
        if thing.extension_handling:
            # SOURCE LINE 105
            __M_writer(u'    ')

            rss = add_sr(join_urls(request.path,'.rss'))
            if thing.extension_handling == "private":
               rss = make_feedurl(c.user, rss)
                 
            
            # SOURCE LINE 109
            __M_writer(u'\n    <link rel="alternate" type="application/atom+xml" title="RSS"\n          href="')
            # SOURCE LINE 111
            __M_writer(conditional_websafe(rss))
            __M_writer(u'" />\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sidebar(context,content=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7a45ad0')._populate(_import_ns, [u'tags', u'classes'])
        _mako_get_namespace(context, '__anon_0x7fc7c7b5f950')._populate(_import_ns, [u'adminbar_stylesheet'])
        _mako_get_namespace(context, '__anon_0x7fc7c7a45d50')._populate(_import_ns, [u'less_js', u'less_stylesheet'])
        __M_writer = context.writer()
        # SOURCE LINE 224
        __M_writer(u'\n  ')
        # SOURCE LINE 225
        __M_writer(conditional_websafe(content))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7a45ad0')._populate(_import_ns, [u'tags', u'classes'])
        _mako_get_namespace(context, '__anon_0x7fc7c7b5f950')._populate(_import_ns, [u'adminbar_stylesheet'])
        _mako_get_namespace(context, '__anon_0x7fc7c7a45d50')._populate(_import_ns, [u'less_js', u'less_stylesheet'])
        adminbar_stylesheet = _import_ns.get('adminbar_stylesheet', context.get('adminbar_stylesheet', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        less_stylesheet = _import_ns.get('less_stylesheet', context.get('less_stylesheet', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 77
        __M_writer(u'\n  ')
        # SOURCE LINE 78
        __M_writer(conditional_websafe(adminbar_stylesheet()))
        __M_writer(u'\n')
        # SOURCE LINE 79
        for extra_stylesheet in getattr(thing, 'extra_stylesheets', ()):
            # SOURCE LINE 80
            __M_writer(u'    ')
            __M_writer(conditional_websafe(less_stylesheet(extra_stylesheet)))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


