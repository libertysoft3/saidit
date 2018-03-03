# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1520060829.823527
_enable_loop = True
_template_filename = u'/home/reddit/src/reddit/r2/r2/templates/interstitial.html'
_template_uri = u'/interstitial.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['interstitial_image_attrs', 'interstitial_message', 'interstitial_title', 'interstitial_buttons']


# SOURCE LINE 23

from r2.lib.template_helpers import static 
from r2.lib.filters import unsafe, safemarkdown


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 28
    ns = runtime.TemplateNamespace('__anon_0x7fc7c7837cd0', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fc7c7837cd0')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7837cd0')._populate(_import_ns, [u'md'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        md = _import_ns.get('md', context.get('md', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 26
        __M_writer(u'\n\n')
        # SOURCE LINE 28
        __M_writer(u'\n\n<div class="interstitial">\n  <img class="interstitial-image"\n       ')
        # SOURCE LINE 32
        __M_writer(conditional_websafe(self.interstitial_image_attrs()))
        __M_writer(u'\n       height="150"\n       width="150">\n  \n  <div class="interstitial-message md-container">\n    <div class="md">\n      <h3>')
        # SOURCE LINE 38
        __M_writer(conditional_websafe(self.interstitial_title()))
        __M_writer(u'</h3>\n\n')
        # SOURCE LINE 40
        if thing.sr_name and thing.sr_description:
            # SOURCE LINE 41
            __M_writer(u'        <div class="interstitial-subreddit-description">\n          <h5>')
            # SOURCE LINE 42
            __M_writer(conditional_websafe(_("r/%s") % thing.sr_name))
            __M_writer(u'</h5>\n          ')
            # SOURCE LINE 43
            __M_writer(conditional_websafe(md(thing.sr_description)))
            __M_writer(u'\n        </div>\n')
        # SOURCE LINE 46
        __M_writer(u'\n      ')
        # SOURCE LINE 47
        __M_writer(conditional_websafe(self.interstitial_message()))
        __M_writer(u'\n    </div>\n  </div>\n  \n  ')
        # SOURCE LINE 51
        __M_writer(conditional_websafe(self.interstitial_buttons()))
        __M_writer(u'\n</div>\n\n')
        # SOURCE LINE 56
        __M_writer(u'\n\n')
        # SOURCE LINE 60
        __M_writer(u'\n\n')
        # SOURCE LINE 66
        __M_writer(u'\n\n')
        # SOURCE LINE 72
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_interstitial_image_attrs(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7837cd0')._populate(_import_ns, [u'md'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 54
        __M_writer(u'\n  src="')
        # SOURCE LINE 55
        __M_writer(conditional_websafe(static(thing.image)))
        __M_writer(u'"\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_interstitial_message(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7837cd0')._populate(_import_ns, [u'md'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        md = _import_ns.get('md', context.get('md', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 62
        __M_writer(u'\n')
        # SOURCE LINE 63
        if thing.message:
            # SOURCE LINE 64
            __M_writer(u'    ')
            __M_writer(conditional_websafe(md(thing.message)))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_interstitial_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7837cd0')._populate(_import_ns, [u'md'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 58
        __M_writer(u'\n  ')
        # SOURCE LINE 59
        __M_writer(conditional_websafe(thing.title))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_interstitial_buttons(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7837cd0')._populate(_import_ns, [u'md'])
        __M_writer = context.writer()
        # SOURCE LINE 68
        __M_writer(u'\n  <div class="buttons">\n    <a href="/" class="c-btn c-btn-primary">')
        # SOURCE LINE 70
        __M_writer(conditional_websafe(_("back to Reddit")))
        __M_writer(u'</a>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


