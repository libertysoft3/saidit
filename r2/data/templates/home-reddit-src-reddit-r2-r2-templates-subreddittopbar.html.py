# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1520060829.120806
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/subreddittopbar.html'
_template_uri = '/subreddittopbar.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23

from r2.lib.template_helpers import format_html


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 26
    ns = runtime.TemplateNamespace('__anon_0x7fc7c7b498d0', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fc7c7b498d0')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7b498d0')._populate(_import_ns, [u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'\n')
        # SOURCE LINE 26
        __M_writer(u'\n\n<div id="sr-header-area">\n  <div class="width-clip">\n    ')
        # SOURCE LINE 30
        __M_writer(conditional_websafe(thing.my_subreddits_dropdown))
        __M_writer(u'\n\n    <div class="sr-list">\n')
        # SOURCE LINE 33
        for m in thing.sr_bar():
            # SOURCE LINE 34
            __M_writer(u'        ')
            __M_writer(conditional_websafe(m.render()))
            __M_writer(u'\n')
        # SOURCE LINE 36
        __M_writer(u'\n      ')
        # SOURCE LINE 37

        editmore = 'edit' if c.user_is_loggedin else 'more'
              
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['editmore'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 39
        __M_writer(u'\n    </div>\n\n    ')
        # SOURCE LINE 42
        __M_writer(conditional_websafe(plain_link(format_html("%s &raquo;", _(editmore)),
                 "/subreddits/", id="sr-more-link")))
        # SOURCE LINE 43
        __M_writer(u'\n  </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


