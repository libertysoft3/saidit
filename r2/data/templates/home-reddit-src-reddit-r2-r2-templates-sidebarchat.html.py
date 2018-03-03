# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1512370610.200401
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/sidebarchat.html'
_template_uri = '/sidebarchat.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        thing = context.get('thing', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<div class="spacer">\n')
        # SOURCE LINE 2
        if thing.chat_client == 'kiwiirc':
            # SOURCE LINE 3
            if thing.user_is_loggedin:
                # SOURCE LINE 4
                __M_writer(u'        <iframe class="chat-iframe kiwiirc" src="https://kiwiirc.com/client/irc.foonetic.net/?nick=')
                __M_writer(conditional_websafe(thing.chat_user))
                __M_writer(u'#')
                __M_writer(conditional_websafe(thing.chat_channel))
                __M_writer(u'"></iframe>\n')
                # SOURCE LINE 5
            else:
                # SOURCE LINE 6
                __M_writer(u'        <iframe class="chat-iframe kiwiirc" src="https://kiwiirc.com/client/irc.foonetic.net/?nick=')
                __M_writer(conditional_websafe(thing.chat_user))
                __M_writer(u'|?#')
                __M_writer(conditional_websafe(thing.chat_channel))
                __M_writer(u'"></iframe>\n')
            # SOURCE LINE 8
        elif thing.chat_client == 'thelounge':
            # SOURCE LINE 9
            if thing.user_is_loggedin:
                # SOURCE LINE 11
                __M_writer(u'        <a target="_blank" class="chat-link" href="')
                __M_writer(conditional_websafe(thing.chat_client_url))
                __M_writer(u'/?tls=true&lockchannel&autologin&user=')
                __M_writer(conditional_websafe(thing.chat_client_user))
                __M_writer(u'&al-password=')
                __M_writer(conditional_websafe(thing.chat_client_password))
                __M_writer(u'&autoconnect&nick=')
                __M_writer(conditional_websafe(thing.chat_user))
                __M_writer(u'&username=')
                __M_writer(conditional_websafe(thing.chat_user))
                __M_writer(u'&realname=')
                __M_writer(conditional_websafe(thing.chat_user))
                __M_writer(u'&join=')
                __M_writer(conditional_websafe(thing.chat_channel))
                __M_writer(u'">chat in new tab</a>\n        <iframe class="chat-iframe thelounge" src="')
                # SOURCE LINE 12
                __M_writer(conditional_websafe(thing.chat_client_url))
                __M_writer(u'/?tls=true&nofocus&lockchannel&autologin&user=')
                __M_writer(conditional_websafe(thing.chat_client_user))
                __M_writer(u'&al-password=')
                __M_writer(conditional_websafe(thing.chat_client_password))
                __M_writer(u'&autoconnect&nick=')
                __M_writer(conditional_websafe(thing.chat_user))
                __M_writer(u'&username=')
                __M_writer(conditional_websafe(thing.chat_user))
                __M_writer(u'&realname=')
                __M_writer(conditional_websafe(thing.chat_user))
                __M_writer(u'&join=')
                __M_writer(conditional_websafe(thing.chat_channel))
                __M_writer(u'"></iframe>\n')
                # SOURCE LINE 13
            else:
                # SOURCE LINE 15
                __M_writer(u'        <a target="_blank" class="chat-link" href="')
                __M_writer(conditional_websafe(thing.chat_client_url))
                __M_writer(u'/?tls=true&lockchannel&autologin&user=')
                __M_writer(conditional_websafe(thing.chat_client_user))
                __M_writer(u'&autoconnect&nick=')
                __M_writer(conditional_websafe(thing.chat_user))
                __M_writer(u'&username=')
                __M_writer(conditional_websafe(thing.chat_user))
                __M_writer(u'&realname=')
                __M_writer(conditional_websafe(thing.chat_user))
                __M_writer(u'&join=')
                __M_writer(conditional_websafe(thing.chat_channel))
                __M_writer(u'">chat in new tab</a>\n        <iframe class="chat-iframe thelounge" src="')
                # SOURCE LINE 16
                __M_writer(conditional_websafe(thing.chat_client_url))
                __M_writer(u'/?tls=true&nofocus&lockchannel&autologin&user=')
                __M_writer(conditional_websafe(thing.chat_client_user))
                __M_writer(u'&autoconnect&nick=')
                __M_writer(conditional_websafe(thing.chat_user))
                __M_writer(u'&username=')
                __M_writer(conditional_websafe(thing.chat_user))
                __M_writer(u'&realname=')
                __M_writer(conditional_websafe(thing.chat_user))
                __M_writer(u'&join=')
                __M_writer(conditional_websafe(thing.chat_channel))
                __M_writer(u'"></iframe>\n')
        # SOURCE LINE 19
        __M_writer(u'</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


