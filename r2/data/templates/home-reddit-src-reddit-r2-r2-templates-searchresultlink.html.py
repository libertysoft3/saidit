# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505025479.217326
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/searchresultlink.html'
_template_uri = '/searchresultlink.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['search_result_content', 'search_result_body', 'search_result_css_class', 'search_result_footer', 'search_result_header', 'search_result_meta', 'flair']


# SOURCE LINE 28

from r2.lib.template_helpers import (
    format_html,
    format_number,
    get_linkflair_css_classes,
)
from r2.lib.pages import WrappedUser


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 25
    ns = runtime.TemplateNamespace('__anon_0x7fb21a5bb890', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fb21a5bb890')] = ns

    # SOURCE LINE 26
    ns = runtime.TemplateNamespace('__anon_0x7fb21a7bc690', context._clean_inheritance_tokens(), templateuri=u'link.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fb21a7bc690')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'searchresultbase.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fb21a5bb890')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'md', u'nsfw_stamp', u'quarantine_stamp', u'thumbnail_img'])
        _mako_get_namespace(context, '__anon_0x7fb21a7bc690')._populate(_import_ns, [u'thumbnail'])
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n')
        # SOURCE LINE 25
        __M_writer(u'\n')
        # SOURCE LINE 26
        __M_writer(u'\n\n')
        # SOURCE LINE 35
        __M_writer(u'\n\n')
        # SOURCE LINE 44
        __M_writer(u'\n\n')
        # SOURCE LINE 56
        __M_writer(u'\n\n')
        # SOURCE LINE 73
        __M_writer(u'\n\n')
        # SOURCE LINE 79
        __M_writer(u'\n\n')
        # SOURCE LINE 112
        __M_writer(u'\n\n')
        # SOURCE LINE 126
        __M_writer(u'\n\n')
        # SOURCE LINE 140
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_search_result_content(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fb21a5bb890')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'md', u'nsfw_stamp', u'quarantine_stamp', u'thumbnail_img'])
        _mako_get_namespace(context, '__anon_0x7fb21a7bc690')._populate(_import_ns, [u'thumbnail'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        thumbnail_img = _import_ns.get('thumbnail_img', context.get('thumbnail_img', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 46
        __M_writer(u'\n')
        # SOURCE LINE 47
        if thing.thumbnail:
            # SOURCE LINE 48
            __M_writer(u'    <a href="')
            __M_writer(conditional_websafe(thing.permalink))
            __M_writer(u'"\n       class="may-blank thumbnail ')
            # SOURCE LINE 49
            __M_writer(conditional_websafe(thing.thumbnail if thing.thumbnail_sprited else ''))
            __M_writer(u'">\n      ')
            # SOURCE LINE 50
            __M_writer(conditional_websafe(thumbnail_img(thing)))
            __M_writer(u'\n    </a>\n')
        # SOURCE LINE 53
        __M_writer(u'  <div>\n    ')
        # SOURCE LINE 54
        __M_writer(conditional_websafe(parent.search_result_content()))
        __M_writer(u'\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_search_result_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fb21a5bb890')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'md', u'nsfw_stamp', u'quarantine_stamp', u'thumbnail_img'])
        _mako_get_namespace(context, '__anon_0x7fb21a7bc690')._populate(_import_ns, [u'thumbnail'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 114
        __M_writer(u'\n')
        # SOURCE LINE 115
        if thing.selftext:
            # SOURCE LINE 116
            __M_writer(u'    <div class="search-expando collapsed">\n      ')
            def ccall(caller):
                def body():
                    md = _import_ns.get('md', context.get('md', UNDEFINED))
                    __M_writer = context.writer()
                    # SOURCE LINE 117
                    __M_writer(u'\n        ')
                    # SOURCE LINE 118
                    __M_writer(conditional_websafe(md(thing.selftext, wrap=True)))
                    __M_writer(u'\n      ')
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 117
                __M_writer(conditional_websafe(parent.search_result_body()))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 119
            __M_writer(u'\n    </div>\n    <div class="search-expando-button collapsed">\n      <span class="search-expando-button-label-collapsed">')
            # SOURCE LINE 122
            __M_writer(conditional_websafe(_("more")))
            __M_writer(u'</span>\n      <span class="search-expando-button-label-expanded">')
            # SOURCE LINE 123
            __M_writer(conditional_websafe(_("less")))
            __M_writer(u'</span>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_search_result_css_class(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fb21a5bb890')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'md', u'nsfw_stamp', u'quarantine_stamp', u'thumbnail_img'])
        _mako_get_namespace(context, '__anon_0x7fb21a7bc690')._populate(_import_ns, [u'thumbnail'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 37
        __M_writer(u'\n  ')
        # SOURCE LINE 38

        has_thumbnail_class = "has-thumbnail" if thing.thumbnail else ""
        linkflair_classes = get_linkflair_css_classes(thing)
        visited_class = 'visited' if thing.visited else ''
          
        
        # SOURCE LINE 42
        __M_writer(u'\n  ')
        # SOURCE LINE 43
        __M_writer(conditional_websafe(parent.search_result_css_class()))
        __M_writer(u' search-result-link ')
        __M_writer(conditional_websafe(has_thumbnail_class))
        __M_writer(u' ')
        __M_writer(conditional_websafe(linkflair_classes))
        __M_writer(u' ')
        __M_writer(conditional_websafe(visited_class))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_search_result_footer(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fb21a5bb890')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'md', u'nsfw_stamp', u'quarantine_stamp', u'thumbnail_img'])
        _mako_get_namespace(context, '__anon_0x7fb21a7bc690')._populate(_import_ns, [u'thumbnail'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 128
        __M_writer(u'\n')
        # SOURCE LINE 129
        if not thing.is_self:
            # SOURCE LINE 130
            __M_writer(u'    ')
            def ccall(caller):
                def body():
                    self = _import_ns.get('self', context.get('self', UNDEFINED))
                    plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
                    __M_writer = context.writer()
                    __M_writer(u'\n      ')
                    # SOURCE LINE 131
                    __M_writer(conditional_websafe(self.search_result_icon('external')))
                    __M_writer(u'\n      ')
                    # SOURCE LINE 132
                    __M_writer(conditional_websafe(plain_link(
          thing.url,
          thing.url,
          _sr_path=False,
          _class='search-link may-blank',
        )))
                    # SOURCE LINE 137
                    __M_writer(u'\n    ')
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 130
                __M_writer(conditional_websafe(parent.search_result_footer()))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 138
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_search_result_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fb21a5bb890')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'md', u'nsfw_stamp', u'quarantine_stamp', u'thumbnail_img'])
        _mako_get_namespace(context, '__anon_0x7fb21a7bc690')._populate(_import_ns, [u'thumbnail'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 58
        __M_writer(u'\n  ')
        def ccall(caller):
            def body():
                thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
                self = _import_ns.get('self', context.get('self', UNDEFINED))
                plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
                __M_writer = context.writer()
                # SOURCE LINE 59
                __M_writer(u'\n')
                # SOURCE LINE 60
                if c.site.link_flair_position == 'left':
                    # SOURCE LINE 61
                    __M_writer(u'      ')
                    __M_writer(conditional_websafe(self.flair()))
                    __M_writer(u'\n')
                # SOURCE LINE 63
                __M_writer(u'    ')
                __M_writer(conditional_websafe(plain_link(
        thing.title,
        thing.permalink,
        _sr_path=False,
        _class='search-title may-blank',
      )))
                # SOURCE LINE 68
                __M_writer(u'\n')
                # SOURCE LINE 69
                if c.site.link_flair_position == 'right':
                    # SOURCE LINE 70
                    __M_writer(u'      ')
                    __M_writer(conditional_websafe(self.flair()))
                    __M_writer(u'\n')
                # SOURCE LINE 72
                __M_writer(u'  ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 59
            __M_writer(conditional_websafe(parent.search_result_header()))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 72
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_search_result_meta(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fb21a5bb890')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'md', u'nsfw_stamp', u'quarantine_stamp', u'thumbnail_img'])
        _mako_get_namespace(context, '__anon_0x7fb21a7bc690')._populate(_import_ns, [u'thumbnail'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 81
        __M_writer(u'\n  ')
        def ccall(caller):
            def body():
                thing_timestamp = _import_ns.get('thing_timestamp', context.get('thing_timestamp', UNDEFINED))
                self = _import_ns.get('self', context.get('self', UNDEFINED))
                thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
                quarantine_stamp = _import_ns.get('quarantine_stamp', context.get('quarantine_stamp', UNDEFINED))
                plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
                nsfw_stamp = _import_ns.get('nsfw_stamp', context.get('nsfw_stamp', UNDEFINED))
                __M_writer = context.writer()
                # SOURCE LINE 82
                __M_writer(u'\n')
                # SOURCE LINE 83
                if thing.quarantine:
                    # SOURCE LINE 84
                    __M_writer(u'      <span class="quarantine-stamp stamp bold-stamp">')
                    __M_writer(conditional_websafe(quarantine_stamp()))
                    __M_writer(u'</span>&#32;\n')
                # SOURCE LINE 86
                if thing.over_18:
                    # SOURCE LINE 87
                    __M_writer(u'      <span class="stamp nsfw-stamp">')
                    __M_writer(conditional_websafe(nsfw_stamp()))
                    __M_writer(u'</span>&#32;\n')
                # SOURCE LINE 89
                if not thing.hide_score:
                    # SOURCE LINE 90
                    __M_writer(u'      ')
                    __M_writer(conditional_websafe(self.search_result_icon('score')))
                    __M_writer(u'\n      <span class="search-score">')
                    # SOURCE LINE 91
                    __M_writer(conditional_websafe(format_number(thing.score)))
                    __M_writer(u' ')
                    __M_writer(conditional_websafe(ungettext('point', 'points', thing.score)))
                    __M_writer(u'</span>&#32;\n')
                # SOURCE LINE 93
                __M_writer(u'    ')
                __M_writer(conditional_websafe(plain_link(
        '%s %s' % (format_number(thing.num_comments), ungettext('comment', 'comments', thing.num_comments)),
        thing.permalink,
        _sr_path=False,
        _class="search-comments may-blank",
      )))
                # SOURCE LINE 98
                __M_writer(u'&#32;\n    <span class="search-time">')
                # SOURCE LINE 99
                __M_writer(conditional_websafe(_("submitted")))
                __M_writer(u'&#32;')
                __M_writer(conditional_websafe(thing_timestamp(thing, thing.timesince, include_tense=True)))
                __M_writer(u'</span>&#32;\n    <span class="search-author">')
                # SOURCE LINE 100
                __M_writer(conditional_websafe(_("by")))
                __M_writer(u'&#32;')
                __M_writer(conditional_websafe(WrappedUser(thing.author, thing.attribs, thing)))
                __M_writer(u'</span>&#32;\n    ')
                # SOURCE LINE 101

                subreddit_link_fmt = format_html('<span>%s</span>', _('to %s')).replace(' ', '&#32;')
                    
                
                # SOURCE LINE 103
                __M_writer(u'\n    ')
                # SOURCE LINE 104
                __M_writer(conditional_websafe(plain_link(
        '/r/%s' % thing.subreddit.name,
        '/r/%s' % thing.subreddit.name,
        _sr_path=False,
        fmt=subreddit_link_fmt,
        _class='search-subreddit-link may-blank',
      )))
                # SOURCE LINE 110
                __M_writer(u'\n  ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 82
            __M_writer(conditional_websafe(parent.search_result_meta()))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 111
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_flair(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fb21a5bb890')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'md', u'nsfw_stamp', u'quarantine_stamp', u'thumbnail_img'])
        _mako_get_namespace(context, '__anon_0x7fb21a7bc690')._populate(_import_ns, [u'thumbnail'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 75
        __M_writer(u'\n')
        # SOURCE LINE 76
        if c.user.pref_show_link_flair and thing.flair_text:
            # SOURCE LINE 77
            __M_writer(u'    <span class="linkflairlabel" title="')
            __M_writer(conditional_websafe(thing.flair_text))
            __M_writer(u'">')
            __M_writer(conditional_websafe(thing.flair_text))
            __M_writer(u'</span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


