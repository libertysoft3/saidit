# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1511947254.20305
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/comment.iframe'
_template_uri = '/comment.iframe'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['entry', 'comment_css_class', 'parent']


# SOURCE LINE 23

import simplejson
from pylons.i18n import _, ungettext
from r2.lib.filters import safemarkdown
from r2.lib.strings import Score
from r2.lib.template_helpers import get_domain, add_sr


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 31
    ns = runtime.TemplateNamespace('__anon_0x7f3a4e095690', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f3a4e095690')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'printable.iframe', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f3a4e095690')._populate(_import_ns, [u'thing_timestamp'])
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 29
        __M_writer(u'\n')
        # SOURCE LINE 30
        __M_writer(u'\n')
        # SOURCE LINE 31
        __M_writer(u'\n\n')
        # SOURCE LINE 41
        __M_writer(u'\n\n')
        # SOURCE LINE 46
        __M_writer(u'\n\n')
        # SOURCE LINE 113
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_entry(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f3a4e095690')._populate(_import_ns, [u'thing_timestamp'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        thing_timestamp = _import_ns.get('thing_timestamp', context.get('thing_timestamp', UNDEFINED))
        def comment_css_class(thing,hide_edits):
            return render_comment_css_class(context,thing,hide_edits)
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 48
        __M_writer(u'\n  ')
        # SOURCE LINE 49

        edited_recently = c.embed_config.get("thing").get("edited")
        hide_edits = (not thing.edits_visible) and edited_recently
          
        
        # SOURCE LINE 52
        __M_writer(u'\n  <article class="reddit-embed-comment ')
        # SOURCE LINE 53
        __M_writer(conditional_websafe(comment_css_class(thing, hide_edits)))
        __M_writer(u'">\n')
        # SOURCE LINE 54
        if thing.deleted:
            # SOURCE LINE 55
            __M_writer(u'      ')
            __M_writer(conditional_websafe(_("This comment was deleted.")))
            __M_writer(u'\n')
            # SOURCE LINE 56
        else:
            # SOURCE LINE 57
            __M_writer(u'      <header class="reddit-embed-comment-header">\n')
            # SOURCE LINE 58
            if thing.author._deleted:
                # SOURCE LINE 59
                __M_writer(u'          <span class="reddit-embed-author reddit-embed-author-deleted">\n            ')
                # SOURCE LINE 60
                __M_writer(conditional_websafe(_("[account deleted]")))
                __M_writer(u'\n          </span>\n')
                # SOURCE LINE 62
            else:
                # SOURCE LINE 63
                __M_writer(u'          <span class="reddit-embed-author">\n            ')
                # SOURCE LINE 64
                __M_writer(conditional_websafe(thing.author.name))
                __M_writer(u'\n          </span>\n')
            # SOURCE LINE 67
            if hide_edits:
                # SOURCE LINE 68
                __M_writer(u'          ')
                __M_writer(conditional_websafe(_("%(name)s's comment was changed.") % dict(name="")))
                __M_writer(u'\n')
                # SOURCE LINE 69
            else:
                # SOURCE LINE 70
                __M_writer(u'        <div class="reddit-embed-comment-meta">\n')
                # SOURCE LINE 71
                if not thing.score_hidden:
                    # SOURCE LINE 72
                    __M_writer(u'            <a href="')
                    __M_writer(conditional_websafe(add_sr(thing.permalink)))
                    __M_writer(u'?context=3"\n               class="reddit-embed-comment-meta-item reddit-embed-score"\n               data-redirect-type="score"\n               data-redirect-thing="')
                    # SOURCE LINE 75
                    __M_writer(conditional_websafe(thing._id))
                    __M_writer(u'">\n              ')
                    # SOURCE LINE 76
                    __M_writer(conditional_websafe(websafe(Score.safepoints(thing.score))))
                    __M_writer(u'\n            </a>\n')
                # SOURCE LINE 79
                if thing.edits_visible and edited_recently:
                    # SOURCE LINE 80
                    __M_writer(u'            <a href="')
                    __M_writer(conditional_websafe(add_sr(thing.permalink)))
                    __M_writer(u'?context=3"\n               class="reddit-embed-comment-meta-item reddit-embed-edited"\n               data-redirect-type="edited"\n               data-redirect-thing="')
                    # SOURCE LINE 83
                    __M_writer(conditional_websafe(thing._id))
                    __M_writer(u'">\n              edited\n            </a>\n')
                # SOURCE LINE 87
                __M_writer(u'          <a href="')
                __M_writer(conditional_websafe(add_sr(thing.permalink)))
                __M_writer(u'?context=3"\n             class="reddit-embed-comment-meta-item reddit-embed-permalink"\n             data-redirect-type="timestamp"\n             data-redirect-thing="')
                # SOURCE LINE 90
                __M_writer(conditional_websafe(thing._id))
                __M_writer(u'">\n            ')
                # SOURCE LINE 91
                __M_writer(conditional_websafe(thing_timestamp(thing, thing.timesince, live=True, include_tense=True)))
                __M_writer(u'\n          </a>\n        </div>\n')
            # SOURCE LINE 95
            __M_writer(u'      </header>\n')
            # SOURCE LINE 96
            if hide_edits:
                # SOURCE LINE 97
                __M_writer(u'        <a href="')
                __M_writer(conditional_websafe(add_sr(thing.permalink)))
                __M_writer(u'?context=3"\n           data-redirect-type="hidden_comment"\n           data-redirect-thing="')
                # SOURCE LINE 99
                __M_writer(conditional_websafe(thing._id))
                __M_writer(u'">\n          ')
                # SOURCE LINE 100
                __M_writer(conditional_websafe(_("View the current version on reddit.")))
                __M_writer(u'\n        </a>\n')
                # SOURCE LINE 102
            else:
                # SOURCE LINE 103
                __M_writer(u'        <blockquote class="reddit-embed-comment-body">\n          ')
                # SOURCE LINE 104
                __M_writer(conditional_websafe(unsafe(safemarkdown(thing.body, nofollow=thing.nofollow))))
                __M_writer(u'\n        </blockquote>\n        <a class="reddit-embed-comment-more" href="javascript:;" target="_self"\n           data-track-action="read_more">\n          ')
                # SOURCE LINE 108
                __M_writer(conditional_websafe(_("Read more")))
                __M_writer(u'\n        </a>\n')
        # SOURCE LINE 112
        __M_writer(u'  </article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_css_class(context,thing,hide_edits):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f3a4e095690')._populate(_import_ns, [u'thing_timestamp'])
        __M_writer = context.writer()
        # SOURCE LINE 43
        __M_writer(u'\n  ')
        # SOURCE LINE 44
        __M_writer(conditional_websafe("reddit-embed-comment-deleted" if thing.deleted else ""))
        __M_writer(u'\n  ')
        # SOURCE LINE 45
        __M_writer(conditional_websafe("reddit-embed-comment-edited" if hide_edits else ""))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_parent(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f3a4e095690')._populate(_import_ns, [u'thing_timestamp'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 33
        __M_writer(u'\n')
        # SOURCE LINE 34
        if c.profilepage:
            # SOURCE LINE 35
            __M_writer(u'    <a href="')
            __M_writer(conditional_websafe(thing.link.url))
            __M_writer(u'"\n')
            # SOURCE LINE 36
            if thing.nofollow:
                # SOURCE LINE 37
                __M_writer(u'         rel="nofollow"\n')
            # SOURCE LINE 39
            __M_writer(u'       >')
            __M_writer(conditional_websafe(thing.link.title))
            __M_writer(u'</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


