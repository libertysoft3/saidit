# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1508401090.042008
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/exploreitem.html'
_template_uri = '/exploreitem.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23

from r2.lib.pages import SubscribeButton
from r2.lib.filters import unsafe, safemarkdown
from r2.lib.strings import Score


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        thing = context.get('thing', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 27
        __M_writer(u'\n\n<div class="explore-item explore-')
        # SOURCE LINE 29
        __M_writer(conditional_websafe(thing.type))
        __M_writer(u'" data-sr_name="')
        __M_writer(conditional_websafe(thing.sr.name))
        __M_writer(u'" data-src="')
        __M_writer(conditional_websafe(thing.src))
        __M_writer(u'">\n  <div class="explore-sr">\n    <span class="explore-label">\n      <span class="explore-label-type">')
        # SOURCE LINE 32
        __M_writer(conditional_websafe(_(thing.type)))
        __M_writer(u'</span> in \n      <a href="/r/')
        # SOURCE LINE 33
        __M_writer(conditional_websafe(thing.sr.name))
        __M_writer(u'" class="explore-label-link" target="_blank">\n        /r/')
        # SOURCE LINE 34
        __M_writer(conditional_websafe(thing.sr.name))
        __M_writer(u'\n      </a>\n    </span>\n    <span class="explore-sr-details">\n      <span>')
        # SOURCE LINE 38
        __M_writer(conditional_websafe(unsafe(Score.readers(thing.sr._ups))))
        __M_writer(u'</span>\n    </span>\n    <span class="explore-feedback">\n      ')
        # SOURCE LINE 41
        __M_writer(conditional_websafe(SubscribeButton(thing.sr, bubble_class="anchor-left explore-subscribe-bubble")))
        __M_writer(u'\n      <span class="explore-feedback-dismiss" title="')
        # SOURCE LINE 42
        __M_writer(conditional_websafe(_('not interested')))
        __M_writer(u'">\n        ')
        # SOURCE LINE 43
        __M_writer(conditional_websafe(_("hide")))
        __M_writer(u'\n      </span>\n    </span>\n  </div>\n  ')
        # SOURCE LINE 47
        __M_writer(conditional_websafe(thing.link))
        __M_writer(u'\n')
        # SOURCE LINE 48
        if thing.comment:
            # SOURCE LINE 49
            __M_writer(u'  <div class="comment">\n    ')
            # SOURCE LINE 50
            __M_writer(conditional_websafe(unsafe(safemarkdown(thing.comment.body))))
            __M_writer(u'\n    <div class="comment-fade"></div>\n  </div>\n  <a class="comment-link" href="')
            # SOURCE LINE 53
            __M_writer(conditional_websafe(thing.link.make_permalink(thing.sr)))
            __M_writer(u'" target="_blank">\n    ')
            # SOURCE LINE 54
            __M_writer(conditional_websafe(_("more comments")))
            __M_writer(u'\n  </a>\n')
        # SOURCE LINE 57
        __M_writer(u'</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


