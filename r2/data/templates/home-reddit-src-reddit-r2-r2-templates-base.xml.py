# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1520062243.574584
_enable_loop = True
_template_filename = u'/home/reddit/src/reddit/r2/r2/templates/base.xml'
_template_uri = u'/base.xml'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['Category', 'Updated', 'Subtitle', 'Title', 'Link', 'Logo', 'Id', 'Icon']


# SOURCE LINE 22

from pylons import app_globals as g
from datetime import datetime
from r2.lib.template_helpers import add_sr, header_url
from r2.lib.template_helpers import static
from r2.lib.template_helpers import html_datetime
from r2.lib.utils import UrlParser
# atom rfc: https://tools.ietf.org/html/rfc4287


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 30
        __M_writer(u'\n<?xml version="1.0" encoding="UTF-8"?>\n<feed xmlns="http://www.w3.org/2005/Atom">\n    ')
        # SOURCE LINE 33
        __M_writer(conditional_websafe(self.Category()))
        __M_writer(u'\n    ')
        # SOURCE LINE 34
        __M_writer(conditional_websafe(self.Updated()))
        __M_writer(u'\n\n')
        # SOURCE LINE 36
        if c.can_apply_styles and not c.css_killswitch:
            # SOURCE LINE 37
            __M_writer(u'        ')
            __M_writer(conditional_websafe(self.Icon()))
            __M_writer(u'\n')
        # SOURCE LINE 39
        __M_writer(u'\n    ')
        # SOURCE LINE 40
        __M_writer(conditional_websafe(self.Id()))
        __M_writer(u'\n    ')
        # SOURCE LINE 41
        __M_writer(conditional_websafe(self.Link()))
        __M_writer(u'\n\n')
        # SOURCE LINE 43
        if c.can_apply_styles and not c.css_killswitch:
            # SOURCE LINE 44
            __M_writer(u'        ')
            __M_writer(conditional_websafe(self.Logo()))
            __M_writer(u'\n')
        # SOURCE LINE 46
        __M_writer(u'\n    ')
        # SOURCE LINE 47
        __M_writer(conditional_websafe(self.Subtitle()))
        __M_writer(u'\n    ')
        # SOURCE LINE 48
        __M_writer(conditional_websafe(self.Title()))
        __M_writer(u'\n\n')
        # SOURCE LINE 51
        __M_writer(u'    ')
        __M_writer(conditional_websafe(next.body()))
        __M_writer(u'\n</feed>\n\n')
        # SOURCE LINE 56
        __M_writer(u'\n')
        # SOURCE LINE 59
        __M_writer(u'\n\n')
        # SOURCE LINE 63
        __M_writer(u'\n\n')
        # SOURCE LINE 73
        __M_writer(u'\n\n')
        # SOURCE LINE 85
        __M_writer(u'\n\n')
        # SOURCE LINE 98
        __M_writer(u'\n\n')
        # SOURCE LINE 104
        __M_writer(u'\n\n')
        # SOURCE LINE 110
        __M_writer(u'\n\n')
        # SOURCE LINE 118
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_Category(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 57
        __M_writer(u'\n    <category term="')
        # SOURCE LINE 58
        __M_writer(conditional_websafe(c.site.name))
        __M_writer(u'" label="/r/')
        __M_writer(conditional_websafe(c.site.name))
        __M_writer(u'"/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_Updated(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 61
        __M_writer(u'\n    <updated>')
        # SOURCE LINE 62
        __M_writer(conditional_websafe(html_datetime(datetime.now(g.tz))))
        __M_writer(u'</updated>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_Subtitle(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 100
        __M_writer(u'\n')
        # SOURCE LINE 101
        if c.site.public_description:
            # SOURCE LINE 102
            __M_writer(u'        <subtitle>')
            __M_writer(conditional_websafe(c.site.public_description))
            __M_writer(u'</subtitle>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_Title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        thing = context.get('thing', UNDEFINED)
        getattr = context.get('getattr', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 65
        __M_writer(u'\n')
        # SOURCE LINE 66
        if getattr(thing, 'title', None):
            # SOURCE LINE 67
            __M_writer(u'        <title>')
            __M_writer(conditional_websafe(thing.title))
            __M_writer(u'</title>\n')
            # SOURCE LINE 68
        elif c.site.title:
            # SOURCE LINE 69
            __M_writer(u'        <title>')
            __M_writer(conditional_websafe(c.site.title))
            __M_writer(u'</title>\n')
            # SOURCE LINE 70
        elif c.site.name:
            # SOURCE LINE 71
            __M_writer(u'        <title>')
            __M_writer(conditional_websafe(c.site.name))
            __M_writer(u'</title>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_Link(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 75
        __M_writer(u'\n    <link rel="self" href="')
        # SOURCE LINE 76
        __M_writer(conditional_websafe(add_sr(request.fullpath,
                                    sr_path=False,
                                    force_hostname=True)))
        # SOURCE LINE 78
        __M_writer(u'"\n     type="application/atom+xml" />\n    <link rel="alternate" href="')
        # SOURCE LINE 80
        __M_writer(conditional_websafe(add_sr(request.fullpath,
                                         sr_path=False,
                                         force_hostname=True,
                                         force_extension='')))
        # SOURCE LINE 83
        __M_writer(u'"\n     type="text/html" />\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_Logo(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 112
        __M_writer(u'\n')
        # SOURCE LINE 115
        if c.site.header:
            # SOURCE LINE 116
            __M_writer(u'        <logo>')
            __M_writer(conditional_websafe(header_url(c.site.header, absolute=True)))
            __M_writer(u'</logo>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_Id(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        thing = context.get('thing', UNDEFINED)
        hasattr = context.get('hasattr', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 87
        __M_writer(u'\n')
        # SOURCE LINE 90
        __M_writer(u'\n    <id>\n')
        # SOURCE LINE 92
        if hasattr(thing, '_fullname'):
            # SOURCE LINE 93
            __M_writer(u'            ')
            __M_writer(conditional_websafe(thing._fullname))
            __M_writer(u'\n')
            # SOURCE LINE 94
        else:
            # SOURCE LINE 95
            __M_writer(u'            ')
            __M_writer(conditional_websafe(request.fullpath))
            __M_writer(u'\n')
        # SOURCE LINE 97
        __M_writer(u'    </id>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_Icon(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 106
        __M_writer(u'\n')
        # SOURCE LINE 109
        __M_writer(u'    <icon>')
        __M_writer(conditional_websafe(static("icon.png", absolute=True)))
        __M_writer(u'/</icon>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


