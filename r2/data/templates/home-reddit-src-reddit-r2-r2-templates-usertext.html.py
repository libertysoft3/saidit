# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1512370184.196398
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/usertext.html'
_template_uri = '/usertext.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['action_button', 'markhelp']


# SOURCE LINE 23

from r2.lib.filters import unsafe, safemarkdown, keep_space
from r2.lib.strings import strings
from r2.lib.utils import randstr

### CUSTOM
from r2.config import feature


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 33
    ns = runtime.TemplateNamespace('__anon_0x7fa55a36eed0', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fa55a36eed0')] = ns

    # SOURCE LINE 32
    ns = runtime.TemplateNamespace('__anon_0x7fa55a36edd0', context._clean_inheritance_tokens(), templateuri=u'printablebuttons.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fa55a36edd0')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fa55a36eed0')._populate(_import_ns, [u'data', u'error_field', u'md', u'_md'])
        _mako_get_namespace(context, '__anon_0x7fa55a36edd0')._populate(_import_ns, [u'toggle_button'])
        toggle_button = _import_ns.get('toggle_button', context.get('toggle_button', UNDEFINED))
        def action_button(name,btn_type,onclick,display):
            return render_action_button(context._locals(__M_locals),name,btn_type,onclick,display)
        error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        def markhelp(show_embed_help=False):
            return render_markhelp(context._locals(__M_locals),show_embed_help)
        data = _import_ns.get('data', context.get('data', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 30
        __M_writer(u'\n\n')
        # SOURCE LINE 32
        __M_writer(u'\n')
        # SOURCE LINE 33
        __M_writer(u'\n\n')
        # SOURCE LINE 108
        __M_writer(u'\n\n')
        # SOURCE LINE 115
        __M_writer(u'\n\n')
        # SOURCE LINE 117
        if thing.have_form:
            # SOURCE LINE 118
            __M_writer(u'  <form action="#" class="')
            __M_writer(conditional_websafe(thing.css_class))
            __M_writer(u' warn-on-unload"\n')
            # SOURCE LINE 119
            if thing.post_form:
                # SOURCE LINE 120
                __M_writer(u'        onsubmit="return post_form(this, \'')
                __M_writer(conditional_websafe(thing.post_form))
                __M_writer(u'\')"\n')
            # SOURCE LINE 122
            __M_writer(u'        ')
            __M_writer(conditional_websafe("style='display:none'" if not thing.display else ""))
            __M_writer(u'\n        id="form-')
            # SOURCE LINE 123
            __M_writer(conditional_websafe(thing.fullname + randstr(3)))
            __M_writer(u'">\n')
            # SOURCE LINE 124
        else:
            # SOURCE LINE 125
            __M_writer(u'  <div class="')
            __M_writer(conditional_websafe(thing.css_class))
            __M_writer(u'">\n')
        # SOURCE LINE 127
        __M_writer(u'\n')
        # SOURCE LINE 129
        __M_writer(u'  <input type="hidden" name="thing_id" value="')
        __M_writer(conditional_websafe(thing.fullname))
        __M_writer(u'"/>\n\n')
        # SOURCE LINE 131
        if thing.source:
            # SOURCE LINE 132
            __M_writer(u'    <input type="hidden" name="source" value="')
            __M_writer(conditional_websafe(thing.source))
            __M_writer(u'">\n')
        # SOURCE LINE 134
        __M_writer(u'\n')
        # SOURCE LINE 135
        if not thing.creating:
            # SOURCE LINE 136
            __M_writer(u'    <div class="usertext-body may-blank-within md-container ')
            __M_writer(conditional_websafe('admin_takedown' if thing.admin_takedown else ''))
            __M_writer(u'">\n')
            # SOURCE LINE 137
            if not thing.expunged:
                # SOURCE LINE 138
                __M_writer(u'\n')
                # SOURCE LINE 140
                if thing.is_chat_post and thing.user_chat_enabled and thing.chat_client == 'kiwiirc':
                    # SOURCE LINE 141
                    if thing.chat_user_is_guest:
                        # SOURCE LINE 142
                        __M_writer(u'            <iframe class="chat-iframe kiwiirc" src="')
                        __M_writer(conditional_websafe(thing.chat_client_url))
                        __M_writer(u'/?nick=')
                        __M_writer(conditional_websafe(thing.chat_user))
                        __M_writer(u'|?#')
                        __M_writer(conditional_websafe(thing.chat_channel))
                        __M_writer(u'"></iframe>\n')
                        # SOURCE LINE 143
                    else:
                        # SOURCE LINE 144
                        __M_writer(u'            <iframe class="chat-iframe kiwiirc" src="')
                        __M_writer(conditional_websafe(thing.chat_client_url))
                        __M_writer(u'/?nick=')
                        __M_writer(conditional_websafe(thing.chat_user))
                        __M_writer(u'#')
                        __M_writer(conditional_websafe(thing.chat_channel))
                        __M_writer(u'"></iframe>\n')
                    # SOURCE LINE 146
                    __M_writer(u'\n')
                    # SOURCE LINE 147
                elif thing.is_chat_post and thing.user_chat_enabled and thing.chat_client == 'thelounge':
                    # SOURCE LINE 148
                    if thing.chat_user_is_guest:
                        # SOURCE LINE 149
                        __M_writer(u'            <iframe class="chat-iframe thelounge" src="')
                        __M_writer(conditional_websafe(thing.chat_client_url))
                        __M_writer(u'/?tls=true&nofocus&lockchannel&autologin&user=')
                        __M_writer(conditional_websafe(thing.chat_client_user))
                        __M_writer(u'&autoconnect&nick=')
                        __M_writer(conditional_websafe(thing.chat_user))
                        __M_writer(u'&username=')
                        __M_writer(conditional_websafe(thing.chat_user))
                        __M_writer(u'&realname=')
                        __M_writer(conditional_websafe(thing.chat_user))
                        __M_writer(u'&join=')
                        __M_writer(conditional_websafe(thing.chat_channel))
                        __M_writer(u'"></iframe>\n')
                        # SOURCE LINE 150
                    else:
                        # SOURCE LINE 151
                        __M_writer(u'            <iframe class="chat-iframe thelounge" src="')
                        __M_writer(conditional_websafe(thing.chat_client_url))
                        __M_writer(u'/?tls=true&nofocus&lockchannel&autologin&user=')
                        __M_writer(conditional_websafe(thing.chat_client_user))
                        __M_writer(u'&al-password=')
                        __M_writer(conditional_websafe(thing.chat_client_password))
                        __M_writer(u'&autoconnect&nick=')
                        __M_writer(conditional_websafe(thing.chat_user))
                        __M_writer(u'&username=')
                        __M_writer(conditional_websafe(thing.chat_user))
                        __M_writer(u'&realname=')
                        __M_writer(conditional_websafe(thing.chat_user))
                        __M_writer(u'&join=')
                        __M_writer(conditional_websafe(thing.chat_channel))
                        __M_writer(u'"></iframe>\n')
                    # SOURCE LINE 153
                    __M_writer(u'\n')
                    # SOURCE LINE 154
                else:
                    # SOURCE LINE 155
                    __M_writer(u'          ')
                    __M_writer(conditional_websafe(unsafe(safemarkdown(thing.text, nofollow = thing.nofollow,
                                        target = thing.target))))
                    # SOURCE LINE 156
                    __M_writer(u'\n')
                # SOURCE LINE 158
            else:
                # SOURCE LINE 159
                __M_writer(u'        <em>')
                __M_writer(conditional_websafe(_("[removed]")))
                __M_writer(u'</em>&#32;\n')
            # SOURCE LINE 161
            __M_writer(u'    </div>\n')
        # SOURCE LINE 163
        __M_writer(u'\n')
        # SOURCE LINE 164
        if thing.editable or thing.creating:
            # SOURCE LINE 166
            __M_writer(u'    <div class="usertext-edit md-container"\n         style="')
            # SOURCE LINE 167
            __M_writer(conditional_websafe("" if thing.creating else 'display: none'))
            __M_writer(u'">\n      <div class="md">\n        <textarea rows="1" cols="1"\n                  name="')
            # SOURCE LINE 170
            __M_writer(conditional_websafe(thing.name))
            __M_writer(u'"\n                  class="')
            # SOURCE LINE 171
            __M_writer(conditional_websafe(thing.textarea_class))
            __M_writer(u'"\n                  ')
            # SOURCE LINE 172
            __M_writer(conditional_websafe(data(**thing.data_attrs)))
            __M_writer(u'\n                  >')
            # SOURCE LINE 173
            __M_writer(conditional_websafe(keep_space(thing.text)))
            __M_writer(u'</textarea>\n      </div>\n\n      <div class="bottom-area">\n        ')
            # SOURCE LINE 177
            __M_writer(conditional_websafe(toggle_button("help-toggle", _("formatting help"), _("hide help"),
                        "helpon", "helpoff",
                         style = "" if thing.creating else "display: none")))
            # SOURCE LINE 179
            __M_writer(u'\n\n        <a href="/help/contentpolicy" class="reddiquette" target="_blank" tabindex="100">')
            # SOURCE LINE 181
            __M_writer(conditional_websafe(_('content policy')))
            __M_writer(u'</a>\n\n')
            # SOURCE LINE 183
            if thing.include_errors:
                # SOURCE LINE 184
                __M_writer(u'          ')
                __M_writer(conditional_websafe(error_field("TOO_LONG", thing.name, "span")))
                __M_writer(u'\n          ')
                # SOURCE LINE 185
                __M_writer(conditional_websafe(error_field("RATELIMIT", "ratelimit", "span")))
                __M_writer(u'\n          ')
                # SOURCE LINE 186
                __M_writer(conditional_websafe(error_field("NO_TEXT", thing.name, "span")))
                __M_writer(u'\n          ')
                # SOURCE LINE 187
                __M_writer(conditional_websafe(error_field("TOO_OLD", "parent", "span")))
                __M_writer(u'\n          ')
                # SOURCE LINE 188
                __M_writer(conditional_websafe(error_field("THREAD_LOCKED", "parent", "span")))
                __M_writer(u'\n          ')
                # SOURCE LINE 189
                __M_writer(conditional_websafe(error_field("DELETED_COMMENT", "parent", "span")))
                __M_writer(u'\n          ')
                # SOURCE LINE 190
                __M_writer(conditional_websafe(error_field("USER_BLOCKED", "parent", "span")))
                __M_writer(u'\n          ')
                # SOURCE LINE 191
                __M_writer(conditional_websafe(error_field("USER_MUTED", "parent", "span")))
                __M_writer(u'\n          ')
                # SOURCE LINE 192
                __M_writer(conditional_websafe(error_field("MUTED_FROM_SUBREDDIT", "parent", "span")))
                __M_writer(u'\n')
            # SOURCE LINE 194
            __M_writer(u'        <div class="usertext-buttons">\n          ')
            # SOURCE LINE 195
            __M_writer(conditional_websafe(action_button("save", "submit", "",
                          thing.creating and thing.have_form)))
            # SOURCE LINE 196
            __M_writer(u'\n          ')
            # SOURCE LINE 197
            __M_writer(conditional_websafe(action_button("cancel", "button", "return cancel_usertext(this);", False)))
            __M_writer(u'\n')
            # SOURCE LINE 198
            if thing.have_form:
                # SOURCE LINE 199
                __M_writer(u'            <span class="status"></span>\n')
            # SOURCE LINE 201
            __M_writer(u'        </div>\n      </div>\n\n      ')
            # SOURCE LINE 204
            __M_writer(conditional_websafe(markhelp(show_embed_help=thing.show_embed_help)))
            __M_writer(u'\n    </div>\n')
        # SOURCE LINE 207
        __M_writer(u'\n')
        # SOURCE LINE 208
        if thing.have_form:
            # SOURCE LINE 209
            __M_writer(u'  </form>\n')
            # SOURCE LINE 210
        else:
            # SOURCE LINE 211
            __M_writer(u'  </div>\n')
        # SOURCE LINE 213
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_action_button(context,name,btn_type,onclick,display):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fa55a36eed0')._populate(_import_ns, [u'data', u'error_field', u'md', u'_md'])
        _mako_get_namespace(context, '__anon_0x7fa55a36edd0')._populate(_import_ns, [u'toggle_button'])
        __M_writer = context.writer()
        # SOURCE LINE 110
        __M_writer(u'\n  <button type="')
        # SOURCE LINE 111
        __M_writer(conditional_websafe(btn_type))
        __M_writer(u'" onclick="')
        __M_writer(conditional_websafe(onclick))
        __M_writer(u'" class="')
        __M_writer(conditional_websafe(name))
        __M_writer(u'"\n          ')
        # SOURCE LINE 112
        __M_writer(conditional_websafe("style='display:none'" if not display else ""))
        __M_writer(u'>\n    ')
        # SOURCE LINE 113
        __M_writer(conditional_websafe(name))
        __M_writer(u'\n  </button>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_markhelp(context,show_embed_help=False):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fa55a36eed0')._populate(_import_ns, [u'data', u'error_field', u'md', u'_md'])
        _mako_get_namespace(context, '__anon_0x7fa55a36edd0')._populate(_import_ns, [u'toggle_button'])
        md = _import_ns.get('md', context.get('md', UNDEFINED))
        _md = _import_ns.get('_md', context.get('_md', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 35
        __M_writer(u'\n  <div class="markhelp" style="display:none">\n    <p>')
        # SOURCE LINE 37
        __M_writer(conditional_websafe(md(strings.formatting_help_info)))
        __M_writer(u'</p>\n    <table class="md">\n      <tr style="background-color: #ffff99; text-align: center">\n        <td><em>')
        # SOURCE LINE 40
        __M_writer(conditional_websafe(_( "you type:")))
        __M_writer(u'</em></td>\n        <td><em>')
        # SOURCE LINE 41
        __M_writer(conditional_websafe(_( "you see:")))
        __M_writer(u'</em></td>\n      </tr>\n      <tr>\n        <td>*')
        # SOURCE LINE 44
        __M_writer(conditional_websafe(_( "italics")))
        __M_writer(u'*</td>\n        <td><em>')
        # SOURCE LINE 45
        __M_writer(conditional_websafe(_( "italics")))
        __M_writer(u'</em></td>\n      </tr>\n      <tr>\n        <td>**')
        # SOURCE LINE 48
        __M_writer(conditional_websafe(_( "bold")))
        __M_writer(u'**</td>\n        <td><b>')
        # SOURCE LINE 49
        __M_writer(conditional_websafe(_( "bold")))
        __M_writer(u'</b></td>\n      </tr>\n      <tr>\n        <td>[reddit!](https://reddit.com)</td>\n        <td><a href="https://reddit.com">reddit!</a></td>\n      </tr>\n      <tr>\n        <td>\n          * ')
        # SOURCE LINE 57
        __M_writer(conditional_websafe(_( "item")))
        __M_writer(u' 1<br/>\n          * ')
        # SOURCE LINE 58
        __M_writer(conditional_websafe(_( "item")))
        __M_writer(u' 2<br/>\n          * ')
        # SOURCE LINE 59
        __M_writer(conditional_websafe(_( "item")))
        __M_writer(u' 3\n        </td>\n        <td>\n          <ul>\n            <li>')
        # SOURCE LINE 63
        __M_writer(conditional_websafe(_( "item")))
        __M_writer(u' 1</li>\n            <li>')
        # SOURCE LINE 64
        __M_writer(conditional_websafe(_( "item")))
        __M_writer(u' 2</li>\n            <li>')
        # SOURCE LINE 65
        __M_writer(conditional_websafe(_( "item")))
        __M_writer(u' 3</li>\n          </ul>\n        </td>\n      </tr>\n      <tr>\n        <td>&gt; ')
        # SOURCE LINE 70
        __M_writer(conditional_websafe(_( "quoted text")))
        __M_writer(u'</td>\n        <td><blockquote>')
        # SOURCE LINE 71
        __M_writer(conditional_websafe(_( "quoted text" )))
        __M_writer(u'</blockquote></td>\n      </tr>\n      <tr>\n          <td>\n              Lines starting with four spaces <br/>\n              are treated like code:<br/><br/>\n              <span class="spaces">\n                  &nbsp;&nbsp;&nbsp;&nbsp;\n              </span>\n              if 1 * 2 &lt; 3:<br/>\n              <span class="spaces">\n                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n              </span>\n              print "hello, world!"<br/>\n          </td>\n          <td>Lines starting with four spaces <br/>\n              are treated like code:<br/>\n              <pre>if 1 * 2 &lt; 3:<br/>&nbsp;&nbsp;&nbsp;&nbsp;print "hello,\n              world!"</pre>\n          </td>\n      </tr>\n      <tr>\n          <td>~~strikethrough~~</td>\n          <td><strike>strikethrough</strike></td>\n      </tr>\n      <tr>\n          <td>super^script</td>\n          <td>super<sup>script</sup></td>\n      </tr>\n')
        # SOURCE LINE 100
        if show_embed_help:
            # SOURCE LINE 101
            __M_writer(u'      <tr>\n          <td>')
            # SOURCE LINE 102
            __M_writer(conditional_websafe(_md('Links on their own line will be embedded:\n\nhttps://example.com')))
            __M_writer(u'</td>\n          <td>')
            # SOURCE LINE 103
            __M_writer(conditional_websafe(_('an embedded version of that link')))
            __M_writer(u'</td>\n      </tr>\n')
        # SOURCE LINE 106
        __M_writer(u'    </table>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


