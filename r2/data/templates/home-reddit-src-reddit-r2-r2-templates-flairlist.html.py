# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1509242599.127487
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/flairlist.html'
_template_uri = '/flairlist.html'
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
        __M_writer(u'\n\n<div class="flairgrant flairlist">\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                # SOURCE LINE 26
                __M_writer(u'\n    <form method="get">\n      ')
                # SOURCE LINE 28
                name = thing.user.name if thing.user else thing.name 
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['name'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n      <input type="text" maxlength="20" id="flair_jump_name" name="name"\n             value="')
                # SOURCE LINE 30
                __M_writer(conditional_websafe(name))
                __M_writer(u'">\n      <button type="submit">')
                # SOURCE LINE 31
                __M_writer(conditional_websafe(_('go')))
                __M_writer(u'</button>\n      ')
                # SOURCE LINE 32
                __M_writer(conditional_websafe(utils.error_field('USER_DOESNT_EXIST', 'name')))
                __M_writer(u'\n    </form>\n')
                # SOURCE LINE 34
                if thing.user or thing.name:
                    # SOURCE LINE 35
                    __M_writer(u'        ')
                    __M_writer(conditional_websafe(utils.plain_link(_('back to full list'), '/about/flair',
                           class_='flairlisthome')))
                    # SOURCE LINE 36
                    __M_writer(u'\n')
                    # SOURCE LINE 37
                elif thing.after:
                    # SOURCE LINE 38
                    __M_writer(u'        ')
                    __M_writer(conditional_websafe(utils.plain_link(_('back to the beginning'), '/about/flair',
                           class_='flairlisthome')))
                    # SOURCE LINE 39
                    __M_writer(u'\n')
                # SOURCE LINE 41
                __M_writer(u'  ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 26
            __M_writer(conditional_websafe(utils.line_field(css_class=u'flair-jump',title=(_('jump to user (or add):')))))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 41
        __M_writer(u'\n  ')
        # SOURCE LINE 42
        flair = thing.flair 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['flair'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        # SOURCE LINE 43
        if flair:
            # SOURCE LINE 44
            __M_writer(u'    <div class="usertable">\n      <span class="header tagline">&nbsp;</span>\n      <span class="header">')
            # SOURCE LINE 46
            __M_writer(conditional_websafe(_('flair text')))
            __M_writer(u'</span>\n      <span class="header">')
            # SOURCE LINE 47
            __M_writer(conditional_websafe(_('css class')))
            __M_writer(u'</span>\n')
            # SOURCE LINE 48
            for row in flair:
                # SOURCE LINE 49
                __M_writer(u'          ')
                __M_writer(conditional_websafe(unsafe(row.render())))
                __M_writer(u'\n')
            # SOURCE LINE 51
            __M_writer(u'    </div>\n')
        # SOURCE LINE 53
        __M_writer(u'</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


