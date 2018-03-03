# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1511947254.189632
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/listing.iframe'
_template_uri = '/listing.iframe'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23

from r2.models import Comment


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        thing = context.get('thing', UNDEFINED)
        len = context.get('len', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'\n\n\n')
        # SOURCE LINE 28
        if len(thing.things):
            # SOURCE LINE 29
            __M_writer(u'  <ol class="reddit-embed-list">\n')
            # SOURCE LINE 30
            for i, t in enumerate(thing.things):
                # SOURCE LINE 31
                __M_writer(u'      <li class="reddit-embed-list-item">\n        ')
                # SOURCE LINE 32
                __M_writer(conditional_websafe(t))
                __M_writer(u'\n      </li>\n')
            # SOURCE LINE 35
            __M_writer(u'  </ol>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


