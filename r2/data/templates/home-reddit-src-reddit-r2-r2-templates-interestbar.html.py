# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505002596.390495
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/interestbar.html'
_template_uri = '/interestbar.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        thing = context.get('thing', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n<div class="sr-interest-bar">\n  <div class="bubble">\n    ')
        # SOURCE LINE 25

        if thing.has_subscribed:
            msg = _("ready for something new? %s subscribe %s to some new subs.")
        else:
            msg = _("it looks like you haven't %s subscribed %s to any subreddits yet. want some ideas?")
        
        pre, sub, post = msg.split("%s")
            
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['msg','pre','post','sub'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 32
        __M_writer(u'\n    <p class="caption">')
        # SOURCE LINE 33
        __M_writer(conditional_websafe(pre))
        __M_writer(u'&#32;<span class="subscribe">')
        __M_writer(conditional_websafe(sub))
        __M_writer(u'</span>&#32;')
        __M_writer(conditional_websafe(post))
        __M_writer(u'</p>\n    <p class="error-caption"></p>\n    <div class="query-box"><input class="query" placeholder="')
        # SOURCE LINE 35
        __M_writer(conditional_websafe(_('what are you interested in?')))
        __M_writer(u'"><div class="throbber"></div></div>\n    <ul class="results">\n      <li>')
        # SOURCE LINE 37
        __M_writer(conditional_websafe(_('try these:')))
        __M_writer(u'</li>\n      <li>\n        <a href="/r/random" class="random" target="_blank">\n          <span class="name">')
        # SOURCE LINE 40
        __M_writer(conditional_websafe(_("serendipity")))
        __M_writer(u'</span>\n        </a>\n      </li>\n    </ul>\n  </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


