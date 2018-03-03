# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505799566.468502
_enable_loop = True
_template_filename = u'/home/reddit/src/reddit/r2/r2/templates/reddittraffic.html'
_template_uri = u'/reddittraffic.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['tables', 'load_timeseries_js', 'sidetables', 'top_content', 'preamble', 'last_modified_message']


# SOURCE LINE 23

import babel.dates

from r2.lib import js
from r2.lib.strings import strings
from r2.lib.template_helpers import static, js_timestamp, format_number

import babel.dates


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 33
    ns = runtime.TemplateNamespace('__anon_0x7ff76ed20a90', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7ff76ed20a90')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7ff76ed20a90')._populate(_import_ns, [u'_md'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        _md = _import_ns.get('_md', context.get('_md', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 31
        __M_writer(u'\n\n')
        # SOURCE LINE 33
        __M_writer(u'\n\n')
        # SOURCE LINE 42
        __M_writer(u'\n\n<div class="md-container wiki-page-content">\n')
        # SOURCE LINE 45
        if thing.place:
            # SOURCE LINE 46
            __M_writer(u'    ')
            __M_writer(conditional_websafe(_md(("# traffic statistics for %(place)s") % dict(place=thing.place), wrap=True)))
            __M_writer(u'\n')
        # SOURCE LINE 48
        __M_writer(u'\n  ')
        # SOURCE LINE 49
        __M_writer(conditional_websafe(self.preamble()))
        __M_writer(u'\n\n  ')
        # SOURCE LINE 51
        __M_writer(conditional_websafe(self.last_modified_message()))
        __M_writer(u'\n\n  ')
        # SOURCE LINE 53
        __M_writer(conditional_websafe(self.top_content()))
        __M_writer(u'\n</div>\n\n')
        # SOURCE LINE 66
        __M_writer(u'\n\n')
        # SOURCE LINE 68
        __M_writer(u'\n\n<div id="charts"></div>\n\n<div class="traffic-tables-side">\n')
        # SOURCE LINE 73
        __M_writer(conditional_websafe(self.sidetables()))
        __M_writer(u'\n</div>\n\n<div class="traffic-tables">\n')
        # SOURCE LINE 77
        __M_writer(conditional_websafe(self.tables()))
        __M_writer(u'\n</div>\n\n<script type="text/javascript">\n  r.timeseries.init()\n</script>\n\n')
        # SOURCE LINE 84
        __M_writer(u'\n\n')
        # SOURCE LINE 121
        __M_writer(u'\n\n')
        # SOURCE LINE 127
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tables(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7ff76ed20a90')._populate(_import_ns, [u'_md'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 123
        __M_writer(u'\n')
        # SOURCE LINE 124
        for table in thing.tables:
            # SOURCE LINE 125
            __M_writer(u'  ')
            __M_writer(conditional_websafe(table))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_load_timeseries_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7ff76ed20a90')._populate(_import_ns, [u'_md'])
        __M_writer = context.writer()
        # SOURCE LINE 35
        __M_writer(u'\n  <!--[if lte IE 8]>\n  ')
        # SOURCE LINE 37
        __M_writer(conditional_websafe(unsafe(js.use('timeseries-ie'))))
        __M_writer(u'\n  <![endif]-->\n  <!--[if !(lte IE 8)]><!-->\n  ')
        # SOURCE LINE 40
        __M_writer(conditional_websafe(unsafe(js.use('timeseries'))))
        __M_writer(u'\n  <!--<![endif]-->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sidetables(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7ff76ed20a90')._populate(_import_ns, [u'_md'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 86
        __M_writer(u'\n  ')
        # SOURCE LINE 87

        day_names = babel.dates.get_day_names(locale=c.locale)
          
        
        # SOURCE LINE 89
        __M_writer(u'\n\n')
        # SOURCE LINE 91
        if thing.dow_summary:
            # SOURCE LINE 92
            __M_writer(u'  <table class="traffic-table">\n  <caption>')
            # SOURCE LINE 93
            __M_writer(conditional_websafe(_("traffic by day of week")))
            __M_writer(u'</caption>\n  <thead>\n  <tr>\n    <th scope="col">')
            # SOURCE LINE 96
            __M_writer(conditional_websafe(_("day")))
            __M_writer(u'</th>\n    <th scope="col">')
            # SOURCE LINE 97
            __M_writer(conditional_websafe(_("uniques")))
            __M_writer(u'</th>\n    <th scope="col">')
            # SOURCE LINE 98
            __M_writer(conditional_websafe(_("pageviews")))
            __M_writer(u'</th>\n  </tr>\n  </thead>\n  <tbody>\n')
            # SOURCE LINE 102
            for dow, cols in thing.dow_summary:
                # SOURCE LINE 103
                __M_writer(u'  <tr>\n    <th scope="row">')
                # SOURCE LINE 104
                __M_writer(conditional_websafe(day_names[dow]))
                __M_writer(u'</th>\n')
                # SOURCE LINE 105
                for col in cols:
                    # SOURCE LINE 106
                    __M_writer(u'    <td>')
                    __M_writer(conditional_websafe(format_number(col)))
                    __M_writer(u'</td>\n')
                # SOURCE LINE 108
                __M_writer(u'  </tr>\n')
            # SOURCE LINE 110
            __M_writer(u'  </tbody>\n  <tfoot>\n  <tr>\n    <th scope="row">')
            # SOURCE LINE 113
            __M_writer(conditional_websafe(_("daily mean")))
            __M_writer(u'</th>\n')
            # SOURCE LINE 114
            for col in thing.dow_means:
                # SOURCE LINE 115
                __M_writer(u'    <td>')
                __M_writer(conditional_websafe(format_number(col)))
                __M_writer(u'</td>\n')
            # SOURCE LINE 117
            __M_writer(u'  </tr>\n  </tfoot>\n  </table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_content(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7ff76ed20a90')._populate(_import_ns, [u'_md'])
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_preamble(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7ff76ed20a90')._populate(_import_ns, [u'_md'])
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_last_modified_message(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7ff76ed20a90')._populate(_import_ns, [u'_md'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 56
        __M_writer(u'\n    <p id="timeseries-unprocessed" data-last-processed="')
        # SOURCE LINE 57
        __M_writer(conditional_websafe(js_timestamp(thing.traffic_last_modified)))
        __M_writer(u'"\n')
        # SOURCE LINE 58
        if thing.traffic_lag.total_seconds() > 10800:
            # SOURCE LINE 59
            __M_writer(u'      class="slow">\n      ')
            # SOURCE LINE 60
            __M_writer(conditional_websafe(strings.traffic_processing_slow % dict(date=babel.dates.format_datetime(thing.traffic_last_modified, format="long", locale=c.locale))))
            __M_writer(u'\n')
            # SOURCE LINE 61
        else:
            # SOURCE LINE 62
            __M_writer(u'      >\n      ')
            # SOURCE LINE 63
            __M_writer(conditional_websafe(strings.traffic_processing_normal % dict(date=babel.dates.format_datetime(thing.traffic_last_modified, format="long", locale=c.locale))))
            __M_writer(u'\n')
        # SOURCE LINE 65
        __M_writer(u'    </p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


