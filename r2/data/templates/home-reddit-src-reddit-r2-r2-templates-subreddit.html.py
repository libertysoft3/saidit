# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505003389.77501
_enable_loop = True
_template_filename = u'/home/reddit/src/reddit/r2/r2/templates/subreddit.html'
_template_uri = u'/subreddit.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['sr_type_icon', 'numcol', 'tagline', 'permission_icons', 'midcol', 'child', 'entry']


# SOURCE LINE 23

from r2.lib.template_helpers import static
from r2.lib.strings import strings
from r2.lib.utils import timesince
from r2.lib.pages import SubscribeButton


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 31
    ns = runtime.TemplateNamespace('__anon_0x7f3608c91d90', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f3608c91d90')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'printable.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f3608c91d90')._populate(_import_ns, [u'plain_link'])
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 28
        __M_writer(u'\n')
        # SOURCE LINE 29
        __M_writer(u'\n\n')
        # SOURCE LINE 31
        __M_writer(u'\n\n')
        # SOURCE LINE 34
        __M_writer(u'\n\n')
        # SOURCE LINE 56
        __M_writer(u'\n\n')
        # SOURCE LINE 63
        __M_writer(u'\n\n')
        # SOURCE LINE 69
        __M_writer(u'\n\n')
        # SOURCE LINE 98
        __M_writer(u'\n\n')
        # SOURCE LINE 105
        __M_writer(u'\n\n')
        # SOURCE LINE 108
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sr_type_icon(context,name,title):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f3608c91d90')._populate(_import_ns, [u'plain_link'])
        __M_writer = context.writer()
        # SOURCE LINE 65
        __M_writer(u'\n  <span class="sr-type-icon sr-type-icon-')
        # SOURCE LINE 66
        __M_writer(conditional_websafe(name))
        __M_writer(u'"\n       title="')
        # SOURCE LINE 67
        __M_writer(conditional_websafe(title))
        __M_writer(u'"\n       alt="')
        # SOURCE LINE 68
        __M_writer(conditional_websafe(title))
        __M_writer(u'"></span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_numcol(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f3608c91d90')._populate(_import_ns, [u'plain_link'])
        __M_writer = context.writer()
        # SOURCE LINE 33
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tagline(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f3608c91d90')._populate(_import_ns, [u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 58
        __M_writer(u'\n')
        # SOURCE LINE 59
        if not thing.score_hidden:
            # SOURCE LINE 60
            __M_writer(u'    ')
            __M_writer(conditional_websafe(self.score(thing)))
            __M_writer(u',\n')
        # SOURCE LINE 62
        __M_writer(u'  ')
        __M_writer(conditional_websafe(_("a community for %(time)s") % dict(time=timesince(thing._date))))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_permission_icons(context,sr):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f3608c91d90')._populate(_import_ns, [u'plain_link'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 72
        __M_writer(u'\n')
        # SOURCE LINE 73
        if sr.spammy():
            # SOURCE LINE 74
            __M_writer(u'    ')
            __M_writer(conditional_websafe(self.sr_type_icon("banned", _("banned"))))
            __M_writer(u'\n')
            # SOURCE LINE 75
        else:
            # SOURCE LINE 76
            if sr.moderator:
                # SOURCE LINE 77
                __M_writer(u'      ')
                __M_writer(conditional_websafe(self.sr_type_icon("moderator", _("moderator"))))
                __M_writer(u'\n')
                # SOURCE LINE 78
            elif sr.type in ("restricted", "private"):
                # SOURCE LINE 79
                if sr.contributor:
                    # SOURCE LINE 80
                    __M_writer(u'        ')
                    __M_writer(conditional_websafe(self.sr_type_icon("approved", _("approved submitter"))))
                    __M_writer(u'\n')
                    # SOURCE LINE 81
                else:
                    # SOURCE LINE 82
                    __M_writer(u'        ')
                    __M_writer(conditional_websafe(self.sr_type_icon("restricted", _("not approved"))))
                    __M_writer(u'\n')
            # SOURCE LINE 85
            __M_writer(u'\n')
            # SOURCE LINE 86
            if sr.type in sr.private_types:
                # SOURCE LINE 87
                __M_writer(u'      ')
                __M_writer(conditional_websafe(self.sr_type_icon("private", _("private"))))
                __M_writer(u'\n')
            # SOURCE LINE 89
            __M_writer(u'\n')
            # SOURCE LINE 90
            if sr.quarantine:
                # SOURCE LINE 91
                __M_writer(u'      ')
                __M_writer(conditional_websafe(self.sr_type_icon("quarantined", _("quarantined"))))
                __M_writer(u'\n')
            # SOURCE LINE 93
            __M_writer(u'\n')
            # SOURCE LINE 94
            if sr.over_18:
                # SOURCE LINE 95
                __M_writer(u'      ')
                __M_writer(conditional_websafe(self.sr_type_icon("nsfw", _("NSFW"))))
                __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_midcol(context,display=True,cls=''):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f3608c91d90')._populate(_import_ns, [u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        def permission_icons(sr):
            return render_permission_icons(context,sr)
        __M_writer = context.writer()
        # SOURCE LINE 100
        __M_writer(u'\n  <div class="midcol">\n    ')
        # SOURCE LINE 102
        __M_writer(conditional_websafe(SubscribeButton(thing)))
        __M_writer(u'\n    ')
        # SOURCE LINE 103
        __M_writer(conditional_websafe(permission_icons(thing)))
        __M_writer(u'\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_child(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f3608c91d90')._populate(_import_ns, [u'plain_link'])
        __M_writer = context.writer()
        # SOURCE LINE 107
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_entry(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f3608c91d90')._populate(_import_ns, [u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 36
        __M_writer(u'\n')
        # SOURCE LINE 37
        fullname = thing._fullname 
        
        __M_writer(u'\n<p class="titlerow">\n  ')
        # SOURCE LINE 39
        __M_writer(conditional_websafe(plain_link('%s: %s' % (thing.path.rstrip('/'), thing.title), thing.path, _class="title")))
        __M_writer(u'\n')
        # SOURCE LINE 40
        if c.user_is_admin:
            # SOURCE LINE 41
            __M_writer(u'  ')
            __M_writer(conditional_websafe(self.admintagline()))
            __M_writer(u'\n')
        # SOURCE LINE 43
        __M_writer(u'</p>\n')
        # SOURCE LINE 44
        if thing.public_description_usertext:
            # SOURCE LINE 45
            __M_writer(u'  <div class="description">\n    ')
            # SOURCE LINE 46
            __M_writer(conditional_websafe(thing.public_description_usertext))
            __M_writer(u'\n  </div>\n')
        # SOURCE LINE 49
        __M_writer(u'<p class="tagline">\n  ')
        # SOURCE LINE 50
        __M_writer(conditional_websafe(self.tagline()))
        __M_writer(u'\n</p>\n<ul class="flat-list buttons">\n  ')
        # SOURCE LINE 53
        __M_writer(conditional_websafe(self.buttons()))
        __M_writer(u'\n</ul>\n<div class="reportform report-')
        # SOURCE LINE 55
        __M_writer(conditional_websafe(thing._fullname))
        __M_writer(u'"></div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


