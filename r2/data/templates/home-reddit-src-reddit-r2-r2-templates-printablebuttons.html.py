# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1520060828.435521
_enable_loop = True
_template_filename = u'/home/reddit/src/reddit/r2/r2/templates/printablebuttons.html'
_template_uri = u'/printablebuttons.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['state_button', 'reports_button', 'linkbuttons', 'big_modbuttons', 'report_reasons', 'ynbutton', 'distinguish_options', 'show_admin_context', 'undistinguish_options', 'bylink_button', 'commentbuttons', 'ignore_reports_toggle', 'ajax_ynbutton', 'toggle_button', 'distinguish_setter', 'distinguish_help', 'distinguish_label', 'messagebuttons', 'banbuttons', 'give_gold', 'simple_button', 'distinguish_noop', 'distinguish']


# SOURCE LINE 25

from r2.config import feature
from r2.lib.filters import conditional_websafe, jssafe
from r2.lib.strings import strings
from r2.models import Link
from r2.models.promo import PROMOTE_STATUS
 

def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7fc7c7a2aa10', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fc7c7a2aa10')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7a2aa10')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data', u'error_field'])
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n')
        # SOURCE LINE 31
        __M_writer(u'\n\n')
        # SOURCE LINE 97
        __M_writer(u'\n\n')
        # SOURCE LINE 104
        __M_writer(u'\n\n')
        # SOURCE LINE 110
        __M_writer(u'\n\n')
        # SOURCE LINE 120
        __M_writer(u'\n\n')
        # SOURCE LINE 126
        __M_writer(u'\n\n')
        # SOURCE LINE 163
        __M_writer(u'\n\n')
        # SOURCE LINE 179
        __M_writer(u'\n\n\n')
        # SOURCE LINE 208
        __M_writer(u'\n\n')
        # SOURCE LINE 220
        __M_writer(u'\n\n')
        # SOURCE LINE 232
        __M_writer(u'\n\n')
        # SOURCE LINE 266
        __M_writer(u'\n\n')
        # SOURCE LINE 278
        __M_writer(u'\n\n')
        # SOURCE LINE 292
        __M_writer(u'\n\n')
        # SOURCE LINE 322
        __M_writer(u'\n\n')
        # SOURCE LINE 442
        __M_writer(u'\n\n')
        # SOURCE LINE 541
        __M_writer(u'\n\n\n')
        # SOURCE LINE 617
        __M_writer(u'\n\n')
        # SOURCE LINE 661
        __M_writer(u'\n\n\n')
        # SOURCE LINE 682
        __M_writer(u'\n\n')
        # SOURCE LINE 732
        __M_writer(u'\n\n')
        # SOURCE LINE 740
        __M_writer(u'\n\n')
        # SOURCE LINE 775
        __M_writer(u'\n\n')
        # SOURCE LINE 797
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_state_button(context,name,title,onclick,executed,clicked=False,a_class='',fmt=None,fmt_param='',hidden_data={},access_required=True,event_action=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7a2aa10')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data', u'error_field'])
        def _link():
            __M_caller = context.caller_stack._push_frame()
            try:
                context._push_buffer()
                __M_writer = context.writer()
                # SOURCE LINE 628
                __M_writer(u'\n    ')
                # SOURCE LINE 629

                access_class = 'access-required' if access_required else ''
                    
                
                # SOURCE LINE 631
                __M_writer(u'\n    <a href="javascript:void(0)"\n       class="')
                # SOURCE LINE 633
                __M_writer(conditional_websafe(a_class or ''))
                __M_writer(u' ')
                __M_writer(conditional_websafe(access_class))
                __M_writer(u'"\n')
                # SOURCE LINE 634
                if event_action:
                    # SOURCE LINE 635
                    __M_writer(u'         data-event-action="')
                    __M_writer(conditional_websafe(event_action))
                    __M_writer(u'"\n')
                # SOURCE LINE 637
                __M_writer(u'       onclick="')
                __M_writer(conditional_websafe(onclick))
                __M_writer(u'">')
                __M_writer(conditional_websafe(title))
                __M_writer(u'</a>\n  ')
            finally:
                __M_buf = context._pop_buffer()
                context.caller_stack._pop_frame()
            return __M_buf.getvalue()
        __M_writer = context.writer()
        # SOURCE LINE 627
        __M_writer(u'\n  ')
        # SOURCE LINE 638
        __M_writer(u'\n  ')
        # SOURCE LINE 639

        link = _link()
        if fmt:
            link = conditional_websafe(fmt) % {fmt_param: link}
            ## preserve spaces before and after < & > for space compression
            link = link.replace(" <", "&#32;<").replace("> ", ">&#32;")
           
        
        # SOURCE LINE 645
        __M_writer(u'   \n\n')
        # SOURCE LINE 647
        if clicked:
            # SOURCE LINE 648
            __M_writer(u'    ')
            __M_writer(conditional_websafe(executed))
            __M_writer(u'\n')
            # SOURCE LINE 649
        else:
            # SOURCE LINE 650
            __M_writer(u'    <form action="/post/')
            __M_writer(conditional_websafe(name))
            __M_writer(u'" method="post" \n          class="state-button ')
            # SOURCE LINE 651
            __M_writer(conditional_websafe(name))
            __M_writer(u'-button">\n        <input type="hidden" name="executed" value="')
            # SOURCE LINE 652
            __M_writer(conditional_websafe(executed))
            __M_writer(u'" />\n')
            # SOURCE LINE 653
            for key, value in hidden_data.iteritems():
                # SOURCE LINE 654
                __M_writer(u'          <input type="hidden" name="')
                __M_writer(conditional_websafe(key))
                __M_writer(u'" value="')
                __M_writer(conditional_websafe(value))
                __M_writer(u'" />\n')
            # SOURCE LINE 656
            __M_writer(u'        <span>\n          ')
            # SOURCE LINE 657
            __M_writer(conditional_websafe(unsafe(link)))
            __M_writer(u'\n        </span>\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_reports_button(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7a2aa10')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data', u'error_field'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 280
        __M_writer(u'\n<li \n')
        # SOURCE LINE 282
        if thing.mod_reports or thing.user_reports:
            # SOURCE LINE 283
            __M_writer(u'      class="rounded reported-stamp stamp has-reasons access-required"\n      title="')
            # SOURCE LINE 284
            __M_writer(conditional_websafe(_('click to show report reasons')))
            __M_writer(u'"\n')
            # SOURCE LINE 285
        else:
            # SOURCE LINE 286
            __M_writer(u'      class="rounded reported-stamp stamp access-required"\n')
        # SOURCE LINE 288
        __M_writer(u'    data-event-action="viewreports"\n    >\n  ')
        # SOURCE LINE 290
        __M_writer(conditional_websafe(strings.reports % thing.thing.reported))
        __M_writer(u'\n</li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_linkbuttons(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7a2aa10')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data', u'error_field'])
        def toggle_button(class_name,title,alt_title,callback,cancelback,css_class='',alt_css_class='',reverse=False,login_required=False,style='',data_attrs=None):
            return render_toggle_button(context,class_name,title,alt_title,callback,cancelback,css_class,alt_css_class,reverse,login_required,style,data_attrs)
        def report_reasons():
            return render_report_reasons(context)
        def reports_button():
            return render_reports_button(context)
        def ignore_reports_toggle(thing):
            return render_ignore_reports_toggle(context,thing)
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        def ynbutton(title,executed,op,callback='null',question=None,post_callback='null',format='%(link)s',format_arg='link',hidden_data={},access_required=True,event_target=None,event_action=None,event_detail=None,_class=''):
            return render_ynbutton(context,title,executed,op,callback,question,post_callback,format,format_arg,hidden_data,access_required,event_target,event_action,event_detail,_class)
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        def big_modbuttons(thing):
            return render_big_modbuttons(context,thing)
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 324
        __M_writer(u'\n')
        # SOURCE LINE 325
        if thing.show_comments:
            # SOURCE LINE 326
            __M_writer(u'    <li class="first">\n    ')
            # SOURCE LINE 327
            __M_writer(conditional_websafe(self.bylink_button(
        thing.comment_label,
        thing.permalink,
        sr_path=(thing.promoted is None),
        a_class=unsafe("bylink %s" % thing.commentcls),
        event_action="comments")))
            # SOURCE LINE 332
            __M_writer(u'\n    </li>\n')
        # SOURCE LINE 335
        if thing.editable and not thing.promoted:
            # SOURCE LINE 336
            __M_writer(u'    <li>\n      ')
            # SOURCE LINE 337
            __M_writer(conditional_websafe(self.simple_button(_("edit"), "edit_usertext", css_class="edit-usertext")))
            __M_writer(u'\n    </li>\n')
        # SOURCE LINE 340
        if thing.show_share:
            # SOURCE LINE 341
            __M_writer(u'    <li class="share">\n      <a class="post-sharing-button" href="javascript: void 0;">')
            # SOURCE LINE 342
            __M_writer(conditional_websafe(_("share")))
            __M_writer(u'</a>\n    </li>\n')
        # SOURCE LINE 345
        if thing.is_loggedin and not thing.deleted:
            # SOURCE LINE 346
            if thing.saved:
                # SOURCE LINE 347
                __M_writer(u'      <li class="link-unsave-button save-button"><a href="#">')
                __M_writer(conditional_websafe(_("unsave")))
                __M_writer(u'</a></li>\n')
                # SOURCE LINE 348
            else:
                # SOURCE LINE 349
                __M_writer(u'      <li class="link-save-button save-button"><a href="#">')
                __M_writer(conditional_websafe(_("save")))
                __M_writer(u'</a></li>\n')
            # SOURCE LINE 351
            __M_writer(u'    <li>\n')
            # SOURCE LINE 352
            if thing.hidden:
                # SOURCE LINE 353
                __M_writer(u'      ')
                __M_writer(conditional_websafe(self.state_button("unhide", _("unhide"), \
        "change_state(this, 'unhide', hide_thing);", _("unhidden"),
        access_required=False, event_action="unhide")))
                # SOURCE LINE 355
                __M_writer(u'\n')
                # SOURCE LINE 356
            else:
                # SOURCE LINE 357
                __M_writer(u'      ')
                __M_writer(conditional_websafe(self.state_button("hide", _("hide"), \
         "change_state(this, 'hide', hide_thing);", _("hidden"),
         access_required=False, event_action="hide")))
                # SOURCE LINE 359
                __M_writer(u'\n')
            # SOURCE LINE 361
            __M_writer(u'    </li>\n')
        # SOURCE LINE 363
        __M_writer(u'\n  ')
        # SOURCE LINE 364
        __M_writer(conditional_websafe(self.distinguish()))
        __M_writer(u'\n  ')
        # SOURCE LINE 365
        __M_writer(conditional_websafe(self.give_gold()))
        __M_writer(u'\n  ')
        # SOURCE LINE 366
        __M_writer(conditional_websafe(self.banbuttons()))
        __M_writer(u'\n')
        # SOURCE LINE 367
        if thing.promoted is not None:
            # SOURCE LINE 368
            if thing.user_is_sponsor or thing.is_author:
                # SOURCE LINE 369
                __M_writer(u'       <li>\n         ')
                # SOURCE LINE 370
                __M_writer(conditional_websafe(plain_link(_("edit"), thing.promo_url, _sr_path = False)))
                __M_writer(u'\n       </li>\n')
            # SOURCE LINE 373
            if c.user_is_sponsor:
                # SOURCE LINE 374
                if thing.show_approval:
                    # SOURCE LINE 375
                    if thing.promote_status not in (PROMOTE_STATUS.rejected, PROMOTE_STATUS.finished):
                        # SOURCE LINE 376
                        __M_writer(u'          <li>\n            <form action="/post/reject" class="rejection-form"\n                 style="display:none"\n')
                        # SOURCE LINE 379
                        if getattr(thing, "hide_after_seen", False):
                            # SOURCE LINE 380
                            __M_writer(u'                   data-hide-after-seen="true"\n')
                        # SOURCE LINE 382
                        __M_writer(u'                 method="post" onsubmit="reject post_form(this, \'unpromote\')">\n              <br/>\n              <input type="hidden" name="executed" value="rejected" />\n              <label>Reason:</label><br/>\n              <textarea name="reason" value="" ></textarea>\n              <br/>\n              <a href="javascript: void 0;"\n                onclick="change_state(this, \'unpromote\', complete_reject_promo)">\n               submit\n              </a>/\n            </form>\n            ')
                        # SOURCE LINE 393
                        __M_writer(conditional_websafe(toggle_button("reject_promo", \
                           _("reject"), _("cancel"), \
                           "reject_promo", "cancel_reject_promo")))
                        # SOURCE LINE 395
                        __M_writer(u'\n          </li>\n')
                    # SOURCE LINE 398
                    if thing.promote_status in (PROMOTE_STATUS.unpaid, PROMOTE_STATUS.unseen, PROMOTE_STATUS.rejected, PROMOTE_STATUS.edited_live):
                        # SOURCE LINE 399
                        __M_writer(u'          <li>\n            ')
                        # SOURCE LINE 400
                        __M_writer(conditional_websafe(ynbutton(_("accept"), \
                       _("accepted"), "promote", \
                       callback="hide_thing" if getattr(thing, "hide_after_seen", False) else "null")))
                        # SOURCE LINE 402
                        __M_writer(u'\n          </li>\n')
                # SOURCE LINE 406
                if thing.is_awaiting_fraud_review:
                    # SOURCE LINE 407
                    __M_writer(u'        <li class="fraud-button">\n          <a href="javascript:void(0)" class="action-thing" data-action-form="#fraud-action-form" title="')
                    # SOURCE LINE 408
                    __M_writer(conditional_websafe(thing.payment_flagged_reason))
                    __M_writer(u'">\n            ')
                    # SOURCE LINE 409
                    __M_writer(conditional_websafe(_("fraud")))
                    __M_writer(u'\n          </a>\n        </li>\n')
            # SOURCE LINE 414
            if thing.user_is_sponsor or thing.is_author:
                # SOURCE LINE 415
                __M_writer(u'      <li>\n        ')
                # SOURCE LINE 416
                __M_writer(conditional_websafe(plain_link(_("traffic"), thing.traffic_url, _sr_path = False)))
                __M_writer(u'\n      </li>\n')
        # SOURCE LINE 420
        __M_writer(u'\n')
        # SOURCE LINE 421
        if thing.show_reports and not thing.show_spam:
            # SOURCE LINE 422
            __M_writer(u'    ')
            __M_writer(conditional_websafe(reports_button()))
            __M_writer(u'\n')
        # SOURCE LINE 424
        __M_writer(u'\n')
        # SOURCE LINE 425
        if getattr(thing.thing, "use_big_modbuttons", False):
            # SOURCE LINE 426
            __M_writer(u'     ')
            __M_writer(conditional_websafe(big_modbuttons(thing.thing)))
            __M_writer(u'\n')
            # SOURCE LINE 427
        elif thing.ignore_reports and thing.can_ban:
            # SOURCE LINE 428
            __M_writer(u'    ')
            __M_writer(conditional_websafe(ignore_reports_toggle(thing.thing)))
            __M_writer(u'\n')
        # SOURCE LINE 430
        __M_writer(u'\n')
        # SOURCE LINE 431
        if thing.show_reports and not thing.show_spam and (thing.mod_reports or thing.user_reports):
            # SOURCE LINE 432
            __M_writer(u'    ')
            __M_writer(conditional_websafe(report_reasons()))
            __M_writer(u'\n')
        # SOURCE LINE 434
        __M_writer(u'\n')
        # SOURCE LINE 436
        if thing.show_chat_link:
            # SOURCE LINE 437
            __M_writer(u'    <li class="chat-popout">\n      <a target="_blank" href="')
            # SOURCE LINE 438
            __M_writer(conditional_websafe(thing.chat_popout_url))
            __M_writer(u'">')
            __M_writer(conditional_websafe(_("open chat in new tab")))
            __M_writer(u'</a>\n    </li>\n')
        # SOURCE LINE 441
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_big_modbuttons(context,thing):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7a2aa10')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data', u'error_field'])
        def ignore_reports_toggle(thing):
            return render_ignore_reports_toggle(context,thing)
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        pretty_button = _import_ns.get('pretty_button', context.get('pretty_button', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 234
        __M_writer(u'\n  <span class="big-mod-buttons">\n')
        # SOURCE LINE 236
        if not thing._deleted:
            # SOURCE LINE 237
            __M_writer(u'      <span role="radiogroup">\n')
            # SOURCE LINE 238
            if not getattr(thing, "moderator_banned", None) or getattr(thing, "autobanned", False):
                # SOURCE LINE 239
                __M_writer(u'          ')
                __M_writer(conditional_websafe(pretty_button(_("spam"), "big_mod_action", -2, "negative", event_action="spam")))
                __M_writer(u'\n          ')
                # SOURCE LINE 240
                __M_writer(conditional_websafe(pretty_button(_("remove"), "big_mod_action", -1, "neutral", event_action="remove")))
                __M_writer(u'\n')
            # SOURCE LINE 242
            __M_writer(u'\n')
            # SOURCE LINE 243
            if getattr(thing, "approval_checkmark", None):
                # SOURCE LINE 244
                __M_writer(u'          ')
                __M_writer(conditional_websafe(pretty_button(_("reapprove"), "big_mod_action",  1, "positive", event_action="approve")))
                __M_writer(u'\n')
                # SOURCE LINE 245
            else:
                # SOURCE LINE 246
                __M_writer(u'          ')
                __M_writer(conditional_websafe(pretty_button(_("approve"), "big_mod_action",  1, "positive", event_action="approve")))
                __M_writer(u'\n')
            # SOURCE LINE 248
            __M_writer(u'      </span>\n')
        # SOURCE LINE 250
        __M_writer(u'\n')
        # SOURCE LINE 251
        if not thing._spam:
            # SOURCE LINE 252
            __M_writer(u'      ')
            __M_writer(conditional_websafe(ignore_reports_toggle(thing)))
            __M_writer(u'\n')
        # SOURCE LINE 254
        __M_writer(u'\n    &#32;\n    <span class="status-msg spammed">\n      ')
        # SOURCE LINE 257
        __M_writer(conditional_websafe(_("spammed")))
        __M_writer(u'\n    </span>\n    <span class="status-msg removed">\n      ')
        # SOURCE LINE 260
        __M_writer(conditional_websafe(_("removed")))
        __M_writer(u'\n    </span>\n    <span class="status-msg approved">\n      ')
        # SOURCE LINE 263
        __M_writer(conditional_websafe(_("approved")))
        __M_writer(u'\n    </span>\n  </span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_report_reasons(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7a2aa10')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data', u'error_field'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 294
        __M_writer(u'\n<ul class="report-reasons rounded">\n')
        # SOURCE LINE 296
        if thing.mod_reports:
            # SOURCE LINE 297
            __M_writer(u'    <li class="report-reason-title">')
            __M_writer(conditional_websafe(_("moderator reports:")))
            __M_writer(u'</li>\n')
            # SOURCE LINE 298
            for reason, user in thing.mod_reports:
                # SOURCE LINE 299
                __M_writer(u'      <li class="report-reason mod-report" title="')
                __M_writer(conditional_websafe(reason))
                __M_writer(u'">')
                __M_writer(conditional_websafe(user))
                __M_writer(u':\n')
                # SOURCE LINE 300
                if reason:
                    # SOURCE LINE 301
                    __M_writer(u'        ')
                    __M_writer(conditional_websafe(reason))
                    __M_writer(u'\n')
                    # SOURCE LINE 302
                else:
                    # SOURCE LINE 303
                    __M_writer(u'        ')
                    __M_writer(conditional_websafe(_("<no reason>")))
                    __M_writer(u'\n')
                # SOURCE LINE 305
                __M_writer(u'      </li>\n')
        # SOURCE LINE 308
        __M_writer(u'\n')
        # SOURCE LINE 309
        if thing.user_reports:
            # SOURCE LINE 310
            __M_writer(u'    <li class="report-reason-title">')
            __M_writer(conditional_websafe(_("user reports:")))
            __M_writer(u'</li>\n')
            # SOURCE LINE 311
            for reason, count in thing.user_reports:
                # SOURCE LINE 312
                __M_writer(u'      <li class="report-reason" title="')
                __M_writer(conditional_websafe(reason))
                __M_writer(u'">')
                __M_writer(conditional_websafe(count))
                __M_writer(u':\n')
                # SOURCE LINE 313
                if reason:
                    # SOURCE LINE 314
                    __M_writer(u'        ')
                    __M_writer(conditional_websafe(reason))
                    __M_writer(u'\n')
                    # SOURCE LINE 315
                else:
                    # SOURCE LINE 316
                    __M_writer(u'        ')
                    __M_writer(conditional_websafe(_("<no reason>")))
                    __M_writer(u'\n')
                # SOURCE LINE 318
                __M_writer(u'      </li>\n')
        # SOURCE LINE 321
        __M_writer(u'</ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_ynbutton(context,title,executed,op,callback='null',question=None,post_callback='null',format='%(link)s',format_arg='link',hidden_data={},access_required=True,event_target=None,event_action=None,event_detail=None,_class=''):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7a2aa10')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data', u'error_field'])
        capture = _import_ns.get('capture', context.get('capture', UNDEFINED))
        data = _import_ns.get('data', context.get('data', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 694
        __M_writer(u'\n  ')
        # SOURCE LINE 695

        if question is None:
            question = _("are you sure?")
        access_class = 'access-required' if access_required else ''
        
        data_attrs = {}
        if event_target:
          data_attrs['type'] = event_target
        if event_action:
          data_attrs['event-action'] = event_action
        if event_detail:
          data_attrs['event-detail'] = event_detail
        
        link = ('<a href="#" class="togglebutton ' + access_class + '" onclick="return toggle(this)" '
                + capture(data, **data_attrs) + '>'
                + conditional_websafe(title) + '</a>')
        link = conditional_websafe(format) % {format_arg : link}
        link = unsafe(link.replace(" <", "&#32;<").replace("> ", ">&#32;"))
           
        
        # SOURCE LINE 713
        __M_writer(u'\n  <form class="toggle ')
        # SOURCE LINE 714
        __M_writer(conditional_websafe(op))
        __M_writer(u'-button ')
        __M_writer(conditional_websafe(_class))
        __M_writer(u'" action="#" method="get">\n    <input type="hidden" name="executed" value="')
        # SOURCE LINE 715
        __M_writer(conditional_websafe(executed))
        __M_writer(u'"/>\n')
        # SOURCE LINE 716
        for k, v in hidden_data.iteritems():
            # SOURCE LINE 717
            __M_writer(u'      <input type="hidden" name="')
            __M_writer(conditional_websafe(k))
            __M_writer(u'" value="')
            __M_writer(conditional_websafe(v))
            __M_writer(u'"/>\n')
        # SOURCE LINE 719
        __M_writer(u'    <span class="option main active">\n      ')
        # SOURCE LINE 720
        __M_writer(conditional_websafe(link))
        __M_writer(u'\n    </span>\n    <span class="option error">\n      ')
        # SOURCE LINE 723
        __M_writer(conditional_websafe(question))
        __M_writer(u'\n      &#32;<a href="javascript:void(0)" class="yes"\n         onclick=\'change_state(this, "')
        # SOURCE LINE 725
        __M_writer(conditional_websafe(op))
        __M_writer(u'", ')
        __M_writer(conditional_websafe(callback))
        __M_writer(u', undefined, ')
        __M_writer(conditional_websafe(post_callback))
        __M_writer(u")'>\n        ")
        # SOURCE LINE 726
        __M_writer(conditional_websafe(_("yes")))
        __M_writer(u'\n      </a>&#32;/&#32;\n      <a href="javascript:void(0)" class="no"\n         onclick="return toggle(this)">')
        # SOURCE LINE 729
        __M_writer(conditional_websafe(_("no")))
        __M_writer(u'</a>\n    </span>\n  </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_distinguish_options(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7a2aa10')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data', u'error_field'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        def distinguish_setter(name,value=None,event_action='distinguish'):
            return render_distinguish_setter(context,name,value,event_action)
        def distinguish_help():
            return render_distinguish_help(context)
        __M_writer = context.writer()
        # SOURCE LINE 128
        __M_writer(u'\n  ')
        # SOURCE LINE 129
        __M_writer(conditional_websafe(_("distinguish this?")))
        __M_writer(u'\n\n')
        # SOURCE LINE 132
        if thing.can_ban:
            # SOURCE LINE 133
            __M_writer(u'    &#32;\n    ')
            # SOURCE LINE 134
            __M_writer(conditional_websafe(distinguish_setter('yes')))
            __M_writer(u'\n    &#32;/\n\n')
            # SOURCE LINE 137
            if thing.show_sticky_comment:
                # SOURCE LINE 138
                __M_writer(u'      &#32;\n      ')
                # SOURCE LINE 139
                __M_writer(conditional_websafe(distinguish_setter(_('yes & sticky'), 'yes_sticky', event_action="sticky_distinguish")))
                __M_writer(u'\n      &#32;/\n')
        # SOURCE LINE 143
        __M_writer(u'  \n  &#32;\n  ')
        # SOURCE LINE 145
        __M_writer(conditional_websafe(distinguish_setter('no', event_action="undistinguish")))
        __M_writer(u'\n  &#32;\n\n')
        # SOURCE LINE 148
        if c.user.employee:
            # SOURCE LINE 149
            __M_writer(u'    /&#32;\n    ')
            # SOURCE LINE 150
            __M_writer(conditional_websafe(distinguish_setter('admin', event_action="admin_distinguish")))
            __M_writer(u'\n    &#32;\n')
        # SOURCE LINE 153
        __M_writer(u'  \n')
        # SOURCE LINE 154
        if c.user_special_distinguish:
            # SOURCE LINE 155
            __M_writer(u'    /&#32;\n    ')
            # SOURCE LINE 156
            __M_writer(conditional_websafe(distinguish_setter(c.user_special_distinguish['name'], 'special', event_action="special_distinguish")))
            __M_writer(u'\n    &#32;\n')
        # SOURCE LINE 159
        __M_writer(u'\n  /&#32;\n  ')
        # SOURCE LINE 161
        __M_writer(conditional_websafe(distinguish_help()))
        __M_writer(u'\n  &#32;\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_show_admin_context(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7a2aa10')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data', u'error_field'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 268
        __M_writer(u'\n')
        # SOURCE LINE 269
        if thing.show_admin_context:
            # SOURCE LINE 270
            __M_writer(u'    <li>\n      <form onsubmit="return post_form(this, \'admin/fullcontext\');" method="post">\n        <input type="hidden" name="thing" id="thing" value="')
            # SOURCE LINE 272
            __M_writer(conditional_websafe(thing.thing._fullname))
            __M_writer(u'" />\n        <input type="hidden" name="author" id="author" value="')
            # SOURCE LINE 273
            __M_writer(conditional_websafe(thing.thing.author_slow._fullname))
            __M_writer(u'" />\n        <a href="#" onclick="$(this).closest(\'form\').submit(); return false">full context</a>\n       </form>\n    </li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_undistinguish_options(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7a2aa10')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data', u'error_field'])
        def distinguish_noop(text):
            return render_distinguish_noop(context,text)
        def distinguish_setter(name,value=None,event_action='distinguish'):
            return render_distinguish_setter(context,name,value,event_action)
        def distinguish_help():
            return render_distinguish_help(context)
        __M_writer = context.writer()
        # SOURCE LINE 165
        __M_writer(u'\n  ')
        # SOURCE LINE 166
        __M_writer(conditional_websafe(_("undistinguish this?")))
        __M_writer(u'\n\n  &#32;\n  ')
        # SOURCE LINE 169
        __M_writer(conditional_websafe(distinguish_setter('yes', value="no", event_action="undistinguish")))
        __M_writer(u'\n  &#32;/\n\n  &#32;\n  ')
        # SOURCE LINE 173
        __M_writer(conditional_websafe(distinguish_noop(_("no"))))
        __M_writer(u'\n  &#32;\n\n  /&#32;\n  ')
        # SOURCE LINE 177
        __M_writer(conditional_websafe(distinguish_help()))
        __M_writer(u'\n  &#32;\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bylink_button(context,title,link,sr_path=True,a_class='bylink',event_action=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7a2aa10')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data', u'error_field'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 777
        __M_writer(u'\n  ')
        # SOURCE LINE 778

        data_attrs = {}
        
        if event_action:
          data_attrs["event-action"] = event_action
        
        inbound_tracking_url = Link.tracking_link(link, thing, element_name=event_action)
        if inbound_tracking_url != link:
          data_attrs["href-url"] = link
          data_attrs["inbound-url"] = inbound_tracking_url
          
        
        # SOURCE LINE 788
        __M_writer(u'\n  ')
        # SOURCE LINE 789
        __M_writer(conditional_websafe(plain_link(
      title,
      link,
      _class=a_class,
      rel="nofollow",
      _sr_path=sr_path,
      data=data_attrs,
  )))
        # SOURCE LINE 796
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_commentbuttons(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7a2aa10')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data', u'error_field'])
        def report_reasons():
            return render_report_reasons(context)
        def reports_button():
            return render_reports_button(context)
        def ignore_reports_toggle(thing):
            return render_ignore_reports_toggle(context,thing)
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        def ynbutton(title,executed,op,callback='null',question=None,post_callback='null',format='%(link)s',format_arg='link',hidden_data={},access_required=True,event_target=None,event_action=None,event_detail=None,_class=''):
            return render_ynbutton(context,title,executed,op,callback,question,post_callback,format,format_arg,hidden_data,access_required,event_target,event_action,event_detail,_class)
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        def big_modbuttons(thing):
            return render_big_modbuttons(context,thing)
        __M_writer = context.writer()
        # SOURCE LINE 444
        __M_writer(u'\n')
        # SOURCE LINE 445
        if not thing.deleted:
            # SOURCE LINE 446
            __M_writer(u'    <li class="first">\n      ')
            # SOURCE LINE 447
            __M_writer(conditional_websafe(self.bylink_button(_("permalink"), thing.permalink, event_action="permalink")))
            __M_writer(u'\n    </li>\n')
            # SOURCE LINE 449
            if thing.embed_button:
                # SOURCE LINE 450
                __M_writer(u'      <li>\n        ')
                # SOURCE LINE 451
                __M_writer(conditional_websafe(thing.embed_button.render()))
                __M_writer(u'\n      </li>\n')
            # SOURCE LINE 454
            __M_writer(u'\n')
            # SOURCE LINE 455
            if thing.saved:
                # SOURCE LINE 456
                __M_writer(u'      <li class="comment-unsave-button save-button">\n        <a href="javascript:void(0)">')
                # SOURCE LINE 457
                __M_writer(conditional_websafe(_("unsave")))
                __M_writer(u'</a>\n      </li>\n')
                # SOURCE LINE 459
            else:
                # SOURCE LINE 460
                __M_writer(u'      <li class="comment-save-button save-button">\n        <a href="javascript:void(0)">')
                # SOURCE LINE 461
                __M_writer(conditional_websafe(_("save")))
                __M_writer(u'</a>\n      </li>\n')
            # SOURCE LINE 464
            __M_writer(u'\n')
            # SOURCE LINE 465
            if c.profilepage:
                # SOURCE LINE 466
                __M_writer(u'      <li>\n        ')
                # SOURCE LINE 467
                __M_writer(conditional_websafe(self.bylink_button(_("context"), thing.permalink + "?context=3", event_action="context")))
                __M_writer(u'\n      </li>\n      <li class="first">\n      ')
                # SOURCE LINE 470
                __M_writer(conditional_websafe(self.bylink_button(
          _("full comments") + " (%d)" % thing.full_comment_count, 
          thing.full_comment_path,
          sr_path=True,
          a_class="bylink may-blank",
          event_action="full_comments")))
                # SOURCE LINE 475
                __M_writer(u'\n      </li>\n')
            # SOURCE LINE 478
            __M_writer(u'\n')
            # SOURCE LINE 479
            if thing.parent_permalink and not thing.profilepage:
                # SOURCE LINE 480
                __M_writer(u'      <li>\n        ')
                # SOURCE LINE 481
                __M_writer(conditional_websafe(self.bylink_button(_("parent"), thing.parent_permalink, event_action="parent")))
                __M_writer(u'\n      </li>\n')
            # SOURCE LINE 484
            __M_writer(u'\n')
            # SOURCE LINE 485
            if thing.is_author:
                # SOURCE LINE 486
                if thing.editable:
                    # SOURCE LINE 487
                    __M_writer(u'        <li>\n          ')
                    # SOURCE LINE 488
                    __M_writer(conditional_websafe(self.simple_button(_("edit"), "edit_usertext", css_class="edit-usertext")))
                    __M_writer(u'\n        </li>\n')
                # SOURCE LINE 491
                __M_writer(u'      <li>\n')
                # SOURCE LINE 492
                if thing.thing.inbox_replies_enabled:
                    # SOURCE LINE 493
                    __M_writer(u'          ')
                    __M_writer(conditional_websafe(ynbutton(_("disable inbox replies"), _("inbox replies disabled"), "sendreplies",
            hidden_data=dict(id=thing.thing._fullname, state=False),
            access_required=False, event_action="disable_inbox_replies")))
                    # SOURCE LINE 495
                    __M_writer(u'\n')
                    # SOURCE LINE 496
                else:
                    # SOURCE LINE 497
                    __M_writer(u'          ')
                    __M_writer(conditional_websafe(ynbutton(_("enable inbox replies"), _("inbox replies enabled"), "sendreplies",
            hidden_data=dict(id=thing.thing._fullname, state=True),
            access_required=False, event_action="enable_inbox_replies")))
                    # SOURCE LINE 499
                    __M_writer(u'\n')
                # SOURCE LINE 501
                __M_writer(u'      </li>\n')
            # SOURCE LINE 503
            __M_writer(u'\n    ')
            # SOURCE LINE 504
            __M_writer(conditional_websafe(self.banbuttons()))
            __M_writer(u'\n    ')
            # SOURCE LINE 505
            __M_writer(conditional_websafe(self.distinguish()))
            __M_writer(u'\n    ')
            # SOURCE LINE 506
            __M_writer(conditional_websafe(self.give_gold()))
            __M_writer(u'\n    ')
            # SOURCE LINE 507
            __M_writer(conditional_websafe(self.show_admin_context()))
            __M_writer(u'\n\n')
            # SOURCE LINE 509
            if not getattr(thing, "suppress_reply_buttons", False) and (thing.can_reply or thing.locked):
                # SOURCE LINE 510
                __M_writer(u'      <li class="reply-button">\n')
                # SOURCE LINE 511
                if thing.can_reply:
                    # SOURCE LINE 512
                    __M_writer(u'        ')
                    __M_writer(conditional_websafe(self.simple_button(_("reply {verb}"), "reply", css_class="access-required", event_action="comment")))
                    __M_writer(u'\n')
                    # SOURCE LINE 513
                else:
                    # SOURCE LINE 514
                    __M_writer(u'        ')
                    __M_writer(conditional_websafe(self.simple_button(_("reply {verb}"), "void", css_class="locked-error access-required", event_action="comment")))
                    __M_writer(u'\n')
                # SOURCE LINE 516
                __M_writer(u'      </li>\n')
            # SOURCE LINE 518
            __M_writer(u'\n')
            # SOURCE LINE 519
            if thing.show_reports and not thing.show_spam:
                # SOURCE LINE 520
                __M_writer(u'      ')
                __M_writer(conditional_websafe(reports_button()))
                __M_writer(u'\n')
            # SOURCE LINE 522
            __M_writer(u'\n')
            # SOURCE LINE 523
            if getattr(thing.thing, "use_big_modbuttons", False):
                # SOURCE LINE 524
                __M_writer(u'       ')
                __M_writer(conditional_websafe(big_modbuttons(thing.thing)))
                __M_writer(u'\n')
                # SOURCE LINE 525
            elif thing.ignore_reports and thing.can_ban:
                # SOURCE LINE 526
                __M_writer(u'      ')
                __M_writer(conditional_websafe(ignore_reports_toggle(thing.thing)))
                __M_writer(u'\n')
            # SOURCE LINE 528
            __M_writer(u'\n')
            # SOURCE LINE 529
            if thing.show_reports and not thing.show_spam and (thing.mod_reports or thing.user_reports):
                # SOURCE LINE 530
                __M_writer(u'      ')
                __M_writer(conditional_websafe(report_reasons()))
                __M_writer(u'\n')
            # SOURCE LINE 532
            __M_writer(u'\n')
            # SOURCE LINE 534
            if thing.show_chat_link:
                # SOURCE LINE 535
                __M_writer(u'      <li class="chat-popout">\n        <a target="_blank" href="')
                # SOURCE LINE 536
                __M_writer(conditional_websafe(thing.chat_popout_url))
                __M_writer(u'">')
                __M_writer(conditional_websafe(_("open chat in new tab")))
                __M_writer(u'</a>\n      </li>\n')
            # SOURCE LINE 539
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_ignore_reports_toggle(context,thing):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7a2aa10')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data', u'error_field'])
        pretty_button = _import_ns.get('pretty_button', context.get('pretty_button', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 222
        __M_writer(u'\n  ')
        # SOURCE LINE 223

        label = _("ignore reports")
        if thing.ignore_reports and thing.reported > 0:
          label += " ({0})".format(thing.reported)
        event_action = "unignorereports" if thing.ignore_reports else "ignorereports"
          
        
        # SOURCE LINE 228
        __M_writer(u'\n  ')
        # SOURCE LINE 229
        __M_writer(conditional_websafe(pretty_button(label, "big_mod_toggle", "'ignore_reports', 'unignore_reports'",
  "neutral" + (" pressed" if thing.ignore_reports else ""),
  event_action=event_action)))
        # SOURCE LINE 231
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_ajax_ynbutton(context,title,op,question=None,_class='',hidden_data={}):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7a2aa10')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data', u'error_field'])
        __M_writer = context.writer()
        # SOURCE LINE 664
        __M_writer(u'\n  <form method="post" action="/api/')
        # SOURCE LINE 665
        __M_writer(conditional_websafe(op))
        __M_writer(u'"\n        class="toggle ajax-yn-button ')
        # SOURCE LINE 666
        __M_writer(conditional_websafe(op))
        __M_writer(u'-button ')
        __M_writer(conditional_websafe(_class))
        __M_writer(u'">\n    <input type="hidden" name="_op" value="')
        # SOURCE LINE 667
        __M_writer(conditional_websafe(op))
        __M_writer(u'" />\n')
        # SOURCE LINE 668
        for k, v in hidden_data.iteritems():
            # SOURCE LINE 669
            __M_writer(u'      <input type="hidden" name="')
            __M_writer(conditional_websafe(k))
            __M_writer(u'" value="')
            __M_writer(conditional_websafe(v))
            __M_writer(u'" />\n')
        # SOURCE LINE 671
        __M_writer(u'    <span class="option main active">\n      <a href="javascript:void(0)" class="togglebutton">')
        # SOURCE LINE 672
        __M_writer(conditional_websafe(title))
        __M_writer(u'</a>\n    </span>\n    <span class="option error">\n      ')
        # SOURCE LINE 675
        __M_writer(conditional_websafe(_("are you sure?") if question is None else question))
        __M_writer(u'\n      &#32;\n      <a href="javascript:void(0)" class="yes">')
        # SOURCE LINE 677
        __M_writer(conditional_websafe(_("yes")))
        __M_writer(u'</a>\n      &#32;/&#32;\n      <a href="javascript:void(0)" class="no">')
        # SOURCE LINE 679
        __M_writer(conditional_websafe(_("no")))
        __M_writer(u'</a>\n    </span>\n  </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_toggle_button(context,class_name,title,alt_title,callback,cancelback,css_class='',alt_css_class='',reverse=False,login_required=False,style='',data_attrs=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7a2aa10')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data', u'error_field'])
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        data = _import_ns.get('data', context.get('data', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 747
        __M_writer(u'\n')
        # SOURCE LINE 748

        if reverse:
            callback, cancelback = cancelback, callback
            title, alt_title = alt_title, title
            css_class, alt_css_class = alt_css_class, css_class
        extra_class = "login-required" if login_required else ""
         
        
        # SOURCE LINE 754
        __M_writer(u'\n<span class="')
        # SOURCE LINE 755
        __M_writer(conditional_websafe(class_name))
        __M_writer(u' toggle" style="')
        __M_writer(conditional_websafe(style))
        __M_writer(u'" ')
        __M_writer(conditional_websafe(data(**data_attrs or dict())))
        __M_writer(u'>\n <a class="option active ')
        # SOURCE LINE 756
        __M_writer(conditional_websafe(css_class))
        __M_writer(u' ')
        __M_writer(conditional_websafe(extra_class))
        __M_writer(u'" href="#" tabindex="100"\n')
        # SOURCE LINE 757
        if not login_required or c.user_is_loggedin:
            # SOURCE LINE 758
            __M_writer(u'      onclick="return toggle(this, ')
            __M_writer(conditional_websafe(callback))
            __M_writer(u', ')
            __M_writer(conditional_websafe(cancelback))
            __M_writer(u')"\n')
        # SOURCE LINE 760
        __M_writer(u'    >\n')
        # SOURCE LINE 761
        if title:
            # SOURCE LINE 762
            __M_writer(u'     ')
            __M_writer(conditional_websafe(title))
            __M_writer(u'\n')
            # SOURCE LINE 763
        else:
            # SOURCE LINE 764
            __M_writer(u'     &nbsp;\n')
        # SOURCE LINE 766
        __M_writer(u' </a>\n <a class="option ')
        # SOURCE LINE 767
        __M_writer(conditional_websafe(alt_css_class))
        __M_writer(u'" href="#">\n')
        # SOURCE LINE 768
        if alt_title:
            # SOURCE LINE 769
            __M_writer(u'     ')
            __M_writer(conditional_websafe(alt_title))
            __M_writer(u'\n')
            # SOURCE LINE 770
        else:
            # SOURCE LINE 771
            __M_writer(u'     &nbsp;\n')
        # SOURCE LINE 773
        __M_writer(u' </a>\n</span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_distinguish_setter(context,name,value=None,event_action='distinguish'):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7a2aa10')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data', u'error_field'])
        __M_writer = context.writer()
        # SOURCE LINE 99
        __M_writer(u'\n  <a class="access-required"\n     href="javascript:void(0)"\n     data-event-action="')
        # SOURCE LINE 102
        __M_writer(conditional_websafe(event_action))
        __M_writer(u'"\n     onclick="return set_distinguish(this, \'')
        # SOURCE LINE 103
        __M_writer(conditional_websafe(jssafe(value or name)))
        __M_writer(u'\')">')
        __M_writer(conditional_websafe(_(name)))
        __M_writer(u'</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_distinguish_help(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7a2aa10')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data', u'error_field'])
        __M_writer = context.writer()
        # SOURCE LINE 122
        __M_writer(u'\n  <a class="nonbutton" href="/wiki/moderation#wiki_distinguishing">\n    ')
        # SOURCE LINE 124
        __M_writer(conditional_websafe(_("help")))
        __M_writer(u'\n  </a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_distinguish_label(context,distinguish_clicked):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7a2aa10')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data', u'error_field'])
        __M_writer = context.writer()
        # SOURCE LINE 112
        __M_writer(u'\n  ')
        # SOURCE LINE 113

        text = _("distinguish") if distinguish_clicked else _("undistinguish")
          
        
        # SOURCE LINE 115
        __M_writer(u'\n  <a class="access-required"\n    href="javascript:void(0)"\n    onclick="return toggle_distinguish_span(this)"\n    data-event-action="distinguish">')
        # SOURCE LINE 119
        __M_writer(conditional_websafe(text))
        __M_writer(u'</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_messagebuttons(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7a2aa10')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data', u'error_field'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        def ynbutton(title,executed,op,callback='null',question=None,post_callback='null',format='%(link)s',format_arg='link',hidden_data={},access_required=True,event_target=None,event_action=None,event_detail=None,_class=''):
            return render_ynbutton(context,title,executed,op,callback,question,post_callback,format,format_arg,hidden_data,access_required,event_target,event_action,event_detail,_class)
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 544
        __M_writer(u' \n')
        # SOURCE LINE 545
        if thing.was_comment:
            # SOURCE LINE 546
            __M_writer(u'    <li>\n      ')
            # SOURCE LINE 547
            __M_writer(conditional_websafe(self.bylink_button(_("context"), thing.permalink + "?context=3", event_action="context")))
            __M_writer(u'\n    </li>\n    <li>\n      ')
            # SOURCE LINE 550
            __M_writer(conditional_websafe(self.bylink_button(
          _("full comments") + " (%d)" % thing.full_comment_count,
          thing.full_comment_path,
          a_class="bylink may-blank full-comments",
          event_action="full_comments")))
            # SOURCE LINE 554
            __M_writer(u'\n    </li>\n')
            # SOURCE LINE 556
        else:
            # SOURCE LINE 557
            __M_writer(u'    <li class="first">\n      ')
            # SOURCE LINE 558
            __M_writer(conditional_websafe(self.bylink_button(_("permalink"), thing.permalink, sr_path=False, event_action="permalink")))
            __M_writer(u'\n    </li>\n    ')
            # SOURCE LINE 560
            __M_writer(conditional_websafe(self.distinguish()))
            __M_writer(u'\n')
        # SOURCE LINE 562
        if thing.user_is_recipient:
            # SOURCE LINE 564
            if not (thing.was_comment or thing.thing.del_on_recipient) and thing.thing.to_id == c.user._id:
                # SOURCE LINE 565
                __M_writer(u'      <li>\n        ')
                # SOURCE LINE 566
                __M_writer(conditional_websafe(ynbutton(_("delete"), _("deleted"), "del_msg", "hide_thing", access_required=False, event_action="delete_message")))
                __M_writer(u'\n      </li>\n')
            # SOURCE LINE 569
            if thing.can_block:
                # SOURCE LINE 570
                __M_writer(u'      ')
                __M_writer(conditional_websafe(self.banbuttons()))
                __M_writer(u'\n')
                # SOURCE LINE 571
                if thing.thing.author_id != c.user._id and thing.thing.author_id not in c.user.enemies:
                    # SOURCE LINE 572
                    if getattr(thing.thing, "from_sr", False):
                        # SOURCE LINE 573
                        if not (thing.thing.user_is_moderator or c.user_is_admin):
                            # SOURCE LINE 574
                            __M_writer(u'              <li>\n')
                            # SOURCE LINE 575
                            if getattr(thing.thing, "sr_blocked", False):
                                # SOURCE LINE 576
                                __M_writer(u'                  ')
                                __M_writer(conditional_websafe(ynbutton(_("unblock subreddit"), _("unblocked"), "unblock_subreddit",
                      access_required=False, event_action="unblock_subreddit")))
                                # SOURCE LINE 577
                                __M_writer(u'\n')
                                # SOURCE LINE 578
                            else:
                                # SOURCE LINE 579
                                __M_writer(u'                  ')
                                __M_writer(conditional_websafe(ynbutton(_("block subreddit"), _("blocked"), "block", "hide_thing",
                      access_required=False, event_action="block_subreddit")))
                                # SOURCE LINE 580
                                __M_writer(u'\n')
                            # SOURCE LINE 582
                            __M_writer(u'              </li>\n')
                        # SOURCE LINE 584
                    else:
                        # SOURCE LINE 585
                        __M_writer(u'            <li>\n              ')
                        # SOURCE LINE 586
                        __M_writer(conditional_websafe(ynbutton(_("block user"), _("blocked"), "block", "hide_thing",
                  access_required=False, event_action="block_user")))
                        # SOURCE LINE 587
                        __M_writer(u'\n            </li>\n')
                    # SOURCE LINE 590
                    if thing.can_mute:
                        # SOURCE LINE 591
                        __M_writer(u'            <li>\n')
                        # SOURCE LINE 592
                        if getattr(thing.thing, "sr_muted", False):
                            # SOURCE LINE 593
                            __M_writer(u'                ')
                            __M_writer(conditional_websafe(ynbutton(_("unmute user"), _("unmuted"), "unmute_message_author",
                    event_action="unmute_user")))
                            # SOURCE LINE 594
                            __M_writer(u'\n')
                            # SOURCE LINE 595
                        else:
                            # SOURCE LINE 596
                            __M_writer(u'                ')
                            __M_writer(conditional_websafe(ynbutton(_("mute user"), _("muted"), "mute_message_author",
                    event_action="mute_user")))
                            # SOURCE LINE 597
                            __M_writer(u'\n')
                        # SOURCE LINE 599
                        __M_writer(u'            </li>\n')
            # SOURCE LINE 603
            __M_writer(u'    <li class="unread">\n     ')
            # SOURCE LINE 604
            __M_writer(conditional_websafe(self.state_button("unread", _("mark unread"), \
        "return change_state(this, 'unread_message', unread_thing, true);", \
         _("unread"), event_action="mark_unread")))
            # SOURCE LINE 606
            __M_writer(u'\n    </li>\n')
        # SOURCE LINE 609
        if thing.can_reply:
            # SOURCE LINE 610
            __M_writer(u'    <li>\n       ')
            # SOURCE LINE 611

            css_class = "" if thing.is_admin_message else "access-required"
                   
            
            # SOURCE LINE 613
            __M_writer(u'\n       ')
            # SOURCE LINE 614
            __M_writer(conditional_websafe(self.simple_button(_("reply {verb}"), "reply", css_class, event_action='reply')))
            __M_writer(u'\n    </li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_banbuttons(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7a2aa10')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data', u'error_field'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        def ynbutton(title,executed,op,callback='null',question=None,post_callback='null',format='%(link)s',format_arg='link',hidden_data={},access_required=True,event_target=None,event_action=None,event_detail=None,_class=''):
            return render_ynbutton(context,title,executed,op,callback,question,post_callback,format,format_arg,hidden_data,access_required,event_target,event_action,event_detail,_class)
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 33
        __M_writer(u'\n')
        # SOURCE LINE 34
        if thing.show_delete:
            # SOURCE LINE 35
            __M_writer(u'    <li>\n      ')
            # SOURCE LINE 36
            __M_writer(conditional_websafe(ynbutton(_("delete"), _("deleted"), "del", "hide_thing", access_required=False, event_action="delete")))
            __M_writer(u'\n    </li>\n')
        # SOURCE LINE 39
        if thing.can_ban:
            # SOURCE LINE 40
            if not getattr(thing.thing, "use_big_modbuttons", False):
                # SOURCE LINE 41
                if not thing.show_spam:
                    # SOURCE LINE 42
                    __M_writer(u'        <li>\n           ')
                    # SOURCE LINE 43
                    __M_writer(conditional_websafe(ynbutton(_("spam"), _("spammed"), "remove", event_action='spam')))
                    __M_writer(u'\n        </li>\n        <li>\n           ')
                    # SOURCE LINE 46
                    __M_writer(conditional_websafe(ynbutton(_("remove"), _("removed"), "remove", hidden_data=dict(spam=False),
             event_action='remove')))
                    # SOURCE LINE 47
                    __M_writer(u'\n        </li>\n')
                # SOURCE LINE 50
                __M_writer(u'\n')
                # SOURCE LINE 51
                if thing.show_approve:
                    # SOURCE LINE 52
                    __M_writer(u'        <li>\n           ')
                    # SOURCE LINE 53
                    __M_writer(conditional_websafe(self.state_button("approve", _("approve"),
              "return change_state(this, 'approve');", _("approved"),
              event_action="approve")))
                    # SOURCE LINE 55
                    __M_writer(u'\n        </li>\n')
        # SOURCE LINE 60
        __M_writer(u'\n')
        # SOURCE LINE 61
        if thing.show_report:
            # SOURCE LINE 62
            __M_writer(u'    <li class="report-button">\n')
            # SOURCE LINE 63
            if feature.is_enabled("new_report_dialog"):
                # SOURCE LINE 64
                __M_writer(u'        <a href="javascript:void(0)" class="reportbtn access-required"\n           data-event-action="report">\n')
                # SOURCE LINE 66
            else:
                # SOURCE LINE 67
                __M_writer(u'        <a href="javascript:void(0)" class="action-thing reportbtn access-required"\n           data-event-action="report">\n')
            # SOURCE LINE 70
            __M_writer(u'        ')
            __M_writer(conditional_websafe(_("report")))
            __M_writer(u'\n      </a>\n    </li>\n')
        # SOURCE LINE 74
        if thing.show_lock:
            # SOURCE LINE 75
            __M_writer(u'    <li>')
            __M_writer(conditional_websafe(ynbutton(_("lock"), _("locked"), "lock", event_action='lock')))
            __M_writer(u'</li>\n')
        # SOURCE LINE 77
        if thing.show_unlock:
            # SOURCE LINE 78
            __M_writer(u'    <li>')
            __M_writer(conditional_websafe(ynbutton(_("unlock"), _("unlocked"), "unlock", event_action='unlock')))
            __M_writer(u'</li>\n')
        # SOURCE LINE 80
        if thing.show_marknsfw:
            # SOURCE LINE 81
            __M_writer(u'    <li>')
            __M_writer(conditional_websafe(ynbutton(_("nsfw"), _("marked"), "marknsfw", event_action='marknsfw')))
            __M_writer(u'</li>\n')
        # SOURCE LINE 83
        if thing.show_unmarknsfw:
            # SOURCE LINE 84
            __M_writer(u'    <li>')
            __M_writer(conditional_websafe(ynbutton(_("un-nsfw"), _("unmarked"), "unmarknsfw", event_action='unmarknsfw')))
            __M_writer(u'</li>\n')
        # SOURCE LINE 86
        if not getattr(thing, 'promoted', None) and thing.show_flair:
            # SOURCE LINE 87
            __M_writer(u'    <li>\n      <a class="flairselectbtn access-required" href="javascript://void(0)"\n         data-event-action="editflair" data-event-detail="set">')
            # SOURCE LINE 89
            __M_writer(conditional_websafe(_('flair')))
            __M_writer(u'</a>\n      <div class="flairselector drop-choices"></div>\n    </li>\n')
        # SOURCE LINE 93
        if thing.show_rescrape:
            # SOURCE LINE 94
            __M_writer(u'    <li>')
            __M_writer(conditional_websafe(ynbutton(_("retry thumb"), _("check back in a few minutes"), "rescrape",
            event_action="retry_thumbnail")))
            # SOURCE LINE 95
            __M_writer(u'</li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_give_gold(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7a2aa10')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data', u'error_field'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 210
        __M_writer(u'\n')
        # SOURCE LINE 211
        if thing.show_givegold:
            # SOURCE LINE 212
            __M_writer(u'    <li class="give-gold-button">\n    <a href="/gold?goldtype=gift&months=1&thing=')
            # SOURCE LINE 213
            __M_writer(conditional_websafe(thing.thing._fullname))
            __M_writer(u'"\n        title="')
            # SOURCE LINE 214
            __M_writer(conditional_websafe(_("give reddit gold in appreciation of this post.")))
            __M_writer(u'"\n        class="give-gold login-required access-required"\n        data-event-action="gild"\n        >')
            # SOURCE LINE 217
            __M_writer(conditional_websafe(_("give gold")))
            __M_writer(u'</a>\n    </li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_simple_button(context,title,nameFunc,css_class='',event_action=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7a2aa10')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data', u'error_field'])
        __M_writer = context.writer()
        # SOURCE LINE 734
        __M_writer(u'\n <a class="')
        # SOURCE LINE 735
        __M_writer(conditional_websafe(css_class))
        __M_writer(u'" href="javascript:void(0)" \n')
        # SOURCE LINE 736
        if event_action:
            # SOURCE LINE 737
            __M_writer(u'      data-event-action="')
            __M_writer(conditional_websafe(event_action))
            __M_writer(u'"\n')
        # SOURCE LINE 739
        __M_writer(u'    onclick="return ')
        __M_writer(conditional_websafe(nameFunc))
        __M_writer(u'(this)">')
        __M_writer(conditional_websafe(title))
        __M_writer(u'</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_distinguish_noop(context,text):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7a2aa10')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data', u'error_field'])
        __M_writer = context.writer()
        # SOURCE LINE 106
        __M_writer(u'\n  <a class="access-required"\n     href="javascript:void(0)"\n     onclick="return toggle_distinguish_span(this)">')
        # SOURCE LINE 109
        __M_writer(conditional_websafe(text))
        __M_writer(u'</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_distinguish(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7a2aa10')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data', u'error_field'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        def undistinguish_options():
            return render_undistinguish_options(context)
        def distinguish_options():
            return render_distinguish_options(context)
        def distinguish_label(distinguish_clicked):
            return render_distinguish_label(context,distinguish_clicked)
        __M_writer = context.writer()
        # SOURCE LINE 182
        __M_writer(u'\n')
        # SOURCE LINE 183
        if thing.show_distinguish:
            # SOURCE LINE 184
            __M_writer(u'  <li class="toggle">\n    <form method="post" action="/post/distinguish">\n      <input type="hidden" value="')
            # SOURCE LINE 186
            __M_writer(conditional_websafe(c.profilepage))
            __M_writer(u'" name="profilepage">\n')
            # SOURCE LINE 187
            if thing.show_sticky_comment:
                # SOURCE LINE 188
                __M_writer(u'      <input type="hidden" value="false" name="sticky">\n')
            # SOURCE LINE 190
            if thing.distinguished:
                # SOURCE LINE 191
                __M_writer(u'        <input type="hidden" value="')
                __M_writer(conditional_websafe(_('undistinguishing...')))
                __M_writer(u'" name="executed"/>\n')
                # SOURCE LINE 192
            else:
                # SOURCE LINE 193
                __M_writer(u'        <input type="hidden" value="')
                __M_writer(conditional_websafe(_('distinguishing...')))
                __M_writer(u'" name="executed"/>\n')
            # SOURCE LINE 195
            __M_writer(u'\n      ')
            # SOURCE LINE 196
            __M_writer(conditional_websafe(distinguish_label(not thing.distinguished)))
            __M_writer(u'\n\n      <span class="option error">\n')
            # SOURCE LINE 199
            if thing.distinguished:
                # SOURCE LINE 200
                __M_writer(u'          ')
                __M_writer(conditional_websafe(undistinguish_options()))
                __M_writer(u'\n')
                # SOURCE LINE 201
            else:
                # SOURCE LINE 202
                __M_writer(u'          ')
                __M_writer(conditional_websafe(distinguish_options()))
                __M_writer(u'\n')
            # SOURCE LINE 204
            __M_writer(u'      </span>\n    </form>\n  </li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


