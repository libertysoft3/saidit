# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505837026.534304
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/searchresultsubreddit.html'
_template_uri = '/searchresultsubreddit.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['search_result_body', 'search_result_css_class', 'permissions_stamps', 'search_result_footer', 'search_result_header', 'search_result_meta']


# SOURCE LINE 28

from r2.lib.template_helpers import format_number, search_url
from r2.lib.utils import timesince


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 25
    ns = runtime.TemplateNamespace('__anon_0x7f2f69703a90', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f2f69703a90')] = ns

    # SOURCE LINE 26
    ns = runtime.TemplateNamespace('__anon_0x7f2f69703690', context._clean_inheritance_tokens(), templateuri=u'subscribebutton.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f2f69703690')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'searchresultbase.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f2f69703a90')._populate(_import_ns, [u'plain_link', u'nsfw_stamp', u'quarantine_stamp'])
        _mako_get_namespace(context, '__anon_0x7f2f69703690')._populate(_import_ns, [u'subscribe_button'])
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n')
        # SOURCE LINE 25
        __M_writer(u'\n')
        # SOURCE LINE 26
        __M_writer(u'\n\n')
        # SOURCE LINE 31
        __M_writer(u'\n\n')
        # SOURCE LINE 35
        __M_writer(u'\n\n')
        # SOURCE LINE 46
        __M_writer(u'\n\n')
        # SOURCE LINE 66
        __M_writer(u'\n\n')
        # SOURCE LINE 74
        __M_writer(u'\n\n')
        # SOURCE LINE 88
        __M_writer(u'\n\n')
        # SOURCE LINE 104
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_search_result_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f2f69703a90')._populate(_import_ns, [u'plain_link', u'nsfw_stamp', u'quarantine_stamp'])
        _mako_get_namespace(context, '__anon_0x7f2f69703690')._populate(_import_ns, [u'subscribe_button'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 68
        __M_writer(u'\n')
        # SOURCE LINE 69
        if thing.public_description:
            # SOURCE LINE 70
            __M_writer(u'    ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    __M_writer(u'\n      ')
                    # SOURCE LINE 71
                    __M_writer(conditional_websafe(thing.public_description))
                    __M_writer(u'\n    ')
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 70
                __M_writer(conditional_websafe(parent.search_result_body()))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 72
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_search_result_css_class(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f2f69703a90')._populate(_import_ns, [u'plain_link', u'nsfw_stamp', u'quarantine_stamp'])
        _mako_get_namespace(context, '__anon_0x7f2f69703690')._populate(_import_ns, [u'subscribe_button'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 33
        __M_writer(u'\n  ')
        # SOURCE LINE 34
        __M_writer(conditional_websafe(parent.search_result_css_class()))
        __M_writer(u' search-result-subreddit\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_permissions_stamps(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f2f69703a90')._populate(_import_ns, [u'plain_link', u'nsfw_stamp', u'quarantine_stamp'])
        _mako_get_namespace(context, '__anon_0x7f2f69703690')._populate(_import_ns, [u'subscribe_button'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        quarantine_stamp = _import_ns.get('quarantine_stamp', context.get('quarantine_stamp', UNDEFINED))
        nsfw_stamp = _import_ns.get('nsfw_stamp', context.get('nsfw_stamp', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 90
        __M_writer(u'\n')
        # SOURCE LINE 91
        if thing.quarantine:
            # SOURCE LINE 92
            __M_writer(u'    <span class="quarantine-stamp stamp bold-stamp">')
            __M_writer(conditional_websafe(quarantine_stamp()))
            __M_writer(u'</span>&#32;\n')
        # SOURCE LINE 94
        if thing.over_18:
            # SOURCE LINE 95
            __M_writer(u'    <span class="stamp nsfw-stamp">')
            __M_writer(conditional_websafe(nsfw_stamp()))
            __M_writer(u'</span>&#32;\n')
        # SOURCE LINE 97
        if thing.display_type == "private":
            # SOURCE LINE 98
            __M_writer(u'    <span class="stamp private-stamp">')
            __M_writer(conditional_websafe(_("private")))
            __M_writer(u'</span>&#32;\n')
            # SOURCE LINE 99
        elif thing.display_type == "restricted": 
            # SOURCE LINE 100
            __M_writer(u'    <span class="stamp restricted-stamp">')
            __M_writer(conditional_websafe(_("restricted")))
            __M_writer(u'</span>&#32;\n')
            # SOURCE LINE 101
        elif thing.display_type == "archived":
            # SOURCE LINE 102
            __M_writer(u'    <span class="stamp archived-stamp">')
            __M_writer(conditional_websafe(_("archived")))
            __M_writer(u'</span>&#32;\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_search_result_footer(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f2f69703a90')._populate(_import_ns, [u'plain_link', u'nsfw_stamp', u'quarantine_stamp'])
        _mako_get_namespace(context, '__anon_0x7f2f69703690')._populate(_import_ns, [u'subscribe_button'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 76
        __M_writer(u'\n  ')
        def ccall(caller):
            def body():
                thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
                self = _import_ns.get('self', context.get('self', UNDEFINED))
                dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
                plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
                __M_writer = context.writer()
                # SOURCE LINE 77
                __M_writer(u'\n    ')
                # SOURCE LINE 78
                pretty_name = thing.path.rstrip('/') 
                
                __M_writer(u'\n    ')
                # SOURCE LINE 79
                __M_writer(conditional_websafe(self.search_result_icon('filter')))
                __M_writer(u'\n    ')
                # SOURCE LINE 80
                __M_writer(conditional_websafe(plain_link(
        _("search within %(subreddit)s") % dict(subreddit=pretty_name),
        search_url(thing.prev_search, thing.name, restrict_sr='on', sort=thing.sort, recent=thing.recent),
        _sr_path=False,
        _class='search-link',
        title=_('search in %(subreddit)s' % dict(subreddit=pretty_name)),
      )))
                # SOURCE LINE 86
                __M_writer(u'\n  ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 77
            __M_writer(conditional_websafe(parent.search_result_footer()))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 87
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_search_result_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f2f69703a90')._populate(_import_ns, [u'plain_link', u'nsfw_stamp', u'quarantine_stamp'])
        _mako_get_namespace(context, '__anon_0x7f2f69703690')._populate(_import_ns, [u'subscribe_button'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 37
        __M_writer(u'\n  ')
        def ccall(caller):
            def body():
                thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
                plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
                __M_writer = context.writer()
                # SOURCE LINE 38
                __M_writer(u'\n    ')
                # SOURCE LINE 39
                __M_writer(conditional_websafe(plain_link(
        thing.title,
        thing.search_path,
        _sr_path=False,
        _class='search-title may-blank',
      )))
                # SOURCE LINE 44
                __M_writer(u'\n  ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 38
            __M_writer(conditional_websafe(parent.search_result_header()))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 45
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_search_result_meta(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f2f69703a90')._populate(_import_ns, [u'plain_link', u'nsfw_stamp', u'quarantine_stamp'])
        _mako_get_namespace(context, '__anon_0x7f2f69703690')._populate(_import_ns, [u'subscribe_button'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 48
        __M_writer(u'\n  ')
        def ccall(caller):
            def body():
                thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
                self = _import_ns.get('self', context.get('self', UNDEFINED))
                subscribe_button = _import_ns.get('subscribe_button', context.get('subscribe_button', UNDEFINED))
                dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
                plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
                __M_writer = context.writer()
                # SOURCE LINE 49
                __M_writer(u'\n    ')
                # SOURCE LINE 50
                data_attrs = {"sr_name": thing.name} 
                
                __M_writer(u'\n')
                # SOURCE LINE 51
                if thing.display_type != "private":
                    # SOURCE LINE 52
                    __M_writer(u'      ')
                    __M_writer(conditional_websafe(subscribe_button(thing, data_attrs, css_class='search-subscribe-button')))
                    __M_writer(u'\n')
                # SOURCE LINE 54
                __M_writer(u'    ')
                __M_writer(conditional_websafe(self.permissions_stamps()))
                __M_writer(u'\n    ')
                # SOURCE LINE 55
                __M_writer(conditional_websafe(plain_link(
        thing.path.rstrip('/'),
        thing.search_path,
        _sr_path=False,
        _class='search-subreddit-link may-blank',
      )))
                # SOURCE LINE 60
                __M_writer(u'&#32;\n')
                # SOURCE LINE 61
                if not thing.score_hidden:
                    # SOURCE LINE 62
                    __M_writer(u'      <span class="search-subscribers">')
                    __M_writer(conditional_websafe(format_number(thing._ups)))
                    __M_writer(u' ')
                    __M_writer(conditional_websafe(ungettext('subscriber', 'subscribers', thing._ups)))
                    __M_writer(u',</span>&#32;\n')
                # SOURCE LINE 64
                __M_writer(u'    <span class="search-time">')
                __M_writer(conditional_websafe(_("a community for %(time)s") % dict(time=timesince(thing._date))))
                __M_writer(u'</span>&#32;\n  ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 49
            __M_writer(conditional_websafe(parent.search_result_meta()))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 65
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


