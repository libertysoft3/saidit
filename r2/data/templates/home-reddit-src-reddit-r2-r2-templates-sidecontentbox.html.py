# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505003389.749566
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/sidecontentbox.html'
_template_uri = '/sidecontentbox.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7f3608bf8c10', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f3608bf8c10')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f3608bf8c10')._populate(_import_ns, [u'tags'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        tags = _import_ns.get('tags', context.get('tags', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n<div class="sidecontentbox ')
        # SOURCE LINE 24
        __M_writer(conditional_websafe(thing.extra_class or ''))
        __M_writer(u' ')
        __M_writer(conditional_websafe('collapsible' if thing.collapsible else ''))
        __M_writer(u'" ')
        __M_writer(conditional_websafe(tags(_id=thing._id)))
        __M_writer(u'>\n')
        # SOURCE LINE 25
        if thing.helplink:
            # SOURCE LINE 26
            __M_writer(u'    ')
            __M_writer(conditional_websafe(thing.helplink))
            __M_writer(u'\n')
        # SOURCE LINE 28
        __M_writer(u'  <div class="title">\n    <h1>')
        # SOURCE LINE 29
        __M_writer(conditional_websafe(thing.title.upper()))
        __M_writer(u'</h1>\n')
        # SOURCE LINE 30
        if thing.collapsible:
            # SOURCE LINE 31
            __M_writer(u'      <span class="collapse-button">-</span>\n')
        # SOURCE LINE 33
        __M_writer(u'  </div>\n  <ul class="content">\n')
        # SOURCE LINE 35
        for c in thing.content:
            # SOURCE LINE 36
            __M_writer(u'      <li>')
            __M_writer(conditional_websafe(c))
            __M_writer(u'</li>\n')
        # SOURCE LINE 38
        __M_writer(u'\n')
        # SOURCE LINE 39
        if thing.more_href:
            # SOURCE LINE 40
            __M_writer(u'      <li class="more">\n        <a href="')
            # SOURCE LINE 41
            __M_writer(conditional_websafe(thing.more_href))
            __M_writer(u'">\n          ')
            # SOURCE LINE 42
            __M_writer(conditional_websafe(thing.more_text))
            __M_writer(u' &raquo;\n        </a>\n      </li>\n')
        # SOURCE LINE 46
        __M_writer(u'  </ul>\n\n')
        # SOURCE LINE 48
        if thing.collapsible:
            # SOURCE LINE 49
            __M_writer(u'    <script>r.ui.collapsibleSideBox("')
            __M_writer(conditional_websafe(thing._id))
            __M_writer(u'")</script>\n')
        # SOURCE LINE 51
        __M_writer(u'</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


