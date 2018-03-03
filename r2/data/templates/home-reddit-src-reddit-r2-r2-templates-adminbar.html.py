# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505002596.118689
_enable_loop = True
_template_filename = u'/home/reddit/src/reddit/r2/r2/templates/adminbar.html'
_template_uri = u'/adminbar.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['adminbar_stylesheet', 'indicator']


# SOURCE LINE 23

from r2.lib.pages.admin_pages import admin_menu


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 26
    ns = runtime.TemplateNamespace('__anon_0x7fde601e2250', context._clean_inheritance_tokens(), templateuri=u'less.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fde601e2250')] = ns

    # SOURCE LINE 27
    ns = runtime.TemplateNamespace('__anon_0x7fde601e2350', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fde601e2350')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fde601e2250')._populate(_import_ns, [u'less_stylesheet'])
        _mako_get_namespace(context, '__anon_0x7fde601e2350')._populate(_import_ns, [u'classes'])
        def indicator(name,label,on):
            return render_indicator(context._locals(__M_locals),name,label,on)
        classes = _import_ns.get('classes', context.get('classes', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'\n')
        # SOURCE LINE 26
        __M_writer(u'\n')
        # SOURCE LINE 27
        __M_writer(u'\n\n')
        # SOURCE LINE 33
        __M_writer(u'\n\n')
        # SOURCE LINE 39
        __M_writer(u'\n\n')
        # SOURCE LINE 41
        if c.show_admin_bar:
            # SOURCE LINE 42
            __M_writer(u'  <div id="admin-bar" ')
            __M_writer(conditional_websafe(classes('admin' if c.user_is_admin else None, 'debug' if g.debug else None)))
            __M_writer(u'>\n    <div class="status-bar">\n      <span class="caption">')
            # SOURCE LINE 44
            __M_writer(conditional_websafe(_('status')))
            __M_writer(u'</span>\n      ')
            # SOURCE LINE 45
            __M_writer(conditional_websafe(indicator('admin', _('admin mode enabled'), c.user_is_admin)))
            __M_writer(u'\n')
            # SOURCE LINE 46
            if c.user_is_admin:
                # SOURCE LINE 47
                __M_writer(u'        <span class="admin-off">')
                __M_writer(conditional_websafe(_('admin off')))
                __M_writer(u'</span>\n')
            # SOURCE LINE 49
            __M_writer(u'      ')
            __M_writer(conditional_websafe(indicator('debug', _('debug mode'), g.debug)))
            __M_writer(u'\n      ')
            # SOURCE LINE 50
            __M_writer(conditional_websafe(indicator('secure', _('secure'), c.secure)))
            __M_writer(u'\n      ')
            # SOURCE LINE 51
            __M_writer(conditional_websafe(indicator('dev-statics', _('development statics'), g.uncompressedJS)))
            __M_writer(u'\n      ')
            # SOURCE LINE 52
            __M_writer(conditional_websafe(indicator('prod-statics', _('production statics'), g.debug and not g.uncompressedJS)))
            __M_writer(u'\n      ')
            # SOURCE LINE 53
            __M_writer(conditional_websafe(indicator('disabled', _('ads disabled'), g.disable_ads)))
            __M_writer(u'\n      ')
            # SOURCE LINE 54
            __M_writer(conditional_websafe(indicator('disabled', _('captcha disabled'), g.disable_captcha)))
            __M_writer(u'\n      ')
            # SOURCE LINE 55
            __M_writer(conditional_websafe(indicator('disabled', _('ratelimit disabled'), g.disable_ratelimit)))
            __M_writer(u'\n      <span class="controls">\n')
            # SOURCE LINE 57
            if c.user_is_admin:
                # SOURCE LINE 58
                __M_writer(u'          ')
                __M_writer(conditional_websafe(admin_menu()))
                __M_writer(u'\n')
            # SOURCE LINE 60
            __M_writer(u'        <span class="timings-button"><span class="state">-</span>')
            __M_writer(conditional_websafe(_('timings')))
            __M_writer(u'</span>\n        <span class="hide-button">')
            # SOURCE LINE 61
            __M_writer(conditional_websafe(_('hide')))
            __M_writer(u'</span>\n      </span>\n    </div>\n    <div class="timings-bar">\n      <div class="expand-button">+</div>\n      <div class="timelines">\n        <div class="timeline timeline-browser"></div>\n        <div class="timeline timeline-server"></div>\n      </div>\n    </div>\n    <div class="show-button"></div>\n  </div>\n  ')
            # SOURCE LINE 73
            from r2.lib import js 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['js'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n  ')
            # SOURCE LINE 74
            __M_writer(conditional_websafe(unsafe(js.use('admin'))))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_adminbar_stylesheet(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fde601e2250')._populate(_import_ns, [u'less_stylesheet'])
        _mako_get_namespace(context, '__anon_0x7fde601e2350')._populate(_import_ns, [u'classes'])
        less_stylesheet = _import_ns.get('less_stylesheet', context.get('less_stylesheet', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 29
        __M_writer(u'\n')
        # SOURCE LINE 30
        if c.show_admin_bar:
            # SOURCE LINE 31
            __M_writer(u'    ')
            __M_writer(conditional_websafe(less_stylesheet('adminbar.less')))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_indicator(context,name,label,on):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fde601e2250')._populate(_import_ns, [u'less_stylesheet'])
        _mako_get_namespace(context, '__anon_0x7fde601e2350')._populate(_import_ns, [u'classes'])
        __M_writer = context.writer()
        # SOURCE LINE 35
        __M_writer(u'\n')
        # SOURCE LINE 36
        if on:
            # SOURCE LINE 37
            __M_writer(u'    <span class="indicator ')
            __M_writer(conditional_websafe(name))
            __M_writer(u'"><span class="icon"></span>')
            __M_writer(conditional_websafe(label))
            __M_writer(u'</span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


