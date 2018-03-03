# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505002596.43807
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/redditfooter.html'
_template_uri = '/redditfooter.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23

from r2.lib.strings import strings
import datetime


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 27
    ns = runtime.TemplateNamespace('__anon_0x7fde5ff2f410', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fde5ff2f410')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fde5ff2f410')._populate(_import_ns, [u'text_with_links'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        text_with_links = _import_ns.get('text_with_links', context.get('text_with_links', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 26
        __M_writer(u'\n')
        # SOURCE LINE 27
        __M_writer(u'\n\n<div class="footer-parent">\n  <div by-zero class="footer rounded">\n')
        # SOURCE LINE 31
        for toolbar in thing.nav:
            # SOURCE LINE 32
            __M_writer(u'      <div class="col">\n        ')
            # SOURCE LINE 33
            __M_writer(conditional_websafe(toolbar))
            __M_writer(u'\n      </div>\n')
        # SOURCE LINE 36
        __M_writer(u'  </div>\n')
        # SOURCE LINE 37
        if g.domain != "antiextremes.com":
            # SOURCE LINE 38
            __M_writer(u'    <!-- http://code.reddit.com/LICENSE see Exhibit B -->\n    <a href="https://www.reddit.com/code/" style="text-align:center;display:block">\n      <img src="https://s3.amazonaws.com/sp.reddit.com/powered_by_reddit.png"\n           alt="Powered by reddit."\n           style="width:140px; height:47px; margin-bottom: 5px"/>\n    </a>\n')
        # SOURCE LINE 45
        __M_writer(u'  <p class="bottommenu">\n    ')
        # SOURCE LINE 46
        __M_writer(conditional_websafe(text_with_links(
            _("Use of this site constitutes acceptance of our "
              "%(user_agreement)s and %(privacy_policy)s"),
            user_agreement=dict(
                link_text=_("User Agreement {Genitive}"),
                path="/help/useragreement",
            ),
            privacy_policy=dict(
                link_text=_("Privacy Policy (updated)"),
                path="/help/privacypolicy",
                _class="updated",
            ),
    )))
        # SOURCE LINE 58
        __M_writer(u'.\n    &copy; ')
        # SOURCE LINE 59
        __M_writer(conditional_websafe(_("%(year)d SaidIt") % \
    dict(year=datetime.datetime.now().timetuple()[0])))
        # SOURCE LINE 60
        # __M_writer(u'\n  </p>\n  <p class="bottommenu">Thanks </p>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


