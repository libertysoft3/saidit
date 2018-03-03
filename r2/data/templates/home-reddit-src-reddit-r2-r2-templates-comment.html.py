# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1520060828.047651
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/comment.html'
_template_uri = '/comment.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['buttons', 'tagline', 'arrows', 'subreddit', 'ParentDiv', 'link', 'midcol', 'Child', 'commentBody', 'fullContext']


# SOURCE LINE 23

from r2.config import feature
from r2.lib.filters import unsafe
from r2.lib.pages.things import CommentButtons
from r2.lib.pages import WrappedUser


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 30
    ns = runtime.TemplateNamespace('__anon_0x7fc7c7b3fe90', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fc7c7b3fe90')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'comment_skeleton.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7b3fe90')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited', u'nsfw_stamp', u'quarantine_stamp'])
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 28
        __M_writer(u'\n\n')
        # SOURCE LINE 30
        __M_writer(u'\n')
        # SOURCE LINE 31
        __M_writer(u'\n\n')
        # SOURCE LINE 36
        __M_writer(u'\n')
        # SOURCE LINE 39
        __M_writer(u'\n\n')
        # SOURCE LINE 44
        __M_writer(u'\n\n')
        # SOURCE LINE 67
        __M_writer(u'\n\n')
        # SOURCE LINE 83
        __M_writer(u'\n\n')
        # SOURCE LINE 140
        __M_writer(u'\n\n')
        # SOURCE LINE 156
        __M_writer(u'\n\n')
        # SOURCE LINE 193
        __M_writer(u'\n\n')
        # SOURCE LINE 200
        __M_writer(u'\n\n')
        # SOURCE LINE 204
        __M_writer(u'\n\n')
        # SOURCE LINE 221
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_buttons(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7b3fe90')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited', u'nsfw_stamp', u'quarantine_stamp'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        quarantine_stamp = _import_ns.get('quarantine_stamp', context.get('quarantine_stamp', UNDEFINED))
        nsfw_stamp = _import_ns.get('nsfw_stamp', context.get('nsfw_stamp', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 206
        __M_writer(u'\n')
        # SOURCE LINE 207
        if c.profilepage:
            # SOURCE LINE 208
            if thing.subreddit.quarantine:
                # SOURCE LINE 209
                __M_writer(u'      <li>\n        <span class="quarantine-stamp stamp">')
                # SOURCE LINE 210
                __M_writer(conditional_websafe(quarantine_stamp()))
                __M_writer(u'</span>\n      </li>\n')
            # SOURCE LINE 213
            if thing.nsfw:
                # SOURCE LINE 214
                __M_writer(u'      <li>\n        <span class="nsfw-stamp stamp">')
                # SOURCE LINE 215
                __M_writer(conditional_websafe(nsfw_stamp()))
                __M_writer(u'</span>\n      </li>\n')
        # SOURCE LINE 219
        __M_writer(u'  ')
        __M_writer(conditional_websafe(CommentButtons(thing)))
        __M_writer(u'\n  ')
        # SOURCE LINE 220
        __M_writer(conditional_websafe(self.admintagline()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tagline(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7b3fe90')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited', u'nsfw_stamp', u'quarantine_stamp'])
        edited = _import_ns.get('edited', context.get('edited', UNDEFINED))
        thing_timestamp = _import_ns.get('thing_timestamp', context.get('thing_timestamp', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 85
        __M_writer(u'\n  ')
        # SOURCE LINE 86

        if c.user_is_admin:
          show = True
        else:
          show = not thing.deleted
          
        
        # SOURCE LINE 91
        __M_writer(u'\n\n  <a href="javascript:void(0)" class="expand" onclick="return togglecomment(this)">\n    ')
        # SOURCE LINE 94
        __M_writer(conditional_websafe("[%s]" % ("+" if thing.collapsed else "–")))
        __M_writer(u'\n  </a>\n\n')
        # SOURCE LINE 97
        if show:
            # SOURCE LINE 98
            if thing.deleted:
                # SOURCE LINE 99
                __M_writer(u'       <em>')
                __M_writer(conditional_websafe(_("deleted comment from")))
                __M_writer(u'</em>&#32;\n')
            # SOURCE LINE 101
            __M_writer(u'     ')
            __M_writer(conditional_websafe(WrappedUser(thing.author, thing.attribs, thing)))
            __M_writer(u'\n     &#32;\n')
            # SOURCE LINE 103
        else:
            # SOURCE LINE 104
            __M_writer(u'     <em>')
            __M_writer(conditional_websafe(_("[deleted]")))
            __M_writer(u'</em>&#32;\n')
        # SOURCE LINE 106
        __M_writer(u'\n')
        # SOURCE LINE 107
        if thing.collapsed and show and hasattr(thing, "collapsed_reason"):
            # SOURCE LINE 108
            __M_writer(u'    <span class="collapsed-reason">')
            __M_writer(conditional_websafe(thing.collapsed_reason))
            __M_writer(u'</span>\n')
        # SOURCE LINE 110
        __M_writer(u'\n')
        # SOURCE LINE 111
        if show and thing.score_hidden:
            # SOURCE LINE 112
            __M_writer(u'    <span title="')
            __M_writer(conditional_websafe(_('this subreddit hides comment scores for %d minutes') % thing.subreddit.comment_score_hide_mins))
            __M_writer(u'">\n      [')
            # SOURCE LINE 113
            __M_writer(conditional_websafe(_("score hidden")))
            __M_writer(u']\n    </span>&#32;\n')
            # SOURCE LINE 115
        elif show and not thing.score_hidden:
            # SOURCE LINE 116
            __M_writer(u'    ')
            __M_writer(conditional_websafe(unsafe(self.score(thing))))
            __M_writer(u'&#32;\n')
        # SOURCE LINE 118
        __M_writer(u'\n  ')
        # SOURCE LINE 119
        __M_writer(conditional_websafe(thing_timestamp(thing, thing.timesince, live=True, include_tense=True)))
        __M_writer(u'\n  ')
        # SOURCE LINE 120
        __M_writer(conditional_websafe(edited(thing, thing.lastedited)))
        __M_writer(u'\n  ')
        # SOURCE LINE 121
        __M_writer(conditional_websafe(self.gildings()))
        __M_writer(u'\n\n')
        # SOURCE LINE 123
        if thing.is_sticky:
            # SOURCE LINE 124
            __M_writer(u'  &#32;\n  <span class="stickied-tagline" title="')
            # SOURCE LINE 125
            __M_writer(conditional_websafe(_("selected by this subreddit's moderators")))
            __M_writer(u'">')
            __M_writer(conditional_websafe(_("stickied comment")))
            __M_writer(u'</span>\n')
        # SOURCE LINE 127
        __M_writer(u'\n  &nbsp;\n  <a href="javascript:void(0)" class="numchildren" onclick="return togglecomment(this)">\n    (')
        # SOURCE LINE 130
        __M_writer(conditional_websafe(thing.numchildren_text))
        __M_writer(u')\n  </a>\n\n  ')
        # SOURCE LINE 133
        __M_writer(conditional_websafe(self.approval_checkmark()))
        __M_writer(u'\n')
        # SOURCE LINE 134
        if getattr(thing, 'savedcategory', None) is not None:
            # SOURCE LINE 135
            __M_writer(u'    ')
            __M_writer(conditional_websafe(plain_link(_('category: %s') % thing.savedcategory,
                 '/user/%s/saved/%s' % (c.user.name, thing.savedcategory),
                 _class='save-category' + ('' if thing.savedcategory else ' hidden')
                )))
            # SOURCE LINE 138
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_arrows(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7b3fe90')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited', u'nsfw_stamp', u'quarantine_stamp'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 202
        __M_writer(u'\n  ')
        # SOURCE LINE 203
        __M_writer(conditional_websafe(parent.midcol()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_subreddit(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        context._push_buffer()
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7b3fe90')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited', u'nsfw_stamp', u'quarantine_stamp'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 41
        __M_writer(u'\n  ')
        # SOURCE LINE 42
        __M_writer(conditional_websafe(plain_link(thing.subreddit.name, thing.subreddit_path, _sr_path=False,
               _class="subreddit hover")))
        # SOURCE LINE 43
        __M_writer(u'\n')
    finally:
        __M_buf = context._pop_buffer()
        context.caller_stack._pop_frame()
    return __M_buf.getvalue()


def render_ParentDiv(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7b3fe90')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited', u'nsfw_stamp', u'quarantine_stamp'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 69
        __M_writer(u'\n  ')
        # SOURCE LINE 70
        __M_writer(conditional_websafe(parent.ParentDiv()))
        __M_writer(u'\n')
        # SOURCE LINE 71
        if not thing.deleted:
            # SOURCE LINE 72
            __M_writer(u'    <a name="')
            __M_writer(conditional_websafe(thing._id36))
            __M_writer(u'"></a>\n')
        # SOURCE LINE 74
        if c.profilepage:
            # SOURCE LINE 75
            __M_writer(u'    ')

            tagline_text = conditional_websafe(thing.taglinetext).replace(" ", "&#32;")
            tagline_attrs = dict(link=self.link(),
                         subreddit=self.subreddit(),
                         author=thing.link_author.render())
                
            
            # SOURCE LINE 80
            __M_writer(u'\n    ')
            # SOURCE LINE 81
            __M_writer(conditional_websafe(unsafe(tagline_text % tagline_attrs)))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_link(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        context._push_buffer()
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7b3fe90')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited', u'nsfw_stamp', u'quarantine_stamp'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 46
        __M_writer(u'\n  ')
        # SOURCE LINE 47


        if thing.link.is_self:
          url = thing.link.url
          inbound_tracking_url = thing.link.tracking_link(url, thing, "title", site_name=False)
        else:
          url = thing.link.url
          inbound_tracking_url = None
          
        
        # SOURCE LINE 55
        __M_writer(u'\n  <a href="')
        # SOURCE LINE 56
        __M_writer(conditional_websafe(url))
        __M_writer(u'" class="title"\n')
        # SOURCE LINE 57
        if inbound_tracking_url and inbound_tracking_url != url:
            # SOURCE LINE 58
            __M_writer(u'       data-inbound-url="')
            __M_writer(conditional_websafe(inbound_tracking_url))
            __M_writer(u'"\n       data-href-url="')
            # SOURCE LINE 59
            __M_writer(conditional_websafe(url))
            __M_writer(u'"\n')
        # SOURCE LINE 61
        if thing.nofollow:
            # SOURCE LINE 62
            __M_writer(u'       rel="nofollow"\n')
        # SOURCE LINE 64
        __M_writer(u'     >\n    ')
        # SOURCE LINE 65
        __M_writer(conditional_websafe(thing.link.title))
        __M_writer(u'\n  </a>\n')
    finally:
        __M_buf = context._pop_buffer()
        context.caller_stack._pop_frame()
    return __M_buf.getvalue()


def render_midcol(context,display=True,cls=''):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7b3fe90')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited', u'nsfw_stamp', u'quarantine_stamp'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 37
        __M_writer(u'\n')
        # SOURCE LINE 38
        __M_writer(conditional_websafe(parent.midcol(cls = cls)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_Child(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7b3fe90')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited', u'nsfw_stamp', u'quarantine_stamp'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 142
        __M_writer(u'\n')
        # SOURCE LINE 143
        if not c.profilepage and thing.link.contest_mode and hasattr(thing, "child") and not thing.parent_id:
            # SOURCE LINE 144
            __M_writer(u'  <a href="#" class="showreplies"\n     onclick="$(this).hide();$(this).parent().find(\'.noncollapsed\').show();return false;">\n    [')
            # SOURCE LINE 146
            __M_writer(conditional_websafe(_("show replies")))
            __M_writer(u']\n  </a>\n  <div class="child noncollapsed" style="display:none">\n')
            # SOURCE LINE 149
        else:
            # SOURCE LINE 150
            __M_writer(u'  <div class="child">\n')
        # SOURCE LINE 152
        if thing.childlisting:
            # SOURCE LINE 153
            __M_writer(u'    ')
            __M_writer(conditional_websafe(thing.childlisting))
            __M_writer(u'\n')
        # SOURCE LINE 155
        __M_writer(u'  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_commentBody(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7b3fe90')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited', u'nsfw_stamp', u'quarantine_stamp'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 195
        __M_writer(u'\n  ')
        # SOURCE LINE 196
        __M_writer(conditional_websafe(parent.commentBody()))
        __M_writer(u'\n')
        # SOURCE LINE 197
        if getattr(thing, 'show_admin_context', None):
            # SOURCE LINE 198
            __M_writer(u'    ')
            __M_writer(conditional_websafe(self.fullContext()))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_fullContext(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7b3fe90')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited', u'nsfw_stamp', u'quarantine_stamp'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 158
        __M_writer(u'\n  <div class="md-container-small full-context-info full-context-info-')
        # SOURCE LINE 159
        __M_writer(conditional_websafe(thing._fullname))
        __M_writer(u'" style="display:none;">\n    <div class="md">\n      <table>\n        <tbody>\n          <tr>\n            <td>')
        # SOURCE LINE 164
        __M_writer(conditional_websafe(thing.author_slow.name))
        __M_writer(u'</td>\n            <td>\n              <div class="arrow full-context-vote-')
        # SOURCE LINE 166
        __M_writer(conditional_websafe(thing._fullname))
        __M_writer(u'"></div>\n            </td>\n            <td><a href="" class="full-context-op-')
        # SOURCE LINE 168
        __M_writer(conditional_websafe(thing._fullname))
        __M_writer(u'"></a></td>\n            <td class="full-context-vote-time-')
        # SOURCE LINE 169
        __M_writer(conditional_websafe(thing._fullname))
        __M_writer(u'"></td>\n          </tr>\n          <tr>\n            <td>')
        # SOURCE LINE 172
        __M_writer(conditional_websafe(thing.author_slow.name))
        __M_writer(u'</td>\n            <td>replied to</td>\n            <td><a href="" class="full-context-op-')
        # SOURCE LINE 174
        __M_writer(conditional_websafe(thing._fullname))
        __M_writer(u'"></a></td>\n            <td class="full-context-comment-time-')
        # SOURCE LINE 175
        __M_writer(conditional_websafe(thing._fullname))
        __M_writer(u'"></td>\n          </tr>\n          <tr>\n            <td><a href="" class="full-context-op-')
        # SOURCE LINE 178
        __M_writer(conditional_websafe(thing._fullname))
        __M_writer(u'"></a></td>\n            <td>\n              <div class="arrow full-op-vote-')
        # SOURCE LINE 180
        __M_writer(conditional_websafe(thing._fullname))
        __M_writer(u'"></div>\n            </td>\n            <td>')
        # SOURCE LINE 182
        __M_writer(conditional_websafe(thing.author_slow.name))
        __M_writer(u'</td>\n            <td class="full-op-vote-time-')
        # SOURCE LINE 183
        __M_writer(conditional_websafe(thing._fullname))
        __M_writer(u'"></td>\n          </tr>\n        </tbody>\n      </table>\n      <div class="parent">\n        <strong>full context:</strong>\n        <p class="full-context-comment-')
        # SOURCE LINE 189
        __M_writer(conditional_websafe(thing._fullname))
        __M_writer(u'"></p>\n      </div>\n    </div>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


