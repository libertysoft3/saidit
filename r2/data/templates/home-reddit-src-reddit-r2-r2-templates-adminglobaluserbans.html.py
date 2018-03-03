# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1515317871.958855
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/adminglobaluserbans.html'
_template_uri = '/adminglobaluserbans.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['globalbannew', 'globalbanedit']


# SOURCE LINE 1

from r2.lib.template_helpers import display_link_karma


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 4
    ns = runtime.TemplateNamespace('__anon_0x7f514c768650', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f514c768650')] = ns

    # SOURCE LINE 5
    ns = runtime.TemplateNamespace('__anon_0x7f514c768a50', context._clean_inheritance_tokens(), templateuri=u'printablebuttons.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f514c768a50')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f514c768650')._populate(_import_ns, [u'error_field', u'thing_timestamp', u'plain_link'])
        _mako_get_namespace(context, '__anon_0x7f514c768a50')._populate(_import_ns, [u'ynbutton'])
        thing_timestamp = _import_ns.get('thing_timestamp', context.get('thing_timestamp', UNDEFINED))
        def globalbanedit(formid,recipient='',notes=''):
            return render_globalbanedit(context._locals(__M_locals),formid,recipient,notes)
        ynbutton = _import_ns.get('ynbutton', context.get('ynbutton', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        def globalbannew():
            return render_globalbannew(context._locals(__M_locals))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(u'\n')
        # SOURCE LINE 5
        __M_writer(u'\n\n')
        # SOURCE LINE 37
        __M_writer(u'\n\n')
        # SOURCE LINE 51
        __M_writer(u'\n\n<h1>global bans</h1>\n<a href="#" onclick="$(\'#addglobalban\').toggle(); return false;">add ban</a>\n')
        # SOURCE LINE 55
        __M_writer(conditional_websafe(globalbannew()))
        __M_writer(u'\n<br/>\n<br/>\n\n<div class="usertable global-bans">\n  <table>\n   <tbody>\n')
        # SOURCE LINE 62
        for ban in thing.bans:
            # SOURCE LINE 63
            __M_writer(u'     <tr>\n       <td><span class="user">')
            # SOURCE LINE 64
            __M_writer(conditional_websafe(plain_link(thing.accounts[ban.user_id].name, "/user/%s/" % thing.accounts[ban.user_id].name, _sr_path=False)))
            __M_writer(u' &nbsp;(<b>')
            __M_writer(conditional_websafe(display_link_karma(thing.accounts[ban.user_id].link_karma)))
            __M_writer(u'</b>)</span></td>\n       <td>')
            # SOURCE LINE 65
            __M_writer(conditional_websafe(thing_timestamp(ban)))
            __M_writer(u' &nbsp;ago</td>\n       <td>\n          <a href="')
            # SOURCE LINE 67
            __M_writer(conditional_websafe('/message/compose/?to=%s' % thing.accounts[ban.user_id].name))
            __M_writer(u'"\n            class="access-required"\n            data-type="account"\n            data-fullname="')
            # SOURCE LINE 70
            __M_writer(conditional_websafe(thing.accounts[ban.user_id]._fullname))
            __M_writer(u'"\n            data-event-action="compose">\n            ')
            # SOURCE LINE 72
            __M_writer(conditional_websafe(_("send message")))
            __M_writer(u'\n          </a>\n       </td>\n       <td>\n         ')
            # SOURCE LINE 76
            __M_writer(conditional_websafe(ynbutton(op='deleteglobalban',
                 title=_("remove"),
                 executed=_('global ban removed, <a href="#" onclick="location.reload();">reload</a> to see changes'),
                 hidden_data=dict(globalban_id=ban._fullname),
                 question=_("remove global ban?"),
                 access_required=False)))
            # SOURCE LINE 81
            __M_writer(u'\n       </td>\n       <td><a href="#" onclick="$(\'#globalbanedit-')
            # SOURCE LINE 83
            __M_writer(conditional_websafe(ban._fullname))
            __M_writer(u'\').toggle(); return false;">edit</a></td>\n       <td>\n         ')
            # SOURCE LINE 85
            __M_writer(conditional_websafe(ban.notes))
            __M_writer(u'\n         ')
            # SOURCE LINE 86
            __M_writer(conditional_websafe(globalbanedit(ban._fullname, thing.accounts[ban.user_id].name, ban.notes)))
            __M_writer(u'\n       </td>\n     </tr>\n')
        # SOURCE LINE 90
        __M_writer(u'   </tbody>\n  </table>\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_globalbannew(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f514c768650')._populate(_import_ns, [u'error_field', u'thing_timestamp', u'plain_link'])
        _mako_get_namespace(context, '__anon_0x7f514c768a50')._populate(_import_ns, [u'ynbutton'])
        error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 7
        __M_writer(u'\n <form action="/post/editglobalban" method="post" class="pretty-form medium-text"\n       style="display:none" onsubmit="return post_form(this, \'editglobalban\');" id="addglobalban">\n  \n  <input type="hidden" name="fullname" value="NEW" />\n  \n  <table class="off-lined-table borderless">\n    <tr>\n      <td><label for="recipient">who to ban?</label></td>\n      <td>\n          <input type="text" name="recipient" id="recipient" required="required" />\n          ')
        # SOURCE LINE 18
        __M_writer(conditional_websafe(error_field("NO_TEXT", "recipient", "span")))
        __M_writer(u'\n          ')
        # SOURCE LINE 19
        __M_writer(conditional_websafe(error_field("INVALID_OPTION", "recipient", "span")))
        __M_writer(u'\n          ')
        # SOURCE LINE 20
        __M_writer(conditional_websafe(error_field("USER_DOESNT_EXIST", "recipient", "span")))
        __M_writer(u'\n      </td>\n    </tr>\n    <tr>\n      <td><label for="notes">admin note</label></td>\n      <td>\n        <input type="text" name="notes" id="notes" value="" />\n        (will not be visible to user)\n        ')
        # SOURCE LINE 28
        __M_writer(conditional_websafe(error_field("NO_TEXT", "notes", "span")))
        __M_writer(u'\n      </td>\n    </tr>\n  </table>\n  <button class="btn" type="submit">add</button>\n  <button class="btn" onclick="$(this).closest(\'form\').hide(); return false;">cancel</button>\n  <span class="status"></span>\n  <br/>\n </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_globalbanedit(context,formid,recipient='',notes=''):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f514c768650')._populate(_import_ns, [u'error_field', u'thing_timestamp', u'plain_link'])
        _mako_get_namespace(context, '__anon_0x7f514c768a50')._populate(_import_ns, [u'ynbutton'])
        error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 39
        __M_writer(u'\n <form action="/post/editglobalban" method="post" class="pretty-form medium-text"\n       style="display:none" onsubmit="return post_form(this, \'editglobalban\');" id="globalbanedit-')
        # SOURCE LINE 41
        __M_writer(conditional_websafe(formid))
        __M_writer(u'">\n  \n  <input type="hidden" name="fullname" value="')
        # SOURCE LINE 43
        __M_writer(conditional_websafe(formid))
        __M_writer(u'" />\n  <input type="hidden" name="recipient" value="')
        # SOURCE LINE 44
        __M_writer(conditional_websafe(recipient))
        __M_writer(u'" />\n\n  <input type="text" name="notes" id="notes" value="')
        # SOURCE LINE 46
        __M_writer(conditional_websafe(notes))
        __M_writer(u'" />\n        ')
        # SOURCE LINE 47
        __M_writer(conditional_websafe(error_field("NO_TEXT", "notes", "span")))
        __M_writer(u'\n  <button class="btn" type="submit">update</button>\n  <span class="status"></span>\n </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


