# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1508303897.804007
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/pagenamenav.compact'
_template_uri = '/pagenamenav.compact'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['domain', 'help', 'nomenu', 'subreddits', 'subreddit', 'newpagelink']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7f4dec465490', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f4dec465490')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f4dec465490')._populate(_import_ns, [u'plain_link'])
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n')
        # SOURCE LINE 29
        __M_writer(u'\n\n')
        # SOURCE LINE 35
        __M_writer(u'\n\n')
        # SOURCE LINE 41
        __M_writer(u'\n\n')
        # SOURCE LINE 45
        __M_writer(u'\n\n')
        # SOURCE LINE 51
        __M_writer(u'\n\n')
        # SOURCE LINE 55
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_domain(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f4dec465490')._populate(_import_ns, [u'plain_link'])
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 25
        __M_writer(u'\n  <span class="hover pagename redditname">\n    ')
        # SOURCE LINE 27
        __M_writer(conditional_websafe(plain_link(c.site.name, c.site.user_path, _sr_path=False)))
        __M_writer(u'\n  </span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_help(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f4dec465490')._populate(_import_ns, [u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 47
        __M_writer(u'\n  <span class="hover pagename redditname">\n    ')
        # SOURCE LINE 49
        __M_writer(conditional_websafe(plain_link(thing.title, "/help", _sr_path=False)))
        __M_writer(u'\n  </span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_nomenu(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f4dec465490')._populate(_import_ns, [u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 43
        __M_writer(u'\n')
        # SOURCE LINE 44
        __M_writer(conditional_websafe(thing.title))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_subreddits(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f4dec465490')._populate(_import_ns, [u'plain_link'])
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 37
        __M_writer(u'\n  <span class="hover pagename redditname">\n    ')
        # SOURCE LINE 39
        __M_writer(conditional_websafe(plain_link(_("subreddits"), "/subreddits/", _sr_path=False)))
        __M_writer(u'\n  </span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_subreddit(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f4dec465490')._populate(_import_ns, [u'plain_link'])
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 31
        __M_writer(u'\n  <span class="hover pagename redditname">\n    ')
        # SOURCE LINE 33
        __M_writer(conditional_websafe(plain_link(c.site.name, c.site.user_path, _sr_path=False)))
        __M_writer(u'\n  </span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_newpagelink(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f4dec465490')._populate(_import_ns, [u'plain_link'])
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 53
        __M_writer(u'\n<span class="newpagelink">reddit all?&#32;')
        # SOURCE LINE 54
        __M_writer(conditional_websafe(plain_link("click here to find new links.", "/new/", _sr_path=False)))
        __M_writer(u'</span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


