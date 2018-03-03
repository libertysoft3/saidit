# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1512343133.265427
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/flairselector.html'
_template_uri = '/flairselector.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        thing = context.get('thing', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n<h2>')
        # SOURCE LINE 23
        __M_writer(conditional_websafe(_("select flair")))
        __M_writer(u'</h2>\n')
        # SOURCE LINE 24
        if thing.choices:
            # SOURCE LINE 25
            __M_writer(u'  <div class="flairoptionpane">\n    <ul>\n')
            # SOURCE LINE 27
            for choice in thing.choices:
                # SOURCE LINE 28
                __M_writer(u'        ')

                li_class = 'flairsample-%s' % thing.position
                if choice.flair_text_editable:
                    li_class += ' texteditable'
                if choice.flair_template_id == thing.matching_template:
                    li_class += ' selected'
                        
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['li_class'] if __M_key in __M_locals_builtin_stored]))
                # SOURCE LINE 34
                __M_writer(u'\n        <li class="')
                # SOURCE LINE 35
                __M_writer(conditional_websafe(li_class))
                __M_writer(u'" id="')
                __M_writer(conditional_websafe(choice.flair_template_id))
                __M_writer(u'">\n          ')
                # SOURCE LINE 36
                __M_writer(conditional_websafe(choice))
                __M_writer(u'\n        </li>\n')
            # SOURCE LINE 39
            __M_writer(u'    </ul>\n  </div>\n  <form action="/post/selectflair" method="post">\n    <div class="flairselection">\n      <div class="flairremove">\n        (<a href="javascript://void(0)">')
            # SOURCE LINE 44
            __M_writer(conditional_websafe(_('remove flair')))
            __M_writer(u'</a>)\n      </div>\n    </div>\n    <input type="hidden" name="flair_template_id">\n    <div class="customizer">\n      <input type="text" size="16" maxlength="64" name="text">\n    </div>\n    <button type="submit">')
            # SOURCE LINE 51
            __M_writer(conditional_websafe(_('save')))
            __M_writer(u'</button>\n    <span class="status"></span>\n  </form>\n')
            # SOURCE LINE 54
        else:
            # SOURCE LINE 55
            __M_writer(u'  <div class="error">')
            __M_writer(conditional_websafe(_("flair selection unavailable")))
            __M_writer(u'</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


