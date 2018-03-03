# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1520060829.454367
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/subredditinfobar.html'
_template_uri = '/subredditinfobar.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23

from r2.config import feature
from r2.lib.filters import websafe
from r2.lib.strings import strings, Score
from r2.lib.pages import WrappedUser, QuarantineOptoutButton, SubscribeButton
from r2.lib.template_helpers import _ws, _wsf
from r2.models.listing import ModListing
 

def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 32
    ns = runtime.TemplateNamespace('__anon_0x7fc7c782c590', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fc7c782c590')] = ns

    # SOURCE LINE 33
    ns = runtime.TemplateNamespace('__anon_0x7fc7c782c450', context._clean_inheritance_tokens(), templateuri=u'printablebuttons.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fc7c782c450')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c782c590')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'text_with_links', u'_mdf'])
        _mako_get_namespace(context, '__anon_0x7fc7c782c450')._populate(_import_ns, [u'ynbutton', u'state_button'])
        thing_timestamp = _import_ns.get('thing_timestamp', context.get('thing_timestamp', UNDEFINED))
        ynbutton = _import_ns.get('ynbutton', context.get('ynbutton', UNDEFINED))
        text_with_links = _import_ns.get('text_with_links', context.get('text_with_links', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        _mdf = _import_ns.get('_mdf', context.get('_mdf', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 30
        __M_writer(u'\n\n')
        # SOURCE LINE 32
        __M_writer(u'\n')
        # SOURCE LINE 33
        __M_writer(u'\n\n<div class="titlebox">\n  <h1 class="hover redditname">\n    ')
        # SOURCE LINE 37
        __M_writer(conditional_websafe(plain_link(thing.sr.name, thing.sr.path, _sr_path=False, _class="hover")))
        __M_writer(u'\n  </h1>\n\n')
        # SOURCE LINE 40
        if thing.quarantine:
            # SOURCE LINE 41
            __M_writer(u'    <div class="quarantine-notice">\n      <div class="md-container">\n        ')
            # SOURCE LINE 43
            __M_writer(conditional_websafe(_mdf("This community is [quarantined](%(link)s) because of its shocking or highly offensive content.",
               wrap=True, link='https://reddit.zendesk.com/hc/en-us/articles/205701245')))
            # SOURCE LINE 44
            __M_writer(u'\n      </div>\n      <form method=\'post\' action=\'/api/quarantine_optout\'>\n        <input type="hidden" name="uh" value="')
            # SOURCE LINE 47
            __M_writer(conditional_websafe(c.modhash))
            __M_writer(u'"/>\n        <input type="hidden" name="sr_name" value="')
            # SOURCE LINE 48
            __M_writer(conditional_websafe(thing.sr.name))
            __M_writer(u'"/>\n        <button class="c-btn btn-quarantine" name="submit" value="submit" type="submit">\n          ')
            # SOURCE LINE 50
            __M_writer(conditional_websafe(_("Leave this community")))
            __M_writer(u'\n        </button>\n      </form>\n    </div>\n')
        # SOURCE LINE 55
        __M_writer(u'\n  ')
        # SOURCE LINE 56
        __M_writer(conditional_websafe(SubscribeButton(thing.sr)))
        __M_writer(u'\n')
        # SOURCE LINE 57
        if not thing.sr.hide_num_users_info:
            # SOURCE LINE 58
            __M_writer(u'  <span class="subscribers">')
            __M_writer(conditional_websafe(unsafe(Score.readers(thing.subscribers))))
            __M_writer(u'</span>\n\n')
            # SOURCE LINE 60
            if thing.active_visitors and thing.active_visitors.logged_in:
                # SOURCE LINE 61
                __M_writer(u'  <p class="users-online ')
                __M_writer(conditional_websafe('fuzzed' if thing.active_visitors.logged_in.is_fuzzed else ''))
                __M_writer(u'" title="')
                __M_writer(conditional_websafe(_('logged-in users viewing this subreddit in the past 15 minutes')))
                __M_writer(u'">\n    ')
                # SOURCE LINE 62
                __M_writer(conditional_websafe(unsafe(Score.users_here_now(thing.active_visitors.logged_in.count, prepend='~' if thing.active_visitors.logged_in.is_fuzzed else ''))))
                __M_writer(u'\n  </p>\n')
        # SOURCE LINE 66
        __M_writer(u'\n')
        # SOURCE LINE 67
        if thing.sr.moderator:
            # SOURCE LINE 68
            __M_writer(u'    <div class="leavemoderator">\n      ')
            # SOURCE LINE 69
            __M_writer(conditional_websafe(text_with_links(ModListing.remove_self_title % dict(action='(%(action)s)'),
          _sr_path=True,
          action=dict(
            ## TRANSLATORS: this label links to the edit moderators page.
            link_text=_('change'),
            path='about/moderators'))))
            # SOURCE LINE 74
            __M_writer(u'\n    </div>\n')
        # SOURCE LINE 77
        __M_writer(u'\n')
        # SOURCE LINE 78
        if thing.sr.contributor:
            # SOURCE LINE 79
            __M_writer(u'    ')
            __M_writer(conditional_websafe(ynbutton(op='leavecontributor',
               title=_('leave'),
               executed=_('you are no longer an approved submitter'),
               question=_('stop being an approved submitter?'),
               format=_('you are an approved submitter on this subreddit. (%(leave)s)'),
               format_arg='leave',
               hidden_data=dict(
                 id=thing.sr._fullname),
               access_required=False,
              )))
            # SOURCE LINE 88
            __M_writer(u'\n')
        # SOURCE LINE 90
        __M_writer(u'\n')
        # SOURCE LINE 91
        if thing.sr_style_toggle:
            # SOURCE LINE 92
            __M_writer(u'    <form class="toggle sr_style_toggle">\n      <input id="sr_style_enabled" type="checkbox" name="sr_style_enabled"\n        ')
            # SOURCE LINE 94
            __M_writer(conditional_websafe('checked="checked"' if thing.use_subreddit_style else ""))
            __M_writer(u'\n      >\n      <label for="sr_style_enabled">\n        ')
            # SOURCE LINE 97
            __M_writer(conditional_websafe(_("Show this subreddit's theme")))
            __M_writer(u'\n      </label>\n      <div id="sr_style_throbber" class="throbber"></div>\n    </form>\n')
        # SOURCE LINE 102
        __M_writer(u'\n')
        # SOURCE LINE 103
        if thing.flair_prefs:
            # SOURCE LINE 104
            __M_writer(u'    ')
            __M_writer(conditional_websafe(thing.flair_prefs))
            __M_writer(u'\n')
        # SOURCE LINE 106
        __M_writer(u'\n')
        # SOURCE LINE 107
        if thing.description_usertext:
            # SOURCE LINE 108
            __M_writer(u'    ')
            __M_writer(conditional_websafe(thing.description_usertext))
            __M_writer(u'\n')
        # SOURCE LINE 110
        __M_writer(u'\n  <div class="bottom">\n')
        # SOURCE LINE 112
        if thing.sr.author:
            # SOURCE LINE 113
            __M_writer(u'      ')
            __M_writer(conditional_websafe(_wsf("created by %(user)s", user=unsafe(thing.creator_text))))
            __M_writer(u'\n')
        # SOURCE LINE 115
        __M_writer(u'    \n    <span class="age">\n      ')
        # SOURCE LINE 117
        __M_writer(conditional_websafe(_("a community for")))
        __M_writer(u'&#32;')
        __M_writer(conditional_websafe(thing_timestamp(thing.sr)))
        __M_writer(u'\n    </span>  \n  </div>\n\n')
        # SOURCE LINE 121
        if c.user_is_admin:
            # SOURCE LINE 122
            __M_writer(u'    <div class="raisedbox spacer">\n')
            # SOURCE LINE 123
            if thing.sr.ban_count:
                # SOURCE LINE 124
                __M_writer(u'        <p>\n          ')
                # SOURCE LINE 125
                __M_writer(conditional_websafe(strings.times_banned % thing.sr.ban_count))
                __M_writer(u'\n        </p>\n')
            # SOURCE LINE 128
            __M_writer(u'      \n')
            # SOURCE LINE 129
            if thing.sr._spam:
                # SOURCE LINE 130
                __M_writer(u'        ')
                __M_writer(conditional_websafe(ynbutton(op='approve',
                   title=_('approve this subreddit'), 
                   executed=_('approved'),
                   hidden_data = dict(id = thing.sr._fullname),
        )))
                # SOURCE LINE 134
                __M_writer(u'\n        \n        <form id="banmessage-form" method="post" onsubmit="return post_form(this, \'admin/add_ban_message\')">\n          <input type="hidden" name="thing" value="')
                # SOURCE LINE 137
                __M_writer(conditional_websafe(thing.sr._fullname))
                __M_writer(u'">\n          <input type="hidden" name="system" value="subreddit">\n          <textarea name="message" rows=4>\n')
                # SOURCE LINE 140
                if getattr(thing.sr, 'ban_info', {}) and 'message' in thing.sr.ban_info:
                    # SOURCE LINE 141
                    __M_writer(u'              ')
                    __M_writer(conditional_websafe(thing.sr.ban_info['message'] or ''))
                    __M_writer(u'\n')
                # SOURCE LINE 143
                __M_writer(u'          </textarea>\n          <input type="submit" class="notes-button" \n            value="Set public ban message (blank for default)">\n        </form>\n        \n')
                # SOURCE LINE 148
                if hasattr(thing.sr, "banner"):
                    # SOURCE LINE 149
                    __M_writer(u'          <p>\n           ')
                    # SOURCE LINE 150
                    __M_writer(conditional_websafe(strings.banned_by % thing.sr.banner))
                    __M_writer(u'\n          </p>\n')
                # SOURCE LINE 153
                if getattr(thing.sr, 'ban_info', {}):
                    # SOURCE LINE 154
                    __M_writer(u'          <p>\n            ')
                    # SOURCE LINE 155
                    __M_writer(conditional_websafe(strings.time_banned % thing.sr.ban_info.get('banned_at') or 'N/A'))
                    __M_writer(u'\n          </p>\n')
                # SOURCE LINE 158
                __M_writer(u'\n')
                # SOURCE LINE 159
            else:
                # SOURCE LINE 160
                __M_writer(u'        ')
                __M_writer(conditional_websafe(ynbutton(op='remove',
                   title=_('ban this subreddit'), 
                   executed=_('banned'),
                   hidden_data = dict(id = thing.sr._fullname),
        )))
                # SOURCE LINE 164
                __M_writer(u'\n')
                # SOURCE LINE 165
                if getattr(thing.sr, 'ban_info', {}):
                    # SOURCE LINE 166
                    __M_writer(u'          <p>\n            ')
                    # SOURCE LINE 167
                    __M_writer(conditional_websafe(strings.time_approved % thing.sr.ban_info.get('unbanned_at') or 'N/A'))
                    __M_writer(u'\n          </p>\n')
            # SOURCE LINE 171
            __M_writer(u'    </div>\n    <div class="clear"></div>\n\n    <div class="quarantine-tool raisedbox spacer collapsed">\n      <div name="expander">\n        <a href="javascript:void(0)" class="expand" onclick="return toggleSrQuarantine(this)">\n          ')
            # SOURCE LINE 177
            __M_writer(conditional_websafe("[%s]" % "+"))
            __M_writer(u'\n        </a>\n        ')
            # SOURCE LINE 179
            __M_writer(conditional_websafe("Show unquarantine tool" if thing.sr.quarantine else "Show quarantine tool"))
            __M_writer(u'\n      </div>\n      <div class="quarantine-info">\n')
            # SOURCE LINE 182
            if not thing.sr.quarantine:
                # SOURCE LINE 183
                __M_writer(u'          ')

                subject = "ATTN: Your subreddit has been quarantined"
                body = "Your subreddit has been [quarantined](https://reddit.zendesk.com/hc/en-us/articles/205701245) due to offensive content."
                button_label = "Quarantine and send modmail"
                          
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['body','button_label','subject'] if __M_key in __M_locals_builtin_stored]))
                # SOURCE LINE 187
                __M_writer(u'\n')
                # SOURCE LINE 188
            else:
                # SOURCE LINE 189
                __M_writer(u'          ')

                subject = "ATTN: Your subreddit is no longer quarantined"
                body = "Your subreddit has been unquarantined."
                button_label = "Unquarantine and send modmail"
                          
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['body','button_label','subject'] if __M_key in __M_locals_builtin_stored]))
                # SOURCE LINE 193
                __M_writer(u'\n')
            # SOURCE LINE 195
            __M_writer(u'        <form id="quarantinemessage-form" method="post" onsubmit="return post_form(this, \'quarantine\')">\n          <input type="hidden" name="subreddit" value="')
            # SOURCE LINE 196
            __M_writer(conditional_websafe(thing.sr._fullname))
            __M_writer(u'">\n          <input type="hidden" name="quarantine" value="')
            # SOURCE LINE 197
            __M_writer(conditional_websafe(not thing.sr.quarantine))
            __M_writer(u'">\n          <label for="subject">Subject:</label>\n          <br>\n          <textarea name="subject">')
            # SOURCE LINE 200
            __M_writer(conditional_websafe(subject))
            __M_writer(u'</textarea>\n          <br>\n          <label for="body">Body:</label>\n          <br>\n          <textarea name="body" rows=4>')
            # SOURCE LINE 204
            __M_writer(conditional_websafe(body))
            __M_writer(u'</textarea>\n          <br>\n          <input type="submit" class="notes-button" value="')
            # SOURCE LINE 206
            __M_writer(conditional_websafe(button_label))
            __M_writer(u'">\n          <br>\n          <label>Message will be sent by u/reddit and won\'t send if left blank</label>\n        </form>\n      </div>\n    </div>\n')
        # SOURCE LINE 213
        __M_writer(u'\n  <div class="clear"> </div>\n  \n\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


