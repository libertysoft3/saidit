# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1506355985.513414
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/subredditstylesheetsource.html'
_template_uri = '/subredditstylesheetsource.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23

from r2.lib import js
from r2.lib.filters import SC_OFF, SC_ON
from r2.lib.template_helpers import static


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 28
    ns = runtime.TemplateNamespace('__anon_0x7f7067bba0d0', context._clean_inheritance_tokens(), templateuri=u'subredditstylesheetbase.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f7067bba0d0')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f7067bba0d0')._populate(_import_ns, [u'make_li'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        make_li = _import_ns.get('make_li', context.get('make_li', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 27
        __M_writer(u'\n')
        # SOURCE LINE 28
        __M_writer(u'\n\n\n')
        # SOURCE LINE 31
        if thing.stylesheet_contents:
            # SOURCE LINE 32
            __M_writer(u'  <link rel="stylesheet" type="text/css" href="')
            __M_writer(conditional_websafe(static("highlight.css")))
            __M_writer(u'">\n\n  <pre class="subreddit-stylesheet-source">\n  <code class="language-css">')
            # SOURCE LINE 35
            __M_writer(conditional_websafe(unsafe(SC_OFF)))
            __M_writer(conditional_websafe(thing.stylesheet_contents))
            __M_writer(conditional_websafe(unsafe(SC_ON)))
            __M_writer(u'</code>\n  </pre>\n\n  ')
            # SOURCE LINE 38
            __M_writer(conditional_websafe(unsafe(js.use("highlight"))))
            __M_writer(u'\n')
        # SOURCE LINE 40
        __M_writer(u'\n')
        # SOURCE LINE 41
        if thing.images:
            # SOURCE LINE 42
            __M_writer(u'  <div id="images">\n    <h2><a name="images">')
            # SOURCE LINE 43
            __M_writer(conditional_websafe(_("images")))
            __M_writer(u'</a></h2>\n    <ul id="image-preview-list" class="image-list">\n')
            # SOURCE LINE 45
            for name, url in thing.images.iteritems():
                # SOURCE LINE 46
                __M_writer(u'         ')
                __M_writer(conditional_websafe(make_li(name=name, img=url, mod=False)))
                __M_writer(u'\n')
            # SOURCE LINE 48
            __M_writer(u'    </ul>\n')
        # SOURCE LINE 50
        __M_writer(u'\n')
        # SOURCE LINE 51
        if not (thing.stylesheet_contents or thing.images):
            # SOURCE LINE 52
            __M_writer(u'  <p class="error">')
            __M_writer(conditional_websafe(_("there doesn't seem to be anything here")))
            __M_writer(u'</p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


