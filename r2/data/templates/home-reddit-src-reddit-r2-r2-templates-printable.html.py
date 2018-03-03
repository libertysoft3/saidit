# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505003062.313481
_enable_loop = True
_template_filename = u'/home/reddit/src/reddit/r2/r2/templates/printable.html'
_template_uri = u'/printable.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['ParentDiv', 'midcol', 'numcol', 'Child', 'RenderPrintable', 'gildings', 'buttons', 'thing_css_rowclass', 'score', 'approval_checkmark', 'arrow', 'entry', 'thing_data_attributes', 'admintagline', 'thing_css_class']


# SOURCE LINE 23

from r2.lib.filters import jssafe
from r2.lib.template_helpers import add_sr, static
from r2.lib.strings import strings
from r2.lib.pages.things import BanButtons
from r2.lib.utils import long_datetime


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 31
    ns = runtime.TemplateNamespace('__anon_0x7f36093a2dd0', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f36093a2dd0')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f36093a2dd0')._populate(_import_ns, [u'classes', u'plain_link'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 29
        __M_writer(u'\n\n')
        # SOURCE LINE 31
        __M_writer(u'\n\n')
        # SOURCE LINE 33
        __M_writer(conditional_websafe(self.RenderPrintable()))
        __M_writer(u'\n\n')
        # SOURCE LINE 53
        __M_writer(u'\n\n')
        # SOURCE LINE 62
        __M_writer(u'\n\n')
        # SOURCE LINE 74
        __M_writer(u'\n\n')
        # SOURCE LINE 85
        __M_writer(u'\n\n')
        # SOURCE LINE 118
        __M_writer(u'\n\n')
        # SOURCE LINE 150
        __M_writer(u'\n\n')
        # SOURCE LINE 194
        __M_writer(u'\n\n')
        # SOURCE LINE 198
        __M_writer(u'\n\n')
        # SOURCE LINE 201
        __M_writer(u'\n\n')
        # SOURCE LINE 204
        __M_writer(u'\n\n')
        # SOURCE LINE 207
        __M_writer(u'\n\n')
        # SOURCE LINE 215
        __M_writer(u'\n\n')
        # SOURCE LINE 238
        __M_writer(u'\n\n')
        # SOURCE LINE 246
        __M_writer(u'\n\n\n')
        # SOURCE LINE 255
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_ParentDiv(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f36093a2dd0')._populate(_import_ns, [u'classes', u'plain_link'])
        __M_writer = context.writer()
        # SOURCE LINE 200
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_midcol(context,display=True,cls=''):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f36093a2dd0')._populate(_import_ns, [u'classes', u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 249
        __M_writer(u'\n  <div class="midcol ')
        # SOURCE LINE 250
        __M_writer(conditional_websafe(cls))
        __M_writer(u'" \n       ')
        # SOURCE LINE 251
        __M_writer(conditional_websafe(not display and "style='display:none'" or ''))
        __M_writer(u'>\n    ')
        # SOURCE LINE 252
        __M_writer(conditional_websafe(self.arrow(thing, 1, thing.likes)))
        __M_writer(u'\n    ')
        # SOURCE LINE 253
        __M_writer(conditional_websafe(self.arrow(thing, 0, thing.likes == False)))
        __M_writer(u'\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_numcol(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f36093a2dd0')._populate(_import_ns, [u'classes', u'plain_link'])
        __M_writer = context.writer()
        # SOURCE LINE 203
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_Child(context,display=True):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f36093a2dd0')._populate(_import_ns, [u'classes', u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 209
        __M_writer(u'\n<div class="child" ')
        # SOURCE LINE 210
        __M_writer(conditional_websafe((not display and "style='display:none'" or "")))
        __M_writer(u'>\n')
        # SOURCE LINE 211
        if thing.childlisting:
            # SOURCE LINE 212
            __M_writer(u'    ')
            __M_writer(conditional_websafe(thing.childlisting))
            __M_writer(u'\n')
        # SOURCE LINE 214
        __M_writer(u'</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_RenderPrintable(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f36093a2dd0')._populate(_import_ns, [u'classes', u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 152
        __M_writer(u'\n')
        # SOURCE LINE 153
        cls = thing.lookups[0].__class__.__name__.lower() 
        
        __M_writer(u'\n')
        # SOURCE LINE 154

        if hasattr(thing, 'render_css_class'):
           cls = thing.render_css_class
        elif hasattr(thing, 'render_class'):
           cls = thing.render_class.__name__.lower()
        else:
           cls = thing.lookups[0].__class__.__name__.lower()
        
        cls += ' ' + getattr(thing, 'extra_css_class', '')
        
        if getattr(thing, "is_self", False):
           selflink = "self"
        else:
           selflink = ""
         
        
        # SOURCE LINE 168
        __M_writer(u'\n<div class="')
        # SOURCE LINE 169
        __M_writer(conditional_websafe(self.thing_css_class(thing)))
        __M_writer(u' ')
        __M_writer(conditional_websafe(self.thing_css_rowclass(thing)))
        __M_writer(u' ')
        __M_writer(conditional_websafe(unsafe(cls)))
        __M_writer(u' ')
        __M_writer(conditional_websafe(selflink))
        __M_writer(u'"\n')
        # SOURCE LINE 170
        if not getattr(thing, 'deleted', False) or getattr(thing, 'can_ban', False):
            # SOURCE LINE 171
            __M_writer(u'      id="thing_')
            __M_writer(conditional_websafe(thing._fullname))
            __M_writer(u'"\n')
        # SOURCE LINE 173
        __M_writer(u'    ')
        __M_writer(conditional_websafe(thing.display))
        __M_writer(u' onclick="click_thing(this)"\n    ')
        # SOURCE LINE 174
        __M_writer(conditional_websafe(unsafe(self.thing_data_attributes(thing))))
        __M_writer(u'>\n  <p class="parent">\n    ')
        # SOURCE LINE 176
        __M_writer(conditional_websafe(self.ParentDiv()))
        __M_writer(u'\n  </p>\n  ')
        # SOURCE LINE 178
        __M_writer(conditional_websafe(self.numcol()))
        __M_writer(u'\n  ')
        # SOURCE LINE 179

        like_cls = "unvoted"
        if getattr(thing, "likes", None):
            like_cls = "likes"
        elif getattr(thing, "likes", None) is False:
            like_cls = "dislikes"
           
        
        # SOURCE LINE 185
        __M_writer(u'\n  ')
        # SOURCE LINE 186
        __M_writer(conditional_websafe(self.midcol(cls = like_cls)))
        __M_writer(u'\n  <div class="entry ')
        # SOURCE LINE 187
        __M_writer(conditional_websafe(like_cls))
        __M_writer(u'">\n    ')
        # SOURCE LINE 188
        __M_writer(conditional_websafe(self.entry()))
        __M_writer(u'\n  </div>\n  ')
        # SOURCE LINE 190
        __M_writer(conditional_websafe(self.Child()))
        __M_writer(u'\n  <div class="clearleft"></div>\n</div>\n<div class="clearleft"></div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_gildings(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f36093a2dd0')._populate(_import_ns, [u'classes', u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 64
        __M_writer(u'\n')
        # SOURCE LINE 65
        if thing.gilded_message:
            # SOURCE LINE 66
            __M_writer(u'  <a href="')
            __M_writer(conditional_websafe(thing.subreddit_path))
            __M_writer(u'gilded">\n    <span class="gilded-icon" title="')
            # SOURCE LINE 67
            __M_writer(conditional_websafe(thing.gilded_message))
            __M_writer(u'" data-count="')
            __M_writer(conditional_websafe(thing.gildings))
            __M_writer(u'">\n')
            # SOURCE LINE 68
            if thing.gildings > 1:
                # SOURCE LINE 69
                __M_writer(u'        x')
                __M_writer(conditional_websafe(thing.gildings))
                __M_writer(u'\n')
            # SOURCE LINE 71
            __M_writer(u'    </span>\n  </a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_buttons(context,ban=True):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f36093a2dd0')._populate(_import_ns, [u'classes', u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 196
        __M_writer(u'\n  ')
        # SOURCE LINE 197
        __M_writer(conditional_websafe(BanButtons(thing)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_thing_css_rowclass(context,what):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f36093a2dd0')._populate(_import_ns, [u'classes', u'plain_link'])
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 87
        __M_writer(u'\n  ')
        # SOURCE LINE 88

        rowstyle = getattr(what, "rowstyle", "")
        
        if what.show_spam:
          rowclass = "spam"
          if what.show_spam == "author":
            rowclass += " banned-user"
        elif what.show_reports:
          rowclass = "reported"
        else:
          rowclass = ""
        
        if getattr(what, "deleted", False):
          rowclass += " deleted"
        if hasattr(what, "saved") and what.saved:
          rowclass += " saved"
        if hasattr(what, "hidden") and what.hidden:
          rowclass += " hidden"
        if hasattr(what, "gildings") and what.gildings > 0:
          rowclass += " gilded"
        if hasattr(what, "user_gilded") and what.user_gilded:
          rowclass += " user-gilded"
        if not getattr(what, "archived", False) and getattr(what, "locked", False):
          rowclass += " locked"
        if getattr(what, "use_sticky_style", False):
          rowclass += " stickied"
        if getattr(what, "is_controversial", False):
          rowclass += " controversial"
          
        
        # SOURCE LINE 116
        __M_writer(u'\n  ')
        # SOURCE LINE 117
        __M_writer(conditional_websafe(rowstyle))
        __M_writer(u'&#32;')
        __M_writer(conditional_websafe(rowclass))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_score(context,thing,tag='span'):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f36093a2dd0')._populate(_import_ns, [u'classes', u'plain_link'])
        zip = _import_ns.get('zip', context.get('zip', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 240
        __M_writer(u'\n')
        # SOURCE LINE 241
        for cls, score in zip(["dislikes", "unvoted", "likes"], thing.display_score):
            # SOURCE LINE 242
            __M_writer(u'    <')
            __M_writer(conditional_websafe(tag))
            __M_writer(u' class="score ')
            __M_writer(conditional_websafe(cls))
            __M_writer(u'">\n      ')
            # SOURCE LINE 243
            __M_writer(conditional_websafe(score))
            __M_writer(u'\n    </')
            # SOURCE LINE 244
            __M_writer(conditional_websafe(tag))
            __M_writer(u'>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_approval_checkmark(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f36093a2dd0')._populate(_import_ns, [u'classes', u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 55
        __M_writer(u'\n')
        # SOURCE LINE 56
        if getattr(thing, "approval_checkmark", None):
            # SOURCE LINE 57
            __M_writer(u'      <img class="approval-checkmark" title="')
            __M_writer(conditional_websafe(thing.approval_checkmark))
            __M_writer(u'"\n           src="')
            # SOURCE LINE 58
            __M_writer(conditional_websafe(static('green-check.png')))
            __M_writer(u'"\n           onclick="alert(\'')
            # SOURCE LINE 59
            __M_writer(conditional_websafe(thing.approval_checkmark))
            __M_writer(u'\\n\\n')
            __M_writer(conditional_websafe(jssafe(_("(no need to click for this info; just hover over the checkmark next time)"))))
            __M_writer(u'\')"\n         >\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_arrow(context,this,dir,mod):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f36093a2dd0')._populate(_import_ns, [u'classes', u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        classes = _import_ns.get('classes', context.get('classes', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 217
        __M_writer(u'\n')
        # SOURCE LINE 218
 
        arrow_type = "up" if dir > 0 else "down"
        arrow_class = arrow_type + ("mod" if mod else "")
        login_class = "login-required" if not g.read_only_mode else ""
        archived_class = "archived" if not getattr(thing, 'votable', True) else ""
        access_class = "access-required"
        
        
        # SOURCE LINE 224
        __M_writer(u'\n  <div ')
        # SOURCE LINE 225
        __M_writer(conditional_websafe(classes("arrow", arrow_class, login_class, archived_class, access_class)))
        __M_writer(u'\n    data-event-action="')
        # SOURCE LINE 226
        __M_writer(conditional_websafe(arrow_type))
        __M_writer(u'vote"\n')
        # SOURCE LINE 227
        if not g.read_only_mode:
            # SOURCE LINE 228
            __M_writer(u'       role="button"\n')
            # SOURCE LINE 229
            if dir > 0:
                # SOURCE LINE 230
                __M_writer(u'       aria-label="')
                __M_writer(conditional_websafe(_("upvote")))
                __M_writer(u'"\n')
                # SOURCE LINE 231
            else:
                # SOURCE LINE 232
                __M_writer(u'       aria-label="')
                __M_writer(conditional_websafe(_("downvote")))
                __M_writer(u'"\n')
            # SOURCE LINE 234
            __M_writer(u'       tabindex="0"\n')
        # SOURCE LINE 236
        __M_writer(u'    >\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_entry(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f36093a2dd0')._populate(_import_ns, [u'classes', u'plain_link'])
        __M_writer = context.writer()
        # SOURCE LINE 206
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_thing_data_attributes(context,what):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f36093a2dd0')._populate(_import_ns, [u'classes', u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 120
        __M_writer(u'\n')
        # SOURCE LINE 121
        if not getattr(what, 'deleted', False):
            # SOURCE LINE 122
            __M_writer(u'      ')
            cls = thing.lookups[0].__class__.__name__.lower() 
            
            __M_writer(u'\n      data-fullname="')
            # SOURCE LINE 123
            __M_writer(conditional_websafe(what._fullname))
            __M_writer(u'"\n      data-type="')
            # SOURCE LINE 124
            __M_writer(conditional_websafe(unsafe(cls)))
            __M_writer(u'"\n')
        # SOURCE LINE 126
        __M_writer(u'\n')
        # SOURCE LINE 127
        if hasattr(what, 'campaign'):
            # SOURCE LINE 128
            __M_writer(u'      data-cid="')
            __M_writer(conditional_websafe(what.campaign))
            __M_writer(u'"\n')
        # SOURCE LINE 130
        __M_writer(u'\n')
        # SOURCE LINE 131
        if hasattr(what, 'imp_pixel'):
            # SOURCE LINE 132
            __M_writer(u'      data-imp-pixel="')
            __M_writer(conditional_websafe(what.imp_pixel))
            __M_writer(u'"\n')
        # SOURCE LINE 134
        __M_writer(u'\n')
        # SOURCE LINE 135
        if hasattr(what, 'adserver_imp_pixel'):
            # SOURCE LINE 136
            __M_writer(u'      data-adserver-imp-pixel="')
            __M_writer(conditional_websafe(what.adserver_imp_pixel))
            __M_writer(u'"\n')
        # SOURCE LINE 138
        __M_writer(u'\n')
        # SOURCE LINE 139
        if hasattr(what, 'adserver_click_url'):
            # SOURCE LINE 140
            __M_writer(u'      data-adserver-click-url="')
            __M_writer(conditional_websafe(what.adserver_click_url))
            __M_writer(u'"\n')
        # SOURCE LINE 142
        __M_writer(u'\n')
        # SOURCE LINE 143
        if hasattr(what, 'third_party_tracking_url'):
            # SOURCE LINE 144
            __M_writer(u'      data-third-party-tracking-url="')
            __M_writer(conditional_websafe(what.third_party_tracking_url))
            __M_writer(u'"\n')
        # SOURCE LINE 146
        __M_writer(u'\n')
        # SOURCE LINE 147
        if hasattr(what, 'third_party_tracking_url_2'):
            # SOURCE LINE 148
            __M_writer(u'      data-third-party-tracking-two-url="')
            __M_writer(conditional_websafe(what.third_party_tracking_url_2))
            __M_writer(u'"\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_admintagline(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f36093a2dd0')._populate(_import_ns, [u'classes', u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 35
        __M_writer(u'\n')
        # SOURCE LINE 36
        if thing.show_spam:
            # SOURCE LINE 37
            if thing.banned_at:
                # SOURCE LINE 38
                __M_writer(u'        <li title="')
                __M_writer(conditional_websafe(_("removed at %(time)s") % dict(time=long_datetime(thing.banned_at))))
                __M_writer(u'">\n')
                # SOURCE LINE 39
            else:
                # SOURCE LINE 40
                __M_writer(u'        <li>\n')
            # SOURCE LINE 42
            __M_writer(u'      <b>[\n')
            # SOURCE LINE 43
            if c.user_is_admin:
                # SOURCE LINE 44
                __M_writer(u'          ')
                __M_writer(conditional_websafe("auto" if thing.autobanned else ""))
                __M_writer(conditional_websafe(strings.banned))
                __M_writer(u' \n          ')
                # SOURCE LINE 45
                __M_writer(conditional_websafe(("by %s" % thing.banner) if thing.banner else ""))
                __M_writer(u'\n')
                # SOURCE LINE 46
            elif thing.moderator_banned and thing.banner:
                # SOURCE LINE 47
                __M_writer(u'          ')
                __M_writer(conditional_websafe(strings.banned_by % thing.banner))
                __M_writer(u'\n')
                # SOURCE LINE 48
            else:
                # SOURCE LINE 49
                __M_writer(u'          ')
                __M_writer(conditional_websafe(strings.banned))
                __M_writer(u'\n')
            # SOURCE LINE 51
            __M_writer(u'      ]</li></b>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_thing_css_class(context,what):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f36093a2dd0')._populate(_import_ns, [u'classes', u'plain_link'])
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 76
        __M_writer(u'\n  ')
        # SOURCE LINE 77

        cssclass = "thing"
        if (not getattr(what, 'deleted', False) or
                getattr(what, 'can_ban', False) or
               (getattr(what, 'promoted', False) and c.user_is_sponsor)):
          cssclass += " id-" + what._fullname
          
        
        # SOURCE LINE 83
        __M_writer(u'\n  ')
        # SOURCE LINE 84
        __M_writer(conditional_websafe(cssclass))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


