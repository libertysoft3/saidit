# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1508315329.597778
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/multiinfobar.html'
_template_uri = '/multiinfobar.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23

from r2.config import feature
from r2.lib.strings import strings, Score
from r2.lib.pages import WrappedUser, UserText
from r2.lib.template_helpers import _ws, _wsf, format_html
 

def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 30
    ns = runtime.TemplateNamespace('__anon_0x7f7e31236d10', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f7e31236d10')] = ns

    # SOURCE LINE 31
    ns = runtime.TemplateNamespace('__anon_0x7f7e31236ad0', context._clean_inheritance_tokens(), templateuri=u'printablebuttons.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f7e31236ad0')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f7e31236d10')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'text_with_links'])
        _mako_get_namespace(context, '__anon_0x7f7e31236ad0')._populate(_import_ns, [u'ynbutton', u'state_button'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        thing_timestamp = _import_ns.get('thing_timestamp', context.get('thing_timestamp', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 28
        __M_writer(u'\n\n')
        # SOURCE LINE 30
        __M_writer(u'\n')
        # SOURCE LINE 31
        __M_writer(u'\n<div class="titlebox multi-details" data-path="')
        # SOURCE LINE 32
        __M_writer(conditional_websafe(thing.multi.path))
        __M_writer(u'">\n  <h1 class="hover redditname">\n    <a href="')
        # SOURCE LINE 34
        __M_writer(conditional_websafe(thing.multi.path))
        __M_writer(u'">')
        __M_writer(conditional_websafe(_('%s subreddits') % thing.multi.name))
        __M_writer(u'</a><div class="throbber"></div>\n  </h1>\n  <h2><a href="/user/')
        # SOURCE LINE 36
        __M_writer(conditional_websafe(thing.multi.owner.name))
        __M_writer(u'">')
        __M_writer(conditional_websafe(_('curated by /u/%s') % thing.multi.owner.name))
        __M_writer(u'</a></h2>\n  <div class="gray-buttons settings">\n')
        # SOURCE LINE 38
        if thing.can_edit:
            # SOURCE LINE 39
            __M_writer(u'      <div class="visibility-group">\n        <label><input type="radio" name="visibility" value="private" ')
            # SOURCE LINE 40
            __M_writer(conditional_websafe('checked' if thing.multi.visibility == 'private' else ''))
            __M_writer(u'>')
            __M_writer(conditional_websafe(_('private')))
            __M_writer(u'</label>\n        <label><input type="radio" name="visibility" value="public" ')
            # SOURCE LINE 41
            __M_writer(conditional_websafe('checked' if thing.multi.visibility == 'public' else ''))
            __M_writer(u'>')
            __M_writer(conditional_websafe(_('public')))
            __M_writer(u'</label>\n')
            # SOURCE LINE 42
            if feature.is_enabled('multireddit_customizations') or thing.multi.visibility == 'hidden':
                # SOURCE LINE 43
                __M_writer(u'          <label><input type="radio" name="visibility" value="hidden" ')
                __M_writer(conditional_websafe('checked' if thing.multi.visibility == 'hidden' else ''))
                __M_writer(u'>')
                __M_writer(conditional_websafe(_('hidden')))
                __M_writer(u'</label>\n')
            # SOURCE LINE 45
            __M_writer(u'      </div>\n      <div class="spacer gray-buttons settings">\n')
            # SOURCE LINE 47
            if thing.can_copy:
                # SOURCE LINE 48
                __M_writer(u'          <button class="show-copy">')
                __M_writer(conditional_websafe(_('copy')))
                __M_writer(u'</button>\n')
            # SOURCE LINE 50
            if thing.can_rename:
                # SOURCE LINE 51
                __M_writer(u'          <button class="show-rename">')
                __M_writer(conditional_websafe(_('rename')))
                __M_writer(u'</button>\n')
            # SOURCE LINE 53
            __M_writer(u'        <button class="delete">')
            __M_writer(conditional_websafe(_('delete')))
            __M_writer(u'</button>\n      </div>\n')
            # SOURCE LINE 55
            if feature.is_enabled('multireddit_customizations'):
                # SOURCE LINE 56
                __M_writer(u'      <div>\n        <select name="key_color">\n')
                # SOURCE LINE 58
                if thing.multi.key_color not in thing.color_options:
                    # SOURCE LINE 59
                    __M_writer(u'            <option selected value="')
                    __M_writer(conditional_websafe(thing.multi.key_color))
                    __M_writer(u'">')
                    __M_writer(conditional_websafe(_('custom')))
                    __M_writer(u'</option>\n')
                # SOURCE LINE 61
                for color, name in thing.color_options.iteritems():
                    # SOURCE LINE 62
                    __M_writer(u'            <option ')
                    __M_writer(conditional_websafe('selected' if color == thing.multi.key_color else ''))
                    __M_writer(u' value="')
                    __M_writer(conditional_websafe(color))
                    __M_writer(u'">')
                    __M_writer(conditional_websafe(_(name)))
                    __M_writer(u'</option>\n')
                # SOURCE LINE 64
                __M_writer(u'        </select>\n        <select name="icon_name">\n          <option ')
                # SOURCE LINE 66
                __M_writer(conditional_websafe('' if thing.multi.icon_id else 'selected'))
                __M_writer(u' value="">')
                __M_writer(conditional_websafe(_('default')))
                __M_writer(u'</option>\n')
                # SOURCE LINE 67
                for icon_name in thing.icon_options:
                    # SOURCE LINE 68
                    __M_writer(u'            <option ')
                    __M_writer(conditional_websafe('selected' if icon_name == thing.multi.icon_id else ''))
                    __M_writer(u' value="')
                    __M_writer(conditional_websafe(icon_name))
                    __M_writer(u'">')
                    __M_writer(conditional_websafe(icon_name))
                    __M_writer(u'</option>\n')
                # SOURCE LINE 70
                __M_writer(u'        </select>\n      </div>\n')
            # SOURCE LINE 73
        else:
            # SOURCE LINE 74
            if thing.can_copy:
                # SOURCE LINE 75
                __M_writer(u'        <button class="show-copy">')
                __M_writer(conditional_websafe(_('create a copy')))
                __M_writer(u'</button>\n')
        # SOURCE LINE 78
        __M_writer(u'  </div>\n\n')
        # SOURCE LINE 80
        if thing.can_copy:
            # SOURCE LINE 81
            __M_writer(u'    <form class="copy-multi">\n      <input type="text" class="multi-name" placeholder="')
            # SOURCE LINE 82
            __M_writer(conditional_websafe(_('copy name')))
            __M_writer(u'"><button class="copy">')
            __M_writer(conditional_websafe(_('copy')))
            __M_writer(u' &rsaquo;</button>\n      <div class="throbber"></div>\n      <div class="error copy-error"></div>\n    </form>\n')
        # SOURCE LINE 87
        __M_writer(u'\n')
        # SOURCE LINE 88
        if thing.can_rename:
            # SOURCE LINE 89
            __M_writer(u'    <form class="rename-multi">\n      <p class="warning">')
            # SOURCE LINE 90
            __M_writer(conditional_websafe(_('warning: renaming a multi will break any links and references to the old name.')))
            __M_writer(u'</p>\n      <input type="text" class="multi-name" placeholder="')
            # SOURCE LINE 91
            __M_writer(conditional_websafe(_('new name')))
            __M_writer(u'"><button class="rename">')
            __M_writer(conditional_websafe(_('rename')))
            __M_writer(u' &rsaquo;</button>\n      <div class="throbber"></div>\n      <div class="error rename-error"></div>\n    </form>\n')
        # SOURCE LINE 96
        __M_writer(u'\n  <div class="description">\n    ')
        # SOURCE LINE 98
        __M_writer(conditional_websafe(UserText(None, text=thing.description_md, post_form=None, editable=True, include_errors=False)))
        __M_writer(u'\n')
        # SOURCE LINE 99
        if thing.can_edit:
            # SOURCE LINE 100
            __M_writer(u'      <div class="gray-buttons settings">\n        <button class="edit-description">')
            # SOURCE LINE 101
            __M_writer(conditional_websafe(_('edit description')))
            __M_writer(u'</button>\n\n')
            # SOURCE LINE 103
            if thing.share_url:
                # SOURCE LINE 104
                __M_writer(u'          <a class="share-in-sr" href="')
                __M_writer(conditional_websafe(thing.share_url))
                __M_writer(u'">')
                __M_writer(conditional_websafe(_('share')))
                __M_writer(u' &rsaquo;</a>\n')
            # SOURCE LINE 106
            __M_writer(u'      </div>\n')
        # SOURCE LINE 108
        __M_writer(u'  </div>\n\n  ')
        # SOURCE LINE 110
        sr_count = format_html('<span class="count">%s</span>&#32;', len(thing.srs)) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['sr_count'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n  <h3>')
        # SOURCE LINE 111
        __M_writer(conditional_websafe(_wsf('%(count)s subreddits in this multi:', count=sr_count)))
        __M_writer(u'</h3>\n  <ul class="subreddits">\n')
        # SOURCE LINE 113
        for sr in thing.srs:
            # SOURCE LINE 114
            __M_writer(u'    <li data-name="')
            __M_writer(conditional_websafe(sr.name))
            __M_writer(u'">\n      <a href="/r/')
            # SOURCE LINE 115
            __M_writer(conditional_websafe(sr.name))
            __M_writer(u'">/r/')
            __M_writer(conditional_websafe(sr.name))
            __M_writer(u'</a>\n      <button class="remove-sr">')
            # SOURCE LINE 116
            __M_writer(conditional_websafe(_('remove')))
            __M_writer(u'</button>\n    </li>\n')
        # SOURCE LINE 119
        __M_writer(u'  </ul>\n\n')
        # SOURCE LINE 121
        if thing.can_edit:
            # SOURCE LINE 122
            __M_writer(u'    <form class="add-sr">\n      ')
            # SOURCE LINE 123
            __M_writer(conditional_websafe(thing.subreddit_selector))
            __M_writer(u'\n      <div class="error add-error"></div>\n    </form>\n')
        # SOURCE LINE 127
        __M_writer(u'\n  <div class="bottom">\n')
        # SOURCE LINE 129
        if thing.multi.owner:
            # SOURCE LINE 130
            __M_writer(u'      ')
            __M_writer(conditional_websafe(_wsf("created by %(user)s", user=WrappedUser(thing.multi.owner))))
            __M_writer(u'\n')
        # SOURCE LINE 132
        __M_writer(u'\n    <span class="age">\n      ')
        # SOURCE LINE 134
        __M_writer(conditional_websafe(_("a multireddit for")))
        __M_writer(u'&#32;')
        __M_writer(conditional_websafe(thing_timestamp(thing.multi)))
        __M_writer(u'\n    </span>\n  </div>\n\n  <div id="multi-recs" class="recommend-box">\n\n    <div class="recs">\n      <div>\n        <h1>\n          ')
        # SOURCE LINE 143
        __M_writer(conditional_websafe(_("people also added:")))
        __M_writer(u'\n        </h1>\n      </div>\n      <ul class="recommendations"></ul>\n      <span class="more">')
        # SOURCE LINE 147
        __M_writer(conditional_websafe(_("more suggestions")))
        __M_writer(u'</span>\n    </div>\n\n    <div class="endoflist">\n      <h1>')
        # SOURCE LINE 151
        __M_writer(conditional_websafe(_("no more suggestions!")))
        __M_writer(u'</h1>\n      <div class="heading">')
        # SOURCE LINE 152
        __M_writer(conditional_websafe(_("would you like to...")))
        __M_writer(u'</div>\n      <ul>\n        <li>\n          <a href="/r/ModeratorDuck/wiki/subreddit_classification" target="_blank">\n            ')
        # SOURCE LINE 156
        __M_writer(conditional_websafe(_("check out subreddits by category")))
        __M_writer(u'\n          </a>\n        </li>\n        <li>\n          <a href="/r/random" target="_blank">\n            ')
        # SOURCE LINE 161
        __M_writer(conditional_websafe(_("explore a random subreddit")))
        __M_writer(u'\n          </a>\n        </li>\n        <li>\n          <a class="reset">\n            ')
        # SOURCE LINE 166
        __M_writer(conditional_websafe(_("see the suggestions again")))
        __M_writer(u'\n          </a>\n        </li>\n      </ul>\n    </div>\n\n  </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


