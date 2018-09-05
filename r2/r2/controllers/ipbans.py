import urllib
from pylons import request
from pylons import app_globals as g
from reddit_base import RedditController
from r2.lib.pages import AdminPage, AdminIpBans
from r2.lib.validator import *

class IpBansController(RedditController):

    @validate(VAdmin())
    def GET_index(self):
        res = AdminPage(content = AdminIpBans(), title = '[ADMIN] IP Bans').render()
        return res