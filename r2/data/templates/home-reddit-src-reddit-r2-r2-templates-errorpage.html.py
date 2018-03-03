# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505003077.530224
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/errorpage.html'
_template_uri = '/errorpage.html'
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
        __M_writer(u'\n')
        # SOURCE LINE 23

        from r2.lib.template_helpers import static
        from r2.lib.filters import unsafe, safemarkdown
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['safemarkdown','unsafe','static'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 26
        __M_writer(u'\n\n<div id="classy-error" class="content">\n  <img src="')
        # SOURCE LINE 29
        __M_writer(conditional_websafe(static(thing.image_url)))
        __M_writer(u'" alt="" />\n\n  <h1>')
        # SOURCE LINE 31
        __M_writer(conditional_websafe(thing.title))
        __M_writer(u'</h1>\n  <div class="errorpage-message">\n  ')
        # SOURCE LINE 33
        __M_writer(conditional_websafe(unsafe(safemarkdown(thing.message, wrap=False))))
        __M_writer(u'\n')
        # SOURCE LINE 34
        if thing.explanation:
            # SOURCE LINE 35
            __M_writer(u'    &mdash; ')
            __M_writer(conditional_websafe(thing.explanation))
            __M_writer(u'\n')
        # SOURCE LINE 37
        __M_writer(u'  </div>\n\n')
        # SOURCE LINE 39
        if thing.sr_description:
            # SOURCE LINE 40
            __M_writer(u'  <div class="errorpage-message sr-description">\n      <h2>')
            # SOURCE LINE 41
            __M_writer(conditional_websafe(_("a message from the moderators of /r/%s") % c.site.name))
            __M_writer(u'</h2>\n      ')
            # SOURCE LINE 42
            __M_writer(conditional_websafe(unsafe(safemarkdown(thing.sr_description, wrap=False))))
            __M_writer(u'\n  </div>\n')
        # SOURCE LINE 45
        __M_writer(u'\n')
        # SOURCE LINE 46
        if thing.include_message_mods_link:
            # SOURCE LINE 47
            __M_writer(u'  <div id="private-subreddit-message-link" class="errorpage-message">\n    <a href="/message/compose/?to=/r/')
            # SOURCE LINE 48
            __M_writer(conditional_websafe(c.site.name))
            __M_writer(u'">')
            __M_writer(conditional_websafe(_("send a message to the moderators")))
            __M_writer(u'</a>\n  </div>\n')
        # SOURCE LINE 51
        __M_writer(u'</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


