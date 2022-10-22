# The contents of this file are subject to the Common Public Attribution
# License Version 1.0. (the "License"); you may not use this file except in
# compliance with the License. You may obtain a copy of the License at
# http://code.reddit.com/LICENSE. The License is based on the Mozilla Public
# License Version 1.1, but Sections 14 and 15 have been added to cover use of
# software over a computer network and provide for limited attribution for the
# Original Developer. In addition, Exhibit A has been modified to be consistent
# with Exhibit B.
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License for
# the specific language governing rights and limitations under the License.
#
# The Original Code is reddit.
#
# The Original Developer is the Initial Developer.  The Initial Developer of
# the Original Code is reddit Inc.
#
# All portions of the code written by reddit are Copyright (c) 2006-2015 reddit
# Inc. All Rights Reserved.
###############################################################################

from reddit_base import RedditController
from r2.lib.pages import AdminPage, AdminCreddits, AdminGold
from r2.lib.validator import *
from pylons import app_globals as g

class AdminToolController(RedditController):
    @validate(
        VAdmin(),
        recipient=nop('recipient'),
    )
    def GET_creddits(self, recipient):
        return AdminPage(content=AdminCreddits(recipient)).render()

    @validate(
        VAdmin(),
        recipient=nop('recipient'),
    )
    def GET_gold(self, recipient):
        return AdminPage(content=AdminGold(recipient)).render()

    @validatedForm(
        VAdmin(),
        VModhash(),
        thing=VByName('thing'),
        system=VLength('system', 1024),
        message=VLength('message', 10000),
    )
    def POST_add_ban_message(self, form, jquery, thing, system, message):
        if form.has_errors(('thing', 'system', 'message'),
                           errors.TOO_LONG):
            return

        from r2.models import admintools
        admintools.set_ban_message(thing, system, message)
        form.refresh()

    # CUSTOM: Shadowban
    @noresponse(
        VAdmin(),
        VModhash(),
        victim=VExistingUname("victim", allow_deleted=True),
        reverse=VBoolean("reverse")
    )
    def POST_ban_user(self, victim, reverse):
        if victim == None:
            return
        if reverse:
            victim._spam = False
        # Don't ban admins
        elif not victim.name in g.admins:
            victim._spam = True
        victim._commit()

    # CUSTOM: Ban account from logging in
    @noresponse(
        VAdmin(),
        VModhash(),
        victim=VExistingUname("victim", allow_deleted=True),
        reverse=VBoolean("reverse")
    )
    def POST_lock_user(self, victim, reverse):
        if victim == None:
            return
        if reverse:
            victim._banned = 0
        # Don't ban admins
        elif not victim.name in g.admins:
            victim._banned = 1
        # _commit() isn't necessary here, because setting _banned handles
        # everything

    # CUSTOM: Suspension w/ notification
    @validatedForm(
        VAdmin(),
        VModhash(),
        victim=VExistingUname("victim", allow_deleted=True),
        ban_reason=VLength('ban_reason', 100),
        duration=VInt('duration', min=1, max=999),
        ban_message=VMarkdownLength('ban_message', max_length=1000,
            empty_error=None)
    )
    def POST_suspend_user(self, form, jquery, victim, ban_reason, duration, ban_message):
        from datetime import datetime, timedelta
        from r2.models import bans
        from r2.lib.system_messages import send_suspension_message
        if form.has_errors("ban_reason", "ban_message", errors.TOO_LONG):
            return
        if victim == None:
            return
        if victim.name in g.admins:
            return
        victim.in_timeout = True
        victim._commit()
        if victim.timeout_expiration:
            TempTimeout.unschedule(victim)
        if duration:
            TempTimeout.schedule(victim, timedelta(days=duration))
        send_suspension_message(victim,
                                c.user,
                                ban_message,
                                duration,
                                ban_reason)
    @noresponse(
        VAdmin(),
        VModhash(),
        victim=VExistingUname("victim", allow_deleted=True)
    )
    def POST_unsuspend_user(self, victim):
        if victim == None:
            return
        victim.in_timeout = False
        victim._commit()
        if victim.timeout_expiration:
            TempTimeout.unschedule(victim)

    # CUSTOM: "Spiderban"
    @noresponse(
        VAdmin(),
        VModhash(),
        victim=VExistingUname("victim", allow_deleted=True),
        reverse=VBoolean("reverse")
    )
    def POST_spiderban_user(self, victim, reverse):
        if victim == None:
            return
        if reverse:
            victim.spiderbanned = False
        elif not victim.name in g.admins:
            victim.spiderbanned = True
        victim._commit()
