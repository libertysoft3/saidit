# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1509242599.154735
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/flairtemplateeditor.html'
_template_uri = '/flairtemplateeditor.html'
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
        __M_writer(u'\n\n<div class="flairtemplate flairrow">\n  <form action="/post/flairtemplate"\n        ')
        # SOURCE LINE 27
        __M_writer(conditional_websafe('id=%s' % thing.id if thing.id else ''))
        __M_writer(u'\n        method="post" class="medium-text flair-entry">\n')
        # SOURCE LINE 29
        if thing.id:
            # SOURCE LINE 30
            __M_writer(u'      <input type="hidden" name="flair_template_id" value="')
            __M_writer(conditional_websafe(thing.id))
            __M_writer(u'" />\n')
        # SOURCE LINE 32
        __M_writer(u'    <input type="hidden" name="flair_type" value="')
        __M_writer(conditional_websafe(thing.flair_type))
        __M_writer(u'" />\n    <span class="flaircell flairsample-')
        # SOURCE LINE 33
        __M_writer(conditional_websafe(thing.position))
        __M_writer(u' tagline">\n')
        # SOURCE LINE 34
        if thing.text or thing.css_class:
            # SOURCE LINE 35
            __M_writer(u'        ')
            __M_writer(conditional_websafe(unsafe(thing.sample.render())))
            __M_writer(u'\n')
        # SOURCE LINE 37
        __M_writer(u'    </span>\n    <span class="flaircell narrow">\n      <input type="checkbox" name="text_editable"\n          ')
        # SOURCE LINE 40
        __M_writer(conditional_websafe('checked="checked"' if thing.text_editable else ''))
        __M_writer(u' />\n    </span>\n    <span class="flaircell">\n      <input type="text" size="32" maxlength="64" name="text"\n             value="')
        # SOURCE LINE 44
        __M_writer(conditional_websafe(thing.text))
        __M_writer(u'" />\n    </span>\n    <span class="flaircell">\n      <input type="text" size="32" maxlength="1000" name="css_class"\n             value="')
        # SOURCE LINE 48
        __M_writer(conditional_websafe(thing.css_class))
        __M_writer(u'" />\n    </span>\n    <button type="submit">save</button>\n')
        # SOURCE LINE 51
        if thing.id:
            # SOURCE LINE 52
            __M_writer(u'      <button class="flairdeletebtn">delete</button>\n')
        # SOURCE LINE 54
        __M_writer(u'    <span class="status"></span>\n    ')
        # SOURCE LINE 55
        __M_writer(conditional_websafe(utils.error_field('BAD_CSS_NAME', 'css_class')))
        __M_writer(u'\n    ')
        # SOURCE LINE 56
        __M_writer(conditional_websafe(utils.error_field('TOO_MUCH_FLAIR_CSS', 'css_class')))
        __M_writer(u'\n  </form>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


