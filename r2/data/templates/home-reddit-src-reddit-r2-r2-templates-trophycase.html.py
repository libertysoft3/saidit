# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505003903.175391
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/trophycase.html'
_template_uri = '/trophycase.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['trophy_info', 'trophy_table']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7f3607eb9350', context._clean_inheritance_tokens(), templateuri=u'printablebuttons.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f3607eb9350')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f3607eb9350')._populate(_import_ns, [u'ynbutton'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        def trophy_table(trophies,header=''):
            return render_trophy_table(context._locals(__M_locals),trophies,header)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n')
        # SOURCE LINE 53
        __M_writer(u'\n\n')
        # SOURCE LINE 56
        if not thing.trophies:
            # SOURCE LINE 57
            __M_writer(u'  <div class="dust">')
            __M_writer(conditional_websafe(_("dust")))
            __M_writer(u'</div>\n')
        # SOURCE LINE 59
        __M_writer(u'\n')
        # SOURCE LINE 81
        __M_writer(u'\n\n')
        # SOURCE LINE 83
        __M_writer(conditional_websafe(trophy_table(thing.trophies)))
        __M_writer(u'\n\n')
        # SOURCE LINE 85
        if c.user_is_admin and thing.invisible_trophies:
            # SOURCE LINE 86
            __M_writer(u'  ')
            __M_writer(conditional_websafe(trophy_table(thing.invisible_trophies, "<p>Invisibles:</p>")))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_trophy_info(context,trophy,center):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f3607eb9350')._populate(_import_ns, [u'ynbutton'])
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        ynbutton = _import_ns.get('ynbutton', context.get('ynbutton', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 25
        __M_writer(u'\n  <td class="trophy-info"\n')
        # SOURCE LINE 27
        if center:
            # SOURCE LINE 28
            __M_writer(u'        colspan="2"\n')
        # SOURCE LINE 30
        __M_writer(u'      >\n    <div>\n      ')
        # SOURCE LINE 32
        trophy_url = trophy.trophy_url 
        
        __M_writer(u'\n')
        # SOURCE LINE 33
        if trophy_url:
            # SOURCE LINE 34
            __M_writer(u'       <a href="')
            __M_writer(conditional_websafe(trophy_url))
            __M_writer(u'">\n')
        # SOURCE LINE 36
        __M_writer(u'       <img class="trophy-icon" src="')
        __M_writer(conditional_websafe(trophy._thing2.imgurl % 40))
        __M_writer(u'" />\n       <br/>\n       <span class="trophy-name">')
        # SOURCE LINE 38
        __M_writer(conditional_websafe(trophy._thing2.title))
        __M_writer(u'</span>\n       <br/>\n')
        # SOURCE LINE 40
        if hasattr(trophy, "description"):
            # SOURCE LINE 41
            __M_writer(u'       <span class="trophy-description">')
            __M_writer(conditional_websafe(trophy.description))
            __M_writer(u'</span>\n       <br/>\n')
        # SOURCE LINE 44
        if trophy_url:
            # SOURCE LINE 45
            __M_writer(u'       </a>\n')
        # SOURCE LINE 47
        if c.user_is_admin:
            # SOURCE LINE 48
            __M_writer(u'      ')
            __M_writer(conditional_websafe(ynbutton(_("remove"), _("removed"), "removetrophy", "hide_thing",
      hidden_data=dict(trophy_fn=trophy._id36))))
            # SOURCE LINE 49
            __M_writer(u'\n')
        # SOURCE LINE 51
        __M_writer(u'    </div>\n  </td>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_trophy_table(context,trophies,header=''):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f3607eb9350')._populate(_import_ns, [u'ynbutton'])
        def trophy_info(trophy,center):
            return render_trophy_info(context,trophy,center)
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        enumerate = _import_ns.get('enumerate', context.get('enumerate', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 60
        __M_writer(u'\n\n  ')
        # SOURCE LINE 62
        __M_writer(conditional_websafe(unsafe(header)))
        __M_writer(u'\n\n  <table class="trophy-table">\n')
        # SOURCE LINE 65
        for i, trophy in enumerate(trophies):
            # SOURCE LINE 66
            if i % 2 == 0:
                # SOURCE LINE 67
                __M_writer(u'       <tr>\n')
            # SOURCE LINE 69
            __M_writer(u'\n      ')
            # SOURCE LINE 70
            __M_writer(conditional_websafe(trophy_info(trophy, i == len(trophies) - 1)))
            __M_writer(u'\n\n')
            # SOURCE LINE 72
            if i % 2 == 1:
                # SOURCE LINE 73
                __M_writer(u'       </tr>\n')
        # SOURCE LINE 76
        __M_writer(u'\n')
        # SOURCE LINE 77
        if len(trophies) % 2 == 1:
            # SOURCE LINE 78
            __M_writer(u'      </tr>\n')
        # SOURCE LINE 80
        __M_writer(u'  </table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


