# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505003062.181779
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/link.html'
_template_uri = '/link.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['domain', 'numcol', 'tagline', 'thumbnail', 'subreddit', 'buttons', 'thing_data_attributes', 'midcol', 'child', 'make_link', 'entry', 'bottom_buttons', 'thing_css_class', 'flair']


# SOURCE LINE 23

from pylons import app_globals as g

from r2.config import feature
from r2.lib.filters import conditional_websafe
from r2.lib.template_helpers import (
    get_domain,
    get_linkflair_css_classes,
    js_timestamp,
    make_url_protocol_relative,
)
from r2.lib.pages.things import LinkButtons
from r2.lib.pages import WrappedUser
from r2.lib.strings import Score, strings


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 41
    ns = runtime.TemplateNamespace('__anon_0x7f36095cc710', context._clean_inheritance_tokens(), templateuri=u'printablebuttons.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f36095cc710')] = ns

    # SOURCE LINE 40
    ns = runtime.TemplateNamespace('__anon_0x7f36095cc650', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f36095cc650')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'printable.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f36095cc710')._populate(_import_ns, [u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f36095cc650')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited', u'nsfw_stamp', u'quarantine_stamp', u'thumbnail_img'])
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 37
        __M_writer(u'\n \n')
        # SOURCE LINE 39
        __M_writer(u'\n')
        # SOURCE LINE 40
        __M_writer(u'\n')
        # SOURCE LINE 41
        __M_writer(u'\n \n')
        # SOURCE LINE 47
        __M_writer(u'\n\n')
        # SOURCE LINE 75
        __M_writer(u'\n\n')
        # SOURCE LINE 93
        __M_writer(u'\n\n')
        # SOURCE LINE 99
        __M_writer(u'\n\n')
        # SOURCE LINE 169
        __M_writer(u'\n\n')
        # SOURCE LINE 174
        __M_writer(u'\n\n')
        # SOURCE LINE 196
        __M_writer(u'\n\n')
        # SOURCE LINE 201
        __M_writer(u'\n\n')
        # SOURCE LINE 219
        __M_writer(u'\n\n\n')
        # SOURCE LINE 234
        __M_writer(u'\n\n')
        # SOURCE LINE 257
        __M_writer(u'\n\n')
        # SOURCE LINE 260
        __M_writer(u'\n\n')
        # SOURCE LINE 266
        __M_writer(u'\n\n')
        # SOURCE LINE 274
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_domain(context,link=True):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f36095cc710')._populate(_import_ns, [u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f36095cc650')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited', u'nsfw_stamp', u'quarantine_stamp', u'thumbnail_img'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 222
        __M_writer(u'\n  <span class="domain">\n')
        # SOURCE LINE 224
        if link:
            # SOURCE LINE 225
            __M_writer(u'      (<a href="')
            __M_writer(conditional_websafe(thing.domain_path))
            __M_writer(u'">')
            __M_writer(conditional_websafe(thing.domain_str))
            __M_writer(u'</a>)\n')
            # SOURCE LINE 226
        else:
            # SOURCE LINE 227
            __M_writer(u'      (')
            __M_writer(conditional_websafe(thing.domain_str))
            __M_writer(u')\n')
        # SOURCE LINE 229
        if c.user_is_admin:
            # SOURCE LINE 230
            __M_writer(u'      &#32;\n      <a class="adminbox" href="/admin/domain/')
            # SOURCE LINE 231
            __M_writer(conditional_websafe(thing.domain))
            __M_writer(u'">d</a>\n')
        # SOURCE LINE 233
        __M_writer(u'  </span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_numcol(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f36095cc710')._populate(_import_ns, [u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f36095cc650')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited', u'nsfw_stamp', u'quarantine_stamp', u'thumbnail_img'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 43
        __M_writer(u'\n  <span class="rank">\n    ')
        # SOURCE LINE 45
        __M_writer(conditional_websafe(thing.num_text))
        __M_writer(u'\n  </span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tagline(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f36095cc710')._populate(_import_ns, [u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f36095cc650')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited', u'nsfw_stamp', u'quarantine_stamp', u'thumbnail_img'])
        edited = _import_ns.get('edited', context.get('edited', UNDEFINED))
        thing_timestamp = _import_ns.get('thing_timestamp', context.get('thing_timestamp', UNDEFINED))
        capture = _import_ns.get('capture', context.get('capture', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 236
        __M_writer(u'\n  ')
        # SOURCE LINE 237

        taglinetext = conditional_websafe(thing.taglinetext).replace(" ", "&#32;")
          
        
        # SOURCE LINE 239
        __M_writer(u'\n  ')
        # SOURCE LINE 240
        __M_writer(conditional_websafe(unsafe(taglinetext % dict(reddit=self.subreddit(),
                              score=capture(self.score, thing, tag='span'),
                              when=capture(thing_timestamp, thing, thing.timesince, live=True, include_tense=True),
                              author=WrappedUser(thing.author, thing.attribs, thing).render(),
                              lastedited=capture(edited, thing, thing.lastedited)
                              ))))
        # SOURCE LINE 245
        __M_writer(u'\n  ')
        # SOURCE LINE 246
        __M_writer(conditional_websafe(self.gildings()))
        __M_writer(u'\n')
        # SOURCE LINE 247
        if thing.use_sticky_style:
            # SOURCE LINE 248
            __M_writer(u'    &#32;-&#32;<span class="stickied-tagline" title="selected by this subreddit\'s moderators">announcement</span>\n')
        # SOURCE LINE 250
        __M_writer(u'\n')
        # SOURCE LINE 251
        if getattr(thing, 'savedcategory', None) is not None:
            # SOURCE LINE 252
            __M_writer(u'    ')
            __M_writer(conditional_websafe(plain_link(_('category: %s') % thing.savedcategory,
                 '/user/%s/saved/%s' % (c.user.name, thing.savedcategory),
                 _class='save-category' + ('' if thing.savedcategory else ' hidden')
                )))
            # SOURCE LINE 255
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_thumbnail(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f36095cc710')._populate(_import_ns, [u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f36095cc650')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited', u'nsfw_stamp', u'quarantine_stamp', u'thumbnail_img'])
        def make_link(name,css_class,tabindex=0):
            return render_make_link(context,name,css_class,tabindex)
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 268
        __M_writer(u'\n')
        # SOURCE LINE 269
        if thing.thumbnail:
            # SOURCE LINE 270
            __M_writer(u'  ')
            def ccall(caller):
                def body():
                    thumbnail_img = _import_ns.get('thumbnail_img', context.get('thumbnail_img', UNDEFINED))
                    __M_writer = context.writer()
                    __M_writer(u'\n    ')
                    # SOURCE LINE 271
                    __M_writer(conditional_websafe(thumbnail_img(thing)))
                    __M_writer(u'\n  ')
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 270
                __M_writer(conditional_websafe(make_link('thumbnail', 'thumbnail ' + (thing.thumbnail if thing.thumbnail_sprited else ''))))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 272
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_subreddit(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        context._push_buffer()
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f36095cc710')._populate(_import_ns, [u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f36095cc650')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited', u'nsfw_stamp', u'quarantine_stamp', u'thumbnail_img'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 198
        __M_writer(u'\n  ')
        # SOURCE LINE 199
        __M_writer(conditional_websafe(plain_link('/r/' + thing.subreddit.name, thing.subreddit_path, _sr_path=False,
               _class="subreddit hover may-blank")))
        # SOURCE LINE 200
        __M_writer(u'\n')
    finally:
        __M_buf = context._pop_buffer()
        context.caller_stack._pop_frame()
    return __M_buf.getvalue()


def render_buttons(context,comments=True,delete=True,report=True,additional=''):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f36095cc710')._populate(_import_ns, [u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f36095cc650')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited', u'nsfw_stamp', u'quarantine_stamp', u'thumbnail_img'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 262
        __M_writer(u'\n  ')
        # SOURCE LINE 263
        __M_writer(conditional_websafe(LinkButtons(thing, comments = comments, delete = delete,
                report = report,
               )))
        # SOURCE LINE 265
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_thing_data_attributes(context,what):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f36095cc710')._populate(_import_ns, [u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f36095cc650')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited', u'nsfw_stamp', u'quarantine_stamp', u'thumbnail_img'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 176
        __M_writer(u'\n  ')
        # SOURCE LINE 177
        __M_writer(conditional_websafe(parent.thing_data_attributes(what)))
        __M_writer(u'\n\n')
        # SOURCE LINE 179
        if not getattr(what, 'deleted', False):
            # SOURCE LINE 180
            __M_writer(u'    data-author="')
            __M_writer(conditional_websafe(what.author.name))
            __M_writer(u'"\n    data-author-fullname="')
            # SOURCE LINE 181
            __M_writer(conditional_websafe(what.author._fullname))
            __M_writer(u'"\n')
        # SOURCE LINE 183
        __M_writer(u'\n  data-subreddit="')
        # SOURCE LINE 184
        __M_writer(conditional_websafe(what.subreddit.name))
        __M_writer(u'"\n  data-subreddit-fullname="')
        # SOURCE LINE 185
        __M_writer(conditional_websafe(what.subreddit._fullname))
        __M_writer(u'"\n\n  data-timestamp="')
        # SOURCE LINE 187
        __M_writer(conditional_websafe(js_timestamp(what._date)))
        __M_writer(u'"\n\n  data-url="')
        # SOURCE LINE 189
        __M_writer(conditional_websafe(thing.href_url))
        __M_writer(u'"\n  data-domain="')
        # SOURCE LINE 190
        __M_writer(conditional_websafe(what.domain))
        __M_writer(u'"\n  data-rank="')
        # SOURCE LINE 191
        __M_writer(conditional_websafe(what.num_text))
        __M_writer(u'"\n\n')
        # SOURCE LINE 193
        if getattr(what, 'can_ban', False):
            # SOURCE LINE 194
            __M_writer(u'    data-can-ban="true"\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_midcol(context,display=True,cls=''):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f36095cc710')._populate(_import_ns, [u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f36095cc650')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited', u'nsfw_stamp', u'quarantine_stamp', u'thumbnail_img'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 203
        __M_writer(u'\n    <div class="midcol ')
        # SOURCE LINE 204
        __M_writer(conditional_websafe(cls))
        __M_writer(u'"\n       ')
        # SOURCE LINE 205
        __M_writer(conditional_websafe(not display and "style='display:none'" or ''))
        __M_writer(u'>\n    ')
        # SOURCE LINE 206
        __M_writer(conditional_websafe(self.arrow(thing, 1, thing.likes)))
        __M_writer(u'\n')
        # SOURCE LINE 207
        if thing.pref_compress:
            # SOURCE LINE 208
            __M_writer(u'      <div class="score-placeholder"></div>\n')
            # SOURCE LINE 209
        elif thing.hide_score:
            # SOURCE LINE 210
            __M_writer(u'      <div class="score likes">&bull;</div> \n      <div class="score unvoted">&bull;</div> \n      <div class="score dislikes">&bull;</div> \n')
            # SOURCE LINE 213
        else:
            # SOURCE LINE 214
            __M_writer(u'      ')
            __M_writer(conditional_websafe(self.score(thing, tag='div')))
            __M_writer(u'\n')
        # SOURCE LINE 216
        __M_writer(u'    ')
        __M_writer(conditional_websafe(self.arrow(thing, 0, thing.likes == False)))
        __M_writer(u'\n  </div>\n ')
        # SOURCE LINE 218
        __M_writer(conditional_websafe(self.thumbnail()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_child(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f36095cc710')._populate(_import_ns, [u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f36095cc650')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited', u'nsfw_stamp', u'quarantine_stamp', u'thumbnail_img'])
        __M_writer = context.writer()
        # SOURCE LINE 259
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_make_link(context,name,css_class,tabindex=0):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f36095cc710')._populate(_import_ns, [u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f36095cc650')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited', u'nsfw_stamp', u'quarantine_stamp', u'thumbnail_img'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        caller = _import_ns.get('caller', context.get('caller', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 49
        __M_writer(u'\n  ')
        # SOURCE LINE 50

        media_override = thing.link_child and getattr(thing, 'media_override', False)
        if thing.is_self:
          url = thing.href_url
          inbound_tracking_url = thing.tracking_link(url, thing, name)
        else:
          url = thing.href_url
          inbound_tracking_url = None
          
        
        # SOURCE LINE 58
        __M_writer(u'\n  <a class="')
        # SOURCE LINE 59
        __M_writer(conditional_websafe(css_class))
        __M_writer(u' may-blank ')
        __M_writer(conditional_websafe( c.user_is_loggedin and 'loggedin' or ''))
        __M_writer(u'\n            ')
        # SOURCE LINE 60
        __M_writer(conditional_websafe( media_override and 'open-expando' or '' ))
        __M_writer(u'"\n     href="')
        # SOURCE LINE 61
        __M_writer(conditional_websafe(url))
        __M_writer(u'"\n')
        # SOURCE LINE 62
        if tabindex:
            # SOURCE LINE 63
            __M_writer(u'       tabindex="')
            __M_writer(conditional_websafe(tabindex))
            __M_writer(u'"\n')
        # SOURCE LINE 65
        if thing.nofollow:
            # SOURCE LINE 66
            __M_writer(u'       rel="nofollow"\n')
        # SOURCE LINE 68
        if inbound_tracking_url and inbound_tracking_url != url:
            # SOURCE LINE 69
            __M_writer(u'       data-href-url="')
            __M_writer(conditional_websafe(url))
            __M_writer(u'"\n       data-inbound-url="')
            # SOURCE LINE 70
            __M_writer(conditional_websafe(inbound_tracking_url))
            __M_writer(u'"\n')
        # SOURCE LINE 72
        __M_writer(u'     >\n     ')
        # SOURCE LINE 73
        __M_writer(conditional_websafe(caller.body()))
        __M_writer(u'\n  </a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_entry(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f36095cc710')._populate(_import_ns, [u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f36095cc650')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited', u'nsfw_stamp', u'quarantine_stamp', u'thumbnail_img'])
        def make_link(name,css_class,tabindex=0):
            return render_make_link(context,name,css_class,tabindex)
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        def bottom_buttons():
            return render_bottom_buttons(context)
        def flair():
            return render_flair(context)
        __M_writer = context.writer()
        # SOURCE LINE 101
        __M_writer(u'\n  <p class="title">\n')
        # SOURCE LINE 103
        if c.site.link_flair_position == 'left':
            # SOURCE LINE 104
            __M_writer(u'      ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                __M_writer(conditional_websafe(flair()))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n')
        # SOURCE LINE 106
        __M_writer(u'    ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                __M_writer(u'\n      ')
                # SOURCE LINE 107
                __M_writer(conditional_websafe(thing.title))
                __M_writer(u'\n    ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 106
            __M_writer(conditional_websafe(make_link('title', 'title', tabindex=1)))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 108
        __M_writer(u'\n')
        # SOURCE LINE 109
        if c.site.link_flair_position == 'right':
            # SOURCE LINE 110
            __M_writer(u'      ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                __M_writer(conditional_websafe(flair()))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n')
        # SOURCE LINE 112
        __M_writer(u'    ')
        __M_writer(conditional_websafe(self.approval_checkmark()))
        __M_writer(u'\n    &#32;\n\n    ')
        # SOURCE LINE 115
        __M_writer(conditional_websafe(self.domain()))
        __M_writer(u'\n\n')
        # SOURCE LINE 117
        if c.user_is_admin:
            # SOURCE LINE 118
            for link_note in thing.link_notes:
                # SOURCE LINE 119
                __M_writer(u'           &#32;<span class="link-note">[')
                __M_writer(conditional_websafe(link_note))
                __M_writer(u']</span>\n')
        # SOURCE LINE 122
        __M_writer(u'  </p>\n\n')
        # SOURCE LINE 125
        __M_writer(u'  ')
        selftext_hide = thing.is_self and not thing.selftext 
        
        __M_writer(u'\n')
        # SOURCE LINE 126
        if thing.link_child:
            # SOURCE LINE 127
            if not thing.link_child.expand and not selftext_hide:
                # SOURCE LINE 128
                __M_writer(u'      <div class="expando-button collapsed\n                  ')
                # SOURCE LINE 129
                __M_writer(conditional_websafe(thing.link_child.css_style))
                __M_writer(u'"></div>\n')
                # SOURCE LINE 130
            elif thing.link_child.expand and not thing.link_child.position_inline:
                # SOURCE LINE 131
                __M_writer(u'      <div class="expando-button expanded\n                  ')
                # SOURCE LINE 132
                __M_writer(conditional_websafe(thing.link_child.css_style))
                __M_writer(u'"></div>\n')
        # SOURCE LINE 135
        __M_writer(u'\n  <p class="tagline">\n    ')
        # SOURCE LINE 137
        __M_writer(conditional_websafe(self.tagline()))
        __M_writer(u'\n  </p>\n\n  ')
        # SOURCE LINE 140
 
        child_content = ""
        if thing.link_child and thing.link_child.load:
          child_content = unsafe(thing.link_child.content())
        expand = thing.link_child and thing.link_child.expand
        position_inline = thing.link_child and thing.link_child.position_inline
          
        
        # SOURCE LINE 146
        __M_writer(u'\n\n')
        # SOURCE LINE 149
        if not position_inline:
            # SOURCE LINE 150
            __M_writer(u'    ')
            __M_writer(conditional_websafe(bottom_buttons()))
            __M_writer(u'\n')
        # SOURCE LINE 152
        __M_writer(u'\n  <div class="expando expando-uninitialized" ')
        # SOURCE LINE 153
        __M_writer(conditional_websafe("style='display: none'" if not expand else ""))
        __M_writer(u'\n')
        # SOURCE LINE 154
        if not expand and child_content:
            # SOURCE LINE 155
            __M_writer(u'      data-cachedhtml="')
            __M_writer(conditional_websafe(websafe(child_content)))
            __M_writer(u'"\n')
        # SOURCE LINE 157
        __M_writer(u'  >\n')
        # SOURCE LINE 158
        if expand:
            # SOURCE LINE 159
            __M_writer(u'      ')
            __M_writer(conditional_websafe(child_content))
            __M_writer(u'\n')
            # SOURCE LINE 160
        else:
            # SOURCE LINE 161
            __M_writer(u'      <span class="error">loading...</span>\n')
        # SOURCE LINE 163
        __M_writer(u'  </div>\n\n')
        # SOURCE LINE 166
        if position_inline:
            # SOURCE LINE 167
            __M_writer(u'    ')
            __M_writer(conditional_websafe(bottom_buttons()))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bottom_buttons(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f36095cc710')._populate(_import_ns, [u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f36095cc650')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited', u'nsfw_stamp', u'quarantine_stamp', u'thumbnail_img'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        quarantine_stamp = _import_ns.get('quarantine_stamp', context.get('quarantine_stamp', UNDEFINED))
        nsfw_stamp = _import_ns.get('nsfw_stamp', context.get('nsfw_stamp', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 77
        __M_writer(u'\n  <ul class="flat-list buttons">\n')
        # SOURCE LINE 79
        if thing.quarantine:
            # SOURCE LINE 80
            __M_writer(u'      <li>\n        <span class="quarantine-stamp stamp">')
            # SOURCE LINE 81
            __M_writer(conditional_websafe(quarantine_stamp()))
            __M_writer(u'</span>\n      </li>\n')
        # SOURCE LINE 84
        if thing.nsfw:
            # SOURCE LINE 85
            __M_writer(u'     <li>\n       <span class="nsfw-stamp stamp">')
            # SOURCE LINE 86
            __M_writer(conditional_websafe(nsfw_stamp()))
            __M_writer(u'</span>\n     </li>\n')
        # SOURCE LINE 89
        __M_writer(u'    ')
        __M_writer(conditional_websafe(self.buttons()))
        __M_writer(u'\n    ')
        # SOURCE LINE 90
        __M_writer(conditional_websafe(self.admintagline()))
        __M_writer(u'\n  </ul>\n  <div class="reportform report-')
        # SOURCE LINE 92
        __M_writer(conditional_websafe(thing._fullname))
        __M_writer(u'"></div>\n ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_thing_css_class(context,what):
    __M_caller = context.caller_stack._push_frame()
    try:
        context._push_buffer()
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f36095cc710')._populate(_import_ns, [u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f36095cc650')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited', u'nsfw_stamp', u'quarantine_stamp', u'thumbnail_img'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 171
        __M_writer(u'\n  ')
        # SOURCE LINE 172
        __M_writer(conditional_websafe(parent.thing_css_class(what)))
        __M_writer(u' ')
        __M_writer(conditional_websafe("over18" if thing.over_18 else ""))
        __M_writer(u' ')
        __M_writer(conditional_websafe(thing.visited and 'visited' or ''))
        __M_writer(u'\n  ')
        # SOURCE LINE 173
        __M_writer(conditional_websafe(get_linkflair_css_classes(thing, on_class="linkflair", off_class="")))
        __M_writer(u'\n')
    finally:
        __M_buf = context._pop_buffer()
        context.caller_stack._pop_frame()
    return __M_buf.getvalue()


def render_flair(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f36095cc710')._populate(_import_ns, [u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f36095cc650')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited', u'nsfw_stamp', u'quarantine_stamp', u'thumbnail_img'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 95
        __M_writer(u'\n')
        # SOURCE LINE 96
        if c.user.pref_show_link_flair and thing.flair_text:
            # SOURCE LINE 97
            __M_writer(u'    <span class="linkflairlabel" title="')
            __M_writer(conditional_websafe(thing.flair_text))
            __M_writer(u'">')
            __M_writer(conditional_websafe(thing.flair_text))
            __M_writer(u'</span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


