# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1520059070.48598
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/wikieditpage.html'
_template_uri = '/wikieditpage.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23

from r2.lib.filters import keep_space


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 27
    ns = runtime.TemplateNamespace('__anon_0x7f6494e62310', context._clean_inheritance_tokens(), templateuri=u'printablebuttons.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f6494e62310')] = ns

    # SOURCE LINE 28
    ns = runtime.TemplateNamespace('__anon_0x7f6494e62410', context._clean_inheritance_tokens(), templateuri=u'usertext.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f6494e62410')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f6494e62310')._populate(_import_ns, [u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f6494e62410')._populate(_import_ns, [u'markhelp'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        toggle_button = _import_ns.get('toggle_button', context.get('toggle_button', UNDEFINED))
        markhelp = _import_ns.get('markhelp', context.get('markhelp', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'\n\n')
        # SOURCE LINE 27
        __M_writer(u'\n')
        # SOURCE LINE 28
        __M_writer(u'\n\n<div style="display: none;" id="wiki_edit_conflict">\n    <h2 class="error">there was a conflict editing</h2>\n    <h1>')
        # SOURCE LINE 32
        __M_writer(conditional_websafe(_("your edit")))
        __M_writer(u'</h1>\n    <em>')
        # SOURCE LINE 33
        __M_writer(conditional_websafe(_("this edit is for you to resolve the conflict, any text in the box below will not save.")))
        __M_writer(u'</em><br/>\n    <textarea id="youredit"></textarea>\n    <span id="yourdiff"></span>\n    <h1>')
        # SOURCE LINE 36
        __M_writer(conditional_websafe(_("current edit")))
        __M_writer(u'</h1>\n</div>\n\n<div style="display: none;" id="wiki_special_error">\n    <h1>Errors: </h1>\n    <span id="specials" class="error"></span>\n</div>\n\n<form method="post" id="editform" onsubmit="r.wiki.submitEdit(event)">\n    <textarea name="content" rows="20" cols="20" style="width: 100%" id="wiki_page_content">')
        # SOURCE LINE 45
        __M_writer(conditional_websafe(keep_space(thing.page_content)))
        __M_writer(u'</textarea>\n    ')
        # SOURCE LINE 46
        __M_writer(conditional_websafe(toggle_button("help-toggle", _("formatting help"), _("hide help"), "r.wiki.helpon", "r.wiki.helpoff")))
        __M_writer(u'\n    ')
        # SOURCE LINE 47
        __M_writer(conditional_websafe(markhelp()))
        __M_writer(u'\n    <br/><br/>\n    <label for="reason">')
        # SOURCE LINE 49
        __M_writer(conditional_websafe(_("reason for revision")))
        __M_writer(u'</label><br/>\n    <input type="text" name="reason" maxlength="256" id="wiki_revision_reason" />\n    <input type="hidden" id="previous" name="previous" value="')
        # SOURCE LINE 51
        __M_writer(conditional_websafe(thing.previous))
        __M_writer(u'" />\n    <br/><br/><input type="submit" id="wiki_save_button" class="wiki_button" value="')
        # SOURCE LINE 52
        __M_writer(conditional_websafe(_('save page')))
        __M_writer(u'" />\n    <span class="throbber" />\n</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


