# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505982946.181788
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/wikibasepage.html'
_template_uri = '/wikibasepage.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['content', 'global_stylesheets', 'actionsbar']


# SOURCE LINE 22

from r2.config import feature


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 26
    ns = runtime.TemplateNamespace('__anon_0x7f20bc77b250', context._clean_inheritance_tokens(), templateuri=u'less.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f20bc77b250')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'reddit.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f20bc77b250')._populate(_import_ns, [u'less_stylesheet'])
        __M_writer = context.writer()
        # SOURCE LINE 24
        __M_writer(u'\n\n')
        # SOURCE LINE 26
        __M_writer(u'\n')
        # SOURCE LINE 27
        __M_writer(u'\n\n')
        # SOURCE LINE 32
        __M_writer(u'\n\n')
        # SOURCE LINE 53
        __M_writer(u'\n\n')
        # SOURCE LINE 88
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f20bc77b250')._populate(_import_ns, [u'less_stylesheet'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        def actionsbar(actions):
            return render_actionsbar(context,actions)
        __M_writer = context.writer()
        # SOURCE LINE 55
        __M_writer(u'\n    ')
        # SOURCE LINE 56
        __M_writer(conditional_websafe(thing.infobar))
        __M_writer(u'\n    <span>\n        <h1 class="wikititle">\n')
        # SOURCE LINE 59
        if thing.pagetitle:
            # SOURCE LINE 60
            __M_writer(u'                ')
            __M_writer(conditional_websafe(thing.pagetitle))
            __M_writer(u'\n')
        # SOURCE LINE 62
        if thing.page:
            # SOURCE LINE 63
            __M_writer(u'                <strong>')
            __M_writer(conditional_websafe(thing.page))
            __M_writer(u'</strong>\n')
        # SOURCE LINE 65
        __M_writer(u'        </h1>\n        \n')
        # SOURCE LINE 67
        if thing.pageactions:
            # SOURCE LINE 68
            __M_writer(u'            <span class="pageactions">\n                ')
            # SOURCE LINE 69
            __M_writer(conditional_websafe(actionsbar(thing.pageactions)))
            __M_writer(u'\n            </span>\n')
        # SOURCE LINE 72
        __M_writer(u'    </span>\n        \n    <div class="wiki-page-content md-container">\n')
        # SOURCE LINE 75
        if thing.description:
            # SOURCE LINE 76
            __M_writer(u'            <div class="description">\n                <h2>\n')
            # SOURCE LINE 78
            for desc in thing.description:
                # SOURCE LINE 79
                __M_writer(u'                        ')
                __M_writer(conditional_websafe(desc))
                __M_writer(u'<br/>\n')
            # SOURCE LINE 81
            __M_writer(u'                </h2>\n            </div>\n')
        # SOURCE LINE 84
        __M_writer(u'        ')
        __M_writer(conditional_websafe(thing.content()))
        __M_writer(u'\n    </div>\n\n    <!--reddit wikis are powered by Cray-1\u2122 supercomputers-->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_global_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f20bc77b250')._populate(_import_ns, [u'less_stylesheet'])
        less_stylesheet = _import_ns.get('less_stylesheet', context.get('less_stylesheet', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 29
        __M_writer(u'\n    ')
        # SOURCE LINE 30
        __M_writer(conditional_websafe(parent.global_stylesheets()))
        __M_writer(u'\n    ')
        # SOURCE LINE 31
        __M_writer(conditional_websafe(less_stylesheet('wiki.less')))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_actionsbar(context,actions):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f20bc77b250')._populate(_import_ns, [u'less_stylesheet'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 34
        __M_writer(u'\n')
        # SOURCE LINE 35
        for action in actions:
            # SOURCE LINE 36
            __M_writer(u'        <a class="wikiaction wikiaction-')
            __M_writer(conditional_websafe(action[0]))
            __M_writer(u'\n')
            # SOURCE LINE 37
            if action[0] == thing.action[0]:
                # SOURCE LINE 38
                __M_writer(u'            wikiaction-current\n')
            # SOURCE LINE 40
            __M_writer(u'        "\n')
            # SOURCE LINE 41
            if action[2]:
                # SOURCE LINE 42
                __M_writer(u'            href="')
                __M_writer(conditional_websafe(thing.base_url))
                __M_writer(u'/')
                __M_writer(conditional_websafe(action[0]))
                __M_writer(u'/')
                __M_writer(conditional_websafe(thing.page))
                __M_writer(u'"\n')
                # SOURCE LINE 43
            else:
                # SOURCE LINE 44
                __M_writer(u'            href="')
                __M_writer(conditional_websafe(thing.base_url))
                __M_writer(u'/')
                __M_writer(conditional_websafe(action[0]))
                __M_writer(u'"\n')
            # SOURCE LINE 46
            __M_writer(u'        data-type="subreddit"\n')
            # SOURCE LINE 47
            if action[3]:
                # SOURCE LINE 48
                __M_writer(u'            data-event-action="pageview"\n            data-event-detail="')
                # SOURCE LINE 49
                __M_writer(conditional_websafe(action[3]))
                __M_writer(u'"\n')
            # SOURCE LINE 51
            __M_writer(u'        >')
            __M_writer(conditional_websafe(action[1]))
            __M_writer(u'</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


