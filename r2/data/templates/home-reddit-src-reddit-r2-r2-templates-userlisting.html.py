# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505799503.843174
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/userlisting.html'
_template_uri = '/userlisting.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['add_form', 'listing']


# SOURCE LINE 23

from r2.config import feature
from r2.lib.template_helpers import format_html
 

def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 27
    ns = runtime.TemplateNamespace('__anon_0x7ff76fc13f50', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7ff76fc13f50')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7ff76fc13f50')._populate(_import_ns, [u'error_field', u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        def add_form(title,dest,add_type,container_name,verb=None,permissions_form=None):
            return render_add_form(context._locals(__M_locals),title,dest,add_type,container_name,verb,permissions_form)
        def listing():
            return render_listing(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 26
        __M_writer(u'\n')
        # SOURCE LINE 27
        __M_writer(u'\n\n')
        # SOURCE LINE 108
        __M_writer(u'\n\n')
        # SOURCE LINE 151
        __M_writer(u'\n\n<div class="')
        # SOURCE LINE 153
        __M_writer(conditional_websafe(thing._class))
        __M_writer(u' usertable">\n')
        # SOURCE LINE 154
        if thing.addable and thing.has_add_form:
            # SOURCE LINE 155
            __M_writer(u'    ')
            __M_writer(conditional_websafe(add_form(thing.form_title, thing.destination, thing.type, thing.container_name, permissions_form=thing.permissions_form)))
            __M_writer(u'\n')
        # SOURCE LINE 157
        __M_writer(u'\n')
        # SOURCE LINE 158
        if thing.show_jump_to:
            # SOURCE LINE 159
            __M_writer(u'    <h1>')
            __M_writer(conditional_websafe(_('jump to')))
            __M_writer(u'</h1>\n    <form class="pretty-form medium-text">\n        <label for="user">')
            # SOURCE LINE 161
            __M_writer(conditional_websafe(_('username')))
            __M_writer(u'&nbsp;</label>\n        <input type="text" id="user" name="user"\n')
            # SOURCE LINE 163
            if thing.jump_to_value:
                # SOURCE LINE 164
                __M_writer(u'            value="')
                __M_writer(conditional_websafe(thing.jump_to_value))
                __M_writer(u'"\n')
            # SOURCE LINE 166
            __M_writer(u'        >\n        <button type="submit">')
            # SOURCE LINE 167
            __M_writer(conditional_websafe(_('go')))
            __M_writer(u'</button>\n    </form>\n')
        # SOURCE LINE 170
        __M_writer(u'\n')
        # SOURCE LINE 171
        __M_writer(conditional_websafe(listing()))
        __M_writer(u'\n\n')
        # SOURCE LINE 173
        if thing.jump_to_value:
            # SOURCE LINE 174
            __M_writer(u'    <p class="nextprev">\n        ')
            # SOURCE LINE 175
            __M_writer(conditional_websafe(plain_link(_("show all"), request.path, rel="nofollow")))
            __M_writer(u'\n    </p>\n')
        # SOURCE LINE 178
        __M_writer(u'\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_add_form(context,title,dest,add_type,container_name,verb=None,permissions_form=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7ff76fc13f50')._populate(_import_ns, [u'error_field', u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        caller = _import_ns.get('caller', context.get('caller', UNDEFINED))
        error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 29
        __M_writer(u'\n  <form action="/post/')
        # SOURCE LINE 30
        __M_writer(conditional_websafe(dest))
        __M_writer(u'"\n        method="post" class="pretty-form medium-text friend-add"\n        onsubmit="return post_form(this, \'')
        # SOURCE LINE 32
        __M_writer(conditional_websafe(dest))
        __M_writer(u'\')"\n        id="')
        # SOURCE LINE 33
        __M_writer(conditional_websafe(add_type))
        __M_writer(u'">\n    <h1>')
        # SOURCE LINE 34
        __M_writer(conditional_websafe(title))
        __M_writer(u'</h1>\n\n    <input type="hidden" name="action" value="add">\n    <input type="hidden" name="container" value="')
        # SOURCE LINE 37
        __M_writer(conditional_websafe(container_name))
        __M_writer(u'">\n    <input type="hidden" name="type" value="')
        # SOURCE LINE 38
        __M_writer(conditional_websafe(add_type))
        __M_writer(u'">\n')
        # SOURCE LINE 39
        if add_type in ("banned", "wikibanned"):
            # SOURCE LINE 40
            __M_writer(u'        <label for="name">')
            __M_writer(conditional_websafe(_('who to ban?')))
            __M_writer(u' &nbsp;</label>\n        <input type="text" class="friend-name" name="name" id="name">\n        <div>\n')
            # SOURCE LINE 43
            if feature.is_enabled("subreddit_rules", subreddit=c.site.name):
                # SOURCE LINE 44
                __M_writer(u'          <label for="ban_reason">')
                __M_writer(conditional_websafe(_("reason")))
                __M_writer(u'</label>\n          <select name="ban_reason">\n')
                # SOURCE LINE 46
                if thing.rules:
                    # SOURCE LINE 47
                    __M_writer(u'              <optgroup label="Subreddit Rules">\n')
                    # SOURCE LINE 48
                    for rule in thing.rules:
                        # SOURCE LINE 49
                        __M_writer(u'                  <option value="')
                        __M_writer(conditional_websafe(rule['short_name']))
                        __M_writer(u'">')
                        __M_writer(conditional_websafe(rule['short_name']))
                        __M_writer(u'</option>\n')
                    # SOURCE LINE 51
                    __M_writer(u'              </optgroup>\n')
                # SOURCE LINE 53
                __M_writer(u'            <optgroup label="Site Rules">\n')
                # SOURCE LINE 54
                for rule in thing.system_rules:
                    # SOURCE LINE 55
                    __M_writer(u'                <option value="')
                    __M_writer(conditional_websafe(rule))
                    __M_writer(u'">')
                    __M_writer(conditional_websafe(rule))
                    __M_writer(u'</option>\n')
                # SOURCE LINE 57
                __M_writer(u'            </optgroup>\n            <option value="other">')
                # SOURCE LINE 58
                __M_writer(conditional_websafe(_("Other")))
                __M_writer(u'</option>\n          </select>\n')
            # SOURCE LINE 61
            __M_writer(u'          <div>\n            <label for="note">')
            # SOURCE LINE 62
            __M_writer(conditional_websafe(_("mod note")))
            __M_writer(u'\n            <input type="text" maxlength="300" name="note" id="note">\n            <span>')
            # SOURCE LINE 64
            __M_writer(conditional_websafe(_('(will not be visible to user)')))
            __M_writer(u'</span>\n          </div>\n        </div>\n        <div>\n            <label for="duration">')
            # SOURCE LINE 68
            __M_writer(conditional_websafe(_('how long?')))
            __M_writer(u'</label>\n            <input type="number" min="1" max="999" name="duration" id="duration">\n            <span>')
            # SOURCE LINE 70
            __M_writer(conditional_websafe(_('days (leave blank for permanent)')))
            __M_writer(u'</span>\n        </div>\n')
            # SOURCE LINE 72
        elif add_type == "muted":
            # SOURCE LINE 73
            __M_writer(u'        <label for="name">')
            __M_writer(conditional_websafe(_('who to mute?')))
            __M_writer(u' &nbsp;</label>\n        <input type="text" class="friend-name" name="name" id="name">\n        <div>\n            <label for="note">')
            # SOURCE LINE 76
            __M_writer(conditional_websafe(_('why the mute?')))
            __M_writer(u'</label>\n            <input type="text" maxlength="300" name="note" id="note">\n            <span>')
            # SOURCE LINE 78
            __M_writer(conditional_websafe(_('(will not be visible to user)')))
            __M_writer(u'</span>\n        </div>\n')
            # SOURCE LINE 80
        else:
            # SOURCE LINE 81
            __M_writer(u'        <input type="text" name="name" id="name">\n')
        # SOURCE LINE 83
        if add_type == "banned":
            # SOURCE LINE 84
            __M_writer(u'      <div>\n          <label for="note">')
            # SOURCE LINE 85
            __M_writer(conditional_websafe(_('note to include in ban PM')))
            __M_writer(u'</label>\n          <textarea name="ban_message" id="ban_message"></textarea>\n      </div>\n')
        # SOURCE LINE 89
        if permissions_form:
            # SOURCE LINE 90
            __M_writer(u'      ')
            __M_writer(conditional_websafe(permissions_form))
            __M_writer(u'\n      &#32;\n      <span class="permissions-edit">\n        (<a href="javascript:void(0)">')
            # SOURCE LINE 93
            __M_writer(conditional_websafe(_('change')))
            __M_writer(u'</a>)\n      </span>\n')
        # SOURCE LINE 96
        __M_writer(u'    <button class="btn" type="submit">')
        __M_writer(conditional_websafe(verb or _("add")))
        __M_writer(u'</button>\n    <span class="status"></span>\n    ')
        # SOURCE LINE 98
        __M_writer(conditional_websafe(error_field("NO_USER", "name")))
        __M_writer(u'\n    ')
        # SOURCE LINE 99
        __M_writer(conditional_websafe(error_field("USER_DOESNT_EXIST", "name")))
        __M_writer(u'\n    ')
        # SOURCE LINE 100
        __M_writer(conditional_websafe(error_field("ALREADY_MODERATOR", "name")))
        __M_writer(u'\n    ')
        # SOURCE LINE 101
        __M_writer(conditional_websafe(error_field("CANT_RESTRICT_MODERATOR", "name")))
        __M_writer(u'\n    ')
        # SOURCE LINE 102
        __M_writer(conditional_websafe(error_field("BANNED_FROM_SUBREDDIT", "name")))
        __M_writer(u'\n    ')
        # SOURCE LINE 103
        __M_writer(conditional_websafe(error_field("MUTED_FROM_SUBREDDIT", "name")))
        __M_writer(u'\n')
        # SOURCE LINE 104
        if caller:
            # SOURCE LINE 105
            __M_writer(u'      ')
            __M_writer(conditional_websafe(caller.body()))
            __M_writer(u'\n')
        # SOURCE LINE 107
        __M_writer(u'  </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_listing(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7ff76fc13f50')._populate(_import_ns, [u'error_field', u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 110
        __M_writer(u'\n  <div class="')
        # SOURCE LINE 111
        __M_writer(conditional_websafe(thing.type))
        __M_writer(u'-table"\n    style="')
        # SOURCE LINE 112
        __M_writer(conditional_websafe('display:none' if not thing.things and not thing.show_not_found else ''))
        __M_writer(u'">\n    <h1>\n      ')
        # SOURCE LINE 114
        __M_writer(conditional_websafe(thing.title))
        __M_writer(u'\n    </h1>\n\n    <table>\n')
        # SOURCE LINE 118
        if thing.headers:
            # SOURCE LINE 119
            __M_writer(u'        <tr>\n')
            # SOURCE LINE 120
            for header in thing.headers:
                # SOURCE LINE 121
                __M_writer(u'            <th>')
                __M_writer(conditional_websafe(header))
                __M_writer(u'</th>\n')
            # SOURCE LINE 123
            __M_writer(u'        </tr>\n')
        # SOURCE LINE 125
        if thing.things:
            # SOURCE LINE 126
            for item in thing.things:
                # SOURCE LINE 127
                __M_writer(u'                ')
                __M_writer(conditional_websafe(item))
                __M_writer(u'\n')
            # SOURCE LINE 129
        else:
            # SOURCE LINE 130
            __M_writer(u'        <tr class="notfound"><td>')
            __M_writer(conditional_websafe(_('No items found') if thing.show_not_found else ''))
            __M_writer(u'</td></tr>\n')
        # SOURCE LINE 132
        __M_writer(u'    </table>\n  </div>\n\n')
        # SOURCE LINE 135
        if thing.nextprev and (thing.prev or thing.next):
            # SOURCE LINE 136
            __M_writer(u'  <p class="nextprev"> ')
            __M_writer(conditional_websafe(_("view more:")))
            __M_writer(u'&#32;\n')
            # SOURCE LINE 137
            if thing.prev:
                # SOURCE LINE 138
                __M_writer(u'    ')
                __M_writer(conditional_websafe(plain_link(_("first"), thing.first, rel="nofollow first")))
                __M_writer(u' \n    <span class="separator"></span>\n    ')
                # SOURCE LINE 140
                __M_writer(conditional_websafe(plain_link(format_html("&lsaquo; %s", _("prev")), thing.prev, rel="nofollow prev")))
                __M_writer(u'\n')
            # SOURCE LINE 142
            if thing.prev and thing.next:
                # SOURCE LINE 143
                __M_writer(u'    <span class="separator"></span>\n')
            # SOURCE LINE 145
            if thing.next:
                # SOURCE LINE 146
                __M_writer(u'  ')
                __M_writer(conditional_websafe(plain_link(format_html("%s &rsaquo;", _("next")), thing.next, rel="nofollow next")))
                __M_writer(u'\n')
            # SOURCE LINE 148
            __M_writer(u'  </p>\n')
        # SOURCE LINE 150
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


