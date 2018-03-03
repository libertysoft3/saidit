# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1509315370.349594
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/usertext.compact'
_template_uri = '/usertext.compact'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['action_button']


# SOURCE LINE 23

from r2.lib.filters import unsafe, safemarkdown, keep_space
from r2.lib.strings import strings
from r2.lib.utils import randstr


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 29
    ns = runtime.TemplateNamespace('__anon_0x7f8da4472450', context._clean_inheritance_tokens(), templateuri=u'printablebuttons.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f8da4472450')] = ns

    # SOURCE LINE 30
    ns = runtime.TemplateNamespace('__anon_0x7f8da4472c90', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f8da4472c90')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8da4472450')._populate(_import_ns, [u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f8da4472c90')._populate(_import_ns, [u'error_field', u'md'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
        md = _import_ns.get('md', context.get('md', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 27
        __M_writer(u'\n\n')
        # SOURCE LINE 29
        __M_writer(u'\n')
        # SOURCE LINE 30
        __M_writer(u'\n\n')
        # SOURCE LINE 37
        __M_writer(u'\n\n')
        # SOURCE LINE 39
        if thing.have_form:
            # SOURCE LINE 40
            __M_writer(u'  <form action="#" class="')
            __M_writer(conditional_websafe(thing.css_class))
            __M_writer(u'"\n        onsubmit="return post_form(this, \'')
            # SOURCE LINE 41
            __M_writer(conditional_websafe(thing.post_form))
            __M_writer(u'\')"\n        ')
            # SOURCE LINE 42
            __M_writer(conditional_websafe("style='display:none'" if not thing.display else ""))
            __M_writer(u'\n        id="form-')
            # SOURCE LINE 43
            __M_writer(conditional_websafe(thing.fullname + randstr(3)))
            __M_writer(u'">\n')
            # SOURCE LINE 44
        else:
            # SOURCE LINE 45
            __M_writer(u'  <div class="')
            __M_writer(conditional_websafe(thing.css_class))
            __M_writer(u'">\n')
        # SOURCE LINE 47
        __M_writer(u'\n')
        # SOURCE LINE 49
        __M_writer(u'  <input type="hidden" name="thing_id" value="')
        __M_writer(conditional_websafe(thing.fullname or ''))
        __M_writer(u'"/>\n\n')
        # SOURCE LINE 51
        if not thing.creating:
            # SOURCE LINE 52
            if not thing.expunged:
                # SOURCE LINE 53
                __M_writer(u'    <div class="usertext-body">\n      ')
                # SOURCE LINE 54
                __M_writer(conditional_websafe(unsafe(safemarkdown(thing.text, nofollow = thing.nofollow,
                                        target = thing.target))))
                # SOURCE LINE 55
                __M_writer(u'\n    </div>\n')
                # SOURCE LINE 57
            else:
                # SOURCE LINE 58
                __M_writer(u'    <em>')
                __M_writer(conditional_websafe(_("[removed]")))
                __M_writer(u'</em>&#32;\n')
        # SOURCE LINE 61
        __M_writer(u'\n')
        # SOURCE LINE 62
        if thing.editable or thing.creating:
            # SOURCE LINE 64
            __M_writer(u'    <div class="usertext-edit"\n         style="')
            # SOURCE LINE 65
            __M_writer(conditional_websafe("" if thing.creating else 'display: none'))
            __M_writer(u'">\n')
            # SOURCE LINE 67
            __M_writer(u'      <div>\n        <textarea rows="1" cols="1"\n                  name="')
            # SOURCE LINE 69
            __M_writer(conditional_websafe(thing.name))
            __M_writer(u'"\n                  >')
            # SOURCE LINE 70
            __M_writer(conditional_websafe(keep_space(thing.text)))
            __M_writer(u'</textarea>\n      </div>\n\n      <div class="bottom-area">\n        <div class="usertext-buttons">\n          <a href="#" class="help-toggle newbutton">')
            # SOURCE LINE 75
            __M_writer(conditional_websafe(_("help")))
            __M_writer(u'</a>\n          <button type="submit" class="save newbutton">')
            # SOURCE LINE 76
            __M_writer(conditional_websafe(_("Send")))
            __M_writer(u'</button>\n          <button type="button" class="cancel newbutton" style="display: none;"\n            onclick="return cancel_usertext(this)">\n            ')
            # SOURCE LINE 79
            __M_writer(conditional_websafe(_("Cancel")))
            __M_writer(u'</button>\n')
            # SOURCE LINE 80
            if thing.have_form:
                # SOURCE LINE 81
                __M_writer(u'            <span class="status"></span>\n')
            # SOURCE LINE 83
            __M_writer(u'        <div style="clear: both"></div>\n        </div>\n        ')
            # SOURCE LINE 85
            __M_writer(conditional_websafe(error_field("TOO_LONG", thing.name, "span")))
            __M_writer(u'\n        ')
            # SOURCE LINE 86
            __M_writer(conditional_websafe(error_field("RATELIMIT", "ratelimit", "span")))
            __M_writer(u'\n        ')
            # SOURCE LINE 87
            __M_writer(conditional_websafe(error_field("NO_TEXT", thing.name, "span")))
            __M_writer(u'\n        ')
            # SOURCE LINE 88
            __M_writer(conditional_websafe(error_field("DELETED_COMMENT", "parent", "span")))
            __M_writer(u'\n        ')
            # SOURCE LINE 89
            __M_writer(conditional_websafe(error_field("USER_BLOCKED", "parent", "span")))
            __M_writer(u'\n        ')
            # SOURCE LINE 90
            __M_writer(conditional_websafe(error_field("USER_MUTED", "parent", "span")))
            __M_writer(u'\n        ')
            # SOURCE LINE 91
            __M_writer(conditional_websafe(error_field("MUTED_FROM_SUBREDDIT", "parent", "span")))
            __M_writer(u'\n      </div>\n      <div class="markhelp-parent">\n      <p>')
            # SOURCE LINE 94
            __M_writer(conditional_websafe(md(strings.formatting_help_info)))
            __M_writer(u'</p>\n      <table class="markhelp">\n        <tr style="background-color: #ffff99; text-align: center">\n          <td><em>')
            # SOURCE LINE 97
            __M_writer(conditional_websafe(_( "you type:")))
            __M_writer(u'</em></td>\n          <td><em>')
            # SOURCE LINE 98
            __M_writer(conditional_websafe(_( "you see:")))
            __M_writer(u'</em></td>\n        </tr>\n        <tr>\n          <td>*')
            # SOURCE LINE 101
            __M_writer(conditional_websafe(_( "italics")))
            __M_writer(u'*</td>\n          <td><em>')
            # SOURCE LINE 102
            __M_writer(conditional_websafe(_( "italics")))
            __M_writer(u'</em></td>\n        </tr>\n        <tr>\n          <td>**')
            # SOURCE LINE 105
            __M_writer(conditional_websafe(_( "bold")))
            __M_writer(u'**</td>\n          <td><b>')
            # SOURCE LINE 106
            __M_writer(conditional_websafe(_( "bold")))
            __M_writer(u'</b></td>\n        </tr>\n        <tr>\n          <td>[reddit!](https://reddit.com)</td>\n          <td><a href="https://reddit.com">reddit!</a></td>\n        </tr>\n        <tr>\n          <td>\n            * ')
            # SOURCE LINE 114
            __M_writer(conditional_websafe(_( "item")))
            __M_writer(u' 1<br/>\n            * ')
            # SOURCE LINE 115
            __M_writer(conditional_websafe(_( "item")))
            __M_writer(u' 2<br/>\n            * ')
            # SOURCE LINE 116
            __M_writer(conditional_websafe(_( "item")))
            __M_writer(u' 3\n          </td>\n          <td>\n            <ul>\n              <li>')
            # SOURCE LINE 120
            __M_writer(conditional_websafe(_( "item")))
            __M_writer(u' 1</li>\n              <li>')
            # SOURCE LINE 121
            __M_writer(conditional_websafe(_( "item")))
            __M_writer(u' 2</li>\n              <li>')
            # SOURCE LINE 122
            __M_writer(conditional_websafe(_( "item")))
            __M_writer(u' 3</li>\n            </ul>\n          </td>\n        </tr>\n        <tr>\n          <td>&gt; ')
            # SOURCE LINE 127
            __M_writer(conditional_websafe(_( "quoted text")))
            __M_writer(u'</td>\n          <td><blockquote>')
            # SOURCE LINE 128
            __M_writer(conditional_websafe(_( "quoted text" )))
            __M_writer(u'</blockquote></td>\n        </tr>\n        <tr>\n            <td>\n                Lines starting with four spaces <br/>\n                are treated like code:<br/><br/>\n                <span class="spaces">\n                    &nbsp;&nbsp;&nbsp;&nbsp;\n                </span>\n                if 1 * 2 &lt; 3:<br/>\n                <span class="spaces">\n                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n                </span>\n                print "hello, world!"<br/>\n            </td>\n            <td>Lines starting with four spaces <br/>\n                are treated like code:<br/>\n                <pre>if 1 * 2 &lt; 3:<br/>&nbsp;&nbsp;&nbsp;&nbsp;print "hello,\n                world!"</pre>\n            </td>\n        </tr>\n        <tr>\n            <td>~~strikethrough~~</td>\n            <td><strike>strikethrough</strike></td>\n        </tr>\n        <tr>\n            <td>super^script</td>\n            <td>super<sup>script</sup></td>\n        </tr>\n      </table>\n      </div>\n    </div>\n')
        # SOURCE LINE 161
        __M_writer(u'\n')
        # SOURCE LINE 162
        if thing.have_form:
            # SOURCE LINE 163
            __M_writer(u'  </form>\n')
            # SOURCE LINE 164
        else:
            # SOURCE LINE 165
            __M_writer(u'  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_action_button(context,name,btn_type,onclick,display):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8da4472450')._populate(_import_ns, [u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f8da4472c90')._populate(_import_ns, [u'error_field', u'md'])
        __M_writer = context.writer()
        # SOURCE LINE 32
        __M_writer(u'\n  <button type="')
        # SOURCE LINE 33
        __M_writer(conditional_websafe(btn_type))
        __M_writer(u'" onclick="')
        __M_writer(conditional_websafe(onclick))
        __M_writer(u'" class="')
        __M_writer(conditional_websafe(name))
        __M_writer(u'"\n          ')
        # SOURCE LINE 34
        __M_writer(conditional_websafe("style='display:none'" if not display else ""))
        __M_writer(u'>\n    ')
        # SOURCE LINE 35
        __M_writer(conditional_websafe(name))
        __M_writer(u'\n  </button>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


