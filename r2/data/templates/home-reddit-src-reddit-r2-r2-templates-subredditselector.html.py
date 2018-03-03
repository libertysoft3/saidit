# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1520057702.578291
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/subredditselector.html'
_template_uri = '/subredditselector.html'
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
    # SOURCE LINE 1
    ns = runtime.TemplateNamespace('__anon_0x7f6495240bd0', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f6495240bd0')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f6495240bd0')._populate(_import_ns, [u'error_field'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        # SOURCE LINE 6
        __M_writer(u'\n\n<div id="sr-autocomplete-area">\n  <input id="sr-autocomplete" name="sr" type="text"\n         autocomplete="off"\n')
        # SOURCE LINE 11
        if thing.include_searches:
            # SOURCE LINE 12
            __M_writer(u'           onkeyup="sr_name_up(event)"\n')
        # SOURCE LINE 14
        __M_writer(u'         onkeydown="return sr_name_down(event)"\n         onblur="hide_sr_name_list()"\n')
        # SOURCE LINE 16
        if thing.default_sr:
            # SOURCE LINE 17
            __M_writer(u'           value="')
            __M_writer(conditional_websafe(thing.default_sr.name))
            __M_writer(u'"\n')
        # SOURCE LINE 19
        if thing.required:
            # SOURCE LINE 20
            __M_writer(u'         required\n')
        # SOURCE LINE 22
        if thing.class_name:
            # SOURCE LINE 23
            __M_writer(u'          class="')
            __M_writer(conditional_websafe(thing.class_name))
            __M_writer(u'"\n')
        # SOURCE LINE 25
        if thing.placeholder:
            # SOURCE LINE 26
            __M_writer(u'          placeholder="')
            __M_writer(conditional_websafe(thing.placeholder))
            __M_writer(u'"\n')
        # SOURCE LINE 28
        __M_writer(u'         />\n')
        # SOURCE LINE 29
        if thing.show_add:
            # SOURCE LINE 30
            __M_writer(u'    <button class="add">')
            __M_writer(conditional_websafe(_("add")))
            __M_writer(u'</button>\n')
        # SOURCE LINE 32
        __M_writer(u'  <ul id="sr-drop-down">\n    <li class="sr-name-row"\n        onmouseover="highlight_reddit(this)"\n        onmousedown="return sr_dropdown_mdown(this)"\n        onmouseup="sr_dropdown_mup(this)">nothin</li>\n  </ul>\n</div>\n<script type="text/javascript">\n  r.config.sr_cache = ')
        # SOURCE LINE 40
        __M_writer(conditional_websafe(unsafe(thing.sr_searches)))
        __M_writer(u';\n</script>\n')
        # SOURCE LINE 42
        __M_writer(conditional_websafe(error_field("SUBREDDIT_NOEXIST", "sr", "div")))
        __M_writer(u'\n')
        # SOURCE LINE 43
        __M_writer(conditional_websafe(error_field("SUBREDDIT_NOTALLOWED", "sr", "div")))
        __M_writer(u'\n')
        # SOURCE LINE 44
        __M_writer(conditional_websafe(error_field("SUBREDDIT_REQUIRED", "sr", "div")))
        __M_writer(u'\n\n<div id="suggested-reddits">\n')
        # SOURCE LINE 47
        for title, subreddits in thing.subreddit_names:
            # SOURCE LINE 48
            __M_writer(u'    <h3>')
            __M_writer(conditional_websafe(title))
            __M_writer(u'</h3>\n    <ul>\n')
            # SOURCE LINE 50
            for name in subreddits:
                # SOURCE LINE 51
                __M_writer(u'      <li>\n        <a href="#" tabindex="100" onclick="set_sr_name(this); return false">')
                # SOURCE LINE 52
                __M_writer(conditional_websafe(name))
                __M_writer(u'</a>&#32;\n      </li>\n')
            # SOURCE LINE 55
            __M_writer(u'    </ul>\n')
        # SOURCE LINE 57
        __M_writer(u'</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


