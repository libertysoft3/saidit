# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1520060829.766698
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/goldpayment.html'
_template_uri = '/goldpayment.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['stripe_button', 'creddits_button', 'stripe_form', 'paypal_button', 'base_stripe_form', 'coinbase_button']


# SOURCE LINE 22

from r2.lib.filters import websafe
from r2.lib.template_helpers import _ws
 

def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 26
    ns = runtime.TemplateNamespace('__anon_0x7fc7c7944410', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fc7c7944410')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7944410')._populate(_import_ns, [u'md', u'_md'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        _md = _import_ns.get('_md', context.get('_md', UNDEFINED))
        md = _import_ns.get('md', context.get('md', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 25
        __M_writer(u'\n')
        # SOURCE LINE 26
        __M_writer(u'\n')
        # SOURCE LINE 27

        clone_class = ''
        if thing.clone_template:
          if thing.thing_type == 'comment':
            clone_class = 'cloneable-comment'
          else:
            clone_class = 'cloneable-link'
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['clone_class'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 34
        __M_writer(u'\n\n<div class="gold-wrap ')
        # SOURCE LINE 36
        __M_writer(conditional_websafe(clone_class))
        __M_writer(u'">\n  <h1 class="gold-banner"><a href="')
        # SOURCE LINE 37
        __M_writer(conditional_websafe('/gold' if thing.goldtype != 'creddits' else '/creddits'))
        __M_writer(u'">')
        __M_writer(conditional_websafe(_('reddit gold')))
        __M_writer(u'</a></h1>\n\n  <div class="fancy">\n    <div class="fancy-inner">\n      <div class="fancy-content">\n        <div class="gold-form gold-payment">\n')
        # SOURCE LINE 43
        if thing.clone_template:
            # SOURCE LINE 44
            __M_writer(u'            <button class="close-button">')
            __M_writer(conditional_websafe(_('close')))
            __M_writer(u'</button>\n')
        # SOURCE LINE 46
        __M_writer(u'          <div class="container">\n            <h2 class="sidelines"><span>')
        # SOURCE LINE 47
        __M_writer(conditional_websafe(_('In Summation')))
        __M_writer(u'</span></h2>\n\n            <div class="transaction-summary">\n              ')
        # SOURCE LINE 50
        __M_writer(conditional_websafe(md(thing.summary)))
        __M_writer(u'\n\n              <div>\n                ')
        # SOURCE LINE 53
        __M_writer(conditional_websafe(_md('> By purchasing Reddit Gold, you agree to the [Reddit User Agreement.](/help/useragreement)')))
        __M_writer(u'\n              </div>\n\n')
        # SOURCE LINE 56
        if thing.thing and not thing.clone_template:
            # SOURCE LINE 57
            __M_writer(u'                <div class="gift-message">\n                  ')
            # SOURCE LINE 58
            __M_writer(conditional_websafe(md(thing.description, wrap=True)))
            __M_writer(u'\n                </div>\n')
        # SOURCE LINE 61
        __M_writer(u'\n')
        # SOURCE LINE 62
        if thing.giftmessage:
            # SOURCE LINE 63
            __M_writer(u'                <p>')
            __M_writer(conditional_websafe(_('The following gift note will be attached:')))
            __M_writer(u'</p>\n                <div class="gift-message">\n                  ')
            # SOURCE LINE 65
            __M_writer(conditional_websafe(md(thing.giftmessage, wrap=True)))
            __M_writer(u'\n                </div>\n')
        # SOURCE LINE 68
        __M_writer(u'            </div>\n          </div>\n\n')
        # SOURCE LINE 71
        if thing.clone_template:
            # SOURCE LINE 72
            __M_writer(u'            <ul class="indent">\n              <li>\n                <input type="checkbox" id="signed-false" name="signed" ')
            # SOURCE LINE 74
            __M_writer(conditional_websafe('checked' if not c.user.gild_reveal_username else ''))
            __M_writer(u'>')
            __M_writer(conditional_websafe(_('make my gift anonymous')))
            __M_writer(u'\n              </li>\n              <li>\n                <input type="checkbox" id="message" name="message">')
            # SOURCE LINE 77
            __M_writer(conditional_websafe(_('include a message')))
            __M_writer(u'\n              </li>\n              <li>\n                <textarea rows="3" cols="50" id="giftmessage" name="giftmessage" placeholder="')
            # SOURCE LINE 80
            __M_writer(conditional_websafe(_('enter your message')))
            __M_writer(u'" class="hidden giftmessage" maxlength="500">')
            __M_writer(conditional_websafe(thing.giftmessage))
            __M_writer(u'</textarea>\n              </li>\n            </ul>\n')
        # SOURCE LINE 84
        __M_writer(u'            <div class="buttons">\n              <p>')
        # SOURCE LINE 85
        __M_writer(conditional_websafe(_("Please select a payment method.")))
        __M_writer(u'</p>\n\n')
        # SOURCE LINE 87
        if thing.can_use_creddits:
            # SOURCE LINE 88
            __M_writer(u'                ')
            __M_writer(conditional_websafe(self.creddits_button()))
            __M_writer(u'\n')
        # SOURCE LINE 90
        __M_writer(u'\n')
        # SOURCE LINE 91
        if thing.paypal_buttonid:
            # SOURCE LINE 92
            __M_writer(u'                ')
            __M_writer(conditional_websafe(self.paypal_button()))
            __M_writer(u'\n')
        # SOURCE LINE 94
        __M_writer(u'\n')
        # SOURCE LINE 95
        if thing.coinbase_button_id:
            # SOURCE LINE 96
            __M_writer(u'                ')
            __M_writer(conditional_websafe(self.coinbase_button()))
            __M_writer(u'\n')
        # SOURCE LINE 98
        __M_writer(u'\n')
        # SOURCE LINE 99
        if thing.stripe_key:
            # SOURCE LINE 100
            __M_writer(u'                ')
            __M_writer(conditional_websafe(self.stripe_button()))
            __M_writer(u'\n')
        # SOURCE LINE 102
        __M_writer(u'\n')
        # SOURCE LINE 103
        if thing.stripe_key and not thing.clone_template:
            # SOURCE LINE 104
            __M_writer(u'                ')
            __M_writer(conditional_websafe(self.stripe_form()))
            __M_writer(u'\n')
        # SOURCE LINE 106
        __M_writer(u'\n')
        # SOURCE LINE 107
        if thing.clone_template:
            # SOURCE LINE 108
            __M_writer(u'                <div class="note">\n')
            # SOURCE LINE 109
            if not thing.user_creddits:
                # SOURCE LINE 110
                __M_writer(u'                    ')
                __M_writer(conditional_websafe(_md("Give gold often? Consider [buying creddits to use](/creddits), they're 40% cheaper if purchased in a set of 12.")))
                __M_writer(u'\n')
            # SOURCE LINE 112
            __M_writer(u'                  ')
            __M_writer(conditional_websafe(_md("Would you like to [learn more about giving gold](/gilding)?")))
            __M_writer(u'\n                </div>\n')
        # SOURCE LINE 115
        __M_writer(u'          </div>\n          <div class="throbber"></div>\n          <span role="presentation" class="gold-snoo" title="')
        # SOURCE LINE 117
        __M_writer(conditional_websafe(_('Felicitations on this momentous occasion!')))
        __M_writer(u'"></span>\n        </div>\n      </div>\n    </div>\n  </div>\n</div>\n\n')
        # SOURCE LINE 136
        __M_writer(u'\n\n')
        # SOURCE LINE 150
        __M_writer(u'\n\n')
        # SOURCE LINE 157
        __M_writer(u'\n\n')
        # SOURCE LINE 233
        __M_writer(u'\n\n')
        # SOURCE LINE 245
        __M_writer(u'\n\n')
        # SOURCE LINE 256
        __M_writer(u'\n\n')
        # SOURCE LINE 258
        if not thing.clone_template:
            # SOURCE LINE 259
            __M_writer(u'<script src="//checkout.google.com/files/digital/ga_post.js"\n  type="text/javascript"></script>\n')
        # SOURCE LINE 262
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stripe_button(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7944410')._populate(_import_ns, [u'md', u'_md'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 152
        __M_writer(u'\n  <span class="gold-checkout">\n    <button data-vendor="credit card" class="btn stripe-gold gold-button">')
        # SOURCE LINE 154
        __M_writer(conditional_websafe(_('Credit Card')))
        __M_writer(u'</button>\n    <input type="hidden" name="custom" value="')
        # SOURCE LINE 155
        __M_writer(conditional_websafe(thing.passthrough))
        __M_writer(u'" class="passthrough">\n  </span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_creddits_button(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7944410')._populate(_import_ns, [u'md', u'_md'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 124
        __M_writer(u'\n  <form id="giftgold" action="/api/spendcreddits" method="post"\n        class="gold-checkout creddits-gold"\n        data-vendor="creddits">\n    <input type="hidden" name="months" value="')
        # SOURCE LINE 128
        __M_writer(conditional_websafe(thing.months))
        __M_writer(u'">\n    <input type="hidden" name="passthrough" value="')
        # SOURCE LINE 129
        __M_writer(conditional_websafe(thing.passthrough))
        __M_writer(u'" class="passthrough">\n    <button class="btn gold-button" type="button"><span class="snoo-head"></span>')
        # SOURCE LINE 130
        __M_writer(conditional_websafe(_("creddits")))
        __M_writer(u'</button>\n    <span class="status">\n      <span class="remaining" data-current="')
        # SOURCE LINE 132
        __M_writer(conditional_websafe(thing.months))
        __M_writer(u'" data-total="')
        __M_writer(conditional_websafe(thing.user_creddits))
        __M_writer(u'" data-template="')
        __M_writer(conditional_websafe(websafe(_ws('(use %(current)s of your %(total)s creddits)')) % dict(current='<%- current %>', total='<%- total %>')))
        __M_writer(u'">\n      </span>\n    </span>\n  </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stripe_form(context,display=False):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7944410')._populate(_import_ns, [u'md', u'_md'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        def base_stripe_form():
            return render_base_stripe_form(context)
        __M_writer = context.writer()
        # SOURCE LINE 235
        __M_writer(u'\n<div id="stripe-payment"\n     class="charge"\n     ')
        # SOURCE LINE 238
        __M_writer(conditional_websafe(not display and "style='display:none'" or ''))
        __M_writer(u'>\n  <input type="hidden" name="pennies" value="')
        # SOURCE LINE 239
        __M_writer(conditional_websafe(thing.price.pennies))
        __M_writer(u'">\n  <input type="hidden" name="months" value="')
        # SOURCE LINE 240
        __M_writer(conditional_websafe(thing.months))
        __M_writer(u'">\n  <input type="hidden" name="period" value="')
        # SOURCE LINE 241
        __M_writer(conditional_websafe(thing.period))
        __M_writer(u'">\n  <input type="hidden" name="passthrough" value="')
        # SOURCE LINE 242
        __M_writer(conditional_websafe(thing.passthrough))
        __M_writer(u'">\n  ')
        # SOURCE LINE 243
        __M_writer(conditional_websafe(base_stripe_form()))
        __M_writer(u'\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_paypal_button(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7944410')._populate(_import_ns, [u'md', u'_md'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 138
        __M_writer(u'\n  <form action="https://www.paypal.com/cgi-bin/webscr" method="post"\n        class="gold-checkout"\n        data-vendor="paypal" target="')
        # SOURCE LINE 141
        __M_writer(conditional_websafe('_blank' if thing.clone_template else '_top'))
        __M_writer(u'">\n    <input type="hidden" name="cmd" value="_s-xclick">\n    <input type="hidden" name="custom" value="')
        # SOURCE LINE 143
        __M_writer(conditional_websafe(thing.passthrough))
        __M_writer(u'" class="passthrough">\n')
        # SOURCE LINE 144
        if thing.quantity:
            # SOURCE LINE 145
            __M_writer(u'      <input type="hidden" name="quantity" value="')
            __M_writer(conditional_websafe(thing.quantity))
            __M_writer(u'">\n')
        # SOURCE LINE 147
        __M_writer(u'    <input type="hidden" name="hosted_button_id" value="')
        __M_writer(conditional_websafe(thing.paypal_buttonid))
        __M_writer(u'">\n    <button type="submit" class="btn gold-button" type="button">')
        # SOURCE LINE 148
        __M_writer(conditional_websafe(_("PayPal")))
        __M_writer(u'</button>\n  </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_base_stripe_form(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7944410')._populate(_import_ns, [u'md', u'_md'])
        xrange = _import_ns.get('xrange', context.get('xrange', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 159
        __M_writer(u'\n  <script type="text/javascript" src="https://js.stripe.com/v1/"></script>\n\n  <div id="base-stripe-form"\n        class="gold-checkout"\n        data-vendor="stripe">\n    <div class="stripe-note">\n      <a class="icon" href="https://stripe.com/help/security">powered by stripe</a>\n      <div>')
        # SOURCE LINE 167
        __M_writer(conditional_websafe(_('Stripe is PCI compliant and your credit card information is sent directly to them.')))
        __M_writer(u'</div>\n    </div>\n    <table class="credit-card-input">\n      <tr>\n        <th><label>')
        # SOURCE LINE 171
        __M_writer(conditional_websafe(_('name')))
        __M_writer(u'</label></th>\n        <td><input type="text" autocomplete="off" class="card-name"></td>\n      </tr>\n      <tr>\n        <th><label>')
        # SOURCE LINE 175
        __M_writer(conditional_websafe(_('card number')))
        __M_writer(u'</label></th>\n        <td><input type="text" autocomplete="off" class="card-number"></td>\n      </tr>\n      <tr>\n        <th><label>')
        # SOURCE LINE 179
        __M_writer(conditional_websafe(_('cvc')))
        __M_writer(u'</label></th>\n        <td><input type="text" autocomplete="off" class="card-cvc"></td>\n      </tr>\n      <tr>\n        <th><label>')
        # SOURCE LINE 183
        __M_writer(conditional_websafe(_('expiration date')))
        __M_writer(u'</label></th>\n        <td>\n          ')
        # SOURCE LINE 185
 
        import datetime
        months = ['%02d' % m for m in xrange(1, 13)]
        years = ['%04d' % y for y in xrange(datetime.datetime.now().year,
                                            datetime.datetime.now().year + 25)]
                   
        
        # SOURCE LINE 190
        __M_writer(u'\n          <select class="card-expiry-month" title=')
        # SOURCE LINE 191
        __M_writer(conditional_websafe(_('month')))
        __M_writer(u'>\n')
        # SOURCE LINE 192
        for m in months:
            # SOURCE LINE 193
            __M_writer(u'              <option value="')
            __M_writer(conditional_websafe(m))
            __M_writer(u'">')
            __M_writer(conditional_websafe(m))
            __M_writer(u'</option>\n')
        # SOURCE LINE 195
        __M_writer(u'          </select>\n          <select class="card-expiry-year" title=')
        # SOURCE LINE 196
        __M_writer(conditional_websafe(_('year')))
        __M_writer(u'>\n')
        # SOURCE LINE 197
        for y in years:
            # SOURCE LINE 198
            __M_writer(u'              <option value="')
            __M_writer(conditional_websafe(y))
            __M_writer(u'">')
            __M_writer(conditional_websafe(y))
            __M_writer(u'</option>\n')
        # SOURCE LINE 200
        __M_writer(u'          </select>\n        </td>\n      </tr>\n      <tr>\n        <th><label>')
        # SOURCE LINE 204
        __M_writer(conditional_websafe(_('address line 1')))
        __M_writer(u'</label></th>\n        <td><input type="text" class="card-address_line1"></td>\n      </tr>\n      <tr>\n        <th><label>')
        # SOURCE LINE 208
        __M_writer(conditional_websafe(_('address line 2')))
        __M_writer(u'</label></th>\n        <td><input type="text" class="card-address_line2"></td>\n      </tr>\n      <tr>\n        <th><label>')
        # SOURCE LINE 212
        __M_writer(conditional_websafe(_('city')))
        __M_writer(u'</label></th>\n        <td><input type="text" class="card-address_city"></td>\n      </tr>\n      <tr>\n        <th><label>')
        # SOURCE LINE 216
        __M_writer(conditional_websafe(_('state/province')))
        __M_writer(u'</label></th>\n        <td><input type="text" class="card-address_state"></td>\n      </tr>\n      <tr>\n        <th><label>')
        # SOURCE LINE 220
        __M_writer(conditional_websafe(_('country')))
        __M_writer(u'</label></th>\n        <td><input type="text" class="card-address_country"></td>\n      </tr>\n      <tr>\n        <th><label>')
        # SOURCE LINE 224
        __M_writer(conditional_websafe(_('zip')))
        __M_writer(u'</label></th>\n        <td><input type="text" class="card-address_zip" length="12"></td>\n      </tr>\n    </table>\n    <input type="hidden" name="stripePublicKey" value="')
        # SOURCE LINE 228
        __M_writer(conditional_websafe(thing.stripe_key))
        __M_writer(u'">\n    <input type="hidden" name="stripeToken" value="">\n    <button class="btn gold-button stripe-submit">')
        # SOURCE LINE 230
        __M_writer(conditional_websafe(_('Submit')))
        __M_writer(u'</button>\n    <span class="status"></span>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_coinbase_button(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7944410')._populate(_import_ns, [u'md', u'_md'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 247
        __M_writer(u'\n  <button class="btn coinbase-gold gold-button gold-checkout"\n          data-vendor="coinbase"\n')
        # SOURCE LINE 250
        if not thing.clone_template:
            # SOURCE LINE 251
            __M_writer(u'            onclick="window.open(\'https://coinbase.com/checkouts/')
            __M_writer(conditional_websafe(thing.coinbase_button_id))
            __M_writer(u'?c=')
            __M_writer(conditional_websafe(thing.passthrough))
            __M_writer(u'\')"\n')
        # SOURCE LINE 253
        __M_writer(u'          >')
        __M_writer(conditional_websafe(_('Bitcoin')))
        __M_writer(u'</button>\n  <input type="hidden" name="cbbaseurl" value="https://coinbase.com/checkouts/')
        # SOURCE LINE 254
        __M_writer(conditional_websafe(thing.coinbase_button_id))
        __M_writer(u'">\n  <input type="hidden" name="custom" value="')
        # SOURCE LINE 255
        __M_writer(conditional_websafe(thing.passthrough))
        __M_writer(u'" class="passthrough">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


