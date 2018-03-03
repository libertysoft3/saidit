# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1520060829.719807
_enable_loop = True
_template_filename = u'/home/reddit/src/reddit/r2/r2/templates/subredditreportform.html'
_template_uri = u'/subredditreportform.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['reddit_report_form', 'report_form_base', 'report_form_reason_other', 'report_form_reason', 'subreddit_report_form']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 22
    ns = runtime.TemplateNamespace('__anon_0x7fc7c779d310', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fc7c779d310')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c779d310')._populate(_import_ns, [u'error_field'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        # SOURCE LINE 51
        __M_writer(u'\n\n')
        # SOURCE LINE 90
        __M_writer(u'\n\n')
        # SOURCE LINE 111
        __M_writer(u'\n\n')
        # SOURCE LINE 133
        __M_writer(u'\n\n')
        # SOURCE LINE 142
        __M_writer(u'\n\n')
        # SOURCE LINE 144
        if thing.rules:
            # SOURCE LINE 145
            __M_writer(u'    ')
            __M_writer(conditional_websafe(self.subreddit_report_form(
        fullname=thing.thing_fullname,
        rules=thing.rules,
        system_rules=thing.system_rules,
        sr_name=thing.sr_name,
    )))
            # SOURCE LINE 150
            __M_writer(u'\n')
            # SOURCE LINE 151
        else:
            # SOURCE LINE 152
            __M_writer(u'    ')
            __M_writer(conditional_websafe(self.reddit_report_form(
        fullname=thing.thing_fullname,
        system_rules=thing.system_rules,
    )))
            # SOURCE LINE 155
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_reddit_report_form(context,fullname,system_rules,sr_name=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c779d310')._populate(_import_ns, [u'error_field'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 92
        __M_writer(u'\n    ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                # SOURCE LINE 96
                __M_writer(u'\n        <ol class="report-reason-list">\n')
                # SOURCE LINE 98
                for rule in system_rules:
                    # SOURCE LINE 99
                    __M_writer(u'                ')
                    __M_writer(conditional_websafe(self.report_form_reason(rule)))
                    __M_writer(u'\n')
                # SOURCE LINE 101
                __M_writer(u'            ')
                __M_writer(conditional_websafe(self.report_form_reason_other()))
                __M_writer(u'\n        </ol>\n        <div class="report-header">\n')
                # SOURCE LINE 104
                if sr_name:
                    # SOURCE LINE 105
                    __M_writer(u'                ')
                    __M_writer(conditional_websafe(_("Reports go to community moderators anonymously")))
                    __M_writer(u'\n')
                    # SOURCE LINE 106
                else:
                    # SOURCE LINE 107
                    __M_writer(u'                ')
                    __M_writer(conditional_websafe(_("Reports go to Reddit admins")))
                    __M_writer(u'\n')
                # SOURCE LINE 109
                __M_writer(u'        </div>\n    ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 93
            __M_writer(conditional_websafe(self.report_form_base(fullname=(fullname),rules_page_link=u'/help/contentpolicy')))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 110
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_report_form_base(context,fullname,rules_page_link):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c779d310')._populate(_import_ns, [u'error_field'])
        caller = _import_ns.get('caller', context.get('caller', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 24
        __M_writer(u'\n    <form id="report-action-form"\n            class="subreddit-report-form rounded">\n        <input type="hidden"\n                name="thing_id"\n                value="')
        # SOURCE LINE 29
        __M_writer(conditional_websafe(fullname))
        __M_writer(u'">\n        <a href="')
        # SOURCE LINE 30
        __M_writer(conditional_websafe(rules_page_link))
        __M_writer(u'"\n                class="action-icon action-icon-info c-hide-text may-blank"\n                title="')
        # SOURCE LINE 32
        __M_writer(conditional_websafe(_('View the community rules')))
        __M_writer(u'">\n            ')
        # SOURCE LINE 33
        __M_writer(conditional_websafe(_('View the community rules')))
        __M_writer(u'\n        </a>\n        <div class="reason-prompt report-header">\n            ')
        # SOURCE LINE 36
        __M_writer(conditional_websafe(_("What rule does this break?")))
        __M_writer(u'\n        </div>\n\n        ')
        # SOURCE LINE 39
        __M_writer(conditional_websafe(caller.body()))
        __M_writer(u'\n\n        <div class="c-submit-group">\n            <button type="button" class="btn c-btn c-btn-secondary report-cancel">\n                ')
        # SOURCE LINE 43
        __M_writer(conditional_websafe(_("cancel")))
        __M_writer(u'\n            </button>&#32;\n            <button type="submit" class="btn c-btn c-btn-primary submit-action-thing" disabled>\n                ')
        # SOURCE LINE 46
        __M_writer(conditional_websafe(_("report")))
        __M_writer(u'\n            </button>\n        </div>\n        <span class="status" style="display: none"></span>\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_report_form_reason_other(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c779d310')._populate(_import_ns, [u'error_field'])
        error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 113
        __M_writer(u'\n    <li class="report-reason-item report-reason-other">\n        <label>\n            <input type="radio"\n                    name="reason"\n                    value="other">\n            <div class="report-reason-display">\n                <div>\n                    ')
        # SOURCE LINE 121
        __M_writer(conditional_websafe(_("Other (max %(num)s characters):") % dict(num=100)))
        __M_writer(u'\n                </div>\n                <input type="text"\n                        class="c-form-control"\n                        name="other_reason"\n                        value=""\n                        maxlength="100"\n                        disabled>\n                ')
        # SOURCE LINE 129
        __M_writer(conditional_websafe(error_field("TOO_LONG", "other_reason", "span")))
        __M_writer(u'\n            </div>\n        </label>\n    </li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_report_form_reason(context,rule):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c779d310')._populate(_import_ns, [u'error_field'])
        __M_writer = context.writer()
        # SOURCE LINE 135
        __M_writer(u'\n    <li class="report-reason-item">\n        <label>\n          <input type="radio" name="reason" value="')
        # SOURCE LINE 138
        __M_writer(conditional_websafe(rule))
        __M_writer(u'">\n          <div class="report-reason-display">')
        # SOURCE LINE 139
        __M_writer(conditional_websafe(rule))
        __M_writer(u'</div>\n        </label>\n    </li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_subreddit_report_form(context,fullname,system_rules,rules,sr_name):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c779d310')._populate(_import_ns, [u'error_field'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 53
        __M_writer(u'\n    ')
        # SOURCE LINE 54

        rules_page_link = "/r/%s/about/rules" % sr_name
            
        
        # SOURCE LINE 56
        __M_writer(u'\n    ')
        def ccall(caller):
            def body():
                dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
                __M_writer = context.writer()
                # SOURCE LINE 60
                __M_writer(u'\n        <ol class="report-reason-list">\n')
                # SOURCE LINE 62
                if rules:
                    # SOURCE LINE 63
                    for rule in rules:
                        # SOURCE LINE 64
                        __M_writer(u'                    ')
                        __M_writer(conditional_websafe(self.report_form_reason(rule.get("short_name"))))
                        __M_writer(u'\n')
                # SOURCE LINE 67
                __M_writer(u'            <li class="report-reason-item report-reason-reddit" \n                <label>\n                    <input type="radio"\n                            class="site-reason-radio"\n                            name="reason"\n                            value="site_reason_selected">\n                    <div class="report-reason-display">\n                        <select name="site_reason">\n')
                # SOURCE LINE 75
                for rule in system_rules:
                    # SOURCE LINE 76
                    __M_writer(u'                                <option value="')
                    __M_writer(conditional_websafe(rule))
                    __M_writer(u'">\n                                    ')
                    # SOURCE LINE 77
                    __M_writer(conditional_websafe(_("Reddit rule: %(rule_name)s" % dict(rule_name=rule))))
                    __M_writer(u'\n                                </option>\n')
                # SOURCE LINE 80
                __M_writer(u'                        </select>\n                    </div>\n                </label>\n            </li>\n            ')
                # SOURCE LINE 84
                __M_writer(conditional_websafe(self.report_form_reason_other()))
                __M_writer(u'\n            <div class="report-header">\n                ')
                # SOURCE LINE 86
                __M_writer(conditional_websafe(_("Reports go to community moderators anonymously")))
                __M_writer(u'\n            </div>\n        </ol>\n    ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 57
            __M_writer(conditional_websafe(self.report_form_base(fullname=(fullname),rules_page_link=(unsafe(rules_page_link)))))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 89
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


