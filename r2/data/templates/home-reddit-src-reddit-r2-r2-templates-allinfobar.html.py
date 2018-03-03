# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505002703.64176
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/allinfobar.html'
_template_uri = '/allinfobar.html'
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
    ns = runtime.TemplateNamespace('__anon_0x7fde5ffcf450', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fde5ffcf450')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fde5ffcf450')._populate(_import_ns, [u'plain_link', u'classes', u'_md'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        classes = _import_ns.get('classes', context.get('classes', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        _md = _import_ns.get('_md', context.get('_md', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n<div ')
        # SOURCE LINE 25
        __M_writer(conditional_websafe(classes("titlebox", "rounded", thing.css_class)))
        __M_writer(u'>\n  <h1 class="hover redditname special">\n    ')
        # SOURCE LINE 27
        __M_writer(conditional_websafe(plain_link(thing.sr.name, thing.sr.path, _sr_path=False, _class="hover")))
        __M_writer(u'\n  </h1>\n\n  <div class="usertext">\n    ')
        # SOURCE LINE 31
        __M_writer(conditional_websafe(_md(thing.description, wrap=True)))
        __M_writer(u'\n  </div>\n</div>\n\n')
        # SOURCE LINE 35
        if thing.allminus_url:
            # SOURCE LINE 36
            __M_writer(u'  <div class="giftgold allminus-link">\n    <a href="')
            # SOURCE LINE 37
            __M_writer(conditional_websafe(thing.allminus_url))
            __M_writer(u'">')
            __M_writer(conditional_websafe(_("Exclude your subscribed subs")))
            __M_writer(u'</a>\n  </div>\n')
        # SOURCE LINE 40
        __M_writer(u'\n<div class="giftgold allminus-link">\n    <a href="/me/f/all">')
        # SOURCE LINE 42
        __M_writer(conditional_websafe(_("Exclude custom subs")))
        __M_writer(u'</a>\n</div>\n\n')
        # SOURCE LINE 45
        if not thing.gilding_listing:
            # SOURCE LINE 46
            __M_writer(u'<div class="gilded-link">\n  <a href="/r/all/gilded">')
            # SOURCE LINE 47
            __M_writer(conditional_websafe(_("See gilded comments and submissions")))
            __M_writer(u'</a>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


