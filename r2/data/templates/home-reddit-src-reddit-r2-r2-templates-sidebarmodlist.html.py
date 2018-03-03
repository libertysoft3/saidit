# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505839975.037472
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/sidebarmodlist.html'
_template_uri = '/sidebarmodlist.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23

from r2.config import feature


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 27
    ns = runtime.TemplateNamespace('__anon_0x7f2f68662f10', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f2f68662f10')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f2f68662f10')._populate(_import_ns, [u'nsfw_stamp', u'quarantine_stamp'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        quarantine_stamp = _import_ns.get('quarantine_stamp', context.get('quarantine_stamp', UNDEFINED))
        nsfw_stamp = _import_ns.get('nsfw_stamp', context.get('nsfw_stamp', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'\n\n')
        # SOURCE LINE 27
        __M_writer(u'\n\n<ul id="side-mod-list">\n')
        # SOURCE LINE 30
        for sr in thing.subreddits:
            # SOURCE LINE 31
            __M_writer(u'  ')

            if sr.spammy():
              sr_class = 'sr-banned'
            else:
              sr_class = ''
              
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['sr_class'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 36
            __M_writer(u'\n\n  <li class="')
            # SOURCE LINE 38
            __M_writer(conditional_websafe(sr_class))
            __M_writer(u'">\n    <a href="')
            # SOURCE LINE 39
            __M_writer(conditional_websafe(sr.path))
            __M_writer(u'" title="/r/')
            __M_writer(conditional_websafe(sr.name))
            __M_writer(u'">/r/')
            __M_writer(conditional_websafe(sr.name))
            __M_writer(u'</a>\n')
            # SOURCE LINE 40
            if sr.quarantine:
                # SOURCE LINE 41
                __M_writer(u'      <span class="quarantine-stamp stamp">')
                __M_writer(conditional_websafe(quarantine_stamp()))
                __M_writer(u'</span>\n')
                # SOURCE LINE 42
            elif sr.over_18 and c.user.pref_label_nsfw:
                # SOURCE LINE 43
                __M_writer(u'      <span class="nsfw-stamp stamp">')
                __M_writer(conditional_websafe(nsfw_stamp()))
                __M_writer(u'</span>\n')
            # SOURCE LINE 45
            __M_writer(u'  </li>\n')
        # SOURCE LINE 47
        __M_writer(u"</ul>\n\n<script>new r.ui.Summarize($('#side-mod-list'), 5)</script>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


