
from pylons import request
from pylons import app_globals as g
from reddit_base import RedditController
from r2.lib.pages import AdminPage, AdminGlobalUserBans
from r2.lib.validator import *

class GlobalUserBansController(RedditController):

    @validate(VAdmin())
    def GET_index(self):
        res = AdminPage(content = AdminGlobalUserBans(), title = '[ADMIN] Global Bans').render()
        return res

