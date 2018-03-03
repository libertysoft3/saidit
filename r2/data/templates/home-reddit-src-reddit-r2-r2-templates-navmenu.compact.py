# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1508303897.816405
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/navmenu.compact'
_template_uri = '/navmenu.compact'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['tabmenu', 'flatlist', 'dropdown']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'\n\n\n')
        # SOURCE LINE 50
        __M_writer(u'\n\n')
        # SOURCE LINE 67
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tabmenu(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        thing = context.get('thing', UNDEFINED)
        str = context.get('str', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 52
        __M_writer(u'\n')
        # SOURCE LINE 53
        if thing:
            # SOURCE LINE 54
            __M_writer(u'    ')
            css_class = str(thing.css_class) if thing.css_class else "" 
            
            __M_writer(u'\n    <ul class="tabmenu ')
            # SOURCE LINE 55
            __M_writer(conditional_websafe(css_class))
            __M_writer(u'"\n        ')
            # SOURCE LINE 56
            __M_writer(conditional_websafe("id='%s'" % thing._id if thing._id else ""))
            __M_writer(u'>\n')
            # SOURCE LINE 57
            for i, option in enumerate(thing):
                # SOURCE LINE 58
                __M_writer(u'        ')

                option.selected = (option == thing.selected)
                        
                
                # SOURCE LINE 60
                __M_writer(u'\n        <li ')
                # SOURCE LINE 61
                __M_writer(conditional_websafe("class='selected'" if option.selected else ""))
                __M_writer(u'>\n          ')
                # SOURCE LINE 62
                __M_writer(conditional_websafe(option))
                __M_writer(u'\n        </li>\n')
            # SOURCE LINE 65
            __M_writer(u'    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_flatlist(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        thing = context.get('thing', UNDEFINED)
        str = context.get('str', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 28
        __M_writer(u'\n  ')
        # SOURCE LINE 29
        css_class = str(thing.css_class) if thing.css_class else "" 
        
        __M_writer(u'\n')
        # SOURCE LINE 30
        if thing:
            # SOURCE LINE 31
            __M_writer(u'    <ul class="')
            __M_writer(conditional_websafe(css_class))
            __M_writer(u' hover"\n        ')
            # SOURCE LINE 32
            __M_writer(conditional_websafe("id='%s'" % thing._id if thing._id else ""))
            __M_writer(u'>\n\n\n')
            # SOURCE LINE 35
            for i, option in enumerate(thing):
                # SOURCE LINE 36
                __M_writer(u'        ')

           ##option.title isn't the title, option.render() is the entire link
                if option == thing.selected:
                  class_name = "class='selected'"
                  option.selected = True                                           
                else:
                  class_name = ""
                        
                
                # SOURCE LINE 43
                __M_writer(u'\n        <li ')
                # SOURCE LINE 44
                __M_writer(conditional_websafe(class_name))
                __M_writer(u'>\n          ')
                # SOURCE LINE 45
                __M_writer(conditional_websafe(option))
                __M_writer(u'\n        </li>\n')
            # SOURCE LINE 48
            __M_writer(u'    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_dropdown(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        def flatlist():
            return render_flatlist(context)
        __M_writer = context.writer()
        # SOURCE LINE 23
        __M_writer(u'\n  ')
        # SOURCE LINE 24
        __M_writer(conditional_websafe(flatlist()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


