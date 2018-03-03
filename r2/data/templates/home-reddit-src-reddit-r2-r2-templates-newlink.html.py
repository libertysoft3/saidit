# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505003402.500909
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/newlink.html'
_template_uri = '/newlink.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23

from r2.lib.strings import strings
from r2.lib.pages import SubredditSelector, UserText
from r2.lib.template_helpers import add_sr, _wsf, format_html
from r2.lib.filters import safemarkdown


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 31
    ns = runtime.TemplateNamespace(u'utils', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'utils')] = ns

    # SOURCE LINE 30
    ns = runtime.TemplateNamespace('__anon_0x7f3608adcc10', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f3608adcc10')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f3608adcc10')._populate(_import_ns, [u'error_field', u'submit_form', u'_a_buffered', u'text_with_links'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        utils = _mako_get_namespace(context, 'utils')
        _a_buffered = _import_ns.get('_a_buffered', context.get('_a_buffered', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 28
        __M_writer(u'\n\n')
        # SOURCE LINE 30
        __M_writer(u'\n')
        # SOURCE LINE 31
        __M_writer(u'\n\n')
        # SOURCE LINE 33

        if thing.default_sr:
          sr = format_html("&#32;%s", unsafe(_a_buffered(thing.default_sr.name, href=thing.default_sr.path)))
        else:
          sr = _("SaidIt")
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['sr'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 38
        __M_writer(u'\n\n<h1>')
        # SOURCE LINE 40
        __M_writer(conditional_websafe(_wsf("submit to %(sr)s", sr=sr)))
        __M_writer(u'</h1>\n\n')
        def ccall(caller):
            def body():
                error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
                dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
                text_with_links = _import_ns.get('text_with_links', context.get('text_with_links', UNDEFINED))
                __M_writer = context.writer()
                # SOURCE LINE 45
                __M_writer(u'\n\n')
                # SOURCE LINE 47
                if thing.show_link and thing.show_self:
                    # SOURCE LINE 48
                    __M_writer(conditional_websafe(thing.formtabs_menu))
                    __M_writer(u'\n')
                # SOURCE LINE 50
                __M_writer(u'\n<div class="formtabs-content">\n\n<div class="spacer">\n')
                # SOURCE LINE 54
                if thing.show_link:
                    # SOURCE LINE 55
                    __M_writer(u'        <div id="link-desc" class="infobar">')
                    __M_writer(conditional_websafe(strings.submit_link))
                    __M_writer(u'</div>\n')
                # SOURCE LINE 57
                if thing.show_self:
                    # SOURCE LINE 58
                    __M_writer(u'        <div id="text-desc" class="infobar">')
                    __M_writer(conditional_websafe(strings.submit_text))
                    __M_writer(u'</div>\n')
                # SOURCE LINE 60
                __M_writer(u'</div>\n\n<div class="spacer">\n  ')
                def ccall(caller):
                    def body():
                        __M_writer = context.writer()
                        # SOURCE LINE 63
                        __M_writer(u'\n    <textarea name="title" rows="2" required>')
                        # SOURCE LINE 64
                        __M_writer(conditional_websafe(thing.title))
                        __M_writer(u'</textarea>\n    ')
                        # SOURCE LINE 65
                        __M_writer(conditional_websafe(error_field("NO_TEXT", "title", "div")))
                        __M_writer(u'\n    ')
                        # SOURCE LINE 66
                        __M_writer(conditional_websafe(error_field("TOO_LONG", "title", "div")))
                        __M_writer(u'\n  ')
                        return ''
                    return [body]
                context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
                try:
                    # SOURCE LINE 63
                    __M_writer(conditional_websafe(utils.round_field(id=u'title-field',title=(_('title')))))
                finally:
                    context.caller_stack.nextcaller = None
                # SOURCE LINE 67
                __M_writer(u'\n</div>\n\n')
                # SOURCE LINE 70
                if thing.show_link:
                    # SOURCE LINE 71
                    __M_writer(u'<div class="spacer">\n  ')
                    def ccall(caller):
                        def body():
                            __M_writer = context.writer()
                            # SOURCE LINE 72
                            __M_writer(u'\n    <input name="kind" value="link" type="hidden"/>\n    <input id="url" name="url" type="url" value="')
                            # SOURCE LINE 74
                            __M_writer(conditional_websafe(thing.url))
                            __M_writer(u'" required>\n    ')
                            # SOURCE LINE 75
                            __M_writer(conditional_websafe(error_field("NO_URL", "url", "div")))
                            __M_writer(u'\n    ')
                            # SOURCE LINE 76
                            __M_writer(conditional_websafe(error_field("BAD_URL", "url", "div")))
                            __M_writer(u'\n    ')
                            # SOURCE LINE 77
                            __M_writer(conditional_websafe(error_field("DOMAIN_BANNED", "url", "div")))
                            __M_writer(u'\n    ')
                            # SOURCE LINE 78
                            __M_writer(conditional_websafe(error_field("ALREADY_SUB", "url", "div")))
                            __M_writer(u'\n    ')
                            # SOURCE LINE 79
                            __M_writer(conditional_websafe(error_field("NO_LINKS", "sr")))
                            __M_writer(u'\n    ')
                            # SOURCE LINE 80
                            __M_writer(conditional_websafe(error_field("NO_SELFS", "sr")))
                            __M_writer(u'\n\n    <div id="suggest-title">\n      <span class="title-status"></span>\n      <button type="button" tabindex="100" onclick="fetch_title()">')
                            # SOURCE LINE 84
                            __M_writer(conditional_websafe(_("suggest title")))
                            __M_writer(u'</button>\n    </div>\n  ')
                            return ''
                        return [body]
                    context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
                    try:
                        # SOURCE LINE 72
                        __M_writer(conditional_websafe(utils.round_field(id=u'url-field',title=(_('url')))))
                    finally:
                        context.caller_stack.nextcaller = None
                    # SOURCE LINE 86
                    __M_writer(u'\n</div>\n')
                # SOURCE LINE 89
                __M_writer(u'\n')
                # SOURCE LINE 90
                if thing.show_self:
                    # SOURCE LINE 91
                    __M_writer(u'<div class="spacer">\n  ')
                    def ccall(caller):
                        def body():
                            __M_writer = context.writer()
                            # SOURCE LINE 92
                            __M_writer(u'\n    <input name="kind" value="self" type="hidden"/>\n\n    ')
                            # SOURCE LINE 95
                            __M_writer(conditional_websafe(UserText(None, text = thing.text, have_form = False, creating = True)))
                            __M_writer(u'\n\n    ')
                            # SOURCE LINE 97
                            __M_writer(conditional_websafe(error_field("NO_SELFS", "sr")))
                            __M_writer(u'\n  ')
                            return ''
                        return [body]
                    context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
                    try:
                        # SOURCE LINE 92
                        __M_writer(conditional_websafe(utils.round_field(title=(_('text')),id=u'text-field',description=(_('(optional)')))))
                    finally:
                        context.caller_stack.nextcaller = None
                    # SOURCE LINE 98
                    __M_writer(u'\n</div>\n')
                # SOURCE LINE 101
                __M_writer(u'\n<div class="spacer">\n  ')
                def ccall(caller):
                    def body():
                        __M_writer = context.writer()
                        # SOURCE LINE 103
                        __M_writer(u'\n    ')
                        # SOURCE LINE 104
                        __M_writer(conditional_websafe(SubredditSelector(thing.default_sr, extra_subreddits=thing.extra_subreddits, required=True)))
                        __M_writer(u'\n  ')
                        return ''
                    return [body]
                context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
                try:
                    # SOURCE LINE 103
                    __M_writer(conditional_websafe(utils.round_field(id=u'reddit-field',title=(_('choose a subreddit')))))
                finally:
                    context.caller_stack.nextcaller = None
                # SOURCE LINE 105
                __M_writer(u'\n</div>\n\n<div class="spacer">\n    <div class="submit_text roundfield">\n        <h1>')
                # SOURCE LINE 110
                __M_writer(conditional_websafe(_wsf('submitting to %(sr)s', sr=unsafe('/r/<span class="sr"></span>'))))
                __M_writer(u'</h1>\n        <span class="content md-container">\n')
                # SOURCE LINE 112
                if thing.default_sr and thing.default_sr.submit_text:
                    # SOURCE LINE 113
                    __M_writer(u'                ')
                    __M_writer(conditional_websafe(unsafe(safemarkdown(thing.default_sr.submit_text))))
                    __M_writer(u'\n')
                # SOURCE LINE 115
                __M_writer(u'        </span>\n    </div>\n</div>\n\n<div class="spacer">\n  ')
                def ccall(caller):
                    def body():
                        __M_writer = context.writer()
                        # SOURCE LINE 120
                        __M_writer(u'\n    <input class="nomargin" type="checkbox" checked="checked" name="sendreplies" id="sendreplies" data-send-checked="true"/>\n    <label for="sendreplies">\n      ')
                        # SOURCE LINE 123
                        __M_writer(conditional_websafe(_("send replies to my inbox")))
                        __M_writer(u'\n    </label>\n  ')
                        return ''
                    return [body]
                context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
                try:
                    # SOURCE LINE 120
                    __M_writer(conditional_websafe(utils.round_field(title=(_('options')))))
                finally:
                    context.caller_stack.nextcaller = None
                # SOURCE LINE 125
                __M_writer(u'\n</div>\n\n')
                # SOURCE LINE 128
                __M_writer(conditional_websafe(thing.captcha))
                __M_writer(u'\n    \n</div>\n\n<div class="roundfield info-notice">\n  ')
                # SOURCE LINE 133
                __M_writer(conditional_websafe(text_with_links(_("please be mindful of SaidIt's %(content_policy)s."),
      content_policy=dict(
        link_text=_("content policy"),
        path="/r/AntiExtremes/comments/63/antiextremescom_content_policy/",
        target="_blank")
        )))
                # SOURCE LINE 142
                __M_writer(u'\n</div>\n\n<input name="resubmit" value="')
                # SOURCE LINE 145
                __M_writer(conditional_websafe(thing.resubmit))
                __M_writer(u'" type="hidden"/>\n<div class="spacer">\n  <button class="btn" name="submit" value="form" type="submit">')
                # SOURCE LINE 147
                __M_writer(conditional_websafe(_("submit")))
                __M_writer(u'</button>\n  <span class="status"></span>\n  ')
                # SOURCE LINE 149
                __M_writer(conditional_websafe(error_field("RATELIMIT", "ratelimit")))
                __M_writer(u'\n  ')
                # SOURCE LINE 150
                __M_writer(conditional_websafe(error_field("INVALID_OPTION", "sr")))
                __M_writer(u'\n  ')
                # SOURCE LINE 151
                __M_writer(conditional_websafe(error_field("IN_TIMEOUT", "sr")))
                __M_writer(u'\n</div>\n')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 42
            __M_writer(conditional_websafe(utils.submit_form(onsubmit=u"return post_form(this, 'submit', linkstatus, null, true)",_class=u'submit content warn-on-unload',_id=u'newlink')))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 153
        __M_writer(u'\n\n')
        # SOURCE LINE 155
        if thing.show_self and thing.show_link:
            # SOURCE LINE 156
            __M_writer(u'<script type="text/javascript">\n  $(function() {\n  var form = $("#newlink");\n  if(form.length) {\n    var default_menu = form.find(".')
            # SOURCE LINE 160
            __M_writer(conditional_websafe(thing.default_tab))
            __M_writer(u'-button:first");\n    select_form_tab(default_menu, "')
            # SOURCE LINE 161
            __M_writer(conditional_websafe(thing.default_show))
            __M_writer(u'", "')
            __M_writer(conditional_websafe(thing.default_hide))
            __M_writer(u'");\n    }\n  });\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


