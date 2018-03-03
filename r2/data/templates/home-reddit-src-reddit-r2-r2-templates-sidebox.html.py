# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1520060829.42823
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/sidebox.html'
_template_uri = '/sidebox.html'
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
    ns = runtime.TemplateNamespace('__anon_0x7fc7c783bc10', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fc7c783bc10')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c783bc10')._populate(_import_ns, [u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n<div class="sidebox ')
        # SOURCE LINE 25
        __M_writer(conditional_websafe(thing.css_class))
        __M_writer(conditional_websafe(' disabled' if thing.disabled else ''))
        __M_writer(u'">\n  <div class="morelink">\n    ')
        # SOURCE LINE 27
        __M_writer(conditional_websafe(plain_link(thing.title, thing.link, _sr_path=thing.sr_path,
                 _class='login-required access-required' if thing.show_cover else None,
                 target=thing.target, data=thing.data_attrs)))
        # SOURCE LINE 29
        __M_writer(u'\n    <div class="nub"> </div>\n  </div>\n\n')
        # SOURCE LINE 33
        if thing.subtitles:
            # SOURCE LINE 34
            if thing.show_icon:
                # SOURCE LINE 35
                __M_writer(u'      <div class="spacer">\n      ')
                # SOURCE LINE 36
                __M_writer(conditional_websafe(plain_link('', thing.link, _sr_path=thing.sr_path,
                   _class='login-required access-required' if thing.show_cover else None)))
                # SOURCE LINE 37
                __M_writer(u'\n')
                # SOURCE LINE 38
            else:
                # SOURCE LINE 39
                __M_writer(u'      <div class="spacer no-icon">\n')
            # SOURCE LINE 41
            for subtitle in thing.subtitles:
                # SOURCE LINE 42
                __M_writer(u'        <div class="subtitle">')
                __M_writer(conditional_websafe(subtitle))
                __M_writer(u'</div>\n')
            # SOURCE LINE 44
            __M_writer(u'    </div>\n')
        # SOURCE LINE 46
        __M_writer(u'</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


