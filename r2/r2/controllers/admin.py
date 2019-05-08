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