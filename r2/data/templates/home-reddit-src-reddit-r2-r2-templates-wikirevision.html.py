# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505982992.066385
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/wikirevision.html'
_template_uri = '/wikirevision.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 26

from urllib import quote


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7f20bcaecb50', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f20bcaecb50')] = ns

    # SOURCE LINE 24
    ns = runtime.TemplateNamespace('__anon_0x7f20bcaec6d0', context._clean_inheritance_tokens(), templateuri=u'printablebuttons.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f20bcaec6d0')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f20bcaecb50')._populate(_import_ns, [u'timestamp'])
        _mako_get_namespace(context, '__anon_0x7f20bcaec6d0')._populate(_import_ns, [u'ynbutton'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        ynbutton = _import_ns.get('ynbutton', context.get('ynbutton', UNDEFINED))
        timestamp = _import_ns.get('timestamp', context.get('timestamp', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n')
        # SOURCE LINE 24
        __M_writer(u'\n\n')
        # SOURCE LINE 28
        __M_writer(u'\n\n<tr class="revision\n')
        # SOURCE LINE 31
        if thing._hidden:
            # SOURCE LINE 32
            __M_writer(u'       hidden\n')
        # SOURCE LINE 34
        if thing.admin_deleted:
            # SOURCE LINE 35
            __M_writer(u'        deleted\n')
        # SOURCE LINE 37
        __M_writer(u'    ">\n    \n')
        # SOURCE LINE 39
        if thing.show_compare:
            # SOURCE LINE 40
            __M_writer(u'            <td style="white-space: nowrap;">\n                <input type="radio" name="v1" value="')
            # SOURCE LINE 41
            __M_writer(conditional_websafe(thing._id))
            __M_writer(u'" checked="yes">\n                <input type="radio" name="v2" value="')
            # SOURCE LINE 42
            __M_writer(conditional_websafe(thing._id))
            __M_writer(u'" checked="yes">\n            </td>\n')
        # SOURCE LINE 45
        __M_writer(u'    \n    <td style="white-space: nowrap;">\n        ')
        # SOURCE LINE 47
        __M_writer(conditional_websafe(timestamp(thing.date, live=True, include_tense=True)))
        __M_writer(u'\n    </td>\n    \n')
        # SOURCE LINE 50
        if not thing.show_extended:
            # SOURCE LINE 51
            __M_writer(u'        <td>\n            <a href="')
            # SOURCE LINE 52
            __M_writer(conditional_websafe(c.wiki_base_url))
            __M_writer(u'/')
            __M_writer(conditional_websafe(thing.page))
            __M_writer(u'">')
            __M_writer(conditional_websafe(thing.page))
            __M_writer(u'</a>\n        </td>\n')
        # SOURCE LINE 55
        __M_writer(u'    \n    <td>\n        <a href="')
        # SOURCE LINE 57
        __M_writer(conditional_websafe(c.wiki_base_url))
        __M_writer(u'/')
        __M_writer(conditional_websafe(thing.page))
        __M_writer(u'?v=')
        __M_writer(conditional_websafe(thing._id))
        __M_writer(u'">view</a>\n    </td>\n    \n    <td>\n        ')
        # SOURCE LINE 61
        __M_writer(conditional_websafe(thing.printable_author))
        __M_writer(u'\n    </td>\n    \n    <td style="font-style: italic;">\n        ')
        # SOURCE LINE 65
        __M_writer(conditional_websafe(thing._get('reason')))
        __M_writer(u'\n    </td>\n   \n')
        # SOURCE LINE 68
        if thing.show_extended:
            # SOURCE LINE 69
            __M_writer(u'        <td>\n            <a href="#" class="revision_hide access-required"\n               data-revision="')
            # SOURCE LINE 71
            __M_writer(conditional_websafe(thing._id))
            __M_writer(u'"\n               data-type="wikipage"\n               data-event-action="wikirevise"\n               data-event-detail="hide"\n               >hide</a>\n        </td>\n        <td class="wiki_revert" style="white-space: nowrap;">\n            ')
            # SOURCE LINE 78
            __M_writer(conditional_websafe(ynbutton(_("revert here"), 
                       _("done"),
                       quote("..%s/revert" % c.wiki_api_url), 
                       hidden_data=dict(revision=thing._id, page=thing.page), 
                       post_callback="$.refresh",
                       event_target='wikipage',
                       event_action='wikirevise',
                       event_detail='revert'
                      )
             ))
            # SOURCE LINE 87
            __M_writer(u'\n        </td>\n')
        # SOURCE LINE 90
        __M_writer(u'\n')
        # SOURCE LINE 91
        if c.user_is_admin:
            # SOURCE LINE 92
            __M_writer(u'        <td>\n            <a href="#" class="revision_delete" data-revision="')
            # SOURCE LINE 93
            __M_writer(conditional_websafe(thing._id))
            __M_writer(u'">delete</a>\n        </td>\n')
        # SOURCE LINE 96
        __M_writer(u'</tr>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


