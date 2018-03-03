# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1511947254.247692
_enable_loop = True
_template_filename = u'/home/reddit/src/reddit/r2/r2/templates/base.iframe'
_template_uri = u'/base.iframe'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23

import json

from r2.lib.filters import unsafe
from r2.lib import js
from r2.lib.template_helpers import add_sr, get_domain, static


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 30
    ns = runtime.TemplateNamespace('__anon_0x7f3a4d159350', context._clean_inheritance_tokens(), templateuri=u'less.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f3a4d159350')] = ns

    # SOURCE LINE 31
    ns = runtime.TemplateNamespace('__anon_0x7f3a4d090090', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f3a4d090090')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f3a4d159350')._populate(_import_ns, [u'less_js', u'less_stylesheet'])
        _mako_get_namespace(context, '__anon_0x7f3a4d090090')._populate(_import_ns, [u'text_with_links', u'plain_link'])
        less_stylesheet = _import_ns.get('less_stylesheet', context.get('less_stylesheet', UNDEFINED))
        less_js = _import_ns.get('less_js', context.get('less_js', UNDEFINED))
        text_with_links = _import_ns.get('text_with_links', context.get('text_with_links', UNDEFINED))
        next = _import_ns.get('next', context.get('next', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 29
        __M_writer(u'\n')
        # SOURCE LINE 30
        __M_writer(u'\n')
        # SOURCE LINE 31
        __M_writer(u'\n\n')
        # SOURCE LINE 33

        link_data = {"redirect-type": "link", "redirect-thing": thing.link._id}
        sr_data = {"redirect-type": "subreddit"}
        reddit_data = {"redirect-type": "logo"}
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['reddit_data','sr_data','link_data'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 37
        __M_writer(u'\n\n<!doctype html>\n<html>\n    <head>\n        <meta charset=utf-8>\n        <base target="_blank" href="')
        # SOURCE LINE 43
        __M_writer(conditional_websafe(add_sr("/", sr_path=False, force_hostname=True)))
        __M_writer(u'">\n        <title></title>\n        ')
        # SOURCE LINE 45
        __M_writer(conditional_websafe(less_stylesheet("reddit-embed.less")))
        __M_writer(u'\n    </head>\n    <body>\n        <div class="reddit-embed">\n          <div class="reddit-embed-content">\n            ')
        # SOURCE LINE 50
        __M_writer(conditional_websafe(next.body()))
        __M_writer(u'\n          </div>\n          <footer class="reddit-embed-footer" role="contentinfo">\n            <p>\n                ')
        # SOURCE LINE 54
        __M_writer(conditional_websafe(text_with_links(
                    _("from discussion %(link)s on %(subreddit)s"),
                    link=dict(link_text=thing.link.title, path=thing.link.permalink, data=link_data),
                    subreddit=dict(link_text=("/r/%s" % c.site.name), path=c.site.path, data=sr_data),
                )))
        # SOURCE LINE 58
        __M_writer(u'\n            </p>\n            ')
        # SOURCE LINE 60
        __M_writer(conditional_websafe(plain_link("reddit", "/", _sr_path=False, _class="reddit-embed-footer-img", data=reddit_data)))
        __M_writer(u'\n          </footer>\n        </div>\n        <script>\n            window.REDDIT_EMBED_CONFIG = ')
        # SOURCE LINE 64
        __M_writer(conditional_websafe(unsafe(json.dumps(c.embed_config))))
        __M_writer(u';\n        </script>\n        ')
        # SOURCE LINE 66
        __M_writer(conditional_websafe(unsafe(js.use('reddit-embed'))))
        __M_writer(u'\n        ')
        # SOURCE LINE 67
        __M_writer(conditional_websafe(less_js()))
        __M_writer(u'\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


