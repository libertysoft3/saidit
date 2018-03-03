# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505007497.848071
_enable_loop = True
_template_filename = u'/home/reddit/src/reddit/r2/r2/templates/utils/gold.html'
_template_uri = u'/utils/gold.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['gold_dropdown']


# SOURCE LINE 23

from r2.lib.strings import Score


# SOURCE LINE 32

month_options = (1, 3)
year_options = (1, 2, 3)
  

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'\n\n')
        # SOURCE LINE 50
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_gold_dropdown(context,what,chosen_months,somethings=None,append_or_somethings=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 27
        __M_writer(u'\n  ')
        # SOURCE LINE 28

        if not somethings:
          somethings = what
          
        
        # SOURCE LINE 31
        __M_writer(u'\n  ')
        # SOURCE LINE 35
        __M_writer(u'\n  <select id=')
        # SOURCE LINE 36
        __M_writer(conditional_websafe(what))
        __M_writer(u' name=')
        __M_writer(conditional_websafe(what))
        __M_writer(u' class="gold-dropdown">\n')
        # SOURCE LINE 37
        for i in month_options:
            # SOURCE LINE 38
            __M_writer(u'       <option value="')
            __M_writer(conditional_websafe(i))
            __M_writer(u'" ')
            __M_writer(conditional_websafe("selected" if chosen_months == i else ""))
            __M_writer(u'>\n         ')
            # SOURCE LINE 39
            __M_writer(conditional_websafe(Score.somethings(i, somethings)))
            __M_writer(u': ')
            __M_writer(conditional_websafe(g.gold_month_price * i))
            __M_writer(u'\n         ')
            # SOURCE LINE 40
            __M_writer(conditional_websafe(" or %s" % Score.somethings(i, append_or_somethings) if append_or_somethings else ""))
            __M_writer(u'\n       </option>\n')
        # SOURCE LINE 43
        for i in year_options:
            # SOURCE LINE 44
            __M_writer(u'       <option value="')
            __M_writer(conditional_websafe(i * 12))
            __M_writer(u'" ')
            __M_writer(conditional_websafe("selected" if (chosen_months == (i * 12) or (not chosen_months and i == 1)) else ""))
            __M_writer(u'>\n         ')
            # SOURCE LINE 45
            __M_writer(conditional_websafe(Score.somethings(i * 12, somethings)))
            __M_writer(u' &#32; (special price!): ')
            __M_writer(conditional_websafe(g.gold_year_price * i))
            __M_writer(u'\n         ')
            # SOURCE LINE 46
            __M_writer(conditional_websafe(" or %s" % Score.somethings(i * 12, append_or_somethings) if append_or_somethings else ""))
            __M_writer(u'\n       </option>\n')
        # SOURCE LINE 49
        __M_writer(u'  </select>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


