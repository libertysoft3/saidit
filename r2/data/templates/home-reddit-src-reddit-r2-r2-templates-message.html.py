# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1520060935.72681
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/message.html'
_template_uri = '/message.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['buttons', 'tagline', 'ParentDiv', 'thing_css_rowclass', 'midcol', 'thing_data_attributes', 'entry', 'commentBody', 'thing_css_class', 'subject']


# SOURCE LINE 23

from r2.lib.filters import safemarkdown, websafe, conditional_websafe
from r2.lib.pages.things import MessageButtons
from r2.lib.pages import WrappedUser
from r2.lib.template_helpers import static, format_html
from r2.lib.template_helpers import (
    add_admin_distinguish,
    add_moderator_distinguish,
)
from r2.models import Account


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 37
    ns = runtime.TemplateNamespace('__anon_0x7fc7c796f2d0', context._clean_inheritance_tokens(), templateuri=u'wrappeduser.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fc7c796f2d0')] = ns

    # SOURCE LINE 36
    ns = runtime.TemplateNamespace('__anon_0x7fc7c796f210', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fc7c796f210')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'comment_skeleton.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c796f2d0')._populate(_import_ns, [u'make_distinguish'])
        _mako_get_namespace(context, '__anon_0x7fc7c796f210')._populate(_import_ns, [u'thing_timestamp'])
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 33
        __M_writer(u'\n\n')
        # SOURCE LINE 35
        __M_writer(u'\n')
        # SOURCE LINE 36
        __M_writer(u'\n')
        # SOURCE LINE 37
        __M_writer(u'\n\n')
        # SOURCE LINE 46
        __M_writer(u'\n\n')
        # SOURCE LINE 59
        __M_writer(u'\n\n')
        # SOURCE LINE 69
        __M_writer(u'\n\n')
        # SOURCE LINE 79
        __M_writer(u'\n\n')
        # SOURCE LINE 139
        __M_writer(u'\n\n')
        # SOURCE LINE 182
        __M_writer(u'\n\n')
        # SOURCE LINE 189
        __M_writer(u'\n\n')
        # SOURCE LINE 203
        __M_writer(u'\n\n')
        # SOURCE LINE 207
        __M_writer(u'\n\n')
        # SOURCE LINE 211
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_buttons(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c796f2d0')._populate(_import_ns, [u'make_distinguish'])
        _mako_get_namespace(context, '__anon_0x7fc7c796f210')._populate(_import_ns, [u'thing_timestamp'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 205
        __M_writer(u'\n  ')
        # SOURCE LINE 206
        __M_writer(conditional_websafe(MessageButtons(thing)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tagline(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c796f2d0')._populate(_import_ns, [u'make_distinguish'])
        _mako_get_namespace(context, '__anon_0x7fc7c796f210')._populate(_import_ns, [u'thing_timestamp'])
        capture = _import_ns.get('capture', context.get('capture', UNDEFINED))
        thing_timestamp = _import_ns.get('thing_timestamp', context.get('thing_timestamp', UNDEFINED))
        make_distinguish = _import_ns.get('make_distinguish', context.get('make_distinguish', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 81
        __M_writer(u'\n  <a href="javascript:void(0)" class="expand" onclick="return togglemessage(this)">\n    ')
        # SOURCE LINE 83
        __M_writer(conditional_websafe("[%s]" % ("+" if thing.collapsed else "–")))
        __M_writer(u'\n  </a>\n\n')
        # SOURCE LINE 86
        if c.user_is_admin:
            # SOURCE LINE 87
            if not thing.was_comment and hasattr(thing, "del_on_recipient") and thing.del_on_recipient:
                # SOURCE LINE 88
                __M_writer(u'       <em>')
                __M_writer(conditional_websafe(_("deleted message")))
                __M_writer(u'</em>&#32;\n')
        # SOURCE LINE 91
        __M_writer(u'\n  ')
        # SOURCE LINE 92

        substitutions = {}
        
        if thing.sr_id:
            path = thing.subreddit.path.rstrip('/')
        
            if getattr(thing, "subreddit_distinguish", None) == "admin":
                distinguish_attribs_list = []
                add_admin_distinguish(distinguish_attribs_list)
                distinguish = format_html(capture(make_distinguish, distinguish_attribs_list))
                type = "admin-distinguish"
                substitutions['subreddit'] = format_html(u'<span class="subreddit"><a href="%(path)s" class="%(type)s">%(path)s</a>%(distinguish)s</span>', path=path, distinguish=distinguish, type=type)
            elif getattr(thing, "subreddit_distinguish", None) == "moderator":
                distinguish_attribs_list = []
                add_moderator_distinguish(distinguish_attribs_list, thing.subreddit)
                distinguish = format_html(capture(make_distinguish, distinguish_attribs_list))
                type = "moderator-distinguish"
                substitutions['subreddit'] = format_html(u'<span class="subreddit"><a href="%(path)s" class="%(type)s">%(path)s</a>%(distinguish)s</span>', path=path, distinguish=distinguish, type=type)
            else:
                substitutions['subreddit'] = format_html(u'<span class="subreddit"><a href="%(path)s">%(path)s</a></span>', path=path)
        
        substitutions['author'] = format_html(u'<span class="sender">%s</span>', WrappedUser(thing.author, thing.attribs, thing))
        
        if isinstance(thing.to, Account):
            to_attribs = []
            if thing.sr_id and not thing.was_comment:
                if thing.to.name in g.admins:
                    add_admin_distinguish(to_attribs)
                elif thing.to_is_moderator:
                    add_moderator_distinguish(to_attribs, thing.subreddit)
            substitutions['dest'] = format_html(u'<span class="recipient">%s</span>', WrappedUser(thing.to, to_attribs, thing))
        elif thing.sr_id:
            substitutions['dest'] = format_html(u'<span class="recipient subreddit"><a href="%(path)s">%(path)s</a></span>', path=thing.subreddit.path)
        
        substitutions['when'] = unsafe(capture(thing_timestamp, thing, thing.timesince, live=True, include_tense=True))
        
        taglinetext = conditional_websafe(thing.taglinetext).replace(' ', '&#32;')
        taglinetext = format_html(taglinetext, **substitutions)
          
        
        # SOURCE LINE 130
        __M_writer(u'\n\n  <span class="head">\n    ')
        # SOURCE LINE 133
        __M_writer(conditional_websafe(taglinetext))
        __M_writer(u'\n  </span>\n\n')
        # SOURCE LINE 136
        if c.user_is_admin:
            # SOURCE LINE 137
            __M_writer(u'    ')
            __M_writer(conditional_websafe(self.admintagline()))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_ParentDiv(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c796f2d0')._populate(_import_ns, [u'make_distinguish'])
        _mako_get_namespace(context, '__anon_0x7fc7c796f210')._populate(_import_ns, [u'thing_timestamp'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 184
        __M_writer(u'\n')
        # SOURCE LINE 185
        if getattr(thing, 'distinguished', '') == 'gold':
            # SOURCE LINE 186
            __M_writer(u'    <div class="insignia"><img src="')
            __M_writer(conditional_websafe(static('gold/gold-insignia-big.png')))
            __M_writer(u'"></div>\n')
        # SOURCE LINE 188
        __M_writer(conditional_websafe(self.subject()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_thing_css_rowclass(context,what):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c796f2d0')._populate(_import_ns, [u'make_distinguish'])
        _mako_get_namespace(context, '__anon_0x7fc7c796f210')._populate(_import_ns, [u'thing_timestamp'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 61
        __M_writer(u'\n  ')
        # SOURCE LINE 62
        __M_writer(conditional_websafe(parent.thing_css_rowclass(what)))
        __M_writer(u'\n  ')
        # SOURCE LINE 63

        accent_color = getattr(thing, "accent_color", "")
          
        
        # SOURCE LINE 65
        __M_writer(u'\n')
        # SOURCE LINE 66
        if getattr(thing, "is_parent", False) and accent_color:
            # SOURCE LINE 67
            __M_writer(u'    color-bar\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_midcol(context,cls=''):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c796f2d0')._populate(_import_ns, [u'make_distinguish'])
        _mako_get_namespace(context, '__anon_0x7fc7c796f210')._populate(_import_ns, [u'thing_timestamp'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 40
        __M_writer(u'\n')
        # SOURCE LINE 41
        if thing.was_comment and not thing._spam:
            # SOURCE LINE 42
            __M_writer(u'    ')
            __M_writer(conditional_websafe(parent.midcol(display=True, cls = cls)))
            __M_writer(u'\n')
            # SOURCE LINE 43
        else:
            # SOURCE LINE 44
            __M_writer(u'    <div class="midcol" style=\'display:none\'></div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_thing_data_attributes(context,what):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c796f2d0')._populate(_import_ns, [u'make_distinguish'])
        _mako_get_namespace(context, '__anon_0x7fc7c796f210')._populate(_import_ns, [u'thing_timestamp'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 71
        __M_writer(u'\n  ')
        # SOURCE LINE 72
        __M_writer(conditional_websafe(parent.thing_data_attributes(what)))
        __M_writer(u'\n  ')
        # SOURCE LINE 73

        accent_color = getattr(thing, "accent_color", "")
          
        
        # SOURCE LINE 75
        __M_writer(u'\n')
        # SOURCE LINE 76
        if getattr(thing, "is_parent", False) and accent_color:
            # SOURCE LINE 77
            __M_writer(u'    style="border-color:')
            __M_writer(conditional_websafe(accent_color))
            __M_writer(u';"\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_entry(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c796f2d0')._populate(_import_ns, [u'make_distinguish'])
        _mako_get_namespace(context, '__anon_0x7fc7c796f210')._populate(_import_ns, [u'thing_timestamp'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 209
        __M_writer(u'\n  ')
        # SOURCE LINE 210
        __M_writer(conditional_websafe(parent.entry()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_commentBody(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c796f2d0')._populate(_import_ns, [u'make_distinguish'])
        _mako_get_namespace(context, '__anon_0x7fc7c796f210')._populate(_import_ns, [u'thing_timestamp'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 191
        __M_writer(u'\n')
        # SOURCE LINE 192
        if thing.was_comment and hasattr(thing, "parent"):
            # SOURCE LINE 193
            __M_writer(u'    <p>\n      <a href="#" class="parent-link"\n         onclick="return fetch_parent(this, \'')
            # SOURCE LINE 195
            __M_writer(conditional_websafe(thing.parent_permalink))
            __M_writer(u"/.json', '")
            __M_writer(conditional_websafe(thing.parent))
            __M_writer(u'\')">\n        ')
            # SOURCE LINE 196
            __M_writer(conditional_websafe(_("show parent")))
            __M_writer(u'\n      </a>\n    </p>\n')
        # SOURCE LINE 200
        __M_writer(u' <div class="md-container">\n   ')
        # SOURCE LINE 201
        __M_writer(conditional_websafe(unsafe(safemarkdown(thing.body))))
        __M_writer(u'\n </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_thing_css_class(context,what):
    __M_caller = context.caller_stack._push_frame()
    try:
        context._push_buffer()
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c796f2d0')._populate(_import_ns, [u'make_distinguish'])
        _mako_get_namespace(context, '__anon_0x7fc7c796f210')._populate(_import_ns, [u'thing_timestamp'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 48
        __M_writer(u'\n  ')
        # SOURCE LINE 49
        __M_writer(conditional_websafe(parent.thing_css_class(what)))
        __M_writer(u'\n  ')
        # SOURCE LINE 50
        __M_writer(conditional_websafe("new" if thing.new else ""))
        __M_writer(u'\n  ')
        # SOURCE LINE 51
        __M_writer(conditional_websafe("was-comment" if thing.was_comment else ""))
        __M_writer(u'\n  ')
        # SOURCE LINE 52
        __M_writer(conditional_websafe("recipient" if thing.user_is_recipient else ""))
        __M_writer(u'\n  ')
        # SOURCE LINE 53
        __M_writer(conditional_websafe("message-reply" if getattr(thing, "is_child", False) else ""))
        __M_writer(u'\n  ')
        # SOURCE LINE 54
        __M_writer(conditional_websafe("message-parent" if getattr(thing, "is_parent", False) else ""))
        __M_writer(u'\n  ')
        # SOURCE LINE 55
        __M_writer(conditional_websafe("gold" if getattr(thing, "distinguished", "") == "gold" else ""))
        __M_writer(u'\n  ')
        # SOURCE LINE 56
        __M_writer(conditional_websafe("gold-auto" if getattr(thing, "distinguished", "") == "gold-auto" else ""))
        __M_writer(u'\n  ')
        # SOURCE LINE 57
        __M_writer(conditional_websafe("threaded" if getattr(thing, "threaded", "") else ""))
        __M_writer(u'\n  ')
        # SOURCE LINE 58
        __M_writer(conditional_websafe("most-recent" if getattr(thing, "most_recent", "") else ""))
        __M_writer(u'\n')
    finally:
        __M_buf = context._pop_buffer()
        context.caller_stack._pop_frame()
    return __M_buf.getvalue()


def render_subject(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c796f2d0')._populate(_import_ns, [u'make_distinguish'])
        _mako_get_namespace(context, '__anon_0x7fc7c796f210')._populate(_import_ns, [u'thing_timestamp'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 141
        __M_writer(u'\n  <p class="subject">\n')
        # SOURCE LINE 143
        if getattr(thing, "is_parent", False):
            # SOURCE LINE 144
            if thing.sr_id:
                # SOURCE LINE 145
                __M_writer(u'         <span class="correspondent reddit rounded">\n           ')
                # SOURCE LINE 146

                if getattr(thing, "user_is_moderator", False):
                  sr_path = "%smessage/moderator/inbox" % thing.subreddit.path
                else:
                  sr_path = thing.subreddit.path
                accent_color = getattr(thing, "accent_color", "")
                           
                
                # SOURCE LINE 152
                __M_writer(u'\n           <a href="')
                # SOURCE LINE 153
                __M_writer(conditional_websafe(sr_path))
                __M_writer(u'">\n')
                # SOURCE LINE 154
                if accent_color:
                    # SOURCE LINE 155
                    __M_writer(u'               <span class="marker-dot" style="background-color:')
                    __M_writer(conditional_websafe(accent_color))
                    __M_writer(u';"></span>\n')
                # SOURCE LINE 157
                __M_writer(u'             /r/')
                __M_writer(conditional_websafe(thing.subreddit.name))
                __M_writer(u'\n           </a>\n         </span>\n')
                # SOURCE LINE 160
            else:
                # SOURCE LINE 161
                __M_writer(u'         <span class="correspondent rounded">\n           ')
                # SOURCE LINE 162

                corr = thing.author if thing.user_is_recipient else thing.to
                            
                
                # SOURCE LINE 164
                __M_writer(u'\n           ')
                # SOURCE LINE 165
                __M_writer(conditional_websafe(WrappedUser(corr)))
                __M_writer(u'\n         </span>\n')
        # SOURCE LINE 169
        __M_writer(u'    <span class="subject-text">')
        __M_writer(conditional_websafe(thing.subject))
        __M_writer(u'</span>\n')
        # SOURCE LINE 170
        if thing.was_comment:
            # SOURCE LINE 171
            __M_writer(u'    <a href="')
            __M_writer(conditional_websafe(thing.link_permalink))
            __M_writer(u'" class="title">')
            __M_writer(conditional_websafe(thing.link_title))
            __M_writer(u'</a>\n')
            # SOURCE LINE 172
        elif getattr(thing, "is_parent", False):
            # SOURCE LINE 173
            __M_writer(u'    <br/>\n      <a class="expand-btn" href="#" onclick="return show_all_messages(this)">\n        ')
            # SOURCE LINE 175
            __M_writer(conditional_websafe(_("expand all")))
            __M_writer(u'\n      </a>\n      <a class="expand-btn" href="#"  onclick="return hide_all_messages(this)">\n        ')
            # SOURCE LINE 178
            __M_writer(conditional_websafe(_("collapse all")))
            __M_writer(u'\n      </a>\n')
        # SOURCE LINE 181
        __M_writer(u' </p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


