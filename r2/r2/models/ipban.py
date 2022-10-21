from pylons import app_globals as g

from r2.lib.db.operators import asc, desc, lower
from r2.lib.db.thing import Thing, Relation, NotFound
from r2.lib.memoize import memoize

class IpBan(Thing):
    _cache = g.thingcache
    _essentials = ('ip', ) # wow python
    _defaults = dict(level=4, # 1 = new accounts banned,
                              # 2 = all accounts banned,
                              # 3 = all accounts banned retroactively,
                              # 4 = access entirely blocked (default because this is the original IP ban)
    )
    _data_int_props = Thing._data_int_props + ('level', )

    @classmethod
    def _cache_prefix(cls):
        return "ipban:"

    # NOTE: THIS SPECIFIES THE DATA MODEL
    @classmethod
    def _new(cls, ip, level=1, notes=''):
        a = IpBan(ip=ip, level=level, notes=notes)
        a._commit()
        IpBan._all_bans_cache(_update=True)

    @classmethod
    @memoize('ipban.all_bans')
    def _all_bans_cache(cls):
        return [ a._id for a in IpBan._query(sort=desc('_date'), limit=10000) ]

    @classmethod
    def _all_bans(cls, _update=False):
        all = IpBan._all_bans_cache(_update=_update)
        # "Can't just return Award._byID() results because the ordering will be lost"
        d = IpBan._byID(all, data=True)
        return [ d[id] for id in all ]

    @classmethod
    def _all_banned_ips(cls, _update=False):
        all = IpBan._all_bans_cache(_update=_update)
        d = IpBan._byID(all, data=True)
        return [ d[id].ip for id in all ]

    @classmethod
    def _by_ip(cls, ip):
        q = cls._query(IpBan.c.ip == ip)
        q._limit = 1
        ipbans = list(q)
        if ipbans:
            return cls._byID(ipbans[0]._id, True)
        else:
            raise NotFound, 'IpBan for ip %s' % ip
