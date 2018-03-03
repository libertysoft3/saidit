# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1520060955.684459
_enable_loop = True
_template_filename = u'/home/reddit/src/reddit/r2/r2/templates/captcha.html'
_template_uri = u'/captcha.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['captcha_basics', 'captchagen', 'rounded_captcha']


# SOURCE LINE 23
from r2.lib.template_helpers import static 

def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 26
    ns = runtime.TemplateNamespace(u'utils', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'utils')] = ns

    # SOURCE LINE 25
    ns = runtime.TemplateNamespace('__anon_0x7fc7c75f9e90', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fc7c75f9e90')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c75f9e90')._populate(_import_ns, [u'error_field'])
        def rounded_captcha():
            return render_rounded_captcha(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n')
        # SOURCE LINE 25
        __M_writer(u'\n')
        # SOURCE LINE 26
        __M_writer(u'\n\n')
        # SOURCE LINE 29
        __M_writer(u'\n')
        # SOURCE LINE 30
        __M_writer(conditional_websafe(rounded_captcha()))
        __M_writer(u'\n\n')
        # SOURCE LINE 46
        __M_writer(u'\n\n')
        # SOURCE LINE 54
        __M_writer(u'\n\n')
        # SOURCE LINE 104
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_captcha_basics(context,iden=''):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c75f9e90')._populate(_import_ns, [u'error_field'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 32
        __M_writer(u'\n  ')
        # SOURCE LINE 33

        iden = getattr(thing, "iden", iden)
          
        
        # SOURCE LINE 35
        __M_writer(u'\n  <input name="iden" value="')
        # SOURCE LINE 36
        __M_writer(conditional_websafe(iden))
        __M_writer(u'" type="hidden"/>\n\n  <img class="capimage"\n       alt="visual CAPTCHA"\n')
        # SOURCE LINE 40
        if hasattr(thing, "iden"):
            # SOURCE LINE 41
            __M_writer(u'       src="/captcha/')
            __M_writer(conditional_websafe(thing.iden))
            __M_writer(u'.png" \n')
            # SOURCE LINE 42
        else:
            # SOURCE LINE 43
            __M_writer(u'       src="')
            __M_writer(conditional_websafe(static('kill.png')))
            __M_writer(u'" \n')
        # SOURCE LINE 45
        __M_writer(u'       />\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_captchagen(context,iden,error='',tabulate=False,tabular=True,size=60,label=True,show_error=True,tabindex=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c75f9e90')._populate(_import_ns, [u'error_field'])
        def captcha_basics(iden=''):
            return render_captcha_basics(context,iden)
        error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 56
        __M_writer(u'\n')
        # SOURCE LINE 57
        if tabulate:
            # SOURCE LINE 58
            __M_writer(u'<table>\n')
        # SOURCE LINE 60
        if tabular:
            # SOURCE LINE 61
            __M_writer(u'  <tr>\n    <td></td>\n    <td>\n')
        # SOURCE LINE 65
        __M_writer(u'  ')
        __M_writer(conditional_websafe(captcha_basics(iden)))
        __M_writer(u'\n')
        # SOURCE LINE 66
        if tabular:
            # SOURCE LINE 67
            __M_writer(u'  </td>\n  </tr>\n  <tr>\n     <td align="right">\n')
            # SOURCE LINE 71
        else:
            # SOURCE LINE 72
            __M_writer(u'     <span class="cap-reply">\n')
        # SOURCE LINE 74
        if label:
            # SOURCE LINE 75
            __M_writer(u'         <label for="captcha_">')
            __M_writer(conditional_websafe(_("human?")))
            __M_writer(u'</label>\n')
        # SOURCE LINE 77
        if tabular:
            # SOURCE LINE 78
            __M_writer(u'     </td>\n     <td>\n')
        # SOURCE LINE 81
        __M_writer(u'          <input class="captcha cap-text" id="captcha_"\n                 name="captcha" type="text" size="')
        # SOURCE LINE 82
        __M_writer(conditional_websafe(size))
        __M_writer(u'"\n                 placeholder="type the letters from the image above"\n')
        # SOURCE LINE 84
        if tabindex:
            # SOURCE LINE 85
            __M_writer(u'                   tabindex="')
            __M_writer(conditional_websafe(tabindex))
            __M_writer(u'"\n')
        # SOURCE LINE 87
        __M_writer(u'                 />\n')
        # SOURCE LINE 88
        if tabular:
            # SOURCE LINE 89
            __M_writer(u'     </td>\n     <td>\n')
            # SOURCE LINE 91
        else:
            # SOURCE LINE 92
            __M_writer(u'     </span>\n')
        # SOURCE LINE 94
        if show_error:
            # SOURCE LINE 95
            __M_writer(u'       ')
            __M_writer(conditional_websafe(error_field("BAD_CAPTCHA", "captcha")))
            __M_writer(u'\n')
        # SOURCE LINE 97
        if tabular:
            # SOURCE LINE 98
            __M_writer(u'    </td>\n  </tr>\n')
        # SOURCE LINE 101
        if tabulate:
            # SOURCE LINE 102
            __M_writer(u'</table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_rounded_captcha(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c75f9e90')._populate(_import_ns, [u'error_field'])
        utils = _mako_get_namespace(context, 'utils')
        __M_writer = context.writer()
        # SOURCE LINE 48
        __M_writer(u'\n')
        def ccall(caller):
            def body():
                def captcha_basics(iden=''):
                    return render_captcha_basics(context,iden)
                error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
                __M_writer = context.writer()
                # SOURCE LINE 49
                __M_writer(u'\n    ')
                # SOURCE LINE 50
                __M_writer(conditional_websafe(captcha_basics()))
                __M_writer(u'\n    <input name="captcha" class="captcha" type="text" />\n    ')
                # SOURCE LINE 52
                __M_writer(conditional_websafe(error_field("BAD_CAPTCHA", "captcha")))
                __M_writer(u'\n  ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 49
            __M_writer(conditional_websafe(utils.round_field(css_class=u'captcha',description=(_('(sorry)')),title=(_('are you human?')))))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 53
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


