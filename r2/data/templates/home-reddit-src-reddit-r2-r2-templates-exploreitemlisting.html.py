# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1507991800.594515
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/exploreitemlisting.html'
_template_uri = '/exploreitemlisting.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23

from r2.lib.template_helpers import format_html


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 26
    ns = runtime.TemplateNamespace('__anon_0x7f30ef3fe9d0', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f30ef3fe9d0')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f30ef3fe9d0')._populate(_import_ns, [u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'\n')
        # SOURCE LINE 26
        __M_writer(u'\n')
        # SOURCE LINE 27

        _id = ("_%s" % thing.parent_name) if hasattr(thing, 'parent_name') else ''
        cls = "exploreitemlisting"
         
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['_id','cls'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 30
        __M_writer(u'\n\n<div id="siteTable')
        # SOURCE LINE 32
        __M_writer(conditional_websafe(_id))
        __M_writer(u'" class="sitetable ')
        __M_writer(conditional_websafe(cls))
        __M_writer(u'">\n  <div class="explore-header">\n    <span id="explore-settings">\n      <form method="POST" action="/post/explore_settings">\n        <input type="hidden" name="uh" value="')
        # SOURCE LINE 36
        __M_writer(conditional_websafe(c.modhash))
        __M_writer(u'">\n        <span>\n          <input type="checkbox" name="pers" value=1 ')
        # SOURCE LINE 38
        __M_writer(conditional_websafe("checked" if thing.settings.personalized else ""))
        __M_writer(u'>\n            ')
        # SOURCE LINE 39
        __M_writer(conditional_websafe(_("personalized")))
        __M_writer(u'\n          </input>\n          <input type="checkbox" name="disc" value=1 ')
        # SOURCE LINE 41
        __M_writer(conditional_websafe("checked" if thing.settings.discovery else ""))
        __M_writer(u'>\n            ')
        # SOURCE LINE 42
        __M_writer(conditional_websafe(_("discovery")))
        __M_writer(u'\n          </input>\n          <input type="checkbox" name="ris" value=1 ')
        # SOURCE LINE 44
        __M_writer(conditional_websafe("checked" if thing.settings.rising else ""))
        __M_writer(u'>\n            ')
        # SOURCE LINE 45
        __M_writer(conditional_websafe(_("rising")))
        __M_writer(u'\n          </input>\n          <input type="checkbox" name="nsfw" value=1 ')
        # SOURCE LINE 47
        __M_writer(conditional_websafe("checked" if thing.settings.nsfw else ""))
        __M_writer(u'>\n            ')
        # SOURCE LINE 48
        __M_writer(conditional_websafe(_("nsfw")))
        __M_writer(u'\n          </input>\n        </span>\n        <button type="submit">\n          ')
        # SOURCE LINE 52
        __M_writer(conditional_websafe(_("apply")))
        __M_writer(u'\n        </button>\n      </form>\n    </span>\n  </div>\n')
        # SOURCE LINE 57
        if thing.things:
            # SOURCE LINE 58
            for a in thing.things:
                # SOURCE LINE 59
                __M_writer(u'        ')
                __M_writer(conditional_websafe(a))
                __M_writer(u'\n')
            # SOURCE LINE 61
            __M_writer(u'      <div class="nav-buttons">\n        <span class="nextprev">')
            # SOURCE LINE 62
            __M_writer(conditional_websafe(_("view more:")))
            __M_writer(u'&#32;\n          ')
            # SOURCE LINE 63
            __M_writer(conditional_websafe(plain_link(format_html("%s &rsaquo;", _("reload suggestions")), request.url, _sr_path=False)))
            __M_writer(u'\n        </span>\n      </div>\n')
            # SOURCE LINE 66
        else:
            # SOURCE LINE 67
            __M_writer(u'    <div class="explore-header">\n      <span class="explore-title">\n        ')
            # SOURCE LINE 69
            __M_writer(conditional_websafe(_("Our robots have no suggestions at the moment.")))
            __M_writer(u'\n      </span>\n    </div>\n    <div class="nav-buttons">\n      <span class="nextprev">\n        ')
            # SOURCE LINE 74
            __M_writer(conditional_websafe(plain_link(format_html("%s &rsaquo;", _("try again")), "/explore", _sr_path=False)))
            __M_writer(u'\n      </span>\n    </div>\n')
        # SOURCE LINE 78
        __M_writer(u'</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


