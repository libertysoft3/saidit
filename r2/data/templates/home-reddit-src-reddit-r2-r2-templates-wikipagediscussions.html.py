# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1506018968.207753
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/wikipagediscussions.html'
_template_uri = '/wikipagediscussions.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23

from r2.lib.template_helpers import get_domain


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        thing = context.get('thing', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'\n\n')
        # SOURCE LINE 27
        __M_writer(conditional_websafe(thing.listing))
        __M_writer(u'\n\n<div class="morelink discussionlink">\n<a class="access-required"\n   href="/submit?url=')
        # SOURCE LINE 31
        __M_writer(conditional_websafe(g.default_scheme))
        __M_writer(u'://')
        __M_writer(conditional_websafe(get_domain()))
        __M_writer(u'/wiki/')
        __M_writer(conditional_websafe(thing.page))
        __M_writer(u'&resubmit=true&no_self=true&title=Check+out+this+wiki+page"\n   type="subreddit"\n   data-event-action="submit"\n   data-event-detail="link"\n>')
        # SOURCE LINE 35
        __M_writer(conditional_websafe(_("submit a discussion")))
        __M_writer(u'\n<div class="nub"></div>\n</a>\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


