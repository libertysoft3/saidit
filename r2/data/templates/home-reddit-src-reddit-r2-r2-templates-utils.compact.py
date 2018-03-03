# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1508303897.890642
_enable_loop = True
_template_filename = u'/home/reddit/src/reddit/r2/r2/templates/utils.compact'
_template_uri = u'/utils.compact'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['toggle_button', 'icon_button']


# SOURCE LINE 23

import string


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'\n\n')
        # SOURCE LINE 38
        __M_writer(u'\n')
        # SOURCE LINE 59
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_toggle_button(context,togglename,toggled=False):
    __M_caller = context.caller_stack._push_frame()
    try:
        def icon_button(text,css_class,href='javascript:void(0)',outer_class='',**kw):
            return render_icon_button(context,text,css_class,href,outer_class,**kw)
        endif = context.get('endif', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 39
        __M_writer(u'\n    ')
        # SOURCE LINE 40

        if toggled:
            togglestyle = {"style": "display: none;"}
            untogglestyle = {}
        else:
            togglestyle = {}
            untogglestyle = {"style": "display: none;"}
        endif
        
        if togglename == "hide":
            untext = ""
        else:
            untext = "un"
        endif
        
        
        # SOURCE LINE 54
        __M_writer(u'\n')
        # SOURCE LINE 56
        __M_writer(u'    ')
        __M_writer(conditional_websafe(icon_button( string.capitalize(togglename), togglename + "-icon", onclick="change_state(this,'" + togglename + "', " + togglename + "_thing)", outer_class=togglename + "-button", **togglestyle)))
        __M_writer(u'\n')
        # SOURCE LINE 58
        __M_writer(u'    ')
        __M_writer(conditional_websafe(icon_button( "Un" + togglename, "un" + togglename + "-icon", onclick="change_state(this,'un" + togglename + "', " + untext + togglename + "_thing)", outer_class= "un" + togglename + "-button", **untogglestyle)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_icon_button(context,text,css_class,href='javascript:void(0)',outer_class='',**kw):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 27
        __M_writer(u'\n    <a href="')
        # SOURCE LINE 28
        __M_writer(conditional_websafe(href))
        __M_writer(u'"\n')
        # SOURCE LINE 29
        if outer_class :
            # SOURCE LINE 30
            __M_writer(u'            class="')
            __M_writer(conditional_websafe(outer_class))
            __M_writer(u'"\n')
        # SOURCE LINE 32
        for k, v in kw.iteritems():
            # SOURCE LINE 33
            __M_writer(u'            ')
            __M_writer(conditional_websafe(k))
            __M_writer(u'="')
            __M_writer(conditional_websafe(v))
            __M_writer(u'"\n')
        # SOURCE LINE 35
        __M_writer(u'    >\n    <div class="')
        # SOURCE LINE 36
        __M_writer(conditional_websafe(css_class))
        __M_writer(u'"></div>')
        __M_writer(conditional_websafe(text))
        __M_writer(u'\n    </a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


