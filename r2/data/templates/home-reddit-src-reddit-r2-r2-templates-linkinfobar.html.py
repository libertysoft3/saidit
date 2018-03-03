# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1520060829.38078
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/linkinfobar.html'
_template_uri = '/linkinfobar.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['info_table']


# SOURCE LINE 23

from r2.lib.filters import websafe
from r2.lib.strings import Score
from r2.lib.template_helpers import format_number, format_percent, html_datetime
 

def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 30
    ns = runtime.TemplateNamespace('__anon_0x7fc7c783a850', context._clean_inheritance_tokens(), templateuri=u'printablebuttons.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fc7c783a850')] = ns

    # SOURCE LINE 31
    ns = runtime.TemplateNamespace('__anon_0x7fc7c783a990', context._clean_inheritance_tokens(), templateuri=u'printable.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fc7c783a990')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c783a850')._populate(_import_ns, [u'state_button'])
        _mako_get_namespace(context, '__anon_0x7fc7c783a990')._populate(_import_ns, [u'thing_css_class'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 27
        __M_writer(u'\n\n\n')
        # SOURCE LINE 30
        __M_writer(u'\n')
        # SOURCE LINE 31
        __M_writer(u'\n\n\n\n<div class="linkinfo">\n  <div class="date">\n    <span>\n      ')
        # SOURCE LINE 38
        __M_writer(conditional_websafe(_("this post was submitted on")))
        __M_writer(u'\n      &#32;\n    </span>\n    <time datetime="')
        # SOURCE LINE 41
        __M_writer(conditional_websafe(html_datetime(thing.a._date)))
        __M_writer(u'">\n      ')
        # SOURCE LINE 42
        __M_writer(conditional_websafe(thing.a._date.strftime(thing.datefmt)))
        __M_writer(u'\n    </time>\n  </div>\n\n  <div class="score">\n    ')
        # SOURCE LINE 47
        __M_writer(conditional_websafe(unsafe(Score.PERSON_LABEL % dict(num = format_number(thing.a.score),
                                       persons = websafe(ungettext("point", "points",
                                                                   thing.a.score))))))
        # SOURCE LINE 49
        __M_writer(u'\n    &#32;(')
        # SOURCE LINE 50
        __M_writer(conditional_websafe(_("%(percent)s upvoted") % dict(percent=format_percent(thing.a.upvote_ratio))))
        __M_writer(u')\n  </div>\n\n')
        # SOURCE LINE 53
        if getattr(thing.a, "shortlink", None):
            # SOURCE LINE 54
            __M_writer(u'  <div class="shortlink">\n    shortlink:\n    &#32;\n    <input type="text" value="https://')
            # SOURCE LINE 57
            __M_writer(conditional_websafe(thing.a.shortlink))
            __M_writer(u'" readonly="readonly" id="shortlink-text" />\n  </div>\n')
        # SOURCE LINE 60
        __M_writer(u'\n  ')
        # SOURCE LINE 61
        __M_writer(conditional_websafe(self.info_table()))
        __M_writer(u'\n</div>\n\n')
        # SOURCE LINE 65
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_info_table(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c783a850')._populate(_import_ns, [u'state_button'])
        _mako_get_namespace(context, '__anon_0x7fc7c783a990')._populate(_import_ns, [u'thing_css_class'])
        __M_writer = context.writer()
        # SOURCE LINE 64
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


