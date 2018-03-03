# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505983035.43306
_enable_loop = True
_template_filename = u'/home/reddit/src/reddit/r2/r2/templates/subredditstylesheetbase.html'
_template_uri = u'/subredditstylesheetbase.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['make_li']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7f20bc95ea10', context._clean_inheritance_tokens(), templateuri=u'printablebuttons.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f20bc95ea10')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f20bc95ea10')._populate(_import_ns, [u'ynbutton'])
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n')
        # SOURCE LINE 50
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_make_li(context,name='',img=None,prototype=False,mod=True):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f20bc95ea10')._populate(_import_ns, [u'ynbutton'])
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        ynbutton = _import_ns.get('ynbutton', context.get('ynbutton', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 25
        __M_writer(u'\n  <li ')
        # SOURCE LINE 26
        __M_writer(conditional_websafe("style='display:none'" if img is None else ""))
        __M_writer(u'>\n    <a href="')
        # SOURCE LINE 27
        __M_writer(conditional_websafe(img))
        __M_writer(u'" class="preview">\n      <img id="img-preview-')
        # SOURCE LINE 28
        __M_writer(conditional_websafe(name))
        __M_writer(u'" src="')
        __M_writer(conditional_websafe(img))
        __M_writer(u'" \n           alt="Image ')
        # SOURCE LINE 29
        __M_writer(conditional_websafe(name))
        __M_writer(u'" title="click to preview"/>\n    </a>\n    <div class="description">\n      <b class="img-name">\n        ')
        # SOURCE LINE 33
        __M_writer(conditional_websafe(name))
        __M_writer(u'\n      </b>\n      <br/>\n      <span>link:</span>\n      <pre class="img-url">url(%%')
        # SOURCE LINE 37
        __M_writer(conditional_websafe(name))
        __M_writer(u'%%)</pre>\n')
        # SOURCE LINE 38
        if mod:
            # SOURCE LINE 39
            __M_writer(u'        <br/>\n        <a href="javascript:void(0)" onclick="return paste_url(this)">\n          ')
            # SOURCE LINE 41
            __M_writer(conditional_websafe(_("paste into stylesheet")))
            __M_writer(u'\n        </a>\n        <br/>\n        ')
            # SOURCE LINE 44
            __M_writer(conditional_websafe(ynbutton(_("delete this image"), _("deleted"),
                   "delete_sr_img", callback = "delete_img",
                    hidden_data = dict(img_name = name))))
            # SOURCE LINE 46
            __M_writer(u'\n')
        # SOURCE LINE 48
        __M_writer(u'    </div>\n  </li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


