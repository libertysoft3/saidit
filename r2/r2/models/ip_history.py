#
# The Original Code is saidit.
#
###############################################################################
from pylons import app_globals as g
import r2.lib.db.thing as thing
from r2.lib.db.queries import *
from r2.models import wiki
from r2.models.ip import IPsByAccount, AccountsByIP

class IpHistory(object):

    @classmethod
    def _ips_by_user(cls, user=None):
        lookback = 100
        ips = []

        # TODO: get working, see set_account_ip()
        # ips = IPsByAccount.get(user._id, column_count=1000)
        # g.log.warning("!!! IPsByAccount %s" % ips)

        # account
        ips.append({"ip": user.registration_ip, "date": user._date, "type":"account"})

        # comments
        q = Comment._query(Comment.c.author_id == user._id, sort=desc('_date'))
        q._limit = lookback
        result = list(q)
        seen = []
        for item in result:
            if len(item.ip) > 0 and item.ip not in seen:
                seen.append(item.ip)
                ips.append({"ip": item.ip, "date": item._date, "type":"comment"})

        # links
        q = Link._query(Link.c.author_id == user._id, sort=desc('_date'))
        q._limit = lookback
        result = list(q)
        seen = []
        for item in result:
            if len(item.ip) > 0 and item.ip not in seen:
                seen.append(item.ip)
                ips.append({"ip": item.ip, "date": item._date, "type":"link"})

        # subs
        q = Subreddit._query(Subreddit.c.author_id == user._id, sort=desc('_date'))
        q._limit = lookback
        result = list(q)
        seen = []
        for item in result:
            if len(item.ip) > 0 and item.ip not in seen:
                seen.append(item.ip)
                ips.append({"ip": item.ip, "date": item._date, "type":"sub"})

        # messages
        q = Message._query(Message.c.author_id == user._id, sort=desc('_date'))
        q._limit = lookback
        result = list(q)
        seen = []
        for item in result:
            if len(item.ip) > 0 and item.ip not in seen:
                seen.append(item.ip)
                ips.append({"ip": item.ip, "date": item._date, "type":"message"})

        # sort results by date
        ips = sorted(ips, key=lambda k: k['date'], reverse=True)

        return ips
