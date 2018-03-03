# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505002596.226608
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/searchform.html'
_template_uri = '/searchform.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['search_faq']


# SOURCE LINE 23

from r2.config import feature
from r2.models.subreddit import DefaultSR, AllSR
from r2.lib.template_helpers import add_sr, static


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        thing = context.get('thing', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        dict = context.get('dict', UNDEFINED)
        def search_faq():
            return render_search_faq(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 27
        __M_writer(u'\n\n')
        # SOURCE LINE 55
        __M_writer(u'\n\n<form action="')
        # SOURCE LINE 57
        __M_writer(conditional_websafe(add_sr(thing.search_path)))
        __M_writer(u'" id="search" role="search">\n  <input type="text" \n')
        # SOURCE LINE 59
        if thing.prev_search:
            # SOURCE LINE 60
            __M_writer(u'           value="')
            __M_writer(conditional_websafe(thing.prev_search))
            __M_writer(u'" style="color:black"\n')
        # SOURCE LINE 62
        __M_writer(u'         name="q" placeholder="')
        __M_writer(conditional_websafe(_('search')))
        __M_writer(u'" tabindex="20">\n\n')
        # SOURCE LINE 64
        if feature.is_enabled('legacy_search') or c.user.pref_legacy_search or thing.simple:
            # SOURCE LINE 65
            __M_writer(u'    <input type="submit" value="" tabindex="22">\n')
            # SOURCE LINE 66
        else:
            # SOURCE LINE 67
            __M_writer(u'    <button class="search-submit-button c-btn c-btn-primary" type=\'submit\' aria-label="')
            __M_writer(conditional_websafe(_("Search")))
            __M_writer(u'">\n      <span class="search-icon"></span>\n    </button>\n')
        # SOURCE LINE 71
        __M_writer(u'\n')
        # SOURCE LINE 72
        if thing.subreddit_search:
            # SOURCE LINE 73
            if thing.over18_url and thing.prev_search:
                # SOURCE LINE 74
                __M_writer(u'      <p><a id="search_over18" href="')
                __M_writer(conditional_websafe(thing.over18_url))
                __M_writer(u'" rel="nofollow">')
                __M_writer(conditional_websafe(_('enable NSFW results')))
                __M_writer(u'</a></p>\n')
            # SOURCE LINE 76
        elif thing.simple:
            # SOURCE LINE 77
            __M_writer(u'  <div id="searchexpando" class="infobar">\n')
            # SOURCE LINE 78
            if not isinstance(c.site, (DefaultSR, AllSR)):
                # SOURCE LINE 79
                __M_writer(u'      <label><input type="checkbox" name="restrict_sr" tabindex="21">')
                __M_writer(conditional_websafe(_('limit my search to %(path)s') % dict(path=c.site.path.rstrip('/'))))
                __M_writer(u'</label>\n')
            # SOURCE LINE 81
            __M_writer(u'    ')
            __M_writer(conditional_websafe(search_faq()))
            __M_writer(u'\n  </div>\n')
            # SOURCE LINE 83
        else:
            # SOURCE LINE 84
            if not thing.site or isinstance(thing.site, (DefaultSR, AllSR)):
                # SOURCE LINE 85
                __M_writer(u'      <input type="hidden" name="restrict_sr">\n')
                # SOURCE LINE 86
            else:
                # SOURCE LINE 87
                __M_writer(u'      <label><input type="checkbox" ')
                __M_writer(conditional_websafe('checked="checked"' if thing.restrict_sr else ''))
                __M_writer(u' name="restrict_sr" tabindex="21">\n      ')
                # SOURCE LINE 88
                __M_writer(conditional_websafe(_('limit my search to %(path)s') % dict(path=thing.site.path.rstrip('/'))))
                __M_writer(u'</label>\n')
            # SOURCE LINE 90
            __M_writer(u'    ')
            __M_writer(conditional_websafe(search_faq()))
            __M_writer(u'\n')
        # SOURCE LINE 92
        __M_writer(u'\n')
        # SOURCE LINE 93
        for k, v in thing.search_params.iteritems():
            # SOURCE LINE 94
            __M_writer(u'    <input type="hidden" name="')
            __M_writer(conditional_websafe(k))
            __M_writer(u'" value="')
            __M_writer(conditional_websafe(v))
            __M_writer(u'">\n')
        # SOURCE LINE 96
        __M_writer(u'</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_search_faq(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 29
        __M_writer(u'\n  <div id="moresearchinfo">\n  <p>use the following search parameters to narrow your results:</p>\n\n  <dl>\n      <dt>subreddit:<i>subreddit</i></dt>\n      <dd>')
        # SOURCE LINE 35
        __M_writer(conditional_websafe(_('find submissions in "subreddit"')))
        __M_writer(u'</dd>\n      <dt>author:<i>username</i></dt>\n      <dd>')
        # SOURCE LINE 37
        __M_writer(conditional_websafe(_('find submissions by "username"')))
        __M_writer(u'</dd>\n      <dt>site:<i>example.com</i></dt>\n      <dd>')
        # SOURCE LINE 39
        __M_writer(conditional_websafe(_('find submissions from "example.com"')))
        __M_writer(u'</dd>\n      <dt>url:<i>text</i></dt>\n      <dd>')
        # SOURCE LINE 41
        __M_writer(conditional_websafe(_('search for "text" in url')))
        __M_writer(u'</dd>\n      <dt>selftext:<i>text</i></dt>\n      <dd>')
        # SOURCE LINE 43
        __M_writer(conditional_websafe(_('search for "text" in self post contents')))
        __M_writer(u'</dd>\n      <dt>self:yes (or self:no)</dt>\n      <dd>')
        # SOURCE LINE 45
        __M_writer(conditional_websafe(_('include (or exclude) self posts')))
        __M_writer(u'</dd>\n      <dt>nsfw:yes (or nsfw:no)</dt>\n      <dd>')
        # SOURCE LINE 47
        __M_writer(conditional_websafe(_('include (or exclude) results marked as NSFW')))
        __M_writer(u'</dd>\n  </dl>\n\n  <p>e.g.&#32;<code>subreddit:aww site:imgur.com dog</code></p>\n  <p><a href="https://www.reddit.com/wiki/search">')
        # SOURCE LINE 51
        __M_writer(conditional_websafe(_('see the search faq for details.')))
        __M_writer(u'</a></p>\n  </div>\n\n  <p><a href="https://www.reddit.com/wiki/search" id="search_showmore">')
        # SOURCE LINE 54
        __M_writer(conditional_websafe(_('advanced search: by author, subreddit...')))
        __M_writer(u'</a></p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


