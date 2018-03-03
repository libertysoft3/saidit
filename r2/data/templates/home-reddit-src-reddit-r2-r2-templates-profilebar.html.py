# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1520060938.326321
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/profilebar.html'
_template_uri = '/profilebar.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23
 
from r2.config import feature
from r2.lib.filters import unsafe, safemarkdown
from r2.lib.template_helpers import static, format_number, display_comment_karma, display_link_karma
 

def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 28
    ns = runtime.TemplateNamespace('__anon_0x7fc7c7630e90', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fc7c7630e90')] = ns

    # SOURCE LINE 29
    ns = runtime.TemplateNamespace('__anon_0x7fc7c7630f50', context._clean_inheritance_tokens(), templateuri=u'printablebuttons.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fc7c7630f50')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7630e90')._populate(_import_ns, [u'submit_form', u'plain_link', u'thing_timestamp'])
        _mako_get_namespace(context, '__anon_0x7fc7c7630f50')._populate(_import_ns, [u'toggle_button'])
        toggle_button = _import_ns.get('toggle_button', context.get('toggle_button', UNDEFINED))
        thing_timestamp = _import_ns.get('thing_timestamp', context.get('thing_timestamp', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        enumerate = _import_ns.get('enumerate', context.get('enumerate', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 27
        __M_writer(u'\n')
        # SOURCE LINE 28
        __M_writer(u'\n')
        # SOURCE LINE 29
        __M_writer(u'\n\n<div class="titlebox">\n  <h1>')
        # SOURCE LINE 32
        __M_writer(conditional_websafe(thing.user.name))
        __M_writer(u'\n')
        # SOURCE LINE 33
        if thing.user.employee:
            # SOURCE LINE 34
            __M_writer(u'      <span class="user-distinction">\n        [\n        <span class="admin" title="reddit admin">A</span>\n        ]\n      </span>\n')
        # SOURCE LINE 40
        __M_writer(u'  </h1>\n\n')
        # SOURCE LINE 42
        if c.user_is_loggedin and not thing.viewing_self:
            # SOURCE LINE 43
            __M_writer(u'    <div>\n    ')
            # SOURCE LINE 44
            __M_writer(conditional_websafe(toggle_button("fancy-toggle-button", _("+ friends"), _("- friends"),
         "friend('%s', '%s', 'friend')" % (thing.user.name, c.user._fullname),
         "unfriend('%s', '%s', 'friend')" % (thing.user.name, c.user._fullname),
         css_class = "add", alt_css_class = "remove",
         reverse = thing.is_friend, login_required=True)))
            # SOURCE LINE 48
            __M_writer(u'\n    </div>\n')
        # SOURCE LINE 51
        __M_writer(u'\n  <span class="karma">')
        # SOURCE LINE 52
        __M_writer(conditional_websafe(format_number(display_link_karma(thing.user.link_karma))))
        __M_writer(u'</span>\n  &#32;\n  ')
        # SOURCE LINE 54
        __M_writer(conditional_websafe(_("post karma")))
        __M_writer(u'\n\n  <br/>\n  <span class="karma comment-karma">')
        # SOURCE LINE 57
        __M_writer(conditional_websafe(format_number(display_comment_karma(thing.user.comment_karma))))
        __M_writer(u'</span>\n  &#32;\n  ')
        # SOURCE LINE 59
        __M_writer(conditional_websafe(_("comment karma")))
        __M_writer(u'\n\n')
        # SOURCE LINE 61
        if thing.show_private_info:
            # SOURCE LINE 62
            __M_writer(u'    <table id="per-sr-karma"')
            __M_writer(conditional_websafe(" class='more-karmas'" if not c.user_is_admin else ""))
            __M_writer(u'>\n     <thead>\n        <tr>\n          <th id="sr-karma-header">subreddit</th>\n          <th>post</th>\n          <th>comment</th>\n        </tr>\n     </thead>\n     <tbody>\n')
            # SOURCE LINE 71
            for i, (sr_name, (link_karma, comment_karma)) in enumerate(thing.all_karmas.iteritems()):
                # SOURCE LINE 72
                if c.user_is_admin and i >= 5:
                    # SOURCE LINE 73
                    __M_writer(u'         <tr class="more-karmas">\n')
                    # SOURCE LINE 74
                else:
                    # SOURCE LINE 75
                    __M_writer(u'         <tr>\n')
                # SOURCE LINE 77
                __M_writer(u'\n')
                # SOURCE LINE 78
                if sr_name == "ancient history":
                    # SOURCE LINE 79
                    __M_writer(u'          <th class="helpful" title="')
                    __M_writer(conditional_websafe(_('really obscure karma from before it was cool to track per-subreddit')))
                    __M_writer(u'"><span>')
                    __M_writer(conditional_websafe(_(sr_name)))
                    __M_writer(u'</span></th>\n')
                    # SOURCE LINE 80
                else:
                    # SOURCE LINE 81
                    __M_writer(u'          <th>')
                    __M_writer(conditional_websafe(sr_name))
                    __M_writer(u'</th>\n')
                # SOURCE LINE 83
                __M_writer(u'\n          <td>')
                # SOURCE LINE 84
                __M_writer(conditional_websafe(display_link_karma(link_karma)))
                __M_writer(u'</td>\n          <td>')
                # SOURCE LINE 85
                __M_writer(conditional_websafe(display_comment_karma(comment_karma)))
                __M_writer(u'</td>\n        </tr>\n')
            # SOURCE LINE 88
            __M_writer(u'     </tbody>\n    </table>\n')
            # SOURCE LINE 90
            if not c.user_is_admin or len(thing.all_karmas) > 5:
                # SOURCE LINE 91
                __M_writer(u'    <div class="karma-breakdown">\n      <a href="javascript:void(0)"\n         onclick="$(\'.more-karmas\').show();$(this).hide();return false">\n         show karma breakdown by subreddit\n      </a>\n    </div>\n')
        # SOURCE LINE 99
        __M_writer(u'\n')
        # SOURCE LINE 100
        if thing.user.gold:
            # SOURCE LINE 101
            if thing.show_private_info or thing.user.pref_show_snoovatar:
                # SOURCE LINE 102
                __M_writer(u'      <div class="gold-accent snoovatar-link">\n        <a href="/user/')
                # SOURCE LINE 103
                __M_writer(conditional_websafe(thing.user.name))
                __M_writer(u'/snoo">\n')
                # SOURCE LINE 104
                if thing.viewing_self:
                    # SOURCE LINE 105
                    __M_writer(u'            ')
                    __M_writer(conditional_websafe(_("View/edit my snoovatar")))
                    __M_writer(u'\n')
                    # SOURCE LINE 106
                else:
                    # SOURCE LINE 107
                    __M_writer(u'            ')
                    __M_writer(conditional_websafe(_("%(username)s's snoovatar") % dict(username=thing.user.name)))
                    __M_writer(u'\n')
                # SOURCE LINE 109
                __M_writer(u'        </a>\n      </div>\n')
        # SOURCE LINE 113
        __M_writer(u'\n')
        # SOURCE LINE 114
        if thing.show_users_gold_expiration or thing.show_private_gold_info:
            # SOURCE LINE 115
            __M_writer(u'    <div class="rounded gold-accent gold-expiration-info">\n')
            # SOURCE LINE 116
            if hasattr(thing, "gold_remaining"):
                # SOURCE LINE 117
                __M_writer(u'        <div class="gold-remaining" title="')
                __M_writer(conditional_websafe(thing.user.gold_expiration.strftime('%Y-%m-%d')))
                __M_writer(u'">\n          <span class="karma">\n            ')
                # SOURCE LINE 119
                __M_writer(conditional_websafe(thing.gold_remaining))
                __M_writer(u'\n          </span>\n          <br>\n          ')
                # SOURCE LINE 122
                __M_writer(conditional_websafe(_("of reddit gold remaining")))
                __M_writer(u'\n          <br>\n          <a href="/gold/about">')
                # SOURCE LINE 124
                __M_writer(conditional_websafe(_("view gold features/benefits")))
                __M_writer(u'</a>\n        </div>\n')
                # SOURCE LINE 126
                if thing.show_private_info:
                    # SOURCE LINE 127
                    if hasattr(thing, "paypal_subscr_id"):
                        # SOURCE LINE 128
                        __M_writer(u'             <div>\n              <a href="')
                        # SOURCE LINE 129
                        __M_writer(conditional_websafe(thing.paypal_url))
                        __M_writer(u'">\n                ')
                        # SOURCE LINE 130
                        __M_writer(conditional_websafe(_("Recurring Paypal subscription")))
                        __M_writer(u'\n              </a>\n              &#32;\n              ')
                        # SOURCE LINE 133
                        __M_writer(conditional_websafe(thing.paypal_subscr_id))
                        __M_writer(u'\n            </div>\n')
                    # SOURCE LINE 136
                    __M_writer(u'\n')
                    # SOURCE LINE 137
                    if hasattr(thing, "stripe_customer_id"):
                        # SOURCE LINE 138
                        __M_writer(u'             <div>\n              <a href="/gold/subscription">\n                ')
                        # SOURCE LINE 140
                        __M_writer(conditional_websafe(_("manage recurring subscription")))
                        __M_writer(u'\n              </a>\n            </div>\n')
            # SOURCE LINE 146
            if hasattr(thing, "gold_creddit_message"):
                # SOURCE LINE 147
                __M_writer(u'        <div class="gold-creddits-remaining">\n          ')
                # SOURCE LINE 148
                __M_writer(conditional_websafe(plain_link(thing.gold_creddit_message, "/gold?goldtype=gift")))
                __M_writer(u'\n        </div>\n')
            # SOURCE LINE 151
            if hasattr(thing, "num_gildings_message"):
                # SOURCE LINE 152
                __M_writer(u'        <div>\n          ')
                # SOURCE LINE 153
                __M_writer(conditional_websafe(thing.num_gildings_message))
                __M_writer(u'\n        </div>\n')
            # SOURCE LINE 156
            __M_writer(u'    </div>\n')
        # SOURCE LINE 158
        __M_writer(u'\n')
        # SOURCE LINE 159
        if hasattr(thing, "goldlink"):
            # SOURCE LINE 160
            __M_writer(u'  <div class="giftgold">\n    <a href="')
            # SOURCE LINE 161
            __M_writer(conditional_websafe(thing.goldlink))
            __M_writer(u'" class="access-required"\n       data-type="account" data-fullname="')
            # SOURCE LINE 162
            __M_writer(conditional_websafe(thing.user._fullname))
            __M_writer(u'"\n       data-event-action="gild">\n      ')
            # SOURCE LINE 164
            __M_writer(conditional_websafe(thing.giftmsg))
            __M_writer(u'\n    </a>\n  </div>\n')
        # SOURCE LINE 168
        __M_writer(u'\n  <div class="bottom">\n')
        # SOURCE LINE 170
        if not thing.viewing_self:
            # SOURCE LINE 171
            __M_writer(u'      <img src="')
            __M_writer(conditional_websafe(static('mailgray.png')))
            __M_writer(u'"/>\n      &#32;\n      <a href="')
            # SOURCE LINE 173
            __M_writer(conditional_websafe("/message/compose/?to=%s" % thing.user.name))
            __M_writer(u'" class="access-required"\n         data-type="account" data-fullname="')
            # SOURCE LINE 174
            __M_writer(conditional_websafe(thing.user._fullname))
            __M_writer(u'"\n         data-event-action="compose">\n        ')
            # SOURCE LINE 176
            __M_writer(conditional_websafe(_("send a private message")))
            __M_writer(u'\n      </a>\n')
        # SOURCE LINE 179
        __M_writer(u'\n    <span class="age">\n      ')
        # SOURCE LINE 181
        __M_writer(conditional_websafe(_("redditor for")))
        __M_writer(u'&#32;')
        __M_writer(conditional_websafe(thing_timestamp(thing.user)))
        __M_writer(u'\n    </span>\n  </div>\n\n  <div class="clear"> </div>\n\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


