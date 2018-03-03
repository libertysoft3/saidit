# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1520060829.025438
_enable_loop = True
_template_filename = u'/home/reddit/src/reddit/r2/r2/templates/less.html'
_template_uri = u'/less.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['less_stylesheet', 'less_js']


# SOURCE LINE 23

from r2.lib.template_helpers import static
from r2.lib import js


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 26
        __M_writer(u'\n\n')
        # SOURCE LINE 37
        __M_writer(u'\n\n')
        # SOURCE LINE 46
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_less_stylesheet(context,*names):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 28
        __M_writer(u'\n')
        # SOURCE LINE 29
        for name in names:
            # SOURCE LINE 30
            __M_writer(u'    ')
            name = name[:name.rfind('.less')] 
            
            __M_writer(u'\n')
            # SOURCE LINE 31
            if g.uncompressedJS:
                # SOURCE LINE 32
                __M_writer(u'      <link rel="stylesheet/less" type="text/css" href="')
                __M_writer(conditional_websafe(static(name+'.less')))
                __M_writer(u'" media="all">\n')
                # SOURCE LINE 33
            else:
                # SOURCE LINE 34
                __M_writer(u'      <link rel="stylesheet" type="text/css" href="')
                __M_writer(conditional_websafe(static(name+'.css')))
                __M_writer(u'" media="all">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_less_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 39
        __M_writer(u'\n')
        # SOURCE LINE 40
        if g.uncompressedJS:
            # SOURCE LINE 41
            __M_writer(u'    <script type="text/javascript">\n      less = {env: \'development\'};\n    </script>\n    ')
            # SOURCE LINE 44
            __M_writer(conditional_websafe(unsafe(js.use('less'))))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


