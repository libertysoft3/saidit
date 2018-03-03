# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1508303897.896705
_enable_loop = True
_template_filename = u'/home/reddit/src/reddit/r2/r2/templates/printable.compact'
_template_uri = u'/printable.compact'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['delete_report_buttons']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 50
        __M_writer(u'\n\nempty\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_delete_report_buttons(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        thing = context.get('thing', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 23
        __M_writer(u'\n  ')
        # SOURCE LINE 24

        is_author = (c.user_is_loggedin and thing.author and
        c.user.name == thing.author.name)
           
        
        # SOURCE LINE 27
        __M_writer(u'\n')
        # SOURCE LINE 28
        if is_author:
            # SOURCE LINE 29
            __M_writer(u'    <div class="thing_suboption_popup_container hidden">\n      <div class="thing_suboption_popup">\n       <a href="#" \n          onclick="return change_state(this, \'del\', hide_thing, true)">\n        yes\n       </a>\n       <a href="#" class="thing_option_close">no</a>\n      </div>\n    </div>\n    <a href="#" class="thing_suboption_link">Delete</a>\n')
        # SOURCE LINE 40
        __M_writer(u'  <div class="thing_suboption_popup_container hidden">\n    <div class="thing_suboption_popup">\n      <a href="#" \n        onclick="return change_state(this, \'report\', hide_thing, true)">\n        yes\n      </a>\n      <a href="#" class="thing_option_close">no</a>\n    </div>\n  </div>\n  <a href="#" class="thing_suboption_link">Report</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


