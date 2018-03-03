# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505839980.84055
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/commentvisitsbox.html'
_template_uri = '/commentvisitsbox.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23


from r2.lib.utils import timesince



def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        thing = context.get('thing', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 27
        __M_writer(u'\n\n<div class="rounded gold-accent comment-visits-box">\n  <div class="title">\n    ')
        # SOURCE LINE 31
        __M_writer(conditional_websafe(_("Highlight comments posted since previous visit:")))
        __M_writer(u'&#32;\n    <select id="comment-visits">\n')
        # SOURCE LINE 33
        for i, visit in enumerate(thing.visits):
            # SOURCE LINE 34
            __M_writer(u'        <option value="')
            __M_writer(conditional_websafe(visit.isoformat()))
            __M_writer(u'"\n')
            # SOURCE LINE 35
            if i == 0:
                # SOURCE LINE 36
                __M_writer(u'            selected="selected"\n')
            # SOURCE LINE 38
            __M_writer(u'        >')
            __M_writer(conditional_websafe(timesince(visit, precision=60)))
            __M_writer(u' ')
            __M_writer(conditional_websafe(_("ago")))
            __M_writer(u'</option>\n')
        # SOURCE LINE 40
        __M_writer(u'      <option value="">')
        __M_writer(conditional_websafe(_("no highlighting")))
        __M_writer(u'</option>\n    </select>\n  </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


