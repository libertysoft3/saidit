# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1508303897.859676
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/link.compact'
_template_uri = '/link.compact'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['hide_button', 'save_button', 'flair']


# SOURCE LINE 23

from r2.config import feature
from r2.lib.template_helpers import add_sr
from r2.lib.template_helpers import make_url_protocol_relative
import urllib
from r2.lib.filters import _force_unicode, _force_utf8
 

def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 33
    ns = runtime.TemplateNamespace('__anon_0x7f4de7da0710', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f4de7da0710')] = ns

    # SOURCE LINE 31
    ns = runtime.TemplateNamespace('__anon_0x7f4de7da0550', context._clean_inheritance_tokens(), templateuri=u'printable.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f4de7da0550')] = ns

    # SOURCE LINE 35
    ns = runtime.TemplateNamespace('__anon_0x7f4de7da0e90', context._clean_inheritance_tokens(), templateuri=u'printablebuttons.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f4de7da0e90')] = ns

    # SOURCE LINE 32
    ns = runtime.TemplateNamespace('__anon_0x7f4de7da0d50', context._clean_inheritance_tokens(), templateuri=u'link.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f4de7da0d50')] = ns

    # SOURCE LINE 34
    ns = runtime.TemplateNamespace('__anon_0x7f4de7da05d0', context._clean_inheritance_tokens(), templateuri=u'utils.compact', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f4de7da05d0')] = ns

    # SOURCE LINE 30
    ns = runtime.TemplateNamespace('__anon_0x7f4de7b882d0', context._clean_inheritance_tokens(), templateuri=u'printable.compact', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f4de7b882d0')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f4de7da0710')._populate(_import_ns, [u'plain_link', u'nsfw_stamp', u'quarantine_stamp'])
        _mako_get_namespace(context, '__anon_0x7f4de7da0550')._populate(_import_ns, [u'arrow', u'score'])
        _mako_get_namespace(context, '__anon_0x7f4de7da0e90')._populate(_import_ns, [u'state_button'])
        _mako_get_namespace(context, '__anon_0x7f4de7da0d50')._populate(_import_ns, [u'tagline', u'thumbnail'])
        _mako_get_namespace(context, '__anon_0x7f4de7da05d0')._populate(_import_ns, [u'icon_button', u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f4de7b882d0')._populate(_import_ns, [u'delete_report_buttons'])
        icon_button = _import_ns.get('icon_button', context.get('icon_button', UNDEFINED))
        tagline = _import_ns.get('tagline', context.get('tagline', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        quarantine_stamp = _import_ns.get('quarantine_stamp', context.get('quarantine_stamp', UNDEFINED))
        arrow = _import_ns.get('arrow', context.get('arrow', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        thumbnail = _import_ns.get('thumbnail', context.get('thumbnail', UNDEFINED))
        nsfw_stamp = _import_ns.get('nsfw_stamp', context.get('nsfw_stamp', UNDEFINED))
        def flair():
            return render_flair(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 29
        __M_writer(u'\n')
        # SOURCE LINE 30
        __M_writer(u'\n')
        # SOURCE LINE 31
        __M_writer(u'\n')
        # SOURCE LINE 32
        __M_writer(u'\n')
        # SOURCE LINE 33
        __M_writer(u'\n')
        # SOURCE LINE 34
        __M_writer(u'\n')
        # SOURCE LINE 35
        __M_writer(u'\n\n')
        # SOURCE LINE 41
        __M_writer(u'\n\n')
        # SOURCE LINE 43

        div_class = "thing link id-%s" % thing._fullname
        if thing.use_sticky_style:
            div_class += " stickied"
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['div_class'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 47
        __M_writer(u'\n<div class="')
        # SOURCE LINE 48
        __M_writer(conditional_websafe(div_class))
        __M_writer(u'">\n  <span class="rank">\n    ')
        # SOURCE LINE 50
        __M_writer(conditional_websafe(thing.num_text))
        __M_writer(u'\n  </span>\n  ')
        # SOURCE LINE 52
 
        like_cls = "unvoted"
        if getattr(thing, "likes", None):
            like_cls = "likes"
        elif getattr(thing, "likes", None) is False:
            like_cls = "dislikes"
           
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['like_cls'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 58
        __M_writer(u'\n  <div class="midcol ')
        # SOURCE LINE 59
        __M_writer(conditional_websafe(like_cls))
        __M_writer(u'">\n    ')
        # SOURCE LINE 60
        __M_writer(conditional_websafe(arrow(thing, 1, thing.likes)))
        __M_writer(u'\n    ')
        # SOURCE LINE 61
        __M_writer(conditional_websafe(arrow(thing, 0, thing.likes == False)))
        __M_writer(u'\n  </div>\n')
        # SOURCE LINE 63
        if not c.permalink_page:
            # SOURCE LINE 64
            __M_writer(u'      <div class="commentcount">\n        ')
            # SOURCE LINE 65
            __M_writer(conditional_websafe(plain_link(thing.comment_label, thing.permalink, _class=thing.commentcls)))
            __M_writer(u'\n      </div>\n')
        # SOURCE LINE 68
        __M_writer(u'  <div class="entry ')
        __M_writer(conditional_websafe(like_cls))
        __M_writer(u'">\n  ')
        # SOURCE LINE 69

        if thing.is_self:
            url = add_sr(thing.href_url)
        else:
            url = thing.url
          
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['url'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 74
        __M_writer(u'\n')
        # SOURCE LINE 75
        if c.site.link_flair_position == 'left' and thing.flair_text:
            # SOURCE LINE 76
            __M_writer(u'    ')
            __M_writer(conditional_websafe(flair()))
            __M_writer(u'\n')
        # SOURCE LINE 78
        __M_writer(u'    ')
        __M_writer(conditional_websafe(thumbnail()))
        __M_writer(u'\n    <p class="title">\n    <a href="')
        # SOURCE LINE 80
        __M_writer(conditional_websafe(url))
        __M_writer(u'" class="may-blank">')
        __M_writer(conditional_websafe(thing.title))
        __M_writer(u'</a>\n')
        # SOURCE LINE 81
        if c.site.link_flair_position == 'right' and thing.flair_text:
            # SOURCE LINE 82
            __M_writer(u'      ')
            __M_writer(conditional_websafe(flair()))
            __M_writer(u'\n')
        # SOURCE LINE 84
        __M_writer(u'    <span class="domain">\n')
        # SOURCE LINE 85
        if thing.is_self:
            # SOURCE LINE 86
            __M_writer(u'        (self)\n')
            # SOURCE LINE 87
        else:
            # SOURCE LINE 88
            __M_writer(u'        (<a href="')
            __M_writer(conditional_websafe(thing.domain_path))
            __M_writer(u'.compact">')
            __M_writer(conditional_websafe(thing.domain_str))
            __M_writer(u'</a>)\n')
        # SOURCE LINE 90
        __M_writer(u'    </span>\n')
        # SOURCE LINE 91
        if thing.quarantine:
            # SOURCE LINE 92
            __M_writer(u'      <span class="quarantine-warning">\n        ')
            # SOURCE LINE 93
            __M_writer(conditional_websafe(quarantine_stamp()))
            __M_writer(u'\n      </span>\n')
        # SOURCE LINE 96
        if thing.nsfw:
            # SOURCE LINE 97
            __M_writer(u'      <span class="nsfw-warning">\n        ')
            # SOURCE LINE 98
            __M_writer(conditional_websafe(nsfw_stamp()))
            __M_writer(u'\n      </span>\n')
        # SOURCE LINE 101
        __M_writer(u'    </p>\n    ')
        # SOURCE LINE 102

        video_hide = thing.link_child and thing.link_child.css_style.strip(' ') == 'video'
        selftext_hide = thing.is_self and not thing.selftext
            
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['selftext_hide','video_hide'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 105
        __M_writer(u'\n')
        # SOURCE LINE 106
        if thing.link_child and not c.permalink_page and not video_hide and not selftext_hide:
            # SOURCE LINE 107
            __M_writer(u'      <a href="javascript:void(0)" class="expando-button collapsed\n                  ')
            # SOURCE LINE 108
            __M_writer(conditional_websafe(thing.link_child.css_style))
            __M_writer(u'"></a>\n')
        # SOURCE LINE 110
        __M_writer(u'    <div class="tagline">\n      ')
        # SOURCE LINE 111
        __M_writer(conditional_websafe(tagline()))
        __M_writer(u'\n    </div>\n    </div>\n    <a href="javascript:void(0)" class="options_link"></a>\n    ')
        # SOURCE LINE 115

        expand = thing.link_child and thing.link_child.expand
             
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['expand'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 117
        __M_writer(u'\n  <div class="expando" ')
        # SOURCE LINE 118
        __M_writer(conditional_websafe("style='display: none'" if not expand else ""))
        __M_writer(u'>\n')
        # SOURCE LINE 119
        if thing.link_child:
            # SOURCE LINE 120
            __M_writer(u'      ')
            __M_writer(conditional_websafe(unsafe(thing.link_child.content())))
            __M_writer(u'\n')
        # SOURCE LINE 122
        __M_writer(u'  </div>\n  <div class="clear options_expando hidden">\n    ')
        # SOURCE LINE 124
 
        subject = "[reddit] I wanted to share this link with you"
        body = """%(user)s shared a link with you from reddit (https://www.reddit.com/):

%(link)s

"%(title)s"

there's also a discussion going on here:

%(permalink)s
""" % dict(user = c.user.name if c.user_is_Loggedin else "A reddit user",
        link = _force_unicode(thing.url),
        title = _force_unicode(thing.title),
        permalink = add_sr(thing.permalink, sr_path = False, force_hostname = True, retain_extension=False))
        url = "https://reddit.com/%s" % thing._id36
        title = _force_unicode(thing.title)
        tweet = "%s %s" % (title[0:(139-len(url))], url)
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['body','url','tweet','title','subject'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 142
        __M_writer(u'\n\n        ')
        # SOURCE LINE 144
        __M_writer(conditional_websafe(icon_button("Share", "email-icon", "mailto:?subject=" + urllib.quote(_force_utf8(subject)) + "&body=" + urllib.quote(_force_utf8(body)))))
        __M_writer(u'\n        ')
        # SOURCE LINE 145
        __M_writer(conditional_websafe(self.save_button()))
        __M_writer(u'\n        ')
        # SOURCE LINE 146
        __M_writer(conditional_websafe(self.hide_button()))
        __M_writer(u'\n        ')
        # SOURCE LINE 147
        __M_writer(conditional_websafe(icon_button("Report","report-icon",onclick="return change_state(this, 'report', hide_thing)")))
        __M_writer(u'\n\n      \n\n  </div>\n</div>\n')
        # SOURCE LINE 157
        __M_writer(u'\n')
        # SOURCE LINE 162
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_hide_button(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f4de7da0710')._populate(_import_ns, [u'plain_link', u'nsfw_stamp', u'quarantine_stamp'])
        _mako_get_namespace(context, '__anon_0x7f4de7da0550')._populate(_import_ns, [u'arrow', u'score'])
        _mako_get_namespace(context, '__anon_0x7f4de7da0e90')._populate(_import_ns, [u'state_button'])
        _mako_get_namespace(context, '__anon_0x7f4de7da0d50')._populate(_import_ns, [u'tagline', u'thumbnail'])
        _mako_get_namespace(context, '__anon_0x7f4de7da05d0')._populate(_import_ns, [u'icon_button', u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f4de7b882d0')._populate(_import_ns, [u'delete_report_buttons'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        toggle_button = _import_ns.get('toggle_button', context.get('toggle_button', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 153
        __M_writer(u'\n')
        # SOURCE LINE 154
        if c.user_is_loggedin:
            # SOURCE LINE 155
            __M_writer(u'            ')
            __M_writer(conditional_websafe(toggle_button("hide", thing.hidden)))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_save_button(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f4de7da0710')._populate(_import_ns, [u'plain_link', u'nsfw_stamp', u'quarantine_stamp'])
        _mako_get_namespace(context, '__anon_0x7f4de7da0550')._populate(_import_ns, [u'arrow', u'score'])
        _mako_get_namespace(context, '__anon_0x7f4de7da0e90')._populate(_import_ns, [u'state_button'])
        _mako_get_namespace(context, '__anon_0x7f4de7da0d50')._populate(_import_ns, [u'tagline', u'thumbnail'])
        _mako_get_namespace(context, '__anon_0x7f4de7da05d0')._populate(_import_ns, [u'icon_button', u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f4de7b882d0')._populate(_import_ns, [u'delete_report_buttons'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        toggle_button = _import_ns.get('toggle_button', context.get('toggle_button', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 158
        __M_writer(u'\n')
        # SOURCE LINE 159
        if c.user_is_loggedin:
            # SOURCE LINE 160
            __M_writer(u'        ')
            __M_writer(conditional_websafe(toggle_button("save", thing.saved)))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_flair(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f4de7da0710')._populate(_import_ns, [u'plain_link', u'nsfw_stamp', u'quarantine_stamp'])
        _mako_get_namespace(context, '__anon_0x7f4de7da0550')._populate(_import_ns, [u'arrow', u'score'])
        _mako_get_namespace(context, '__anon_0x7f4de7da0e90')._populate(_import_ns, [u'state_button'])
        _mako_get_namespace(context, '__anon_0x7f4de7da0d50')._populate(_import_ns, [u'tagline', u'thumbnail'])
        _mako_get_namespace(context, '__anon_0x7f4de7da05d0')._populate(_import_ns, [u'icon_button', u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f4de7b882d0')._populate(_import_ns, [u'delete_report_buttons'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 37
        __M_writer(u'\n')
        # SOURCE LINE 38
        if c.user.pref_show_link_flair:
            # SOURCE LINE 39
            __M_writer(u'    <span class="linkflair">')
            __M_writer(conditional_websafe(thing.flair_text))
            __M_writer(u'</span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


