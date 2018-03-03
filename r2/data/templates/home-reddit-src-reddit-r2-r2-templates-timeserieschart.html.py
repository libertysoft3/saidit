# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505799566.49207
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/timeserieschart.html'
_template_uri = '/timeserieschart.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23

import time
import babel.dates
from r2.lib.template_helpers import js_timestamp, format_number


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        thing = context.get('thing', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 27
        __M_writer(u'\n\n')
        # SOURCE LINE 29

        month_names = babel.dates.get_month_names(locale=c.locale)
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['month_names'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 31
        __M_writer(u'\n\n<table id="')
        # SOURCE LINE 33
        __M_writer(conditional_websafe(thing.id))
        __M_writer(u'" class="timeseries ')
        __M_writer(conditional_websafe(thing.classes))
        __M_writer(u'" data-interval="')
        __M_writer(conditional_websafe(thing.interval))
        __M_writer(u'">\n<caption>')
        # SOURCE LINE 34
        __M_writer(conditional_websafe(thing.title))
        __M_writer(u'</caption>\n<thead>\n<tr>\n  <th scope="col">')
        # SOURCE LINE 37
        __M_writer(conditional_websafe(_("date")))
        __M_writer(u'</th>\n')
        # SOURCE LINE 38
        for col in thing.columns:
            # SOURCE LINE 39
            if "color" in col:
                # SOURCE LINE 40
                __M_writer(u'  <th scope="col" title="')
                __M_writer(conditional_websafe(col['title']))
                __M_writer(u'" data-color="')
                __M_writer(conditional_websafe(col['color']))
                __M_writer(u'">')
                __M_writer(conditional_websafe(col['shortname']))
                __M_writer(u'</th>\n')
                # SOURCE LINE 41
            else:
                # SOURCE LINE 42
                __M_writer(u'  <th>')
                __M_writer(conditional_websafe(col['shortname']))
                __M_writer(u'</th>\n')
        # SOURCE LINE 45
        __M_writer(u'</tr>\n</thead>\n<tbody>\n')
        # SOURCE LINE 48
        for date, data in thing.rows:
            # SOURCE LINE 49
            __M_writer(u'<tr\n')
            # SOURCE LINE 50
            if thing.interval == "day" and date.weekday() in (5, 6):
                # SOURCE LINE 51
                __M_writer(u'  class="dow-')
                __M_writer(conditional_websafe(date.weekday()))
                __M_writer(u'"\n')
            # SOURCE LINE 53
            __M_writer(u'  >\n  <th data-value="')
            # SOURCE LINE 54
            __M_writer(conditional_websafe(js_timestamp(date)))
            __M_writer(u'" scope="row">\n')
            # SOURCE LINE 55
            if thing.make_period_link:
                # SOURCE LINE 56
                __M_writer(u'      <a href="')
                __M_writer(conditional_websafe(thing.make_period_link(thing.interval, date)))
                __M_writer(u'">\n')
            # SOURCE LINE 58
            if thing.interval == "hour":
                # SOURCE LINE 59
                __M_writer(u'      ')
                __M_writer(conditional_websafe(babel.dates.format_datetime(date, format="short", locale=c.locale)))
                __M_writer(u'\n')
                # SOURCE LINE 60
            elif thing.interval == "day":
                # SOURCE LINE 61
                __M_writer(u'      ')
                __M_writer(conditional_websafe(babel.dates.format_date(date, format="short", locale=c.locale)))
                __M_writer(u'\n')
                # SOURCE LINE 62
            else:
                # SOURCE LINE 63
                __M_writer(u'      ')
                __M_writer(conditional_websafe(month_names[date.month]))
                __M_writer(u'\n')
            # SOURCE LINE 65
            if thing.make_period_link:
                # SOURCE LINE 66
                __M_writer(u'      </a>\n')
            # SOURCE LINE 68
            __M_writer(u'  </th>\n')
            # SOURCE LINE 69
            for datum in data:
                # SOURCE LINE 70
                if date < thing.latest_available_data:
                    # SOURCE LINE 71
                    __M_writer(u'  <td data-value="')
                    __M_writer(conditional_websafe(datum))
                    __M_writer(u'">')
                    __M_writer(conditional_websafe(format_number(datum)))
                    __M_writer(u'</td>\n')
                    # SOURCE LINE 72
                else:
                    # SOURCE LINE 73
                    __M_writer(u'  <td data-value="-1">')
                    __M_writer(conditional_websafe(_("unavailable")))
                    __M_writer(u'</td>\n')
            # SOURCE LINE 76
            __M_writer(u'</tr>\n')
        # SOURCE LINE 78
        __M_writer(u'</tbody>\n</table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


