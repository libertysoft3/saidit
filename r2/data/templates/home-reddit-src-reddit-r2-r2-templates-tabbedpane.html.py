# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1509242599.118291
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/tabbedpane.html'
_template_uri = '/tabbedpane.html'
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
        thing = context.get('thing', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(conditional_websafe(thing.tabmenu))
        __M_writer(u'\n<div class="tabpane-content">\n')
        # SOURCE LINE 25
        for i, (name, title, pane) in enumerate(thing.tabs):
            # SOURCE LINE 26
            __M_writer(u'    <div id="tabbedpane-')
            __M_writer(conditional_websafe(name))
            __M_writer(u'" class="tabbedpane"\n         ')
            # SOURCE LINE 27
            __M_writer(conditional_websafe("style='display:none'" if i > 0 else ""))
            __M_writer(u'>\n      ')
            # SOURCE LINE 28
            __M_writer(conditional_websafe(pane))
            __M_writer(u'\n    </div>\n')
        # SOURCE LINE 31
        __M_writer(u'</div>\n')
        # SOURCE LINE 32
        if thing.linkable:
            # SOURCE LINE 33
            __M_writer(u'  <script>\n    $(function() {\n        var target = "tab-" + $(window.location).attr("hash").substr(1);\n        $(".tabmenu li").each(function() {\n            if (this.id == target) {\n                $(this).find("a").click();\n            }\n        });\n    });\n  </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


