# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1508357131.110628
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/morechildren.html'
_template_uri = '/morechildren.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['arrows', 'commentBody', 'midcol']


# SOURCE LINE 23

from r2.lib.utils import to36
 

def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'comment_skeleton.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'\n')
        # SOURCE LINE 26
        __M_writer(u'\n\n\n')
        # SOURCE LINE 41
        __M_writer(u'\n\n')
        # SOURCE LINE 44
        __M_writer(u'\n\n')
        # SOURCE LINE 47
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_arrows(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 43
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_commentBody(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        thing = context.get('thing', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 29
        __M_writer(u'\n')
        # SOURCE LINE 30

        cids = [to36(cm) for cm in thing.children]
        
        
        # SOURCE LINE 32
        __M_writer(u'\n<span class="morecomments">\n<a style="font-size: smaller; font-weight: bold" class="button"\n   id="more_')
        # SOURCE LINE 35
        __M_writer(conditional_websafe(thing._fullname))
        __M_writer(u'" href="javascript:void(0)"\n   onclick="return morechildren(this, \'')
        # SOURCE LINE 36
        __M_writer(conditional_websafe(thing.link_name))
        __M_writer(u"', '")
        __M_writer(conditional_websafe(thing.sort))
        __M_writer(u"', '")
        __M_writer(conditional_websafe(",".join(cids)))
        __M_writer(u"', ")
        __M_writer(conditional_websafe(thing.depth))
        __M_writer(u')">\n')
        # SOURCE LINE 37
        __M_writer(conditional_websafe(_("load more comments")))
        __M_writer(u'\n<span class="gray">&nbsp;(')
        # SOURCE LINE 38
        __M_writer(conditional_websafe(thing.count))
        __M_writer(u' ')
        __M_writer(conditional_websafe(ungettext("reply", "replies", thing.count)))
        __M_writer(u')</span>\n</a>\n</span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_midcol(context,cls=''):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 46
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


