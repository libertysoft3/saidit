from pylons import config
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import N_

from urllib import quote

from r2.lib.wrapped import Templated



# Note: User and subreddit chat preferences have already been checked in pages.py
class SidebarChat(Templated):

    # NOTE: system is 'subreddit'
    def __init__(self, system, subject):
        self.chat_client = g.live_config['chat_client']
        self.chat_client_url = g.live_config['chat_client_url']
        self.chat_username = g.live_config['chat_default_username']
        self.chat_password = self.chat_username # default password for old users who have null IRC password preference field set, or if they clear it
        self.chat_subreddit = subject
        self.user_is_loggedin = c.user_is_loggedin

        self.chat_channel = quote(g.live_config['chat_channel_name_prefix'] + subject + g.live_config['chat_channel_name_suffix'])

        if c.user_is_loggedin:
            self.chat_username = c.user.name
            if c.user.pref_irc_username and len(c.user.pref_irc_username) > 0:
                self.chat_username = c.user.pref_irc_username
            self.chat_password = self.chat_username # still a default password
            if c.user.pref_irc_password and len(c.user.pref_irc_password) > 0:
                self.chat_password = c.user.pref_irc_password

        Templated.__init__(self)