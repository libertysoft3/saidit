# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505842325.873437
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/moderatorpermissions.html'
_template_uri = '/moderatorpermissions.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['form_content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7fe407ba78d0', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fe407ba78d0')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fe407ba78d0')._populate(_import_ns, [u'error_field'])
        def form_content():
            return render_form_content(context._locals(__M_locals))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n')
        # SOURCE LINE 42
        __M_writer(u'\n\n<div class="permissions">\n')
        # SOURCE LINE 45
        if thing.embedded:
            # SOURCE LINE 46
            __M_writer(u'    ')
            __M_writer(conditional_websafe(form_content()))
            __M_writer(u'\n')
            # SOURCE LINE 47
        else:
            # SOURCE LINE 48
            __M_writer(u'    <form action="/post/setpermissions" method="post"\n          class="setpermissions pretty-form medium-text"\n          onsubmit="return post_form(this, \'setpermissions\')">\n      ')
            # SOURCE LINE 51
            __M_writer(conditional_websafe(form_content()))
            __M_writer(u'\n      <button type="submit">')
            # SOURCE LINE 52
            __M_writer(conditional_websafe(_('save')))
            __M_writer(u'</button>\n    </form>\n')
        # SOURCE LINE 55
        __M_writer(u'  <div class="permission-summary">\n  </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_content(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fe407ba78d0')._populate(_import_ns, [u'error_field'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 25
        __M_writer(u'\n')
        # SOURCE LINE 26
        if not thing.embedded:
            # SOURCE LINE 27
            __M_writer(u'    <input type="hidden" name="name"\n      value="')
            # SOURCE LINE 28
            __M_writer(conditional_websafe(thing.user.name if thing.user else ''))
            __M_writer(u'" />\n')
        # SOURCE LINE 30
        __M_writer(u'  <input type="hidden" name="type" value="')
        __M_writer(conditional_websafe(thing.permissions_type))
        __M_writer(u'">\n  <input type="hidden" name="permissions"\n    value="')
        # SOURCE LINE 32
        __M_writer(conditional_websafe(thing.permissions.dumps() if thing.permissions else '+all'))
        __M_writer(u'">\n')
        # SOURCE LINE 33
        if not thing.embedded:
            # SOURCE LINE 34
            __M_writer(u'    ')
            __M_writer(conditional_websafe(error_field("USER_DOESNT_EXIST", "name")))
            __M_writer(u'\n    ')
            # SOURCE LINE 35
            __M_writer(conditional_websafe(error_field("NO_USER", "name")))
            __M_writer(u'\n')
        # SOURCE LINE 37
        __M_writer(u'  ')
        __M_writer(conditional_websafe(error_field("INVALID_PERMISSION_TYPE", "type")))
        __M_writer(u'\n  ')
        # SOURCE LINE 38
        __M_writer(conditional_websafe(error_field("INVALID_PERMISSIONS", "permissions")))
        __M_writer(u'\n')
        # SOURCE LINE 39
        if not thing.embedded:
            # SOURCE LINE 40
            __M_writer(u'    <span class="status"></span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


