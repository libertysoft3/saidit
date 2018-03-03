# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1520060828.139482
_enable_loop = True
_template_filename = u'/home/reddit/src/reddit/r2/r2/templates/comment_skeleton.html'
_template_uri = u'/comment_skeleton.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['tagline', 'arrows', 'buttons', 'midcol', 'thing_data_attributes', 'entry', 'commentBody', 'thing_css_class']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 24
    ns = runtime.TemplateNamespace('__anon_0x7fc7c7b3f3d0', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fc7c7b3f3d0')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'printable.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7b3f3d0')._populate(_import_ns, [u'plain_link'])
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n')
        # SOURCE LINE 24
        __M_writer(u'\n\n')
        # SOURCE LINE 28
        __M_writer(u'\n\n')
        # SOURCE LINE 31
        __M_writer(u'\n\n')
        # SOURCE LINE 34
        __M_writer(u'\n\n')
        # SOURCE LINE 37
        __M_writer(u'\n\n')
        # SOURCE LINE 41
        __M_writer(u'\n\n')
        # SOURCE LINE 45
        __M_writer(u'\n\n')
        # SOURCE LINE 63
        __M_writer(u'\n\n')
        # SOURCE LINE 80
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tagline(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7b3f3d0')._populate(_import_ns, [u'plain_link'])
        __M_writer = context.writer()
        # SOURCE LINE 30
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_arrows(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7b3f3d0')._populate(_import_ns, [u'plain_link'])
        __M_writer = context.writer()
        # SOURCE LINE 36
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_buttons(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7b3f3d0')._populate(_import_ns, [u'plain_link'])
        __M_writer = context.writer()
        # SOURCE LINE 33
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_midcol(context,display=True,cls=''):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7b3f3d0')._populate(_import_ns, [u'plain_link'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 26
        __M_writer(u'\n  ')
        # SOURCE LINE 27
        __M_writer(conditional_websafe(parent.midcol(display=display, cls = cls)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_thing_data_attributes(context,what):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7b3f3d0')._populate(_import_ns, [u'plain_link'])
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 47
        __M_writer(u'\n  ')
        # SOURCE LINE 48
        __M_writer(conditional_websafe(parent.thing_data_attributes(what)))
        __M_writer(u'\n\n')
        # SOURCE LINE 50
        if hasattr(what, 'subreddit'):
            # SOURCE LINE 51
            __M_writer(u'    data-subreddit="')
            __M_writer(conditional_websafe(what.subreddit.name))
            __M_writer(u'"\n    data-subreddit-fullname="')
            # SOURCE LINE 52
            __M_writer(conditional_websafe(what.subreddit._fullname))
            __M_writer(u'"\n')
        # SOURCE LINE 54
        __M_writer(u'\n')
        # SOURCE LINE 55
        if not getattr(what, 'deleted', False) and getattr(what, 'author', False):
            # SOURCE LINE 56
            __M_writer(u'    data-author="')
            __M_writer(conditional_websafe(what.author.name))
            __M_writer(u'"\n    data-author-fullname="')
            # SOURCE LINE 57
            __M_writer(conditional_websafe(what.author._fullname))
            __M_writer(u'"\n')
        # SOURCE LINE 59
        __M_writer(u'\n')
        # SOURCE LINE 60
        if getattr(what, 'can_ban', False):
            # SOURCE LINE 61
            __M_writer(u'    data-can-ban="true"\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_entry(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7b3f3d0')._populate(_import_ns, [u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 65
        __M_writer(u'\n')
        # SOURCE LINE 66

        from r2.lib.strings import strings
        
        
        # SOURCE LINE 68
        __M_writer(u'\n\n<p class="tagline">\n  ')
        # SOURCE LINE 71
        __M_writer(conditional_websafe(self.tagline()))
        __M_writer(u'\n</p>\n\n')
        # SOURCE LINE 74
        __M_writer(conditional_websafe(self.commentBody()))
        __M_writer(u'\n\n<ul class="flat-list buttons">\n  ')
        # SOURCE LINE 77
        __M_writer(conditional_websafe(self.buttons()))
        __M_writer(u'\n</ul>\n<div class="reportform report-')
        # SOURCE LINE 79
        __M_writer(conditional_websafe(thing._fullname))
        __M_writer(u'"></div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_commentBody(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7b3f3d0')._populate(_import_ns, [u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 39
        __M_writer(u'\n  ')
        # SOURCE LINE 40
        __M_writer(conditional_websafe(thing.usertext))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_thing_css_class(context,what):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7b3f3d0')._populate(_import_ns, [u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 43
        __M_writer(u'\n  ')
        # SOURCE LINE 44
        __M_writer(conditional_websafe(parent.thing_css_class(what)))
        __M_writer(u' ')
        __M_writer(conditional_websafe("stickied" if getattr(thing, 'is_sticky', None) else ""))
        __M_writer(u' ')
        __M_writer(conditional_websafe("collapsed" if thing.collapsed else "noncollapsed"))
        __M_writer(u' ')
        __M_writer(conditional_websafe("collapsed-for-reason" if hasattr(thing, "collapsed_reason") else ""))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


