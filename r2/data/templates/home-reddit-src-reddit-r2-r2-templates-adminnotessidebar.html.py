# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1515317670.200474
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/adminnotessidebar.html'
_template_uri = '/adminnotessidebar.html'
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
    # SOURCE LINE 24
    ns = runtime.TemplateNamespace('__anon_0x7f514c9f17d0', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f514c9f17d0')] = ns

    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7f514c9f1710', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f514c9f1710')] = ns

    # SOURCE LINE 25
    ns = runtime.TemplateNamespace('__anon_0x7f514c9f1890', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f514c9f1890')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f514c9f17d0')._populate(_import_ns, [u'md'])
        _mako_get_namespace(context, '__anon_0x7f514c9f1710')._populate(_import_ns, [u'error_field'])
        _mako_get_namespace(context, '__anon_0x7f514c9f1890')._populate(_import_ns, [u'timestamp'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        timestamp = _import_ns.get('timestamp', context.get('timestamp', UNDEFINED))
        md = _import_ns.get('md', context.get('md', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n')
        # SOURCE LINE 24
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'\n\n<div class="raisedbox spacer">\n    ')
        # SOURCE LINE 28
        __M_writer(conditional_websafe(_(thing.SYSTEMS[thing.system])))
        __M_writer(u': ')
        __M_writer(conditional_websafe(thing.subject))
        __M_writer(u'\n    <br/>\n    ')
        # SOURCE LINE 30
        __M_writer(conditional_websafe(_('global ban')))
        __M_writer(u': ')
        __M_writer(conditional_websafe(thing.global_ban))
        __M_writer(u'\n    <form id="adminnotes-form" method="post" action="/api/add_admin_note"\n        onsubmit="return post_form(this, \'add_admin_note\')">\n        <input type="hidden" name="system" value="')
        # SOURCE LINE 33
        __M_writer(conditional_websafe(thing.system))
        __M_writer(u'">\n        <input type="hidden" name="subject" value="')
        # SOURCE LINE 34
        __M_writer(conditional_websafe(thing.subject))
        __M_writer(u'">\n        <input type="hidden" name="author" value="')
        # SOURCE LINE 35
        __M_writer(conditional_websafe(thing.author))
        __M_writer(u'">\n        <textarea name="note" rows=4></textarea>\n        ')
        # SOURCE LINE 37
        __M_writer(conditional_websafe(error_field("TOO_LONG", "notes", "span")))
        __M_writer(u'\n        <input type="submit" class="notes-button" value="Add a new Note">\n    </form>\n')
        # SOURCE LINE 40
        if thing.notes:
            # SOURCE LINE 41
            __M_writer(u'        ')
            __M_writer(conditional_websafe(_("Past notes")))
            __M_writer(u':\n        <ul id="past-notes">\n')
            # SOURCE LINE 43
            for note in thing.notes:
                # SOURCE LINE 44
                __M_writer(u'            <li class="adminnote">\n                <div class="adminnote-text">\n                ')
                # SOURCE LINE 46
                __M_writer(conditional_websafe(md(note["note"])))
                __M_writer(u'\n                </div>\n                <div class="adminnote-info tagline">\n                ')
                # SOURCE LINE 49
                __M_writer(conditional_websafe(_("by %(author)s") % dict(
                    author=note["author"],
                )))
                # SOURCE LINE 51
                __M_writer(u'&nbsp;\n                ')
                # SOURCE LINE 52
                __M_writer(conditional_websafe(timestamp(note["when"], include_tense=True)))
                __M_writer(u'\n                </div>\n            </li>\n')
            # SOURCE LINE 56
            __M_writer(u'        </ul>\n')
            # SOURCE LINE 57
        else:
            # SOURCE LINE 58
            __M_writer(u'        ')
            __M_writer(conditional_websafe(_(thing.EMPTY_MESSAGE[thing.system])))
            __M_writer(u'\n')
        # SOURCE LINE 60
        __M_writer(u'</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


