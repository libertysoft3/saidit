# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1517560352.470608
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/preffeeds.html'
_template_uri = '/preffeeds.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['feedbuttons']


# SOURCE LINE 23

from r2.models import make_feedurl
from r2.lib.template_helpers import get_domain
from r2.lib.filters import safemarkdown

# CUSTOM: bugfix
from r2.config import feature


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 30
        __M_writer(u'\n<div class="instructions private-feeds">\n<h1>')
        # SOURCE LINE 32
        __M_writer(conditional_websafe(_("Private RSS feeds")))
        __M_writer(u'</h1>\n\n')
        # SOURCE LINE 34
        __M_writer(conditional_websafe(unsafe(safemarkdown(_("On this page are links to private RSS feeds so that you can get listings of your content (personalized front page, message panel, saved listing, etc.) without having to deal with cookies or other auth.")))))
        __M_writer(u'\n')
        # SOURCE LINE 35
        __M_writer(conditional_websafe(unsafe(safemarkdown(_("Keep in mind that these urls are intended to be private, so **share at your own risk.**")))))
        __M_writer(u'\n')
        # SOURCE LINE 36
        __M_writer(conditional_websafe(unsafe(safemarkdown(_("All feeds are invalidated if you change your password, however.")))))
        __M_writer(u'\n\n')
        # SOURCE LINE 51
        __M_writer(u'\n\n<table class="preftable">\n  <tr>\n    <th>private listings</th>\n    <td class="prefright">\n      ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 57
            __M_writer(conditional_websafe(self.feedbuttons(path=u'/')))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n      ')
        # SOURCE LINE 58
        __M_writer(conditional_websafe(_("your front page")))
        __M_writer(u'\n      <br/>\n      ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 60
            __M_writer(conditional_websafe(self.feedbuttons(path=u'/saved')))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n      ')
        # SOURCE LINE 61
        __M_writer(conditional_websafe(_("your saved links")))
        __M_writer(u'\n    </td>\n  </tr>\n  <tr>\n    <th>private profile pages</th>\n    <td class="prefright">\n      ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 67
            __M_writer(conditional_websafe(self.feedbuttons(path=u'/user/' + (c.user.name) + u'/upvoted')))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n      ')
        # SOURCE LINE 68
        __M_writer(conditional_websafe(_("links you've upvoted")))
        __M_writer(u'\n      <br/>\n      ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 70
            __M_writer(conditional_websafe(self.feedbuttons(path=u'/user/' + (c.user.name) + u'/downvoted')))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n      ')
        # SOURCE LINE 71
        __M_writer(conditional_websafe(_("links you've downvoted")))
        __M_writer(u'\n      <br/>\n      ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 73
            __M_writer(conditional_websafe(self.feedbuttons(path=u'/user/' + (c.user.name) + u'/hidden')))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n      ')
        # SOURCE LINE 74
        __M_writer(conditional_websafe(_("links you've hidden")))
        __M_writer(u'\n    </td>\n  </tr>\n   <tr>\n    <th>your inbox</th>\n    <td class="prefright">\n      ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 80
            __M_writer(conditional_websafe(self.feedbuttons(path=u'/message/inbox/')))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n      ')
        # SOURCE LINE 81
        __M_writer(conditional_websafe(_("everything")))
        __M_writer(u'\n      <br/>\n      ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 83
            __M_writer(conditional_websafe(self.feedbuttons(path=u'/message/unread/')))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n      ')
        # SOURCE LINE 84
        __M_writer(conditional_websafe(_("unread messages")))
        __M_writer(u'\n      <br/>\n      ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 86
            __M_writer(conditional_websafe(self.feedbuttons(path=u'/message/messages/')))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n      ')
        # SOURCE LINE 87
        __M_writer(conditional_websafe(_("messages only")))
        __M_writer(u'\n      <br/>\n      ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 89
            __M_writer(conditional_websafe(self.feedbuttons(path=u'/message/comments/')))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n      ')
        # SOURCE LINE 90
        __M_writer(conditional_websafe(_("comment replies only")))
        __M_writer(u'\n      <br/>\n      ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 92
            __M_writer(conditional_websafe(self.feedbuttons(path=u'/message/selfreply')))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n      ')
        # SOURCE LINE 93
        __M_writer(conditional_websafe(_("self-post replies only")))
        __M_writer(u'\n      <br>\n      ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 95
            __M_writer(conditional_websafe(self.feedbuttons(path=u'/message/mentions')))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n      ')
        # SOURCE LINE 96
        __M_writer(conditional_websafe(_("mentions of your username only")))
        __M_writer(u'\n    </td>\n   </tr>\n')
        # SOURCE LINE 99
        if c.user.is_moderator_somewhere:
            # SOURCE LINE 100
            __M_writer(u'   <tr>\n    <th>your moderator inbox</th>\n    <td class="prefright">\n      ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 103
                __M_writer(conditional_websafe(self.feedbuttons(path=u'/message/moderator/inbox/')))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n      ')
            # SOURCE LINE 104
            __M_writer(conditional_websafe(_("everything")))
            __M_writer(u'\n      <br/>\n      ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 106
                __M_writer(conditional_websafe(self.feedbuttons(path=u'/message/moderator/unread/')))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n      ')
            # SOURCE LINE 107
            __M_writer(conditional_websafe(_("unread messages")))
            __M_writer(u'\n    </td>\n  </tr>\n  <tr>\n    <th>moderator listings</th>\n    <td class="prefright">\n      ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 113
                __M_writer(conditional_websafe(self.feedbuttons(path=u'/r/mod/about/modqueue/')))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n      ')
            # SOURCE LINE 114
            __M_writer(conditional_websafe(_("modqueue")))
            __M_writer(u'\n      <br/>\n      ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 116
                __M_writer(conditional_websafe(self.feedbuttons(path=u'/r/mod/about/reports/')))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n      ')
            # SOURCE LINE 117
            __M_writer(conditional_websafe(_("reports")))
            __M_writer(u'\n      <br/>\n      ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 119
                __M_writer(conditional_websafe(self.feedbuttons(path=u'/r/mod/about/spam/')))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n      ')
            # SOURCE LINE 120
            __M_writer(conditional_websafe(_("spam")))
            __M_writer(u'\n      <br/>\n      ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 122
                __M_writer(conditional_websafe(self.feedbuttons(path=u'/r/mod/about/edited/')))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n      ')
            # SOURCE LINE 123
            __M_writer(conditional_websafe(_("edited")))
            __M_writer(u'\n      <br/>\n      ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 125
                __M_writer(conditional_websafe(self.feedbuttons(path=u'/r/mod/about/log/')))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n      ')
            # SOURCE LINE 126
            __M_writer(conditional_websafe(_("moderation log")))
            __M_writer(u'\n      <br/>\n      ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 128
                __M_writer(conditional_websafe(self.feedbuttons(path=u'/r/mod/about/unmoderated/')))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n      ')
            # SOURCE LINE 129
            __M_writer(conditional_websafe(_("unmoderated posts")))
            __M_writer(u'\n    </td>\n  </tr>\n')
        # SOURCE LINE 133
        __M_writer(u'</table>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_feedbuttons(context,path):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 38
        __M_writer(u'\n')
        # SOURCE LINE 39

        domain = get_domain(subreddit = False)
        scheme = "https" if feature.is_enabled("force_https") else "http"
         
        
        # SOURCE LINE 42
        __M_writer(u'\n  <a class="feedlink rss-link"\n     href="')
        # SOURCE LINE 44
        __M_writer(conditional_websafe(scheme))
        __M_writer(u'://')
        __M_writer(conditional_websafe(domain))
        __M_writer(conditional_websafe(make_feedurl(c.user, path, 'rss')))
        __M_writer(u'">\n    RSS\n  </a>\n  <a class="feedlink json-link"\n     href="')
        # SOURCE LINE 48
        __M_writer(conditional_websafe(scheme))
        __M_writer(u'://')
        __M_writer(conditional_websafe(domain))
        __M_writer(conditional_websafe(make_feedurl(c.user, path, 'json')))
        __M_writer(u'">\n    JSON\n  </a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


