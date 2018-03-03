# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1508403880.17458
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/wikipagesettings.html'
_template_uri = '/wikipagesettings.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 26

from urllib import quote
from r2.lib.pages import WrappedUser


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 24
    ns = runtime.TemplateNamespace(u'utils', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'utils')] = ns

    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7f7518adb9d0', context._clean_inheritance_tokens(), templateuri=u'printablebuttons.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f7518adb9d0')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f7518adb9d0')._populate(_import_ns, [u'ynbutton'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        utils = _mako_get_namespace(context, 'utils')
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n')
        # SOURCE LINE 24
        __M_writer(u'\n\n')
        # SOURCE LINE 29
        __M_writer(u'\n\n<div class="fancy-settings">\n')
        # SOURCE LINE 32
        if thing.show_settings:
            # SOURCE LINE 33
            __M_writer(u'        <form id="pagesettings" method="post">\n            <input type="hidden" name="uh" value="')
            # SOURCE LINE 34
            __M_writer(conditional_websafe(c.modhash))
            __M_writer(u'" />\n            ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    # SOURCE LINE 35
                    __M_writer(u'\n                <input type="radio" name="permlevel" id="permlevel0" value="0"\n')
                    # SOURCE LINE 37
                    if thing.permlevel == 0:
                        # SOURCE LINE 38
                        __M_writer(u'                        checked\n')
                    # SOURCE LINE 40
                    __M_writer(u'                /><label for="permlevel0">')
                    __M_writer(conditional_websafe(_('use subreddit wiki permissions')))
                    __M_writer(u'</label><br/>\n                <input type="radio" name="permlevel" id="permlevel1" value="1"\n')
                    # SOURCE LINE 42
                    if thing.permlevel == 1:
                        # SOURCE LINE 43
                        __M_writer(u'                    checked\n')
                    # SOURCE LINE 45
                    __M_writer(u'                /><label for="permlevel1">')
                    __M_writer(conditional_websafe(_('only approved wiki contributors for this page may edit')))
                    __M_writer(u'</label><br/>\n                <input type="radio" name="permlevel" id="permlevel2" value="2"\n')
                    # SOURCE LINE 47
                    if thing.permlevel == 2:
                        # SOURCE LINE 48
                        __M_writer(u'                    checked\n')
                    # SOURCE LINE 50
                    __M_writer(u'                /><label for="permlevel2">')
                    __M_writer(conditional_websafe(_('only mods may edit and view')))
                    __M_writer(u'</label><br/>\n            ')
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 35
                __M_writer(conditional_websafe(utils.line_field(title=u' ' + (_('who can edit this page?')))))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 51
            __M_writer(u'\n\n            ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    # SOURCE LINE 53
                    __M_writer(u'\n                <input type="checkbox" name="listed" id="listed"\n')
                    # SOURCE LINE 55
                    if thing.listed:
                        # SOURCE LINE 56
                        __M_writer(u'                        checked\n')
                    # SOURCE LINE 58
                    __M_writer(u'                /><label for="listed">')
                    __M_writer(conditional_websafe(_('show this page on the list of wiki pages')))
                    __M_writer(u'</label><br/>\n            ')
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 53
                __M_writer(conditional_websafe(utils.line_field(title=u' ' + (_('show this page on the listing?')))))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 59
            __M_writer(u'\n        </form>\n')
        # SOURCE LINE 62
        if thing.show_editors and thing.permlevel != 2:
            # SOURCE LINE 63
            __M_writer(u'    <br/>\n    ')
            def ccall(caller):
                def body():
                    dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
                    ynbutton = _import_ns.get('ynbutton', context.get('ynbutton', UNDEFINED))
                    __M_writer = context.writer()
                    # SOURCE LINE 64
                    __M_writer(u'\n        <form id="WikiAllowEditor" onsubmit="r.wiki.addUser(event)">\n            <input name="username" maxlength="20" type="text" style="width: 430px;" />\n            <button type="submit" style="font-size: 100%;">')
                    # SOURCE LINE 67
                    __M_writer(conditional_websafe(_('add')))
                    __M_writer(u'</button>\n            <h3 class="error" style="display:none" id="usereditallowerror">')
                    # SOURCE LINE 68
                    __M_writer(conditional_websafe(_('username does not exist')))
                    __M_writer(u'</h2>\n        </form>\n        <br/>\n        <ul>\n')
                    # SOURCE LINE 72
                    for user in thing.mayedit:
                        # SOURCE LINE 73
                        __M_writer(u'            <li>\n                ')
                        # SOURCE LINE 74
                        __M_writer(conditional_websafe(WrappedUser(user)))
                        __M_writer(u'\n                &mdash;&nbsp;\n                ')
                        # SOURCE LINE 76
                        __M_writer(conditional_websafe(ynbutton(_("delete"), _("done"), quote("..%s/alloweditor/del" % (c.wiki_api_url)), hidden_data=dict(username=user.name, page=thing.page), post_callback="$.refresh")))
                        __M_writer(u'\n            </li>\n')
                    # SOURCE LINE 79
                    __M_writer(u'        </ul>\n    ')
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 64
                __M_writer(conditional_websafe(utils.line_field(title=(_('allow users to edit page')))))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 80
            __M_writer(u'\n')
        # SOURCE LINE 82
        __M_writer(u'\n    <input type="submit" class="wiki_button" onclick="$(\'#pagesettings\').submit()" value="')
        # SOURCE LINE 83
        __M_writer(conditional_websafe(_('save settings')))
        __M_writer(u'" />\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


