# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1509242599.144219
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/flairtemplatelist.html'
_template_uri = '/flairtemplatelist.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 25

from r2.models import FlairTemplate, USER_FLAIR, LINK_FLAIR
from r2.lib.pages.pages import FlairTemplateEditor

empty_template = FlairTemplate()
empty_template._committed = True  # to disable unnecessary warning


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7f8d9d4c3310', context._clean_inheritance_tokens(), templateuri=u'printablebuttons.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f8d9d4c3310')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8d9d4c3310')._populate(_import_ns, [u'ynbutton'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        ynbutton = _import_ns.get('ynbutton', context.get('ynbutton', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n')
        # SOURCE LINE 31
        __M_writer(u'\n\n<div class="flairlist usertable">\n  <div class="flairrow">\n    <span class="header tagline">&nbsp;</span>\n    <span class="header narrow">')
        # SOURCE LINE 36
        __M_writer(conditional_websafe(_('user can edit?')))
        __M_writer(u'</span>\n    <span class="header">')
        # SOURCE LINE 37
        __M_writer(conditional_websafe(_('flair text')))
        __M_writer(u'</span>\n    <span class="header">')
        # SOURCE LINE 38
        __M_writer(conditional_websafe(_('css class')))
        __M_writer(u'</span>\n  </div>\n  <div class="flairtemplatelist flairlist pretty-form">\n')
        # SOURCE LINE 41
        for flair_template in thing.templates:
            # SOURCE LINE 42
            __M_writer(u'      ')
            __M_writer(conditional_websafe(flair_template))
            __M_writer(u'\n')
        # SOURCE LINE 44
        __M_writer(u'\n    ')
        # SOURCE LINE 45

        if thing.flair_type == USER_FLAIR:
            empty_id = 'empty-user-flair-template'
        elif thing.flair_type == LINK_FLAIR:
            empty_id = 'empty-link-flair-template'
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['empty_id'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 50
        __M_writer(u'\n    <div id="')
        # SOURCE LINE 51
        __M_writer(conditional_websafe(empty_id))
        __M_writer(u'">\n      ')
        # SOURCE LINE 52
        __M_writer(conditional_websafe(FlairTemplateEditor(empty_template, thing.flair_type)))
        __M_writer(u'\n    </div>\n  </div>\n  ')
        # SOURCE LINE 55
        __M_writer(conditional_websafe(ynbutton(_("clear all flair templates"), _("cleared"),
             "clearflairtemplates",
             hidden_data=dict(flair_type=thing.flair_type))))
        # SOURCE LINE 57
        __M_writer(u'\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


