# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505799316.358004
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/fraudform.html'
_template_uri = '/fraudform.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n<form id="fraud-action-form" class="action-form fraud-action-form rounded" data-form-action="review_fraud">\n  <input type="hidden" name="thing_id" value="thing-fullname">\n  <small class="fraud-reason"></small>\n  <span class="reason-prompt">\n    ')
        # SOURCE LINE 27
        __M_writer(conditional_websafe(_('is this fraud?')))
        __M_writer(u'\n  </span>\n  <ol>\n    <li>\n      <label>\n        <input type="radio" name="fraud" value="True">')
        # SOURCE LINE 32
        __M_writer(conditional_websafe(_("yes")))
        __M_writer(u'\n      </label>\n    </li>\n    <li>\n      <label>\n        <input type="radio" name="fraud" value="False">')
        # SOURCE LINE 37
        __M_writer(conditional_websafe(_("no")))
        __M_writer(u'\n      </label>\n    </li>\n  </ol>\n  <button type="submit" class="btn submit-action-thing" disabled>\n    ')
        # SOURCE LINE 42
        __M_writer(conditional_websafe(_("submit")))
        __M_writer(u'\n  </button>\n  <button type="button" class="btn cancel-action-thing">\n    ')
        # SOURCE LINE 45
        __M_writer(conditional_websafe(_("cancel")))
        __M_writer(u'\n  </button>\n  <span class="status"></span>\n</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


