import urllib
from pylons import request
from pylons import app_globals as g
from reddit_base import RedditController
from r2.lib.pages import AdminPage, AdminGlobalUserBans
from r2.lib.validator import *

class GlobalUserBansController(RedditController):

    @validate(
        VAdmin(),
        recipient=nop('recipient'),
    )
    def GET_index(self, recipient):
        if recipient:
            recipient = urllib.unquote_plus(recipient)
        else:
            recipient = None
        res = AdminPage(content = AdminGlobalUserBans(recipient=recipient), title = '[ADMIN] Global User Bans').render()
        return res

