# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1520060829.684049
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/linkcommentssettings.html'
_template_uri = '/linkcommentssettings.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['suggested_clear_type', 'clear_suggested_sort']


# SOURCE LINE 23

from r2.config import feature
from r2.lib.filters import jssafe


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 28
    ns = runtime.TemplateNamespace('__anon_0x7fc7c777d110', context._clean_inheritance_tokens(), templateuri=u'printablebuttons.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fc7c777d110')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c777d110')._populate(_import_ns, [u'ynbutton'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        ynbutton = _import_ns.get('ynbutton', context.get('ynbutton', UNDEFINED))
        def clear_suggested_sort():
            return render_clear_suggested_sort(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 26
        __M_writer(u'\n\n')
        # SOURCE LINE 28
        __M_writer(u'\n\n\n')
        # SOURCE LINE 34
        __M_writer(u'\n\n')
        # SOURCE LINE 80
        __M_writer(u'\n\n')
        # SOURCE LINE 82
        if thing.can_edit:
            # SOURCE LINE 83
            if thing.suggested_sort == thing.sort:
                # SOURCE LINE 84
                __M_writer(u'    ')
                clear_suggested_sort() 
                
                __M_writer(u'\n')
                # SOURCE LINE 85
            else:
                # SOURCE LINE 86
                __M_writer(u'    ')
                __M_writer(conditional_websafe(ynbutton(_("set as suggested sort"), _("suggested sort set"), "set_suggested_sort",
      hidden_data=dict(id=thing.link._fullname, sort=thing.sort),
      event_target='link', event_action='setsuggestedsort')))
                # SOURCE LINE 88
                __M_writer(u'\n')
        # SOURCE LINE 91
        __M_writer(u'\n')
        # SOURCE LINE 92
        if thing.is_author:
            # SOURCE LINE 93
            if thing.sendreplies:
                # SOURCE LINE 94
                __M_writer(u'    ')
                __M_writer(conditional_websafe(ynbutton(_("disable inbox replies"), _("inbox replies disabled"), "sendreplies",
      hidden_data=dict(id=thing.link._fullname, state=False),
      access_required=False, event_action="disable_inbox_replies")))
                # SOURCE LINE 96
                __M_writer(u'\n')
                # SOURCE LINE 97
            else:
                # SOURCE LINE 98
                __M_writer(u'    ')
                __M_writer(conditional_websafe(ynbutton(_("enable inbox replies"), _("inbox replies enabled"), "sendreplies",
      hidden_data=dict(id=thing.link._fullname, state=True),
      access_required=False, event_action="enable_inbox_replies")))
                # SOURCE LINE 100
                __M_writer(u'\n')
            # SOURCE LINE 102
            __M_writer(u'  &nbsp;<span class="help-hoverable" title="')
            __M_writer(conditional_websafe(_('inbox replies will send you a message when this link receives a new top-level comment')))
            __M_writer(u'">(?)</span>\n')
        # SOURCE LINE 104
        __M_writer(u'\n')
        # SOURCE LINE 105
        if thing.can_edit:
            # SOURCE LINE 106
            if thing.contest_mode:
                # SOURCE LINE 107
                __M_writer(u'    ')
                __M_writer(conditional_websafe(ynbutton(_("disable contest mode"), _("contest mode disabled"), "set_contest_mode",
      hidden_data=dict(id=thing.link._fullname, state=False),
      event_target='link', event_action='unsetcontestmode')))
                # SOURCE LINE 109
                __M_writer(u'\n')
                # SOURCE LINE 110
            else:
                # SOURCE LINE 111
                __M_writer(u'    ')
                __M_writer(conditional_websafe(ynbutton(_("enable contest mode"), _("contest mode enabled"), "set_contest_mode",
      hidden_data=dict(id=thing.link._fullname, state=True),
      event_target='link', event_action='setcontestmode')))
                # SOURCE LINE 113
                __M_writer(u'\n')
        # SOURCE LINE 116
        __M_writer(u'\n')
        # SOURCE LINE 117
        if thing.can_sticky:
            # SOURCE LINE 118
            if thing.stickied:
                # SOURCE LINE 119
                __M_writer(u'    ')
                __M_writer(conditional_websafe(ynbutton(_("remove announcement"), _("removed"), "set_subreddit_sticky",
      hidden_data=dict(id=thing.link._fullname, state=False),
      event_target='link', event_action='unsticky')))
                # SOURCE LINE 121
                __M_writer(u'\n')
                # SOURCE LINE 122
            elif thing.stickies_full:
                # SOURCE LINE 123
                __M_writer(u'    ')
                __M_writer(conditional_websafe(ynbutton(_("make announcement"), _("announced"), "set_subreddit_sticky",
      question=_("make announcement? (bottom announcement will be replaced)"),
      hidden_data=dict(id=thing.link._fullname, state=True),
      event_target='link', event_action='sticky')))
                # SOURCE LINE 126
                __M_writer(u'\n')
                # SOURCE LINE 127
            else:
                # SOURCE LINE 128
                __M_writer(u'    ')
                __M_writer(conditional_websafe(ynbutton(_("make announcement"), _("announced"), "set_subreddit_sticky",
      question=_("make announcement?"),
      hidden_data=dict(id=thing.link._fullname, state=True),
      event_target='link', event_action='sticky')))
                # SOURCE LINE 131
                __M_writer(u'\n')
        # SOURCE LINE 134
        __M_writer(u'\n')
        # SOURCE LINE 135
        if thing.contest_mode:
            # SOURCE LINE 136
            __M_writer(u'  <div class="contest-mode infobar mellow"><strong>')
            __M_writer(conditional_websafe(_("this thread is in contest mode")))
            __M_writer(u'</strong>&#32;- \n')
            # SOURCE LINE 137
            if thing.can_edit:
                # SOURCE LINE 138
                __M_writer(u'    ')
                __M_writer(conditional_websafe(_('as a mod, you can sort comments however you wish and scores are visible. regular users have randomized sorting and cannot see the scores.')))
                __M_writer(u'\n')
                # SOURCE LINE 139
            else:
                # SOURCE LINE 140
                __M_writer(u'    ')
                __M_writer(conditional_websafe(_('contest mode randomizes comment sorting, hides scores, and collapses replies by default.')))
                __M_writer(u'\n')
            # SOURCE LINE 142
            __M_writer(u'  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_suggested_clear_type(context,name,value=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c777d110')._populate(_import_ns, [u'ynbutton'])
        __M_writer = context.writer()
        # SOURCE LINE 31
        __M_writer(u'\n  <a href="javascript:void(0)"\n     onclick="return set_suggested_sort(this, \'')
        # SOURCE LINE 33
        __M_writer(conditional_websafe(jssafe(value or name)))
        __M_writer(u'\')">')
        __M_writer(conditional_websafe(_(name)))
        __M_writer(u'</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_clear_suggested_sort(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c777d110')._populate(_import_ns, [u'ynbutton'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        def suggested_clear_type(name,value=None):
            return render_suggested_clear_type(context,name,value)
        __M_writer = context.writer()
        # SOURCE LINE 36
        __M_writer(u'\n  <li class="toggle">\n    <form method="post" action="/api/set_suggested_sort">\n      <input type="hidden" name="id" value="')
        # SOURCE LINE 39
        __M_writer(conditional_websafe(thing.link._fullname))
        __M_writer(u'" />\n      <input type="hidden" name="sort" value="" />\n      <input type="hidden" value="')
        # SOURCE LINE 41
        __M_writer(conditional_websafe(_('suggested sort cleared')))
        __M_writer(u'" name="executed"/>\n      <a href="javascript:void(0)"\n         onclick="return toggle_clear_suggested_sort(this)"\n         data-event-action="unsetsuggestedsort">\n        ')
        # SOURCE LINE 45
        __M_writer(conditional_websafe(_("clear suggested sort")))
        __M_writer(u'</a>\n      <span class="option error">\n         ')
        # SOURCE LINE 47
        __M_writer(conditional_websafe(_("clear suggested sort?")))
        __M_writer(u'\n\n')
        # SOURCE LINE 49
        if thing.sr.suggested_comment_sort:
            # SOURCE LINE 50
            __M_writer(u'\n           &#32;\n')
            # SOURCE LINE 53
            __M_writer(u'           ')
            __M_writer(conditional_websafe(suggested_clear_type('clear', 'blank')))
            __M_writer(u'\n           &#32;/\n\n')
            # SOURCE LINE 57
            if thing.link.suggested_sort is not None:
                # SOURCE LINE 58
                __M_writer(u'           &#32;\n')
                # SOURCE LINE 60
                __M_writer(u'           ')
                __M_writer(conditional_websafe(suggested_clear_type('use subreddit setting', '')))
                __M_writer(u'\n           &#32;/\n')
            # SOURCE LINE 63
            __M_writer(u'\n')
            # SOURCE LINE 64
        else:
            # SOURCE LINE 65
            __M_writer(u'\n           &#32;\n')
            # SOURCE LINE 68
            __M_writer(u'           ')
            __M_writer(conditional_websafe(suggested_clear_type('clear', '')))
            __M_writer(u'\n           &#32;/\n\n')
        # SOURCE LINE 72
        __M_writer(u'\n         &#32;\n         <a href="javascript:void(0)"\n            onclick="return toggle_clear_suggested_sort(this)">')
        # SOURCE LINE 75
        __M_writer(conditional_websafe(_('cancel')))
        __M_writer(u'</a>\n         &#32;\n      </span>\n    </form>\n  </li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


