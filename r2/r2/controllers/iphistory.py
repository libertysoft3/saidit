import urllib
from pylons import request
from pylons import app_globals as g
from reddit_base import RedditController
from r2.lib.pages import AdminPage, AdminIpHistory
from r2.lib.validator import *

class IpHistoryController(RedditController):

    @validate(
        VAdmin(),
        username=nop('username'),
    )
    def GET_index(self, username):
        if username:
            username = urllib.unquote_plus(username)
            user = Account._by_name(username, True) # allow deleted
            if user:
                res = AdminPage(content = AdminIpHistory(user), title = '[ADMIN] IP History').render()
                return res

        res = AdminPage(content = 'ERROR - user does not exist', title = '[ADMIN] IP History').render()
        return res

