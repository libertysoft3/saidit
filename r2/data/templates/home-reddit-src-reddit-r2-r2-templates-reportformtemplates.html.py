# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505003146.571713
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/reportformtemplates.html'
_template_uri = '/reportformtemplates.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23

from r2.lib.filters import keep_space, unsafe, safemarkdown


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 27
    ns = runtime.TemplateNamespace('__anon_0x7f3609512310', context._clean_inheritance_tokens(), templateuri=u'subredditreportform.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f3609512310')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f3609512310')._populate(_import_ns, [u'subreddit_report_form', u'reddit_report_form', u'report_form_reason'])
        reddit_report_form = _import_ns.get('reddit_report_form', context.get('reddit_report_form', UNDEFINED))
        subreddit_report_form = _import_ns.get('subreddit_report_form', context.get('subreddit_report_form', UNDEFINED))
        report_form_reason = _import_ns.get('report_form_reason', context.get('report_form_reason', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'\n\n')
        # SOURCE LINE 28
        __M_writer(u'\n\n<script id="subreddit-rules-report-template" type="text/template">\n    ')
        # SOURCE LINE 31
        __M_writer(conditional_websafe(subreddit_report_form(
        fullname=unsafe("<%- fullname %>"),
        system_rules=thing.system_rules,
        rules=None,
        sr_name="<%- sr_name %>",
    )))
        # SOURCE LINE 36
        __M_writer(u'\n</script>\n<script id="subreddit-default-report-template" type="text/template">\n    ')
        # SOURCE LINE 39
        __M_writer(conditional_websafe(reddit_report_form(
        fullname=unsafe("<%- fullname %>"),
        system_rules=thing.system_rules,
        sr_name=True,
    )))
        # SOURCE LINE 43
        __M_writer(u'\n</script>\n<script id="reddit-report-template" type="text/template">\n    ')
        # SOURCE LINE 46
        __M_writer(conditional_websafe(reddit_report_form(
        fullname=unsafe("<%- fullname %>"),
        system_rules=thing.system_rules,
    )))
        # SOURCE LINE 49
        __M_writer(u'\n</script>\n<script id="report-reason-template" type="text/template">\n    ')
        # SOURCE LINE 52
        __M_writer(conditional_websafe(report_form_reason(
        rule=unsafe("<%- short_name %>"),
    )))
        # SOURCE LINE 54
        __M_writer(u'\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


