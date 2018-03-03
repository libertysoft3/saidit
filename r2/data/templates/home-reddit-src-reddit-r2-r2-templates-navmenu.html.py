# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505002596.196736
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/navmenu.html'
_template_uri = '/navmenu.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['tabmenu', 'flatlist', 'dropdown']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7fde6027fe50', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fde6027fe50')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fde6027fe50')._populate(_import_ns, [u'plain_link', u'post_link', u'img_link', u'separator'])
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n')
        # SOURCE LINE 55
        __M_writer(u'\n\n\n')
        # SOURCE LINE 86
        __M_writer(u'\n\n\n')
        # SOURCE LINE 106
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tabmenu(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fde6027fe50')._populate(_import_ns, [u'plain_link', u'post_link', u'img_link', u'separator'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        str = _import_ns.get('str', context.get('str', UNDEFINED))
        enumerate = _import_ns.get('enumerate', context.get('enumerate', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 89
        __M_writer(u'\n')
        # SOURCE LINE 90
        if thing:
            # SOURCE LINE 91
            __M_writer(u'    ')
            css_class = str(thing.css_class) if thing.css_class else "" 
            
            __M_writer(u'\n    <ul class="tabmenu ')
            # SOURCE LINE 92
            __M_writer(conditional_websafe(css_class))
            __M_writer(u'"\n        ')
            # SOURCE LINE 93
            __M_writer(conditional_websafe("id='%s'" % thing._id if thing._id else ""))
            __M_writer(u'>\n')
            # SOURCE LINE 94
            for i, option in enumerate(thing):
                # SOURCE LINE 95
                __M_writer(u'        ')

                tab_name = getattr(option, 'tab_name', None)
                li_id = "id='tab-%s'" % tab_name if tab_name else ""
                li_class = "class='selected'" if option == thing.selected else ""
                        
                
                # SOURCE LINE 99
                __M_writer(u'\n        <li ')
                # SOURCE LINE 100
                __M_writer(conditional_websafe(li_id))
                __M_writer(u' ')
                __M_writer(conditional_websafe(li_class))
                __M_writer(u'>\n          ')
                # SOURCE LINE 101
                __M_writer(conditional_websafe(option))
                __M_writer(u'\n        </li>\n')
            # SOURCE LINE 104
            __M_writer(u'    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_flatlist(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fde6027fe50')._populate(_import_ns, [u'plain_link', u'post_link', u'img_link', u'separator'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        separator = _import_ns.get('separator', context.get('separator', UNDEFINED))
        str = _import_ns.get('str', context.get('str', UNDEFINED))
        enumerate = _import_ns.get('enumerate', context.get('enumerate', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 58
        __M_writer(u'\n  ')
        # SOURCE LINE 59
        css_class = str(thing.css_class) if thing.css_class else "" 
        
        __M_writer(u'\n')
        # SOURCE LINE 60
        if thing:
            # SOURCE LINE 61
            __M_writer(u'    <ul class="')
            __M_writer(conditional_websafe(css_class))
            __M_writer(u' hover"\n        ')
            # SOURCE LINE 62
            __M_writer(conditional_websafe("id='%s'" % thing._id if thing._id else ""))
            __M_writer(u'>\n\n')
            # SOURCE LINE 64
            if thing.title:
                # SOURCE LINE 65
                __M_writer(u'        <li class="')
                __M_writer(conditional_websafe(css_class))
                __M_writer(u' title">')
                __M_writer(conditional_websafe(thing.title))
                __M_writer(u'</li>\n')
            # SOURCE LINE 67
            __M_writer(u'\n')
            # SOURCE LINE 68
            for i, option in enumerate(thing):
                # SOURCE LINE 69
                __M_writer(u'        ')

           ##option.title isn't the title, option.render() is the entire link
                if option == thing.selected:
                  class_name = "class='selected'"
                  option.selected = True                                           
                else:
                  class_name = ""
                        
                
                # SOURCE LINE 76
                __M_writer(u'\n        <li ')
                # SOURCE LINE 77
                __M_writer(conditional_websafe(class_name))
                __M_writer(u'>\n')
                # SOURCE LINE 78
                if i > 0:
                    # SOURCE LINE 79
                    __M_writer(u'            ')
                    __M_writer(conditional_websafe(separator(thing.separator)))
                    __M_writer(u'\n')
                # SOURCE LINE 81
                __M_writer(u'          ')
                __M_writer(conditional_websafe(option))
                __M_writer(u'\n        </li>\n')
            # SOURCE LINE 84
            __M_writer(u'    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_dropdown(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fde6027fe50')._populate(_import_ns, [u'plain_link', u'post_link', u'img_link', u'separator'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        str = _import_ns.get('str', context.get('str', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 25
        __M_writer(u'\n')
        # SOURCE LINE 29
        __M_writer(u'  ')
        css_class = str(thing.css_class) if thing.css_class else "" 
        
        __M_writer(u'\n')
        # SOURCE LINE 30
        if thing:
            # SOURCE LINE 31
            if thing.title and thing.selected:
                # SOURCE LINE 32
                __M_writer(u'      <span class="dropdown-title ')
                __M_writer(conditional_websafe(css_class))
                __M_writer(u'">')
                __M_writer(conditional_websafe(thing.title))
                __M_writer(u':&#32;</span>\n')
            # SOURCE LINE 34
            __M_writer(u'\n    <div class="dropdown ')
            # SOURCE LINE 35
            __M_writer(conditional_websafe(css_class))
            __M_writer(u'"\n         ')
            # SOURCE LINE 36
            __M_writer(conditional_websafe("id='%s'" % thing._id if thing._id else ""))
            __M_writer(u'\n         onclick="open_menu(this)">\n \n')
            # SOURCE LINE 39
            if thing.selected:
                # SOURCE LINE 40
                __M_writer(u'          <span class="selected">')
                __M_writer(conditional_websafe(thing.selected.selected_title()))
                __M_writer(u'</span>\n')
                # SOURCE LINE 41
            elif thing.title:
                # SOURCE LINE 42
                __M_writer(u'          <span class="selected title">')
                __M_writer(conditional_websafe(thing.title))
                __M_writer(u'</span>\n')
            # SOURCE LINE 44
            __M_writer(u'    </div>\n\n    <div class="drop-choices ')
            # SOURCE LINE 46
            __M_writer(conditional_websafe(css_class))
            __M_writer(u'">\n')
            # SOURCE LINE 47
            for option in thing:
                # SOURCE LINE 48
                if option != thing.selected:
                    # SOURCE LINE 49
                    __M_writer(u'          ')
                    __M_writer(conditional_websafe(option))
                    __M_writer(u'\n')
            # SOURCE LINE 52
            __M_writer(u'    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


