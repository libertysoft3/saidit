from pylons import app_globals as g

from r2.lib.db.operators import asc, desc, lower
from r2.lib.db.thing import Thing, Relation, NotFound
from r2.lib.memoize import memoize

class GlobalBan(Thing):
    _cache = g.thingcache
    _essentials = ('user_id', ) # wow python

    @classmethod
    def _cache_prefix(cls):
        return "globalban:"

    # TODO - method named all wrong, theres a limit of 5000
    @classmethod
    @memoize('globalban.all_global_bans')
    def _all_global_bans_cache(cls):
        # g.log.warning("!!! dbg: _all_global_bans_cache was flushed, running a db query")
        return [ a._id for a in GlobalBan._query(sort=desc('_date'), limit=5000) ]

    @classmethod
    def _all_global_bans(cls, _update=False):
        all = GlobalBan._all_global_bans_cache(_update=_update)
        # "Can't just return Award._byID() results because the ordering will be lost"
        d = GlobalBan._byID(all, data=True)
        return [ d[id] for id in all ]

    # NOTE: THIS SPECIFIES THE DATA MODEL
    @classmethod
    def _new(cls, user_id, notes=''):
        a = GlobalBan(user_id=user_id, notes=notes)
        a._commit()
        GlobalBan._all_global_bans_cache(_update=True)
        GlobalBan._all_banned_users_cache(_update=True)

    @classmethod
    def _by_user_id(cls, user_id):
        q = cls._query(GlobalBan.c.user_id == user_id)
        q._limit = 1
        globalbans = list(q)

        if globalbans:
            return cls._byID(globalbans[0]._id, True)
        else:
            raise NotFound, 'GlobalBan for user %s' % user_id

    @classmethod
    @memoize('globalban.all_banned_users')
    def _all_banned_users_cache(cls):
        # g.log.warning("!!! dbg: _all_banned_users_cache was flushed, running a db query")
        return [ a.user_id for a in GlobalBan._query() ]

    # TODO - with enough globally banned users, this will no longer be performant. Move ban state to being an Account attribute.
    @classmethod
    def _user_banned(self, user_id):
        if user_id and user_id > 0:
            # g.log.warning("!!! _user_banned() have cached banned users %s" % str(GlobalBan._all_banned_users_cache(_update=False)))
            return user_id in GlobalBan._all_banned_users_cache(_update=False)
        return False


