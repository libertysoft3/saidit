# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505842080.16233
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/modsrinfobar.html'
_template_uri = '/modsrinfobar.html'
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
    ns = runtime.TemplateNamespace('__anon_0x7f2f685eab50', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f2f685eab50')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f2f685eab50')._populate(_import_ns, [u'plain_link', u'_md'])
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        _md = _import_ns.get('_md', context.get('_md', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n<div class="titlebox rounded">\n  <h1 class="hover redditname">\n    ')
        # SOURCE LINE 27
        __M_writer(conditional_websafe(plain_link(c.site.name, c.site.user_path, _sr_path=False, _class="hover")))
        __M_writer(u'\n  </h1>\n\n  <div class="usertext">\n    ')
        # SOURCE LINE 31
        __M_writer(conditional_websafe(_md("/r/mod shows only subreddits you moderate.")))
        __M_writer(u'\n  </div>\n\n  ')
        # SOURCE LINE 34
        __M_writer(conditional_websafe(plain_link(_("filter out subreddits"), "/me/f/mod", _class="modsr-link", _sr_path=False)))
        __M_writer(u'\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


