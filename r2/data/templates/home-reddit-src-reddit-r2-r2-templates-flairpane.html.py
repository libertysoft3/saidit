# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1509242599.108097
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/flairpane.html'
_template_uri = '/flairpane.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 23
    ns = runtime.TemplateNamespace(u'utils', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'utils')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        thing = context.get('thing', UNDEFINED)
        utils = _mako_get_namespace(context, 'utils')
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n<div class="flair-settings fancy-settings">\n  <h1>')
        # SOURCE LINE 25
        __M_writer(conditional_websafe(_("flair settings")))
        __M_writer(u' | &#32;<strong>')
        __M_writer(conditional_websafe(c.site.name))
        __M_writer(u'</strong></h1>\n\n  <div class="pretty-form">\n    <form method="post" action="/post/flairconfig"\n      onsubmit="return post_form(this, \'flairconfig\');">\n      ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                # SOURCE LINE 30
                __M_writer(u'\n        <input type="checkbox"\n            id="sr_flair_enabled"\n            name="flair_enabled"\n')
                # SOURCE LINE 34
                if thing.flair_enabled:
                    # SOURCE LINE 35
                    __M_writer(u'              checked="checked"\n')
                # SOURCE LINE 37
                __M_writer(u'            />\n        <label for="sr_flair_enabled">\n            ')
                # SOURCE LINE 39
                __M_writer(conditional_websafe(_("enable user flair in this subreddit")))
                __M_writer(u'\n        </label>\n        <br>\n        <input type="checkbox"\n            id="sr_flair_self_assign_enabled"\n            name="flair_self_assign_enabled"\n')
                # SOURCE LINE 45
                if thing.flair_self_assign_enabled:
                    # SOURCE LINE 46
                    __M_writer(u'              checked="checked"\n')
                # SOURCE LINE 48
                __M_writer(u'            />\n        <label for="sr_flair_self_assign_enabled">\n            ')
                # SOURCE LINE 50
                __M_writer(conditional_websafe(_("allow users to assign their own flair")))
                __M_writer(u'\n        </label>\n        <br>\n        <input type="checkbox"\n            id="sr_link_flair_self_assign_enabled"\n            name="link_flair_self_assign_enabled"\n')
                # SOURCE LINE 56
                if thing.link_flair_self_assign_enabled:
                    # SOURCE LINE 57
                    __M_writer(u'              checked="checked"\n')
                # SOURCE LINE 59
                __M_writer(u'            />\n        <label for="sr_link_flair_self_assign_enabled">\n            ')
                # SOURCE LINE 61
                __M_writer(conditional_websafe(_("allow submitters to assign their own link flair")))
                __M_writer(u'\n        </label>\n      ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 30
            __M_writer(conditional_websafe(utils.line_field(title=(_('flair options')))))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 63
        __M_writer(u'\n      ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                # SOURCE LINE 64
                __M_writer(u'\n        <table class="small-field">\n          ')
                # SOURCE LINE 66
                __M_writer(conditional_websafe(utils.radio_type('flair_position', "left", _("left"),
                             _("position flair to the left of the username"),
                             thing.flair_position == 'left')))
                # SOURCE LINE 68
                __M_writer(u'\n          ')
                # SOURCE LINE 69
                __M_writer(conditional_websafe(utils.radio_type('flair_position', "right", _("right"),
                             _("position flair to the right of the username"),
                             thing.flair_position == 'right')))
                # SOURCE LINE 71
                __M_writer(u'\n        </table>\n      ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 64
            __M_writer(conditional_websafe(utils.line_field(title=(_('user flair position')))))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 73
        __M_writer(u'\n      ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                # SOURCE LINE 74
                __M_writer(u'\n        <table class="small-field">\n          ')
                # SOURCE LINE 76
                __M_writer(conditional_websafe(utils.radio_type('link_flair_position', "", _("none"),
                             _("don't show link flair"),
                             not thing.link_flair_position)))
                # SOURCE LINE 78
                __M_writer(u'\n          ')
                # SOURCE LINE 79
                __M_writer(conditional_websafe(utils.radio_type('link_flair_position', "left", _("left"),
                             _("position flair to the left of the link"),
                             thing.link_flair_position == 'left')))
                # SOURCE LINE 81
                __M_writer(u'\n          ')
                # SOURCE LINE 82
                __M_writer(conditional_websafe(utils.radio_type('link_flair_position', "right", _("right"),
                             _("position flair to the right of the link"),
                             thing.link_flair_position == 'right')))
                # SOURCE LINE 84
                __M_writer(u'\n        </table>\n      ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 74
            __M_writer(conditional_websafe(utils.line_field(title=(_('link flair position')))))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 86
        __M_writer(u'\n      <div class="save-button">\n        <button type="submit">')
        # SOURCE LINE 88
        __M_writer(conditional_websafe(_("save options")))
        __M_writer(u'</button>\n      </div>\n    </form>\n  </div>\n</div>\n')
        # SOURCE LINE 93
        __M_writer(conditional_websafe(thing.tabs))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


