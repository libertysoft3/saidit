# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1520056307.824672
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/createsubreddit.html'
_template_uri = '/createsubreddit.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23

from r2.config import feature
from r2.lib.filters import keep_space
from r2.lib.menus import menu
from r2.lib.pages import UserText
from r2.lib.strings import strings


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 32
    ns = runtime.TemplateNamespace('__anon_0x7f6494f5ab90', context._clean_inheritance_tokens(), templateuri=u'printablebuttons.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f6494f5ab90')] = ns

    # SOURCE LINE 34
    ns = runtime.TemplateNamespace(u'utils', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'utils')] = ns

    # SOURCE LINE 31
    ns = runtime.TemplateNamespace('__anon_0x7f6494f5aad0', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f6494f5aad0')] = ns

    # SOURCE LINE 30
    ns = runtime.TemplateNamespace('__anon_0x7f6494f5aa50', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f6494f5aa50')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f6494f5ab90')._populate(_import_ns, [u'toggle_button', u'simple_button'])
        _mako_get_namespace(context, '__anon_0x7f6494f5aad0')._populate(_import_ns, [u'image_upload'])
        _mako_get_namespace(context, '__anon_0x7f6494f5aa50')._populate(_import_ns, [u'_md', u'error_field', u'language_tool', u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        utils = _mako_get_namespace(context, 'utils')
        error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
        _md = _import_ns.get('_md', context.get('_md', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 29
        __M_writer(u'\n')
        # SOURCE LINE 30
        __M_writer(u'\n')
        # SOURCE LINE 31
        __M_writer(u'\n')
        # SOURCE LINE 32
        __M_writer(u'\n\n')
        # SOURCE LINE 34
        __M_writer(u'\n\n')
        # SOURCE LINE 36
        if not thing.site and not c.user.can_create_subreddit:
            # SOURCE LINE 37
            __M_writer(u'<div class="infobar">')
            __M_writer(conditional_websafe(_md("""
# can't create sub, your account is too new or you have created too many recently

try participating in other communities on reddit for a little while first before creating your own. please post to /r/help if you need more information about this restriction, or if you require a specific exemption you can [contact the admins](/contact) to request one.
""")))
            # SOURCE LINE 41
            __M_writer(u'</div>\n')
            # SOURCE LINE 42
        else:
            # SOURCE LINE 43
            __M_writer(u'\n<div class="create-reddit fancy-settings thing"\n')
            # SOURCE LINE 45
            if thing.site:
                # SOURCE LINE 46
                __M_writer(u'       id="')
                __M_writer(conditional_websafe(thing.site._fullname))
                __M_writer(u'"\n')
            # SOURCE LINE 48
            __M_writer(u'     >\n\n<div class="pretty-form" id="sr-form">\n\n')
            # SOURCE LINE 52
            if not thing.site:
                # SOURCE LINE 53
                __M_writer(u'    ')
                def ccall(caller):
                    def body():
                        __M_writer = context.writer()
                        # SOURCE LINE 54
                        __M_writer(u'\n      <div class="usertext-edit">\n        <input type="text" name="name" id="name" class="text"\n              value="')
                        # SOURCE LINE 57
                        __M_writer(conditional_websafe(thing.name))
                        __M_writer(u'"/>\n')
                        # SOURCE LINE 58
                        if not thing.site:
                            # SOURCE LINE 59
                            __M_writer(u'          ')
                            __M_writer(conditional_websafe(error_field("SUBREDDIT_EXISTS", "name")))
                            __M_writer(u'\n          ')
                            # SOURCE LINE 60
                            __M_writer(conditional_websafe(error_field("BAD_SR_NAME", "name")))
                            __M_writer(u'\n')
                        # SOURCE LINE 62
                        __M_writer(u'      </div>\n    ')
                        return ''
                    return [body]
                context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
                try:
                    # SOURCE LINE 53
                    __M_writer(conditional_websafe(utils.line_field(description=(_("no spaces, e.g., \"books\" or \"bookclub\". avoid using solely trademarked names, e.g. use \"FansOfAcme\" instead of \"Acme\". once chosen, this name cannot be changed.")),title=(_('name')))))
                finally:
                    context.caller_stack.nextcaller = None
                # SOURCE LINE 63
                __M_writer(u'\n')
                # SOURCE LINE 64
            else:
                # SOURCE LINE 65
                __M_writer(u'  <input type="hidden" name="sr" id="name" value="')
                __M_writer(conditional_websafe(thing.site._fullname))
                __M_writer(u'"/>\n')
            # SOURCE LINE 67
            __M_writer(u'\n  ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    # SOURCE LINE 69
                    __M_writer(u'\n    <div class="usertext-edit">\n')
                    # SOURCE LINE 71
                    if thing.site:
                        # SOURCE LINE 72
                        __M_writer(u'        <input id="title" type="text" name="title" class="text"\n               value="')
                        # SOURCE LINE 73
                        __M_writer(conditional_websafe(thing.site.title))
                        __M_writer(u'"/>\n')
                        # SOURCE LINE 74
                    else:
                        # SOURCE LINE 75
                        __M_writer(u'        <input id="title" type="text" name="title" class="text" />\n')
                    # SOURCE LINE 77
                    __M_writer(u'      ')
                    __M_writer(conditional_websafe(error_field("NO_TEXT", "title")))
                    __M_writer(u'\n      ')
                    # SOURCE LINE 78
                    __M_writer(conditional_websafe(error_field("TOO_LONG", "title")))
                    __M_writer(u'\n    </div>\n  ')
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 68
                __M_writer(conditional_websafe(utils.line_field(description=(_("e.g., books: made from trees or pixels. recommendations, news, or thoughts")),title=(_('title')))))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 80
            __M_writer(u'\n\n  ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    # SOURCE LINE 83
                    __M_writer(u'\n    <div class="usertext-edit md-container">\n      <div class="md">\n        <textarea rows="1" cols="1" name="public_description" class="usertext">\n')
                    # SOURCE LINE 87
                    if thing.site and thing.site.public_description:
                        # SOURCE LINE 88
                        __M_writer(u'            ')
                        __M_writer(conditional_websafe(keep_space(thing.site.public_description or "")))
                        __M_writer(u'\n')
                    # SOURCE LINE 90
                    __M_writer(u'        </textarea>\n        <div class="bottom-area">\n          ')
                    # SOURCE LINE 92
                    __M_writer(conditional_websafe(error_field("TOO_LONG", "public_description")))
                    __M_writer(u'\n        </div>\n      </div>\n    </div>\n  ')
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 82
                __M_writer(conditional_websafe(utils.line_field(css_class=u'usertext',description=(_('Appears in search results and social media links. 500 characters max.')),title=(_('description')))))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 96
            __M_writer(u'\n\n  ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    # SOURCE LINE 99
                    __M_writer(u'\n')
                    # SOURCE LINE 100
                    if thing.site and thing.site.description:
                        # SOURCE LINE 101
                        __M_writer(u'     ')
                        __M_writer(conditional_websafe(UserText(None, text=thing.site.description or "", editable=True, creating=True, name="description", have_form=False)))
                        __M_writer(u'\n')
                        # SOURCE LINE 102
                    else:
                        # SOURCE LINE 103
                        __M_writer(u'     ')
                        __M_writer(conditional_websafe(UserText(None, text="", creating=True, name="description", have_form=False)))
                        __M_writer(u'\n')
                    # SOURCE LINE 105
                    __M_writer(u'  ')
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 98
                __M_writer(conditional_websafe(utils.line_field(css_class=u'usertext',description=(_('shown in the sidebar of your subreddit. 5120 characters max.')),title=(_('sidebar')))))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 105
            __M_writer(u'\n\n  ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    # SOURCE LINE 108
                    __M_writer(u'\n')
                    # SOURCE LINE 109
                    if thing.site and thing.site.submit_text:
                        # SOURCE LINE 110
                        __M_writer(u'     ')
                        __M_writer(conditional_websafe(UserText(None, text=thing.site.submit_text or "", editable=True, creating=True, name="submit_text", have_form=False)))
                        __M_writer(u'\n')
                        # SOURCE LINE 111
                    else:
                        # SOURCE LINE 112
                        __M_writer(u'     ')
                        __M_writer(conditional_websafe(UserText(None, text="", creating=True, name="submit_text", have_form=False)))
                        __M_writer(u'\n')
                    # SOURCE LINE 114
                    __M_writer(u'  ')
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 107
                __M_writer(conditional_websafe(utils.line_field(css_class=u'usertext',description=(_('text to show on submission page. 1024 characters max.')),title=(_('submission text')))))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 114
            __M_writer(u'\n\n  ')
            def ccall(caller):
                def body():
                    language_tool = _import_ns.get('language_tool', context.get('language_tool', UNDEFINED))
                    len = _import_ns.get('len', context.get('len', UNDEFINED))
                    __M_writer = context.writer()
                    # SOURCE LINE 116
                    __M_writer(u'\n    <div class="delete-field">\n      ')
                    # SOURCE LINE 118

                    default_lang = thing.site and thing.site.lang or c.lang or ''
                    default_lang = default_lang.split('-')[0]
                    default_lang = g.lang if len(default_lang) != 2 else default_lang
                           
                    
                    __M_locals_builtin_stored = __M_locals_builtin()
                    __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['default_lang'] if __M_key in __M_locals_builtin_stored]))
                    # SOURCE LINE 122
                    __M_writer(u'\n      ')
                    # SOURCE LINE 123
                    __M_writer(conditional_websafe(language_tool(all_langs = True, default_lang = default_lang)))
                    __M_writer(u'\n    </div>\n  ')
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 116
                __M_writer(conditional_websafe(utils.line_field(title=(_('language')))))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 125
            __M_writer(u'\n\n  ')
            def ccall(caller):
                def body():
                    capture = _import_ns.get('capture', context.get('capture', UNDEFINED))
                    __M_writer = context.writer()
                    # SOURCE LINE 127
                    __M_writer(u'\n    <div class="delete-field">\n      <table>\n      ')
                    # SOURCE LINE 130
                    __M_writer(conditional_websafe(utils.radio_type('type', "public", _("public"),
                         _("anyone can view and submit"),
                         (not thing.site or thing.site.type=='public'))))
                    # SOURCE LINE 132
                    __M_writer(u'\n      ')
                    # SOURCE LINE 133
                    __M_writer(conditional_websafe(utils.radio_type('type', "restricted", _("restricted"),
                         _("anyone can view, but only some are approved to submit links"),
                         (thing.site and thing.site.type=='restricted'))))
                    # SOURCE LINE 135
                    __M_writer(u'\n      ')
                    # SOURCE LINE 136
                    __M_writer(conditional_websafe(utils.radio_type('type', "private", _("private"),
                         _("only approved members can view and submit"),
                         (thing.site and thing.site.type=='private'))))
                    # SOURCE LINE 138
                    __M_writer(u'\n\n      ')
                    # SOURCE LINE 140
                    is_archived = thing.site and thing.site.type == 'archived' 
                    
                    __M_locals_builtin_stored = __M_locals_builtin()
                    __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['is_archived'] if __M_key in __M_locals_builtin_stored]))
                    __M_writer(u'\n')
                    # SOURCE LINE 141
                    if c.user_is_admin or is_archived:
                        # SOURCE LINE 142
                        __M_writer(u'        ')
                        __M_writer(conditional_websafe(utils.radio_type('type', "archived", _("archived"),
                           _("anyone can view, but submissions are no longer accepted"),
                           is_archived)))
                        # SOURCE LINE 144
                        __M_writer(u'\n')
                    # SOURCE LINE 146
                    __M_writer(u'\n      ')
                    # SOURCE LINE 147
                    is_gold_restricted = thing.site and thing.site.type == 'gold_restricted' 
                    
                    __M_locals_builtin_stored = __M_locals_builtin()
                    __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['is_gold_restricted'] if __M_key in __M_locals_builtin_stored]))
                    __M_writer(u'\n')
                    # SOURCE LINE 148
                    if c.user_is_admin or is_gold_restricted:
                        # SOURCE LINE 149
                        __M_writer(u'        ')
                        __M_writer(conditional_websafe(utils.radio_type('type', "gold_restricted", _("gold restricted"),
                           _("anyone can view, but only reddit gold members can submit or comment"),
                           is_gold_restricted)))
                        # SOURCE LINE 151
                        __M_writer(u'\n')
                    # SOURCE LINE 153
                    __M_writer(u'\n      ')
                    # SOURCE LINE 154
                    is_employees_only = thing.site and thing.site.type == 'employees_only' 
                    
                    __M_locals_builtin_stored = __M_locals_builtin()
                    __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['is_employees_only'] if __M_key in __M_locals_builtin_stored]))
                    __M_writer(u'\n')
                    # SOURCE LINE 155
                    if c.user.employee:
                        # SOURCE LINE 156
                        __M_writer(u'        ')
                        __M_writer(conditional_websafe(utils.radio_type('type', "employees_only", _("employees only"),
                           _("only reddit employees can view; the employee list is pulled from live config"),
                           is_employees_only)))
                        # SOURCE LINE 158
                        __M_writer(u'\n')
                    # SOURCE LINE 160
                    __M_writer(u'\n      ')
                    # SOURCE LINE 161

                    is_gold_only = thing.site and thing.site.type == 'gold_only'
                    can_set_gold_only = (is_gold_only or c.user_is_admin or
                            (not thing.site and (c.user.gold or c.user.gold_charter)))
                    if is_gold_only:
                        hover_title = "[!]"
                        hover_text = _('If you switch this subreddit to another type, you will not be able to switch back to "gold only" without the assistance of an admin')
                    else:
                        hover_title = "[?]"
                        hover_text = unsafe(capture(_md, 'BETA: Subreddits can be created as "gold only" during creation by a user that has gold. You can find more info about this feature [here](/gold/about#gold-only-subreddits)'))
                          
                    
                    __M_locals_builtin_stored = __M_locals_builtin()
                    __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['can_set_gold_only','hover_text','hover_title','is_gold_only'] if __M_key in __M_locals_builtin_stored]))
                    # SOURCE LINE 171
                    __M_writer(u'\n      ')
                    # SOURCE LINE 172
                    __M_writer(conditional_websafe(utils.radio_type('type', "gold_only", _("gold only"),
              _("only reddit gold members can view and submit"),
              checked=is_gold_only, disabled=not can_set_gold_only, hover_title=hover_title,
              hover_text=hover_text)))
                    # SOURCE LINE 175
                    __M_writer(u'\n      </table>\n      ')
                    # SOURCE LINE 177
                    __M_writer(conditional_websafe(error_field("INVALID_OPTION", "type")))
                    __M_writer(u'\n      ')
                    # SOURCE LINE 178
                    __M_writer(conditional_websafe(error_field("ADMIN_REQUIRED", "type")))
                    __M_writer(u'\n      ')
                    # SOURCE LINE 179
                    __M_writer(conditional_websafe(error_field("GOLD_REQUIRED", "type")))
                    __M_writer(u'\n      ')
                    # SOURCE LINE 180
                    __M_writer(conditional_websafe(error_field("CANT_CONVERT_TO_GOLD_ONLY", "type")))
                    __M_writer(u'\n    </div>\n  ')
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 127
                __M_writer(conditional_websafe(utils.line_field(title=(_('type')))))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 182
            __M_writer(u'\n\n  ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    # SOURCE LINE 184
                    __M_writer(u'\n    <div class="delete-field">\n      <table>\n        ')
                    # SOURCE LINE 187
                    __M_writer(conditional_websafe(utils.radio_type('link_type', "any", _("any"),
                           _("any link type is allowed"),
                           (not thing.site or thing.site.link_type=='any'))))
                    # SOURCE LINE 189
                    __M_writer(u'\n        ')
                    # SOURCE LINE 190
                    __M_writer(conditional_websafe(utils.radio_type('link_type', "link", _("links only"),
                           _("only links to external sites are allowed"),
                           (thing.site and thing.site.link_type=='link'))))
                    # SOURCE LINE 192
                    __M_writer(u'\n        ')
                    # SOURCE LINE 193
                    __M_writer(conditional_websafe(utils.radio_type('link_type', "self", _("text posts only"),
                           _("only text/self posts are allowed"),
                           (thing.site and thing.site.link_type=='self'))))
                    # SOURCE LINE 195
                    __M_writer(u'\n      </table>\n      ')
                    # SOURCE LINE 197
                    __M_writer(conditional_websafe(error_field("INVALID_OPTION", "link_type")))
                    __M_writer(u'\n    </div>\n    <div class="usertext-edit">\n      <div class="delete-field">\n        <label for="submit_link_label">')
                    # SOURCE LINE 201
                    __M_writer(conditional_websafe(_('Custom label for submit link button (blank for default):')))
                    __M_writer(u'</label>\n        <input id="submit_link_label" type="text" name="submit_link_label" maxlength="60" placeholder="')
                    # SOURCE LINE 202
                    __M_writer(conditional_websafe(strings.submit_link_label))
                    __M_writer(u'"\n')
                    # SOURCE LINE 203
                    if thing.site:
                        # SOURCE LINE 204
                        __M_writer(u'                value="')
                        __M_writer(conditional_websafe(thing.site.submit_link_label))
                        __M_writer(u'"\n')
                    # SOURCE LINE 206
                    __M_writer(u'        >\n      </div>\n      <div class="delete-field">\n        <label for="submit_text_label">')
                    # SOURCE LINE 209
                    __M_writer(conditional_websafe(_('Custom label for submit text post button (blank for default):')))
                    __M_writer(u'</label>\n        <input id="submit_text_label" type="text" name="submit_text_label" maxlength="60" placeholder="')
                    # SOURCE LINE 210
                    __M_writer(conditional_websafe(strings.submit_text_label))
                    __M_writer(u'"\n')
                    # SOURCE LINE 211
                    if thing.site:
                        # SOURCE LINE 212
                        __M_writer(u'                value="')
                        __M_writer(conditional_websafe(thing.site.submit_text_label))
                        __M_writer(u'"\n')
                    # SOURCE LINE 214
                    __M_writer(u'        >\n      </div>\n    </div>\n  ')
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 184
                __M_writer(conditional_websafe(utils.line_field(title=(_('content options')))))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 217
            __M_writer(u'\n  ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    # SOURCE LINE 218
                    __M_writer(u'\n    <div class="delete-field">\n      <table>\n        ')
                    # SOURCE LINE 221
                    __M_writer(conditional_websafe(utils.radio_type('wikimode', "disabled", _("disabled"),
                           _("Wiki is disabled for all users except mods"),
                           (not thing.site or thing.site.wikimode == 'disabled'))))
                    # SOURCE LINE 223
                    __M_writer(u'\n        ')
                    # SOURCE LINE 224
                    __M_writer(conditional_websafe(utils.radio_type('wikimode', "modonly", _("mod editing"),
                           _("Only mods, approved wiki contributors, or those on a page's edit list may edit"),
                           (thing.site and thing.site.wikimode == 'modonly'))))
                    # SOURCE LINE 226
                    __M_writer(u'\n        ')
                    # SOURCE LINE 227
                    __M_writer(conditional_websafe(utils.radio_type('wikimode', "anyone", _("anyone"),
                           _("Anyone who can submit to the subreddit may edit"),
                           (thing.site and thing.site.wikimode == 'anyone'))))
                    # SOURCE LINE 229
                    __M_writer(u'\n      </table>\n      ')
                    # SOURCE LINE 231
                    __M_writer(conditional_websafe(error_field("INVALID_OPTION", "wikimode")))
                    __M_writer(u'\n    </div>\n    <div class="usertext-edit">\n    <div class="delete-field">\n    <label for="wiki_edit_karma">')
                    # SOURCE LINE 235
                    __M_writer(conditional_websafe(_('Subreddit karma required to edit and create wiki pages:')))
                    __M_writer(u'</label>\n')
                    # SOURCE LINE 236
                    if thing.site:
                        # SOURCE LINE 237
                        __M_writer(u'            <input id="wiki_edit_karma" type="text" name="wiki_edit_karma"\n                   value="')
                        # SOURCE LINE 238
                        __M_writer(conditional_websafe(thing.site.wiki_edit_karma))
                        __M_writer(u'"/>\n')
                        # SOURCE LINE 239
                    else:
                        # SOURCE LINE 240
                        __M_writer(u'            <input id="wiki_edit_karma" type="text" name="wiki_edit_karma" value="100" />\n')
                    # SOURCE LINE 242
                    __M_writer(u'        ')
                    __M_writer(conditional_websafe(error_field("BAD_NUMBER", "wiki_edit_karma")))
                    __M_writer(u'\n    </div>\n    <div class="delete-field">\n    <label for="wiki_edit_age">')
                    # SOURCE LINE 245
                    __M_writer(conditional_websafe(_('Account age (days) required to edit and create wiki pages:')))
                    __M_writer(u'</label>\n')
                    # SOURCE LINE 246
                    if thing.site:
                        # SOURCE LINE 247
                        __M_writer(u'            <input id="wiki_edit_age" type="text" name="wiki_edit_age"\n                   value="')
                        # SOURCE LINE 248
                        __M_writer(conditional_websafe(thing.site.wiki_edit_age))
                        __M_writer(u'"/>\n')
                        # SOURCE LINE 249
                    else:
                        # SOURCE LINE 250
                        __M_writer(u'            <input id="wiki_edit_age" type="text" name="wiki_edit_age" value="0" />\n')
                    # SOURCE LINE 252
                    __M_writer(u'        ')
                    __M_writer(conditional_websafe(error_field("BAD_NUMBER", "wiki_edit_age")))
                    __M_writer(u'\n    </div>\n    </div>\n  ')
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 218
                __M_writer(conditional_websafe(utils.line_field(title=(_('wiki')))))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 255
            __M_writer(u'\n\n  ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    # SOURCE LINE 257
                    __M_writer(u'\n  \t<div class="delete-field">\n        <p class="little gray">')
                    # SOURCE LINE 259
                    __M_writer(conditional_websafe(_("high is the standard filter, low disables most filtering, all will filter every post initially and they will need to be approved manually to be visible.")))
                    __M_writer(u'</p>\n  \t\t<table>\n  \t\t\t<tr>\n  \t\t\t\t<td>')
                    # SOURCE LINE 262
                    __M_writer(conditional_websafe(_("links")))
                    __M_writer(u':</td>\n  \t\t\t\t<td>\n  \t\t\t\t\t')
                    # SOURCE LINE 264
                    __M_writer(conditional_websafe(utils.inline_radio_type('spam_links', 'low', _("low"),
  						checked=thing.site and thing.site.spam_links == 'low')))
                    # SOURCE LINE 265
                    __M_writer(u'\n  \t\t\t\t\t')
                    # SOURCE LINE 266
                    __M_writer(conditional_websafe(utils.inline_radio_type('spam_links', 'high', _("high"),
  						checked=not thing.site or thing.site.spam_links == 'high')))
                    # SOURCE LINE 267
                    __M_writer(u'\n  \t\t\t\t\t')
                    # SOURCE LINE 268
                    __M_writer(conditional_websafe(utils.inline_radio_type('spam_links', 'all', _("all"),
  						checked=thing.site and thing.site.spam_links == 'all')))
                    # SOURCE LINE 269
                    __M_writer(u'\n\t  \t\t\t</td>\n\t  \t\t</tr>\n\t  \t\t<tr>\n\t  \t\t\t<td>')
                    # SOURCE LINE 273
                    __M_writer(conditional_websafe(_("self posts")))
                    __M_writer(u':</td>\n\t  \t\t\t<td>\n\t  \t\t\t\t')
                    # SOURCE LINE 275
                    __M_writer(conditional_websafe(utils.inline_radio_type('spam_selfposts', 'low', _("low"),
  						checked=thing.site and thing.site.spam_selfposts == 'low')))
                    # SOURCE LINE 276
                    __M_writer(u'\n  \t\t\t\t\t')
                    # SOURCE LINE 277
                    __M_writer(conditional_websafe(utils.inline_radio_type('spam_selfposts', 'high', _("high"),
  						checked=not thing.site or thing.site.spam_selfposts == 'high')))
                    # SOURCE LINE 278
                    __M_writer(u'\n  \t\t\t\t\t')
                    # SOURCE LINE 279
                    __M_writer(conditional_websafe(utils.inline_radio_type('spam_selfposts', 'all', _("all"),
  						checked=thing.site and thing.site.spam_selfposts == 'all')))
                    # SOURCE LINE 280
                    __M_writer(u'\n\t  \t\t\t</td>\n\t  \t\t</tr>\n\t  \t\t<tr>\n\t  \t\t\t<td>')
                    # SOURCE LINE 284
                    __M_writer(conditional_websafe(_("comments")))
                    __M_writer(u':</td>\n\t  \t\t\t<td>\n\t  \t\t\t\t')
                    # SOURCE LINE 286
                    __M_writer(conditional_websafe(utils.inline_radio_type('spam_comments', 'low', _("low"),
  						checked=not thing.site or thing.site.spam_comments == 'low')))
                    # SOURCE LINE 287
                    __M_writer(u'\n  \t\t\t\t\t')
                    # SOURCE LINE 288
                    __M_writer(conditional_websafe(utils.inline_radio_type('spam_comments', 'high', _("high"),
  						checked=thing.site and thing.site.spam_comments == 'high')))
                    # SOURCE LINE 289
                    __M_writer(u'\n  \t\t\t\t\t')
                    # SOURCE LINE 290
                    __M_writer(conditional_websafe(utils.inline_radio_type('spam_comments', 'all', _("all"),
  						checked=thing.site and thing.site.spam_comments == 'all')))
                    # SOURCE LINE 291
                    __M_writer(u'\n\t  \t\t\t</td>\n\t  \t\t</tr>\n\t\t</table>\n  \t</div>\n  ')
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 257
                __M_writer(conditional_websafe(utils.line_field(title=(_('spam filter strength')))))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 296
            __M_writer(u'\n\n  ')
            def ccall(caller):
                def body():
                    getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
                    __M_writer = context.writer()
                    # SOURCE LINE 298
                    __M_writer(u'\n    <div class="delete-field">\n      <ul>\n        <li>\n          <input class="nomargin" type="checkbox"\n                 name="over_18" id="over_18"\n')
                    # SOURCE LINE 304
                    if thing.site and thing.site.over_18:
                        # SOURCE LINE 305
                        __M_writer(u'                   checked="checked"\n')
                    # SOURCE LINE 307
                    __M_writer(u'          >\n          <label for="over_18">\n            ')
                    # SOURCE LINE 309
                    __M_writer(conditional_websafe(_("viewers must be over eighteen years old")))
                    __M_writer(u'\n          </label>\n        </li>\n')
                    # SOURCE LINE 312
                    if not thing.site or not thing.site.quarantine:
                        # SOURCE LINE 313
                        __M_writer(u'        <li>\n          <input class="nomargin" type="checkbox"\n                 name="allow_top" id="allow_top"\n')
                        # SOURCE LINE 316
                        if not thing.site or thing.site.allow_top:
                            # SOURCE LINE 317
                            __M_writer(u'                   checked="checked"\n')
                        # SOURCE LINE 319
                        __M_writer(u'          >\n          <label for="allow_top">\n            ')
                        # SOURCE LINE 321
                        __M_writer(conditional_websafe(_("allow this subreddit to be included /r/all as well as the default and trending lists")))
                        __M_writer(u'\n          </label>\n        </li>\n        <li>\n          <input class="nomargin" type="checkbox"\n                 name="show_media" id="show_media"\n')
                        # SOURCE LINE 327
                        if thing.site and thing.site.show_media:
                            # SOURCE LINE 328
                            __M_writer(u'                   checked="checked"\n')
                        # SOURCE LINE 330
                        __M_writer(u'          >\n          <label for="show_media">\n            ')
                        # SOURCE LINE 332
                        __M_writer(conditional_websafe(_("show thumbnail images of content")))
                        __M_writer(u'\n          </label>\n        </li>\n')
                        # SOURCE LINE 335
                        if thing.feature_autoexpand_media_previews:
                            # SOURCE LINE 336
                            __M_writer(u'          <li>\n            <input class="nomargin" type="checkbox"\n                   name="show_media_preview" id="show_media_preview"\n')
                            # SOURCE LINE 339
                            if thing.site and thing.site.show_media_preview:
                                # SOURCE LINE 340
                                __M_writer(u'                     checked="checked"\n')
                            # SOURCE LINE 342
                            __M_writer(u'            >\n            <label for="show_media_preview">\n              ')
                            # SOURCE LINE 344
                            __M_writer(conditional_websafe(_("expand media previews on comments pages")))
                            __M_writer(u'\n            </label>\n          </li>\n')
                    # SOURCE LINE 349
                    __M_writer(u'        <li>\n          <input class="nomargin" type="checkbox"\n                 name="exclude_banned_modqueue" id="exclude_banned_modqueue"\n')
                    # SOURCE LINE 352
                    if thing.site and thing.site.exclude_banned_modqueue:
                        # SOURCE LINE 353
                        __M_writer(u'                   checked="checked"\n')
                    # SOURCE LINE 355
                    __M_writer(u'          >\n          <label for="exclude_banned_modqueue">\n            ')
                    # SOURCE LINE 357
                    __M_writer(conditional_websafe(_("exclude posts by site-wide banned users from modqueue/unmoderated")))
                    __M_writer(u'\n          </label>\n        </li>\n        <li>\n          <input class="nomargin" type="checkbox"\n                 name="public_traffic" id="public_traffic"\n                 ')
                    # SOURCE LINE 363
                    __M_writer(conditional_websafe(thing.site and thing.site.public_traffic and "checked='checked'" or ""))
                    __M_writer(u'>\n          <label for="public_traffic">\n            ')
                    # SOURCE LINE 365
                    __M_writer(conditional_websafe(_("make the traffic stats page available to everyone")))
                    __M_writer(u'\n          </label>\n        </li>\n        <li>\n          <input class="nomargin" type="checkbox"\n                 name="collapse_deleted_comments" id="collapse_deleted_comments"\n')
                    # SOURCE LINE 371
                    if thing.site and thing.site.collapse_deleted_comments:
                        # SOURCE LINE 372
                        __M_writer(u'                   checked="checked"\n')
                    # SOURCE LINE 374
                    __M_writer(u'          >\n          <label for="collapse_deleted_comments">\n            ')
                    # SOURCE LINE 376
                    __M_writer(conditional_websafe(_("collapse deleted and removed comments")))
                    __M_writer(u'\n          </label>\n        </li>\n')
                    # SOURCE LINE 379
                    if thing.site and thing.site.type == 'gold_only':
                        # SOURCE LINE 380
                        __M_writer(u'          <li>\n            <input class="nomargin" type="checkbox"\n                   name="hide_ads" id="hide_ads"\n')
                        # SOURCE LINE 383
                        if thing.site.hide_ads:
                            # SOURCE LINE 384
                            __M_writer(u'                     checked="checked"\n')
                        # SOURCE LINE 386
                        __M_writer(u'            >\n            <label class="buygold" for="hide_ads">\n              ')
                        # SOURCE LINE 388
                        __M_writer(conditional_websafe(_("hide ads (only available for gold only subreddits)")))
                        __M_writer(u'\n            </label>\n          </li>\n')
                    # SOURCE LINE 392
                    __M_writer(u'        ')
                    __M_writer(conditional_websafe(error_field("GOLD_ONLY_SR_REQUIRED", "hide_ads")))
                    __M_writer(u'\n      </ul>\n      <div class="usertext-edit">\n        <label for="suggested_comment_sort">')
                    # SOURCE LINE 395
                    __M_writer(conditional_websafe(_('suggested comment sort')))
                    __M_writer(u'&#32;<span class="gray">')
                    __M_writer(conditional_websafe(_('(all comment threads will use this sorting method by default)')))
                    __M_writer(u'</span></label>\n        <select class="nomargin" name="suggested_comment_sort" id="suggested_comment_sort">\n           <option value="">')
                    # SOURCE LINE 397
                    __M_writer(conditional_websafe(_('none (recommended for most subreddits)')))
                    __M_writer(u'</option>\n')
                    # SOURCE LINE 398
                    for sort in thing.comment_sorts:
                        # SOURCE LINE 399
                        __M_writer(u'             <option ')
                        __M_writer(conditional_websafe('selected="selected"' if thing.site and sort == thing.site.suggested_comment_sort else ''))
                        __M_writer(u' value="')
                        __M_writer(conditional_websafe(sort))
                        __M_writer(u'">')
                        __M_writer(conditional_websafe(getattr(menu, sort, sort)))
                        __M_writer(u'</option>\n')
                    # SOURCE LINE 401
                    __M_writer(u'        </select>\n      </div>\n    </div>\n    <div class="usertext-edit">\n      <div class="delete-field">\n        <label for="comment_score_hide_mins">')
                    # SOURCE LINE 406
                    __M_writer(conditional_websafe(_('Minutes to hide comment scores:')))
                    __M_writer(u'</label>\n')
                    # SOURCE LINE 407
                    if thing.site:
                        # SOURCE LINE 408
                        __M_writer(u'                <input id="comment_score_hide_mins" type="text" name="comment_score_hide_mins" placeholder="0"\n                       value="')
                        # SOURCE LINE 409
                        __M_writer(conditional_websafe(thing.site.comment_score_hide_mins))
                        __M_writer(u'" />\n')
                        # SOURCE LINE 410
                    else:
                        # SOURCE LINE 411
                        __M_writer(u'                <input id="comment_score_hide_mins" type="text" name="comment_score_hide_mins" value="0" placeholder="0" />\n')
                    # SOURCE LINE 413
                    __M_writer(u'            ')
                    __M_writer(conditional_websafe(error_field("BAD_NUMBER", "comment_score_hide_mins")))
                    __M_writer(u'\n      </div>\n    </div>\n  ')
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 298
                __M_writer(conditional_websafe(utils.line_field(title=(_('other options')))))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 416
            __M_writer(u'\n\n')
            # SOURCE LINE 418
            if thing.site and thing.site.domain != thing.site._defaults['domain']:
                # SOURCE LINE 419
                __M_writer(u'  ')
                def ccall(caller):
                    def body():
                        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
                        toggle_button = _import_ns.get('toggle_button', context.get('toggle_button', UNDEFINED))
                        __M_writer = context.writer()
                        __M_writer(u'\n    <div class="usertext-edit">\n')
                        # SOURCE LINE 421
                        if thing.site:
                            # SOURCE LINE 422
                            __M_writer(u'        <input id="domain" type="text" name="domain" class="text"\n               value="')
                            # SOURCE LINE 423
                            __M_writer(conditional_websafe(getattr(thing.site, 'domain', None) or ""))
                            __M_writer(u'"/>\n')
                            # SOURCE LINE 424
                        else:
                            # SOURCE LINE 425
                            __M_writer(u'        <input id="domain" type="text" name="domain" class="text" />\n')
                        # SOURCE LINE 427
                        __M_writer(u'      <div class="bottom-area">\n        ')
                        # SOURCE LINE 428
                        __M_writer(conditional_websafe(toggle_button("help-toggle", _("what's this?"), _("hide help"),
            "helpon", "helpoff")))
                        # SOURCE LINE 429
                        __M_writer(u'\n      </div>\n      <div class="infobar markhelp md" style="display: none">\n        ')
                        # SOURCE LINE 432
                        __M_writer(conditional_websafe(_("Own a domain?  Enter it here and then go to your DNS provider and add a CNAME record aliasing your domain to rhs.reddit.com. You will be able to access your reddit through your domain.")))
                        __M_writer(u'\n      </div>\n    </div>\n  ')
                        return ''
                    return [body]
                context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
                try:
                    # SOURCE LINE 419
                    __M_writer(conditional_websafe(utils.line_field(css_class=u'usertext',title=(_('domain')))))
                finally:
                    context.caller_stack.nextcaller = None
                # SOURCE LINE 435
                __M_writer(u'\n')
            # SOURCE LINE 437
            __M_writer(u'\n')
            # SOURCE LINE 438
            if thing.site:
                # SOURCE LINE 439
                __M_writer(u'    ')
                def ccall(caller):
                    def body():
                        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
                        __M_writer = context.writer()
                        __M_writer(u'\n      <ul class="upload">\n        <li>\n        ')
                        # SOURCE LINE 442
                        __M_writer(conditional_websafe(plain_link(_("edit the stylesheet"),
                      "/about/stylesheet",
                      _sr_path = True)))
                        # SOURCE LINE 444
                        __M_writer(u'\n        &#32;\n        <span class="gray">(')
                        # SOURCE LINE 446
                        __M_writer(conditional_websafe(_("leaves this page")))
                        __M_writer(u')</span>\n        </li>\n')
                        # SOURCE LINE 448
                        if thing.allow_image_upload:
                            # SOURCE LINE 449
                            __M_writer(u'          <li>\n            <label for="header-title">header mouseover text:</label>\n            <input type="text" name="header-title" id="header-title"\n                   value="')
                            # SOURCE LINE 452
                            __M_writer(conditional_websafe(thing.site.header_title))
                            __M_writer(u'"\n                   />\n          </li>\n          <li>\n            ')
                            def ccall(caller):
                                def body():
                                    __M_writer = context.writer()
                                    # SOURCE LINE 459
                                    __M_writer(u'\n              <br/>\n              <button id="delete-img" class="delete-img"\n')
                                    # SOURCE LINE 462
                                    if not thing.site.header:
                                        # SOURCE LINE 463
                                        __M_writer(u'                         style="display: none;"\n')
                                    # SOURCE LINE 465
                                    __M_writer(u'                      onclick="return post_form(this.form, \'delete_sr_header\');">\n                ')
                                    # SOURCE LINE 466
                                    __M_writer(conditional_websafe(_('restore default header')))
                                    __M_writer(u'\n              </button>\n              <div class="clearleft"></div>\n              <input type="hidden" name="uh" value="')
                                    # SOURCE LINE 469
                                    __M_writer(conditional_websafe(c.modhash))
                                    __M_writer(u'" />\n              <input type="hidden" name="r"  value="')
                                    # SOURCE LINE 470
                                    __M_writer(conditional_websafe(c.site.name))
                                    __M_writer(u'" />\n              <input type="hidden" name="header" value="1" />\n\n              <script type="text/javascript">\n                function on_image_success(img) {\n                   $("#header-img").log().attr("src", img.attr("src"));\n                }\n              </script>\n            ')
                                    return ''
                                return [body]
                            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
                            try:
                                # SOURCE LINE 456
                                __M_writer(conditional_websafe(utils.image_upload(current_image=(thing.site.header),post_target=u'/api/upload_sr_img',ask_type=(True),label=(_('upload header image')))))
                            finally:
                                context.caller_stack.nextcaller = None
                            # SOURCE LINE 478
                            __M_writer(u'\n          </li>\n')
                        # SOURCE LINE 481
                        __M_writer(u'      </ul>\n    ')
                        return ''
                    return [body]
                context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
                try:
                    # SOURCE LINE 439
                    __M_writer(conditional_websafe(utils.line_field(title=(_('look and feel')))))
                finally:
                    context.caller_stack.nextcaller = None
                # SOURCE LINE 482
                __M_writer(u'\n')
            # SOURCE LINE 484
            __M_writer(u'\n')
            # SOURCE LINE 485
            if thing.site and feature.is_enabled('related_subreddits'):
                # SOURCE LINE 486
                __M_writer(u'  ')
                def ccall(caller):
                    def body():
                        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
                        __M_writer = context.writer()
                        __M_writer(u'\n    <div class="delete-field">\n      <p class="little gray">')
                        # SOURCE LINE 488
                        __M_writer(conditional_websafe(_('similar or related subreddits.')))
                        __M_writer(u'</p>\n      <ul id="related-srs" class="subreddits">\n        <li id="sr-template" style="display:none">\n          <a href=""></a>\n          <button class="remove-sr" onclick="remove_related_sr(this.parentNode)">')
                        # SOURCE LINE 492
                        __M_writer(conditional_websafe(_('remove')))
                        __M_writer(u'</button>\n        </li>\n')
                        # SOURCE LINE 494
                        for sr in thing.site.related_subreddits:
                            # SOURCE LINE 495
                            if sr:
                                # SOURCE LINE 496
                                __M_writer(u'            <li data-name="')
                                __M_writer(conditional_websafe(sr.lower()))
                                __M_writer(u'">\n              <a href="/r/')
                                # SOURCE LINE 497
                                __M_writer(conditional_websafe(sr))
                                __M_writer(u'">/r/')
                                __M_writer(conditional_websafe(sr))
                                __M_writer(u'</a>\n              <button class="remove-sr" onclick="remove_related_sr(this.parentNode)">')
                                # SOURCE LINE 498
                                __M_writer(conditional_websafe(_('remove')))
                                __M_writer(u'</button>\n            </li>\n')
                        # SOURCE LINE 502
                        __M_writer(u'      </ul>\n')
                        # SOURCE LINE 503
                        if hasattr(thing, 'subreddit_selector'):
                            # SOURCE LINE 504
                            __M_writer(u'      <form id="add-related-sr" onsubmit="return add_related_sr(this)">\n        ')
                            # SOURCE LINE 505
                            __M_writer(conditional_websafe(thing.subreddit_selector))
                            __M_writer(u'\n      </form>\n')
                        # SOURCE LINE 508
                        __M_writer(u'      <textarea id="related_subreddits" name="related_subreddits" style="display:none;">\n        ')
                        # SOURCE LINE 509
                        __M_writer(conditional_websafe(keep_space('\n'.join(thing.site.related_subreddits))))
                        __M_writer(u'\n      </textarea>\n      ')
                        # SOURCE LINE 511
                        __M_writer(conditional_websafe(error_field("BAD_SR_NAME", "related_subreddits")))
                        __M_writer(u'\n      ')
                        # SOURCE LINE 512
                        __M_writer(conditional_websafe(error_field("TOO_MANY_SUBREDDITS", "related_subreddits")))
                        __M_writer(u'\n      ')
                        # SOURCE LINE 513
                        __M_writer(conditional_websafe(error_field("SUBREDDIT_NOEXIST", "related_subreddits")))
                        __M_writer(u'\n      <script type="text/javascript">\n        function add_related_sr(form) {\n          $(\'.SUBREDDIT_NOEXIST.field-sr\').hide();\n\n          var sr_name = form.sr.value.trim();\n          if (sr_name) {\n            $.post(\'/api/search_reddit_names.json\', { query: sr_name, exact: true }, \'json\')\n            .done(function(r) {\n              var sr_name = r.names[0];\n              var sr_path = \'/r/\' + sr_name;\n\n              var $sr_list = $(\'#related-srs\');\n              var $sr_item = $sr_list.find(\'[data-name=\' + sr_name.toLowerCase() + \']\');\n              if (!$sr_item.length) {\n                $sr_item = $(\'#sr-template\').clone().removeAttr(\'id\');\n                $sr_item.data(\'name\', sr_name.toLowerCase()).show();\n                $sr_item.find(\'a\').attr(\'href\', sr_path).text(sr_path);\n              }\n              $sr_item.appendTo($sr_list);\n\n              var re = new RegExp(\'(^|\\n)\' + sr_name + \'(\\n|$)\', \'gim\');\n              var $input = $(\'#related_subreddits\');\n              $input.val($input.val().replace(re, \'\').trim() + \'\\n\' + sr_name);\n\n              $(\'#sr-autocomplete\').val(\'\');\n            })\n            .fail(function() {\n              $(\'.SUBREDDIT_NOEXIST.field-sr\').text(r._("that subreddit doesn\'t exist")).show();\n            });\n          }\n\n          return false;\n        }\n\n        function remove_related_sr(item) {\n          var $sr_item = $(item);\n          var sr_name = $sr_item.data(\'name\');\n\n          $sr_item.remove();\n\n          var re = new RegExp(\'(^|\\n)\' + sr_name + \'(\\n|$)\', \'gim\');\n          var $input = $(\'#related_subreddits\');\n          $input.val($input.val().replace(re, \'\\n\').trim());\n        }\n      </script>\n    </div>\n  ')
                        return ''
                    return [body]
                context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
                try:
                    # SOURCE LINE 486
                    __M_writer(conditional_websafe(utils.line_field(title=(_('related subreddits')))))
                finally:
                    context.caller_stack.nextcaller = None
                # SOURCE LINE 560
                __M_writer(u'\n')
            # SOURCE LINE 562
            __M_writer(u'\n')
            # SOURCE LINE 563
            if feature.is_enabled('mobile_settings'):
                # SOURCE LINE 564
                __M_writer(u'  ')
                def ccall(caller):
                    def body():
                        __M_writer = context.writer()
                        __M_writer(u'\n    <ul class="upload">\n')
                        # SOURCE LINE 566
                        if thing.site:
                            # SOURCE LINE 567
                            __M_writer(u'      <li>\n        <p><label>')
                            # SOURCE LINE 568
                            __M_writer(conditional_websafe(_('icon image')))
                            __M_writer(u'</label> <span class="gray">')
                            __M_writer(conditional_websafe(_('icon must be 256x256 pixels. PNG or JPG only.')))
                            __M_writer(u'</span></p>\n        ')
                            def ccall(caller):
                                def body():
                                    __M_writer = context.writer()
                                    # SOURCE LINE 571
                                    __M_writer(u'\n          <button id="delete-icon" class="delete-img"\n')
                                    # SOURCE LINE 573
                                    if not thing.site.icon_img:
                                        # SOURCE LINE 574
                                        __M_writer(u'                    style="display: none;"\n')
                                    # SOURCE LINE 576
                                    __M_writer(u'                  onclick="return post_form(this.form, \'delete_sr_icon\');">\n            ')
                                    # SOURCE LINE 577
                                    __M_writer(conditional_websafe(_('remove custom icon image')))
                                    __M_writer(u'\n          </button>\n          <div class="clearleft"></div>\n          <input type="hidden" name="uh" value="')
                                    # SOURCE LINE 580
                                    __M_writer(conditional_websafe(c.modhash))
                                    __M_writer(u'">\n          <input type="hidden" name="r"  value="')
                                    # SOURCE LINE 581
                                    __M_writer(conditional_websafe(c.site.name))
                                    __M_writer(u'">\n          <input type="hidden" name="upload_type" value="icon">\n        ')
                                    return ''
                                return [body]
                            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
                            try:
                                # SOURCE LINE 569
                                __M_writer(conditional_websafe(utils.image_upload(current_image=(thing.site.icon_img),post_target=u'/api/upload_sr_img',form_id=u'icon-upload')))
                            finally:
                                context.caller_stack.nextcaller = None
                            # SOURCE LINE 583
                            __M_writer(u'\n      </li>\n      <li>\n        <p><label>')
                            # SOURCE LINE 586
                            __M_writer(conditional_websafe(_('header image')))
                            __M_writer(u'</label> <span class="gray">')
                            __M_writer(conditional_websafe(_('header should have 10:3 aspect ratio. PNG or JPG only.')))
                            __M_writer(u'</span></p>\n        <p class="little gray">')
                            # SOURCE LINE 587
                            __M_writer(conditional_websafe(_('minimum size: 640x192px')))
                            __M_writer(u' / ')
                            __M_writer(conditional_websafe(_('maximum size: 1280x384px')))
                            __M_writer(u'</span></p>\n        ')
                            def ccall(caller):
                                def body():
                                    __M_writer = context.writer()
                                    # SOURCE LINE 590
                                    __M_writer(u'\n          <button id="delete-banner" class="delete-img"\n')
                                    # SOURCE LINE 592
                                    if not thing.site.banner_img:
                                        # SOURCE LINE 593
                                        __M_writer(u'                    style="display: none;"\n')
                                    # SOURCE LINE 595
                                    __M_writer(u'                  onclick="return post_form(this.form, \'delete_sr_banner\');">\n            ')
                                    # SOURCE LINE 596
                                    __M_writer(conditional_websafe(_('remove custom header image')))
                                    __M_writer(u'\n          </button>\n          <div class="clearleft"></div>\n          <input type="hidden" name="uh" value="')
                                    # SOURCE LINE 599
                                    __M_writer(conditional_websafe(c.modhash))
                                    __M_writer(u'">\n          <input type="hidden" name="r"  value="')
                                    # SOURCE LINE 600
                                    __M_writer(conditional_websafe(c.site.name))
                                    __M_writer(u'">\n          <input type="hidden" name="upload_type" value="banner">\n        ')
                                    return ''
                                return [body]
                            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
                            try:
                                # SOURCE LINE 588
                                __M_writer(conditional_websafe(utils.image_upload(current_image=(thing.site.banner_img),post_target=u'/api/upload_sr_img',form_id=u'banner-upload')))
                            finally:
                                context.caller_stack.nextcaller = None
                            # SOURCE LINE 602
                            __M_writer(u'\n      </li>\n')
                        # SOURCE LINE 605
                        __M_writer(u'      <li>\n        <p><label>')
                        # SOURCE LINE 606
                        __M_writer(conditional_websafe(_('color')))
                        __M_writer(u'</label> <span class="gray">')
                        __M_writer(conditional_websafe(_('used as a thematic color for your subreddit on mobile')))
                        __M_writer(u'</span></p>\n        <ul class="colors">\n')
                        # SOURCE LINE 608
                        for color, color_name in thing.color_options.iteritems():
                            # SOURCE LINE 609
                            if color:
                                # SOURCE LINE 610
                                __M_writer(u'            <li>\n              <label>\n                <input type="radio" name="key_color" value="')
                                # SOURCE LINE 612
                                __M_writer(conditional_websafe(color))
                                __M_writer(u'"\n')
                                # SOURCE LINE 613
                                if c.site.key_color.lower() == color.lower():
                                    # SOURCE LINE 614
                                    __M_writer(u'                         checked="checked"\n')
                                # SOURCE LINE 616
                                __M_writer(u'                >\n                <div class="swatch" style="background-color: ')
                                # SOURCE LINE 617
                                __M_writer(conditional_websafe(color))
                                __M_writer(u'"></div>\n                ')
                                # SOURCE LINE 618
                                __M_writer(conditional_websafe(_(color_name)))
                                __M_writer(u'\n              </label>\n            </li>\n')
                        # SOURCE LINE 623
                        __M_writer(u'        </ul>\n      </li>\n    </ul>\n  ')
                        return ''
                    return [body]
                context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
                try:
                    # SOURCE LINE 564
                    __M_writer(conditional_websafe(utils.line_field(css_class=u'mobile',title=(_('mobile look and feel')))))
                finally:
                    context.caller_stack.nextcaller = None
                # SOURCE LINE 626
                __M_writer(u'\n')
            # SOURCE LINE 628
            __M_writer(u'\n')
            # SOURCE LINE 630
            if feature.is_enabled('chat'):
                # SOURCE LINE 631
                __M_writer(u'  ')
                def ccall(caller):
                    def body():
                        __M_writer = context.writer()
                        __M_writer(u'\n    <div class="delete-field">\n      <ul>\n        <li>\n          ')
                        # SOURCE LINE 635

                        checked = False
                        if thing.site and thing.site.chat_enabled:
                          checked = True
                        elif not thing.site:
                          ## new sub case
                          checked = True
                                  
                        
                        __M_locals_builtin_stored = __M_locals_builtin()
                        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['checked'] if __M_key in __M_locals_builtin_stored]))
                        # SOURCE LINE 642
                        __M_writer(u'\n          <input class="nomargin" type="checkbox"\n                 name="chat_enabled" id="chat_enabled"\n                 ')
                        # SOURCE LINE 645
                        __M_writer(conditional_websafe("checked='checked'" if checked else ""))
                        __M_writer(u'>\n          <label for="chat_enabled">\n            ')
                        # SOURCE LINE 647
                        __M_writer(conditional_websafe(_("Enable Chat")))
                        __M_writer(u'&#32;&#32;<span class="gray">')
                        __M_writer(conditional_websafe(_("Add sidebar chat, allow chat posts and chat comments")))
                        __M_writer(u'</span>\n          </label>\n        </li>\n      </ul>\n    </div>\n  ')
                        return ''
                    return [body]
                context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
                try:
                    # SOURCE LINE 631
                    __M_writer(conditional_websafe(utils.line_field(title=(_('chat')))))
                finally:
                    context.caller_stack.nextcaller = None
                # SOURCE LINE 652
                __M_writer(u'\n')
            # SOURCE LINE 654
            __M_writer(u'\n')
            # SOURCE LINE 655
            if not thing.site:
                # SOURCE LINE 656
                __M_writer(u'  ')
                __M_writer(conditional_websafe(thing.captcha))
                __M_writer(u'\n')
            # SOURCE LINE 658
            __M_writer(u'\n  <div class="save-button">\n  ')
            # SOURCE LINE 660

            if thing.site:
                name = "edit"
                text = _("save options")
            else:
                name = "create"
                text = _("create")
              
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['text','name'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 667
            __M_writer(u'\n  <button name="')
            # SOURCE LINE 668
            __M_writer(conditional_websafe(name))
            __M_writer(u'" class="btn" type="button"\n          onclick="return post_pseudo_form(\'#sr-form\', \'site_admin\')">\n    ')
            # SOURCE LINE 670
            __M_writer(conditional_websafe(text))
            __M_writer(u'\n  </button>\n  &#32;\n  <span class="status error" style="display:none"></span>\n  ')
            # SOURCE LINE 674
            __M_writer(conditional_websafe(error_field("RATELIMIT", "ratelimit")))
            __M_writer(u'\n  ')
            # SOURCE LINE 675
            __M_writer(conditional_websafe(error_field("CANT_CREATE_SR", "")))
            __M_writer(u'\n  </div>\n</div>\n</div>\n\n')
        # SOURCE LINE 681
        __M_writer(u'\n')
        # SOURCE LINE 682
        if thing.site:
            # SOURCE LINE 683
            __M_writer(u'<script type="text/javascript">\n(function(){\n  var dirty = {};\n\n  $(window).on(\'beforeunload\', function(e) {\n    if ($(\'#sr-form .status:visible\').length) {\n      return;\n    }\n    for (field in dirty) {\n      if (dirty[field]) {\n        return r._(\'There are unsaved changes. Are you sure you want to leave this page?\');\n      }\n    }\n  });\n\n  $(\'#sr-form\').on(\'change\', function(e) {\n    var input = e.target;\n    if (input.tagName == \'SELECT\') {\n      var $default = $(\'option[selected]\', input);\n      var $current = $(\'option:selected\', input);\n      dirty[input.name] = !$default.is($current);\n    } else if (input.type == \'checkbox\' || input.type == \'radio\') {\n      dirty[input.name] = input.checked ? !input.defaultChecked : input.defaultChecked;\n    } else if (input.type == \'file\') {\n      /* ignore */\n    } else {\n      dirty[input.name] = input.value != input.defaultValue;\n    }\n    if (!dirty[input.name]) {\n      delete dirty[input.name];\n    }\n  });\n})();\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


