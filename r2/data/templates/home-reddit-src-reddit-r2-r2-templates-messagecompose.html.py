# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1508299777.220714
_enable_loop = True
_template_filename = u'/home/reddit/src/reddit/r2/r2/templates/messagecompose.html'
_template_uri = u'/messagecompose.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['subject_field', 'message_field', 'to_field', 'captcha_field', 'clippy_field']


# SOURCE LINE 26

import simplejson
from r2.lib import js
from r2.lib.pages import UserText
from r2.lib.template_helpers import static


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 24
    ns = runtime.TemplateNamespace(u'utils', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'utils')] = ns

    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7f4dec5c1910', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f4dec5c1910')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f4dec5c1910')._populate(_import_ns, [u'error_field', u'submit_form'])
        utils = _mako_get_namespace(context, 'utils')
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n')
        # SOURCE LINE 24
        __M_writer(u'\n\n')
        # SOURCE LINE 31
        __M_writer(u'\n\n')
        # SOURCE LINE 33
        __M_writer(conditional_websafe(unsafe(js.use("messagecompose"))))
        __M_writer(u'\n\n<h1>')
        # SOURCE LINE 35
        __M_writer(conditional_websafe(_("send a private message")))
        __M_writer(u'</h1>\n\n')
        def ccall(caller):
            def body():
                def subject_field():
                    return render_subject_field(context._locals(__M_locals))
                def message_field():
                    return render_message_field(context._locals(__M_locals))
                def to_field():
                    return render_to_field(context._locals(__M_locals))
                def captcha_field():
                    return render_captcha_field(context._locals(__M_locals))
                thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
                def clippy_field():
                    return render_clippy_field(context._locals(__M_locals))
                __M_writer = context.writer()
                # SOURCE LINE 39
                __M_writer(u'\n\n')
                # SOURCE LINE 41
                __M_writer(conditional_websafe(to_field()))
                __M_writer(u'\n')
                # SOURCE LINE 42
                __M_writer(conditional_websafe(subject_field()))
                __M_writer(u'\n')
                # SOURCE LINE 43
                __M_writer(conditional_websafe(message_field()))
                __M_writer(u'\n')
                # SOURCE LINE 44
                if thing.admin_check:
                    # SOURCE LINE 45
                    __M_writer(u'  ')
                    __M_writer(conditional_websafe(clippy_field()))
                    __M_writer(u'\n')
                # SOURCE LINE 47
                __M_writer(conditional_websafe(captcha_field()))
                __M_writer(u'\n<input type="hidden" name="source" value="compose">\n\n<button id="send" name="send" type="submit">')
                # SOURCE LINE 50
                __M_writer(conditional_websafe(_("send")))
                __M_writer(u'</button>\n<span class="status"></span>\n\n')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 37
            __M_writer(conditional_websafe(utils.submit_form(action=u'/message/compose',onsubmit=u"return post_form(this, 'compose', null, null, true)",method=u'post',_id=u'compose-message')))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 53
        __M_writer(u'\n\n\n')
        # SOURCE LINE 78
        __M_writer(u'\n\n')
        # SOURCE LINE 94
        __M_writer(u'\n\n')
        # SOURCE LINE 102
        __M_writer(u'\n\n')
        # SOURCE LINE 167
        __M_writer(u'\n\n')
        # SOURCE LINE 173
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_subject_field(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f4dec5c1910')._populate(_import_ns, [u'error_field', u'submit_form'])
        utils = _mako_get_namespace(context, 'utils')
        __M_writer = context.writer()
        # SOURCE LINE 80
        __M_writer(u'\n  <div class="spacer">\n    ')
        def ccall(caller):
            def body():
                thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
                error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
                __M_writer = context.writer()
                # SOURCE LINE 82
                __M_writer(u'\n')
                # SOURCE LINE 84
                __M_writer(u'      <select class="rule_subject" style="display:none">\n        <option value="" selected disabled class="blank"></option>\n        <option value="" class="other">Other</option>\n      </select>\n\n      <input type="text" name="subject" value="')
                # SOURCE LINE 89
                __M_writer(conditional_websafe(thing.subject or ''))
                __M_writer(u'"/>\n      ')
                # SOURCE LINE 90
                __M_writer(conditional_websafe(error_field("NO_SUBJECT", "subject", "span")))
                __M_writer(u'\n      ')
                # SOURCE LINE 91
                __M_writer(conditional_websafe(error_field("TOO_LONG", "subject", "span")))
                __M_writer(u'\n    ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 82
            __M_writer(conditional_websafe(utils.round_field(title=(_('subject')))))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 92
        __M_writer(u'\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_message_field(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f4dec5c1910')._populate(_import_ns, [u'error_field', u'submit_form'])
        utils = _mako_get_namespace(context, 'utils')
        __M_writer = context.writer()
        # SOURCE LINE 96
        __M_writer(u'\n  <div class="spacer">\n    ')
        def ccall(caller):
            def body():
                thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
                __M_writer = context.writer()
                # SOURCE LINE 98
                __M_writer(u'\n      ')
                # SOURCE LINE 99
                __M_writer(conditional_websafe(UserText(None, text=thing.message, have_form = False, creating = True)))
                __M_writer(u'\n    ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 98
            __M_writer(conditional_websafe(utils.round_field(title=(_('message')))))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 100
        __M_writer(u'\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_to_field(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f4dec5c1910')._populate(_import_ns, [u'error_field', u'submit_form'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        utils = _mako_get_namespace(context, 'utils')
        __M_writer = context.writer()
        # SOURCE LINE 56
        __M_writer(u'\n  <div class="spacer">\n')
        # SOURCE LINE 58
        if thing.restrict_recipient:
            # SOURCE LINE 59
            __M_writer(u'      ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    __M_writer(u'\n        <input type="text" class="access-required" name="to" value="')
                    # SOURCE LINE 60
                    __M_writer(conditional_websafe(g.admin_message_acct))
                    __M_writer(u'"\n               data-event-action="changerecipient" readonly />\n      ')
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 59
                __M_writer(conditional_websafe(utils.round_field(title=(_('to')))))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 62
            __M_writer(u'\n')
            # SOURCE LINE 63
        else:
            # SOURCE LINE 64
            __M_writer(u'      ')
            def ccall(caller):
                def body():
                    error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
                    __M_writer = context.writer()
                    # SOURCE LINE 65
                    __M_writer(u'\n        <input type="text" name="to" value="')
                    # SOURCE LINE 66
                    __M_writer(conditional_websafe(thing.to or ''))
                    __M_writer(u'"\n               onchange="')
                    # SOURCE LINE 67
                    __M_writer(conditional_websafe('admincheck(this)' if thing.admin_check else ''))
                    __M_writer(u'"/>\n        ')
                    # SOURCE LINE 68
                    __M_writer(conditional_websafe(error_field("NO_USER", "to")))
                    __M_writer(u'\n        ')
                    # SOURCE LINE 69
                    __M_writer(conditional_websafe(error_field("USER_DOESNT_EXIST", "to")))
                    __M_writer(u'\n        ')
                    # SOURCE LINE 70
                    __M_writer(conditional_websafe(error_field("SUBREDDIT_NOEXIST", "to")))
                    __M_writer(u'\n        ')
                    # SOURCE LINE 71
                    __M_writer(conditional_websafe(error_field("USER_BLOCKED", "to")))
                    __M_writer(u'\n        ')
                    # SOURCE LINE 72
                    __M_writer(conditional_websafe(error_field("USER_BLOCKED_MESSAGE", "to")))
                    __M_writer(u'\n        ')
                    # SOURCE LINE 73
                    __M_writer(conditional_websafe(error_field("USER_MUTED", "to")))
                    __M_writer(u'\n        ')
                    # SOURCE LINE 74
                    __M_writer(conditional_websafe(error_field("MUTED_FROM_SUBREDDIT", "to")))
                    __M_writer(u'\n      ')
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 64
                __M_writer(conditional_websafe(utils.round_field(description=(_('(username, or /r/name for that sub\'s moderators)')),title=(_('to')))))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 75
            __M_writer(u'\n')
        # SOURCE LINE 77
        __M_writer(u'  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_captcha_field(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f4dec5c1910')._populate(_import_ns, [u'error_field', u'submit_form'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 169
        __M_writer(u'\n  <div class="spacer">\n    ')
        # SOURCE LINE 171
        __M_writer(conditional_websafe(thing.captcha))
        __M_writer(u'\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_clippy_field(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f4dec5c1910')._populate(_import_ns, [u'error_field', u'submit_form'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 104
        __M_writer(u'\n  <script type="text/javascript">\n  function admincheck(elem) {\n    var admins = ')
        # SOURCE LINE 107
        __M_writer(conditional_websafe(unsafe(simplejson.dumps(thing.admins))))
        __M_writer(u';\n\n    if ($.inArray(elem.value, admins) >= 0) {\n      $(".admin-to").text(elem.value);\n      $(".clippy").show();\n    } else {\n      $(".clippy").hide();\n    }\n  }\n  </script>\n\n  <div class="clippy" ')
        # SOURCE LINE 118
        __M_writer(conditional_websafe("style='display:none'" if thing.to not in thing.admins else ""))
        __M_writer(u'>\n     <img src="')
        # SOURCE LINE 119
        __M_writer(conditional_websafe(static('alien-clippy.png')))
        __M_writer(u'" />\n     <div class="clippy-bubble">\n       <p class="clippy-headline">It looks like you\'re writing to an admin!</p>\n       <p>\n         Before you click "send", you might want to make sure that\n         &#32;\n         <span class="admin-to">')
        # SOURCE LINE 125
        __M_writer(conditional_websafe(thing.to))
        __M_writer(u'</span>\n         &#32;\n         is the right admin for the job.\n       </p>\n\n       <p>In many cases, there is probably a better alternative than messaging an individual admin:</p>\n\n       <ul>\n         <li>If you\'d like to message all the admins at once, send your message to the&#32;<a href="/message/compose?to=')
        # SOURCE LINE 133
        __M_writer(filters.url_escape(conditional_websafe(g.admin_message_acct)))
        __M_writer(u'">admin message list.</a></li>\n\n         <li>If you think your posts are being caught in the spam filter,\n           please write to\n           &#32;\n           <a href="https://www.reddit.com/wiki/faq#wiki_how_can_i_tell_who_moderates_a_given_subreddit.3F">\n            the moderators of the subreddit\n           </a>\n           &#32;\n           instead.\n         </li>\n\n         <li>If\n           &#32;\n           <span class="admin-to">')
        # SOURCE LINE 147
        __M_writer(conditional_websafe(thing.to))
        __M_writer(u'</span>\n           &#32;<i>is</i>&#32; a moderator of a specific subreddit you\'re\n           inquiring about, and that\'s actually the reason you\'re writing, please\n           message \n           &#32;\n           <a href="https://www.reddit.com/wiki/faq#wiki_how_can_i_tell_who_moderates_a_given_subreddit.3F">\n            all of the moderators of the subreddit\n           </a>\n           &#32; (using the "message the mods" feature located at the top of the\n           mod box) with a direct link to the comment page of the submission or other\n           reason you\'re writing about.\n         </li>\n\n         <li>If you\'re concerned that something is wrong with your entire account, please send your message to the admin list by \n           &#32;<a href="/message/compose?to=')
        # SOURCE LINE 161
        __M_writer(filters.url_escape(conditional_websafe(g.admin_message_acct)))
        __M_writer(u'">messaging all of the admins of ')
        __M_writer(conditional_websafe(g.admin_message_acct))
        __M_writer(u'</a>&#32;(It\'ll be dealt with faster).\n         </li>\n       </ul>\n    </div>\n    <br class="clear"/>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


