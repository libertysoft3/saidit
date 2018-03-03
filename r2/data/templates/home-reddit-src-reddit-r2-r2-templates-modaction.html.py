# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505799486.374855
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/modaction.html'
_template_uri = '/modaction.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 25

from pylons import tmpl_context as c
from r2.lib.filters import _force_unicode
from r2.models import Account, Comment, Link

TITLE_MAX_WIDTH = 50


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7ff76fb09e50', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7ff76fb09e50')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7ff76fb09e50')._populate(_import_ns, [u'timestamp', u'plain_link'])
        timestamp = _import_ns.get('timestamp', context.get('timestamp', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n')
        # SOURCE LINE 31
        __M_writer(u'\n\n<tr class="modactions" style="background-color: ')
        # SOURCE LINE 33
        __M_writer(conditional_websafe(thing.bgcolor))
        __M_writer(u'" data-fullname="')
        __M_writer(conditional_websafe(thing.fullname))
        __M_writer(u'">\n  <td class="timestamp whitespace:nowrap">')
        # SOURCE LINE 34
        __M_writer(conditional_websafe(timestamp(thing.date, live=True, include_tense=True)))
        __M_writer(u'</td>\n')
        # SOURCE LINE 35
        if thing.is_multi:
            # SOURCE LINE 36
            __M_writer(u'    <td class="subreddit">')
            __M_writer(conditional_websafe(plain_link('/r/' + thing.subreddit.name, thing.subreddit.path + 'about/log', title=thing.subreddit.name)))
            __M_writer(u'</td>\n')
        # SOURCE LINE 38
        __M_writer(u'  <td class="whitespace:nowrap">')
        __M_writer(conditional_websafe(thing.mod_button))
        __M_writer(u'</td>\n  <td class="button">')
        # SOURCE LINE 39
        __M_writer(conditional_websafe(thing.action_button))
        __M_writer(u'</td>\n  <td class="description">')
        # SOURCE LINE 40
        __M_writer(conditional_websafe(thing.text))
        __M_writer(u'&#32;\n\n')
        # SOURCE LINE 42
        if hasattr(thing, "target") and isinstance(thing.target, Comment):
            # SOURCE LINE 43
            __M_writer(u'    ')

            title = _force_unicode(thing.parent_link.title)
            if len(title) > TITLE_MAX_WIDTH:
                short_title = title[:TITLE_MAX_WIDTH] + '...'
            else:
                short_title = title
            text = _('comment by %(comment_author)s on "%(link_title)s"')
            text %= {
              'comment_author': '[deleted]' if thing.target_author._deleted else thing.target_author.name,
              'link_title': short_title,
            }
            permalink = thing.target.make_permalink(thing.parent_link, thing.subreddit)
                
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['text','permalink','short_title','title'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 55
            __M_writer(u'\n    ')
            # SOURCE LINE 56
            __M_writer(conditional_websafe(plain_link(text, permalink, title=title, _sr_path=False, _class="may-blank")))
            __M_writer(u'&#32;\n')
            # SOURCE LINE 57
        elif hasattr(thing, "target") and isinstance(thing.target, Link):
            # SOURCE LINE 58
            __M_writer(u'    ')

            title = _force_unicode(thing.target.title)
            if len(title) > TITLE_MAX_WIDTH:
                short_title = title[:TITLE_MAX_WIDTH] + '...'
            else:
                short_title = title
            text = _('link "%(link_title)s" by %(link_author)s')
            text %= {
              'link_title': short_title,
              'link_author': '[deleted]' if thing.target_author._deleted else thing.target_author.name,
            }
            permalink = thing.target.make_permalink(thing.subreddit)
                
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['text','permalink','short_title','title'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 70
            __M_writer(u'\n    ')
            # SOURCE LINE 71
            __M_writer(conditional_websafe(plain_link(text, permalink, title=title, _sr_path=False, _class="may-blank")))
            __M_writer(u'&#32;\n')
            # SOURCE LINE 72
        elif hasattr(thing, "wrapped_user_target"):
            # SOURCE LINE 73
            __M_writer(u'    ')
            __M_writer(conditional_websafe(thing.wrapped_user_target))
            __M_writer(u'&#32;\n')
        # SOURCE LINE 75
        __M_writer(u'\n')
        # SOURCE LINE 76
        if thing.details_text:
            # SOURCE LINE 77
            __M_writer(u'    <em>(')
            __M_writer(conditional_websafe(thing.details_text))
            __M_writer(u')</em>\n')
        # SOURCE LINE 79
        __M_writer(u'  </td>\n</tr>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


