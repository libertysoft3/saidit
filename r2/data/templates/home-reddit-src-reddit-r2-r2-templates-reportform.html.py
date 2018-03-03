# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505827250.50754
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/reportform.html'
_template_uri = '/reportform.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 22

from r2.config import feature
from r2.lib.template_helpers import static


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 26
    ns = runtime.TemplateNamespace('__anon_0x7f39d91c2050', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f39d91c2050')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f39d91c2050')._populate(_import_ns, [u'error_field'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 25
        __M_writer(u'\n')
        # SOURCE LINE 26
        __M_writer(u'\n  ')
        # SOURCE LINE 27

        additional_cls = ""
        if not feature.is_enabled("subreddit_rules", subreddit=c.site.name):
            additional_cls = "report-action-form"
          
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['additional_cls'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 31
        __M_writer(u'\n  <form id="report-action-form" class="action-form ')
        # SOURCE LINE 32
        __M_writer(conditional_websafe(additional_cls))
        __M_writer(u' rounded" data-form-action="report">\n    <input type="hidden" name="thing_id" value="')
        # SOURCE LINE 33
        __M_writer(conditional_websafe(thing.thing_fullname))
        __M_writer(u'">\n    <span class="reason-prompt">\n      ')
        # SOURCE LINE 35
        __M_writer(conditional_websafe(_("why are you reporting this?")))
        __M_writer(u'\n    </span>\n    <ol>\n')
        # SOURCE LINE 38
        for rule in thing.rules:
            # SOURCE LINE 39
            __M_writer(u'        <li>\n          <label>\n            <input type="radio" name="reason" value="')
            # SOURCE LINE 41
            __M_writer(conditional_websafe(rule))
            __M_writer(u'">')
            __M_writer(conditional_websafe(rule))
            __M_writer(u'\n          </label>\n        </li>\n')
        # SOURCE LINE 45
        if thing.system_rules:
            # SOURCE LINE 46
            __M_writer(u'        <li>\n          <label>\n            <input type="radio" name="reason" value="site_reason_selected">\n            <select name="site_reason">\n')
            # SOURCE LINE 50
            for rule in thing.system_rules:
                # SOURCE LINE 51
                __M_writer(u'                <option value="')
                __M_writer(conditional_websafe(rule))
                __M_writer(u'">')
                __M_writer(conditional_websafe(_("reddit rule: %(rule_name)s" % dict(rule_name=rule))))
                __M_writer(u'</option>\n')
            # SOURCE LINE 53
            __M_writer(u'            </select>\n          </label>\n        </li>\n')
        # SOURCE LINE 57
        __M_writer(u'      <li>\n        <label>\n          <input type="radio" name="reason" value="other">')
        # SOURCE LINE 59
        __M_writer(conditional_websafe(_("other (max %(num)s characters):") % dict(num=100)))
        __M_writer(u'\n        </label>\n        <input name="other_reason" value="" maxlength="100" type="text" disabled>\n      </li>\n    </ol>\n    <button type="submit" class="btn submit-action-thing" disabled>\n      ')
        # SOURCE LINE 65
        __M_writer(conditional_websafe(_("submit")))
        __M_writer(u'\n    </button>\n    <button type="button" class="btn cancel-action-thing report-cancel">\n      ')
        # SOURCE LINE 68
        __M_writer(conditional_websafe(_("cancel")))
        __M_writer(u'\n    </button>\n    <span class="status"></span>\n    ')
        # SOURCE LINE 71
        __M_writer(conditional_websafe(error_field("TOO_LONG", "reason", "span")))
        __M_writer(u'\n  </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


