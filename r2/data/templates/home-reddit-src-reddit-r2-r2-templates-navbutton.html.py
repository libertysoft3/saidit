# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505002596.205468
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/navbutton.html'
_template_uri = '/navbutton.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['plain', 'post', 'js']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7fde6025b3d0', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fde6025b3d0')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fde6025b3d0')._populate(_import_ns, [u'plain_link', u'post_link'])
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n')
        # SOURCE LINE 31
        __M_writer(u'\n\n')
        # SOURCE LINE 39
        __M_writer(u'\n\n')
        # SOURCE LINE 47
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_plain(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fde6025b3d0')._populate(_import_ns, [u'plain_link', u'post_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 25
        __M_writer(u'\n  ')
        # SOURCE LINE 26
        __M_writer(conditional_websafe(plain_link(thing.selected_title() if thing.selected else thing.title, 
               thing.path, _sr_path = thing.sr_path,
               target = thing.target, 
               _class = thing.css_class, _id = thing._id,
               data=thing.data)))
        # SOURCE LINE 30
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_post(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fde6025b3d0')._populate(_import_ns, [u'plain_link', u'post_link'])
        post_link = _import_ns.get('post_link', context.get('post_link', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 41
        __M_writer(u'\n  ')
        # SOURCE LINE 42
        __M_writer(conditional_websafe(post_link(thing.selected_title() if thing.selected else thing.title,
              thing.base_path, thing.base_path, thing.action_params,
              _sr_path=thing.sr_path,
              target=thing.target, _class=thing.css_class, _id=thing._id,
              data=thing.data)))
        # SOURCE LINE 46
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fde6025b3d0')._populate(_import_ns, [u'plain_link', u'post_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 33
        __M_writer(u'\n  ')
        # SOURCE LINE 34
        __M_writer(conditional_websafe(plain_link(thing.selected_title() if thing.selected else thing.title, 
               thing.path, _sr_path = False,
               _class = thing.css_class, _id = thing._id, 
               onclick = thing.onclick,
               data=thing.data)))
        # SOURCE LINE 38
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


