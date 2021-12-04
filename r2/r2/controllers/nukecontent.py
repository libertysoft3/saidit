import urllib
from pylons import request
from pylons import app_globals as g
from reddit_base import RedditController
from r2.lib.pages import AdminPage, AdminNukeContent
from r2.lib.validator import *

class NukeContentController(RedditController):

    @validate(
        VAdmin(),
        recipient=nop('recipient'),
    )
    def GET_index(self, recipient):
        if recipient:
            recipient = urllib.unquote_plus(recipient)
        else:
            recipient = None
        res = AdminPage(content = AdminNukeContent(recipient=recipient), title = '[ADMIN] Nuke User Content').render()
        return res

