# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1508299777.199981
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/moderatormessagecompose.html'
_template_uri = '/moderatormessagecompose.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['from_field']


# SOURCE LINE 26

from r2.lib import js


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7f4dec59fd50', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f4dec59fd50')] = ns

    # SOURCE LINE 25
    ns = runtime.TemplateNamespace('__anon_0x7f4dec59fe90', context._clean_inheritance_tokens(), templateuri=u'messagecompose.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f4dec59fe90')] = ns

    # SOURCE LINE 24
    ns = runtime.TemplateNamespace(u'utils', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'utils')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f4dec59fd50')._populate(_import_ns, [u'error_field'])
        _mako_get_namespace(context, '__anon_0x7f4dec59fe90')._populate(_import_ns, [u'to_field', u'subject_field', u'message_field', u'captcha_field'])
        utils = _mako_get_namespace(context, 'utils')
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n')
        # SOURCE LINE 24
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'\n')
        # SOURCE LINE 28
        __M_writer(u'\n\n')
        # SOURCE LINE 30
        __M_writer(conditional_websafe(unsafe(js.use("messagecompose"))))
        __M_writer(u'\n\n<h1>')
        # SOURCE LINE 32
        __M_writer(conditional_websafe(_("send a private message")))
        __M_writer(u'</h1>\n\n')
        def ccall(caller):
            def body():
                subject_field = _import_ns.get('subject_field', context.get('subject_field', UNDEFINED))
                message_field = _import_ns.get('message_field', context.get('message_field', UNDEFINED))
                to_field = _import_ns.get('to_field', context.get('to_field', UNDEFINED))
                captcha_field = _import_ns.get('captcha_field', context.get('captcha_field', UNDEFINED))
                def from_field():
                    return render_from_field(context._locals(__M_locals))
                __M_writer = context.writer()
                # SOURCE LINE 36
                __M_writer(u'\n\n')
                # SOURCE LINE 38
                __M_writer(conditional_websafe(from_field()))
                __M_writer(u'\n')
                # SOURCE LINE 39
                __M_writer(conditional_websafe(to_field()))
                __M_writer(u'\n')
                # SOURCE LINE 40
                __M_writer(conditional_websafe(subject_field()))
                __M_writer(u'\n')
                # SOURCE LINE 41
                __M_writer(conditional_websafe(message_field()))
                __M_writer(u'\n')
                # SOURCE LINE 42
                __M_writer(conditional_websafe(captcha_field()))
                __M_writer(u'\n<input type="hidden" name="source" value="compose">\n\n<button id="send" name="send" type="submit">')
                # SOURCE LINE 45
                __M_writer(conditional_websafe(_("send")))
                __M_writer(u'</button>\n<span class="status"></span>\n\n')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 34
            __M_writer(conditional_websafe(utils.submit_form(action=u'/message/compose',onsubmit=u"return post_form(this, 'compose', null, null, true)",method=u'post',_id=u'compose-message')))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 48
        __M_writer(u'\n\n')
        # SOURCE LINE 73
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_from_field(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f4dec59fd50')._populate(_import_ns, [u'error_field'])
        _mako_get_namespace(context, '__anon_0x7f4dec59fe90')._populate(_import_ns, [u'to_field', u'subject_field', u'message_field', u'captcha_field'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        utils = _mako_get_namespace(context, 'utils')
        error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 50
        __M_writer(u'\n')
        # SOURCE LINE 54
        if not thing.restrict_recipient:
            # SOURCE LINE 55
            __M_writer(u'    <div class="spacer">\n      ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    # SOURCE LINE 56
                    __M_writer(u'\n')
                    # SOURCE LINE 59
                    if thing.only_as_subreddit:
                        # SOURCE LINE 60
                        __M_writer(u'          <input type="text" name="from_sr" value="')
                        __M_writer(conditional_websafe(thing.mod_srs[0].name))
                        __M_writer(u'" readonly>\n')
                        # SOURCE LINE 61
                    else:
                        # SOURCE LINE 62
                        __M_writer(u'          <select name="from_sr">\n            <option value="">')
                        # SOURCE LINE 63
                        __M_writer(conditional_websafe("/u/%s" % c.user.name))
                        __M_writer(u'</option>\n')
                        # SOURCE LINE 64
                        for sr in thing.mod_srs:
                            # SOURCE LINE 65
                            __M_writer(u'              <option value="')
                            __M_writer(conditional_websafe(sr.name))
                            __M_writer(u'">')
                            __M_writer(conditional_websafe("/r/%s" % sr.name))
                            __M_writer(u'</option>\n')
                        # SOURCE LINE 67
                        __M_writer(u'          </select>\n')
                    # SOURCE LINE 69
                    __M_writer(u'      ')
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 56
                __M_writer(conditional_websafe(utils.round_field(title=(_('from')))))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 69
            __M_writer(u'\n      ')
            # SOURCE LINE 70
            __M_writer(conditional_websafe(error_field("NO_SR_TO_SR_MESSAGE", "from")))
            __M_writer(u'\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


