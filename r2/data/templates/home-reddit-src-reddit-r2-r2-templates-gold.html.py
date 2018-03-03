# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505007497.832821
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/gold.html'
_template_uri = '/gold.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['gold_loggedout_content', 'gold_loggedin_content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 24
    ns = runtime.TemplateNamespace('__anon_0x7f360953bc10', context._clean_inheritance_tokens(), templateuri=u'utils/gold.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f360953bc10')] = ns

    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7f360953b0d0', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f360953b0d0')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f360953bc10')._populate(_import_ns, [u'gold_dropdown'])
        _mako_get_namespace(context, '__anon_0x7f360953b0d0')._populate(_import_ns, [u'error_field', u'radio_type', u'_md'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n')
        # SOURCE LINE 24
        __M_writer(u'\n\n<div class="gold-wrap">\n  <h1 class="gold-banner"><a href="/gold">')
        # SOURCE LINE 27
        __M_writer(conditional_websafe(_('reddit gold')))
        __M_writer(u'</a></h1>\n\n  <div class="fancy">\n    <div class="fancy-inner">\n      <div class="fancy-content gold-checkout">\n')
        # SOURCE LINE 32
        if c.user_is_loggedin:
            # SOURCE LINE 33
            __M_writer(u'          ')
            __M_writer(conditional_websafe(self.gold_loggedin_content()))
            __M_writer(u'\n')
            # SOURCE LINE 34
        else:
            # SOURCE LINE 35
            __M_writer(u'          ')
            __M_writer(conditional_websafe(self.gold_loggedout_content()))
            __M_writer(u'\n')
        # SOURCE LINE 37
        __M_writer(u'        <section class="gold-question">\n          <h3 class="toggle">')
        # SOURCE LINE 38
        __M_writer(conditional_websafe(_('What is reddit gold?')))
        __M_writer(u'</h3>\n          <div class="details hidden">\n            <div class="container">\n              ')
        # SOURCE LINE 41
        __M_writer(conditional_websafe(_('reddit gold is our premium membership.  It upgrades your account with access to extra features.')))
        __M_writer(u'\n              &#32;\n              <a href="/gold/about">')
        # SOURCE LINE 43
        __M_writer(conditional_websafe(_('Learn more')))
        __M_writer(u'</a>.\n            </div>\n          </div>\n        </section>\n      </div>\n    </div>\n  </div>  \n</div>\n\n')
        # SOURCE LINE 86
        __M_writer(u'\n\n')
        # SOURCE LINE 226
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_gold_loggedout_content(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f360953bc10')._populate(_import_ns, [u'gold_dropdown'])
        _mako_get_namespace(context, '__anon_0x7f360953b0d0')._populate(_import_ns, [u'error_field', u'radio_type', u'_md'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        gold_dropdown = _import_ns.get('gold_dropdown', context.get('gold_dropdown', UNDEFINED))
        error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 52
        __M_writer(u'\n  <header>\n    <h2 class="loggedout-give-gold sidelines"><span>')
        # SOURCE LINE 54
        __M_writer(conditional_websafe(_('Give Gold')))
        __M_writer(u'</span></h2>\n    <div class="login-note">')
        # SOURCE LINE 55
        __M_writer(conditional_websafe(_('Want to buy gold for yourself?')))
        __M_writer(u'&#32;<a href="/login" class="login-required">')
        __M_writer(conditional_websafe(_("You'll need to log in.")))
        __M_writer(u'</a></div>\n  </header>\n\n  <form class="loggedout-gold-form" name="loggedout-gold-form" action="/gold/payment" method="get">\n    <input type="hidden" name="goldtype" value="code">\n    <div id="form-options" class="container">\n      <section>\n        <label>\n          <h3>')
        # SOURCE LINE 63
        __M_writer(conditional_websafe(_('How many months of gold would you like to give?')))
        __M_writer(u'</h3>\n          ')
        # SOURCE LINE 64
        __M_writer(conditional_websafe(gold_dropdown("months", thing.months, "months")))
        __M_writer(u'\n        </label>\n\n        <label class="loggedout-email">\n          <input type="email" name="email" class="inline" placeholder="enter your email address" value="')
        # SOURCE LINE 68
        __M_writer(conditional_websafe(thing.email))
        __M_writer(u'">\n')
        # SOURCE LINE 71
        if 'email' in request.GET and not thing.email:
            # SOURCE LINE 72
            __M_writer(u'            ')
            __M_writer(conditional_websafe(error_field("NO_EMAIL", "email", "span")))
            __M_writer(u'\n')
        # SOURCE LINE 74
        __M_writer(u'          ')
        __M_writer(conditional_websafe(error_field("BAD_EMAIL", "email", "span")))
        __M_writer(u'\n          <p class="hint">')
        # SOURCE LINE 75
        __M_writer(conditional_websafe(_("(We'll send a code to your email address you can then give to your recipient)")))
        __M_writer(u'</p>\n        </label>\n      </section>\n    </div>\n\n    <section id="payment-options">\n      <div class="buttons">\n        <button type="submit" class="btn gold-button">')
        # SOURCE LINE 82
        __M_writer(conditional_websafe(_("buy reddit gold")))
        __M_writer(u'</button>\n      </div>\n    </section>\n  </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_gold_loggedin_content(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f360953bc10')._populate(_import_ns, [u'gold_dropdown'])
        _mako_get_namespace(context, '__anon_0x7f360953b0d0')._populate(_import_ns, [u'error_field', u'radio_type', u'_md'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        gold_dropdown = _import_ns.get('gold_dropdown', context.get('gold_dropdown', UNDEFINED))
        error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
        radio_type = _import_ns.get('radio_type', context.get('radio_type', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 88
        __M_writer(u'\n  ')
        # SOURCE LINE 89

        is_gift = thing.goldtype in ('code', 'gift')
        
        active_tab = None
        if thing.goldtype:
            if is_gift or thing.goldtype == 'onetime':
                active_tab = 'onetime'
            elif thing.goldtype == 'autorenew':
                active_tab = 'autorenew'
            else:
                active_tab = 'creddits'
        
        
        # SOURCE LINE 100
        __M_writer(u'\n  <form name="gold-form" class="gold-form" action="/gold/payment" method="get">\n  <input type="hidden" name="edit" id="edit" value="true">\n  <input type="hidden" name="goldtype" id="goldtype" value="')
        # SOURCE LINE 103
        __M_writer(conditional_websafe(thing.goldtype))
        __M_writer(u'">\n\n    <section class="tab-chooser">\n      <h3>')
        # SOURCE LINE 106
        __M_writer(conditional_websafe(_('What type of reddit gold would you like to purchase?')))
        __M_writer(u'</h3>\n      <a href="#onetime" class="tab-toggle ')
        # SOURCE LINE 107
        __M_writer(conditional_websafe('active' if active_tab == 'onetime' else ''))
        __M_writer(u'">')
        __M_writer(conditional_websafe(_('one-time purchase')))
        __M_writer(u'</a>\n      <a href="#autorenew" class="tab-toggle ')
        # SOURCE LINE 108
        __M_writer(conditional_websafe('active' if active_tab == 'autorenew' else ''))
        __M_writer(u'">')
        __M_writer(conditional_websafe(_('ongoing subscription')))
        __M_writer(u'</a>\n      <a href="#creddits" class="tab-toggle ')
        # SOURCE LINE 109
        __M_writer(conditional_websafe('active' if active_tab == 'creddits' else ''))
        __M_writer(u'">')
        __M_writer(conditional_websafe(_('creddits')))
        __M_writer(u'</a>\n    </section>\n\n    <div id="form-options" class="container ')
        # SOURCE LINE 112
        __M_writer(conditional_websafe('hidden' if not active_tab else ''))
        __M_writer(u'">\n\n      <section id="creddits" class="tab ')
        # SOURCE LINE 114
        __M_writer(conditional_websafe('active' if active_tab == 'creddits' else ''))
        __M_writer(u'">\n        <h3>')
        # SOURCE LINE 115
        __M_writer(conditional_websafe(_('How many creddits would you like to buy?')))
        __M_writer(u'</h3>\n        ')
        # SOURCE LINE 116
        __M_writer(conditional_websafe(gold_dropdown("num_creddits", thing.months, somethings="creddits")))
        __M_writer(u'\n\n        <section class="creddits-explained">\n          ')
        # SOURCE LINE 119
        __M_writer(conditional_websafe(_('Stored as a balance on your account, creddits allow you to give gold without having to enter payment information. Each creddit you have can be converted into one month of reddit gold.')))
        __M_writer(u'\n          &#32;<a href="/gilding#what-are-creddits">')
        # SOURCE LINE 120
        __M_writer(conditional_websafe(_('Learn more about using creddits')))
        __M_writer(u'</a>.\n        </section>\n      </section>\n\n      <section id="autorenew" class="tab ')
        # SOURCE LINE 124
        __M_writer(conditional_websafe('active' if active_tab == 'autorenew' else ''))
        __M_writer(u'">\n        <h3>')
        # SOURCE LINE 125
        __M_writer(conditional_websafe(_('What type of subscription would you like?')))
        __M_writer(u'</h3>\n        <ul>\n          <li>')
        # SOURCE LINE 127
        __M_writer(conditional_websafe(radio_type("period", "monthly", _("monthly - %s") % g.gold_month_price, "", thing.period == "monthly")))
        __M_writer(u'</li>\n\n          <li>')
        # SOURCE LINE 129
        __M_writer(conditional_websafe(radio_type("period", "yearly", _("yearly - %s (%s/month)") % (g.gold_year_price, g.gold_year_price / 12),"", thing.period != "monthly")))
        __M_writer(u'</li>\n        </ul>\n      </section>\n\n      <section id="onetime" class="tab ')
        # SOURCE LINE 133
        __M_writer(conditional_websafe('active' if active_tab == 'onetime' else ''))
        __M_writer(u'">\n        <h3>')
        # SOURCE LINE 134
        __M_writer(conditional_websafe(_('How many months?')))
        __M_writer(u'</h3>\n        ')
        # SOURCE LINE 135

        append_or_somethings = None
        if c.user_is_loggedin and c.user.gold_creddits > 0:
            append_or_somethings = "creddits"
                
        
        # SOURCE LINE 139
        __M_writer(u'\n        ')
        # SOURCE LINE 140
        __M_writer(conditional_websafe(gold_dropdown("months", thing.months, append_or_somethings=append_or_somethings)))
        __M_writer(u'\n\n        <section id="give-as-gift">\n          <ul>\n            <li>\n            <label>\n              <input type="radio" id="notgift" name="gift" value="0" ')
        # SOURCE LINE 146
        __M_writer(conditional_websafe("checked" if not is_gift else ""))
        __M_writer(u'>\n              ')
        # SOURCE LINE 147
        __M_writer(conditional_websafe(_('purchase this reddit gold for myself')))
        __M_writer(u'\n            </label>\n            </li>\n            <li>\n            <label>\n              <input type="radio" id="gift" name="gift" value="1" ')
        # SOURCE LINE 152
        __M_writer(conditional_websafe("checked" if is_gift else ""))
        __M_writer(u'>\n              ')
        # SOURCE LINE 153
        __M_writer(conditional_websafe(_('give this reddit gold as a gift')))
        __M_writer(u'\n            </label>\n            </li>\n          </ul>\n          <div id="gifting-details" class="')
        # SOURCE LINE 157
        __M_writer(conditional_websafe('hidden' if not is_gift else ''))
        __M_writer(u'">\n            <ul class="indent">\n              <li>\n                ')
        # SOURCE LINE 160
        __M_writer(conditional_websafe(radio_type("gifttype", "code", _("receive gold as a gift code"), "", thing.goldtype == "code")))
        __M_writer(u'\n              </li>\n              <li>\n                ')
        # SOURCE LINE 163
        __M_writer(conditional_websafe(radio_type("gifttype", "gift", _("send gold to a user"), "", thing.goldtype == "gift")))
        __M_writer(u'\n\n                <div class="gift-details ')
        # SOURCE LINE 165
        __M_writer(conditional_websafe('hidden' if not thing.goldtype == 'gift' else ''))
        __M_writer(u'" id="gifttype-details-gift">\n\n                  <label>\n                    ')
        # SOURCE LINE 168
        __M_writer(conditional_websafe(_('who should receive this gold?')))
        __M_writer(u'\n                    <input id="recipient" type="text" name="recipient" value="')
        # SOURCE LINE 169
        __M_writer(conditional_websafe(thing.recipient.name if thing.recipient else ''))
        __M_writer(u'" placeholder="')
        __M_writer(conditional_websafe(_('enter a username')))
        __M_writer(u'" size="13" maxlength="20" class="inline">\n')
        # SOURCE LINE 172
        if 'recipient' in request.GET:
            # SOURCE LINE 173
            __M_writer(u'                      ')
            __M_writer(conditional_websafe(error_field("NO_USER", "recipient", "span")))
            __M_writer(u'\n                      ')
            # SOURCE LINE 174
            __M_writer(conditional_websafe(error_field("USER_DOESNT_EXIST", "recipient", "span")))
            __M_writer(u'\n')
        # SOURCE LINE 176
        __M_writer(u'                  </label>\n\n                  <ul class="indent">\n                    <li>\n                      <label>\n                        <input type="checkbox" id="signed-false" name="signed" value="false" ')
        # SOURCE LINE 181
        __M_writer(conditional_websafe("checked" if not thing.signed else ""))
        __M_writer(u'>\n                        ')
        # SOURCE LINE 182
        __M_writer(conditional_websafe(_('make my gift anonymous')))
        __M_writer(u'\n                      </label>\n                    </li>\n                    <li>\n                      <label>\n                        <input type="checkbox" id="message" name="message" value="message" ')
        # SOURCE LINE 187
        __M_writer(conditional_websafe("checked" if thing.giftmessage else ""))
        __M_writer(u'>\n                        ')
        # SOURCE LINE 188
        __M_writer(conditional_websafe(_('include a message')))
        __M_writer(u'\n                      </label>\n                    </li>\n                    <li>\n                      <textarea rows="5" cols="30" name="giftmessage" id="giftmessage" placeholder="')
        # SOURCE LINE 192
        __M_writer(conditional_websafe(_('enter your message')))
        __M_writer(u'" class="giftmessage" maxlength="500">')
        __M_writer(conditional_websafe(thing.giftmessage))
        __M_writer(u'</textarea>\n                    </li>\n                  </ul>\n                </div>\n              </li>\n            </ul>\n          </div>\n        </section>\n      </section>\n    </div>\n\n    <section id="payment-options" class="')
        # SOURCE LINE 203
        __M_writer(conditional_websafe('hidden' if not active_tab else ''))
        __M_writer(u'">\n      <div class="buttons">\n        <button type="submit" class="btn gold-button">')
        # SOURCE LINE 205
        __M_writer(conditional_websafe(_('continue')))
        __M_writer(u'</button>\n      </div>\n    </section>\n  </form>\n\n  <section id="redeem-a-code" class="')
        # SOURCE LINE 210
        __M_writer(conditional_websafe('hidden' if active_tab else ''))
        __M_writer(u'">\n    <div class="sidelines"><span>')
        # SOURCE LINE 211
        __M_writer(conditional_websafe(_('or')))
        __M_writer(u'</span></div>\n    <form id="redeem-form" action="/api/claimgold" method="post" onsubmit="return post_form(this, \'claimgold\');">\n        <input type="text" name="code" value="" placeholder="')
        # SOURCE LINE 213
        __M_writer(conditional_websafe(_('enter a gift code for redemption')))
        __M_writer(u'" maxlength="20">\n        <div class="redeem-submit hidden">\n          <div class="buttons">\n            <button type="submit" class="btn gold-button">')
        # SOURCE LINE 216
        __M_writer(conditional_websafe(_("redeem this code")))
        __M_writer(u'</button>\n          </div>\n          <div class="errors">\n          ')
        # SOURCE LINE 219
        __M_writer(conditional_websafe(error_field("NO_TEXT", "code", "span")))
        __M_writer(u'\n          ')
        # SOURCE LINE 220
        __M_writer(conditional_websafe(error_field("INVALID_CODE", "code", "span")))
        __M_writer(u'\n          ')
        # SOURCE LINE 221
        __M_writer(conditional_websafe(error_field("CLAIMED_CODE", "code", "span")))
        __M_writer(u'\n          </div>\n        </div>\n    </form>\n  </section>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


