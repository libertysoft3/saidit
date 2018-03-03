# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505002596.263841
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/spotlightlisting.html'
_template_uri = '/spotlightlisting.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 31

from babel.numbers import format_currency


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7fde601bb610', context._clean_inheritance_tokens(), templateuri=u'printablebuttons.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fde601bb610')] = ns

    # SOURCE LINE 24
    ns = runtime.TemplateNamespace('__anon_0x7fde601bb8d0', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fde601bb8d0')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fde601bb610')._populate(_import_ns, [u'ynbutton'])
        _mako_get_namespace(context, '__anon_0x7fde601bb8d0')._populate(_import_ns, [u'tags', u'text_with_links', u'classes'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        classes = _import_ns.get('classes', context.get('classes', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        text_with_links = _import_ns.get('text_with_links', context.get('text_with_links', UNDEFINED))
        ynbutton = _import_ns.get('ynbutton', context.get('ynbutton', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n')
        # SOURCE LINE 24
        __M_writer(u'\n')
        # SOURCE LINE 25

        import json
        from r2.lib.template_helpers import static, format_html
        from r2.lib.wrapped import Templated
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['format_html','json','static','Templated'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 29
        __M_writer(u'\n\n')
        # SOURCE LINE 33
        __M_writer(u'\n\n<div id="siteTable_organic" ')
        # SOURCE LINE 35
        __M_writer(conditional_websafe(classes('organic-listing', 'loading',
    'show-placeholder' if thing.show_placeholder else None,
  )))
        # SOURCE LINE 37
        __M_writer(u'>\n')
        # SOURCE LINE 38
        if thing.things:
            # SOURCE LINE 39
            for link in thing.things:
                # SOURCE LINE 40
                __M_writer(u'      ')
                __M_writer(conditional_websafe(unsafe(link.render(display=False))))
                __M_writer(u'\n')
        # SOURCE LINE 43
        __M_writer(u'\n')
        # SOURCE LINE 44
        if thing.interestbar:
            # SOURCE LINE 45
            __M_writer(u'    <div class="thing interestbar" style="display:none">\n      ')
            # SOURCE LINE 46
                      # SOURCE LINE 49
        __M_writer(u'\n')
        # SOURCE LINE 50
        if thing.navigable:
            # SOURCE LINE 51
            __M_writer(u'    <div class="nextprev">\n      <div class="throbber"></div>\n      <button class="arrow prev">')
            # SOURCE LINE 53
            __M_writer(conditional_websafe(_("prev")))
            __M_writer(u'</button>\n      <button class="arrow next">')
            # SOURCE LINE 54
            __M_writer(conditional_websafe(_("next")))
            __M_writer(u'</button>\n    </div>\n')
        # SOURCE LINE 57
        __M_writer(u'\n  <div class="help help-hoverable">\n    ')
        # SOURCE LINE 59
        __M_writer(conditional_websafe(_("what's this?")))
        __M_writer(u'\n    <div id="spotlight-help" class="hover-bubble help-bubble anchor-top">\n      <div class="help-section help-promoted">\n        <p>\n          ')
        # SOURCE LINE 63
        __M_writer(conditional_websafe(text_with_links(
            _("This sponsored link is an advertisement generated with our %(self_serve_advertisement_tool)s."),
              self_serve_advertisement_tool=dict(link_text=_("self-serve advertisement tool"), path="https://www.reddit.com/wiki/selfserve")
          )))
        # SOURCE LINE 66
        __M_writer(u'\n        </p>\n        <p>\n          ')
        # SOURCE LINE 69
        __M_writer(conditional_websafe(text_with_links(
            _("Use of this tool is open to all members of reddit.com, and for as little as %(price)s you can advertise in this area. %%(get_started)s") % dict(price=format_currency(g.min_total_budget_pennies / 100., 'USD', locale=c.locale)),
              get_started=dict(link_text=format_html("%s &rsaquo;", _("Get started")), path="/advertising")
          )))
        # SOURCE LINE 72
        __M_writer(u'\n        </p>\n      </div>\n      <div class="help-section help-organic">\n        <p>\n          ')
        # SOURCE LINE 77
        __M_writer(conditional_websafe(_("This area shows new and upcoming links. Vote on" +
                " links here to help them become popular, and click" +
                " the forwards and backwards buttons to view more. ")))
        # SOURCE LINE 79
        __M_writer(u'\n        </p>\n')
        # SOURCE LINE 81
        if c.user_is_loggedin:
            # SOURCE LINE 82
            __M_writer(u'          ')
            __M_writer(conditional_websafe(ynbutton(_("here"), _("This element has been disabled."),
                     "disable_ui",
                     format = _("Click %(here)s to disable this feature."),
                     format_arg = "here",
                     hidden_data = dict(id="organic"))))
            # SOURCE LINE 86
            __M_writer(u'\n')
        # SOURCE LINE 88
        __M_writer(u'      </div>\n      <div class="help-section help-interestbar">\n        <p>')
        # SOURCE LINE 90
        __M_writer(conditional_websafe(_("Enter a keyword or topic to discover new subreddits around your interests. Be specific!")))
        __M_writer(u'</p>\n        <p>\n          ')
        # SOURCE LINE 92
        __M_writer(conditional_websafe(text_with_links(
            _("You can access this tool at any time on the %(reddits)s page."),
              reddits=dict(link_text="/subreddits/", path="/subreddits/")
          )))
        # SOURCE LINE 95
        __M_writer(u'\n        </p>\n      </div>\n    </div>\n  </div>\n</div>\n<script>\n  r.spotlight.setup(\n    ')
        # SOURCE LINE 103
        __M_writer(conditional_websafe(unsafe(json.dumps([link._fullname for link in thing.things]))))
        __M_writer(u',\n    ')
        # SOURCE LINE 104
        __M_writer(conditional_websafe(unsafe(json.dumps(thing.interestbar_prob))))
        __M_writer(u',\n    ')
        # SOURCE LINE 105
        __M_writer(conditional_websafe(unsafe(json.dumps(thing.show_promo))))
        __M_writer(u',\n    ')
        # SOURCE LINE 106
        __M_writer(conditional_websafe(unsafe(json.dumps(thing.keywords))))
        __M_writer(u'\n  )\n</script>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


