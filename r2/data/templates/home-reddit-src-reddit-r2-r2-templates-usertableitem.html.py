# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505842325.860975
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/usertableitem.html'
_template_uri = '/usertableitem.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['usertablecell']


# SOURCE LINE 23

from r2.lib.template_helpers import display_link_karma


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 27
    ns = runtime.TemplateNamespace('__anon_0x7fe407a0f950', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fe407a0f950')] = ns

    # SOURCE LINE 26
    ns = runtime.TemplateNamespace('__anon_0x7fe407a0fa50', context._clean_inheritance_tokens(), templateuri=u'printablebuttons.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fe407a0fa50')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fe407a0f950')._populate(_import_ns, [u'plain_link', u'timestamp'])
        _mako_get_namespace(context, '__anon_0x7fe407a0fa50')._populate(_import_ns, [u'ynbutton'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        def usertablecell(cell_type):
            return render_usertablecell(context._locals(__M_locals),cell_type)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'\n')
        # SOURCE LINE 26
        __M_writer(u'\n')
        # SOURCE LINE 27
        __M_writer(u'\n\n<tr class="')
        # SOURCE LINE 29
        __M_writer(conditional_websafe(thing.author_cls))
        __M_writer(u'">\n')
        # SOURCE LINE 30
        for cell_type in thing.cells:
            # SOURCE LINE 31
            __M_writer(u'    <td>\n      ')
            # SOURCE LINE 32
            __M_writer(conditional_websafe(usertablecell(cell_type)))
            __M_writer(u'\n    </td>\n')
        # SOURCE LINE 35
        __M_writer(u'</tr>\n\n')
        # SOURCE LINE 105
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_usertablecell(context,cell_type):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fe407a0f950')._populate(_import_ns, [u'plain_link', u'timestamp'])
        _mako_get_namespace(context, '__anon_0x7fe407a0fa50')._populate(_import_ns, [u'ynbutton'])
        timestamp = _import_ns.get('timestamp', context.get('timestamp', UNDEFINED))
        ynbutton = _import_ns.get('ynbutton', context.get('ynbutton', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 37
        __M_writer(u'\n')
        # SOURCE LINE 38
        if cell_type == "user":
            # SOURCE LINE 39
            __M_writer(u'      <span class="user">\n         ')
            # SOURCE LINE 40
            __M_writer(conditional_websafe(plain_link(thing.user.name, "/user/%s/" % thing.user.name,
                      _sr_path=False)))
            # SOURCE LINE 41
            __M_writer(u'\n         &nbsp;(<b>')
            # SOURCE LINE 42
            __M_writer(conditional_websafe(display_link_karma(thing.user.link_karma)))
            __M_writer(u'</b>)\n      </span>\n      &nbsp;\n')
            # SOURCE LINE 45
        elif c.user_is_loggedin and cell_type == "sendmessage" and c.user != thing.user:
            # SOURCE LINE 46
            __M_writer(u'\n      <a href="')
            # SOURCE LINE 47
            __M_writer(conditional_websafe('/message/compose/?to=%s' % thing.user.name))
            __M_writer(u'" class="access-required"\n         data-type="account"\n         data-fullname="')
            # SOURCE LINE 49
            __M_writer(conditional_websafe(thing.user._fullname))
            __M_writer(u'"\n         data-event-action="compose">\n         ')
            # SOURCE LINE 51
            __M_writer(conditional_websafe(_("send message")))
            __M_writer(u'\n      </a>\n      &nbsp;\n')
            # SOURCE LINE 54
        elif cell_type == "remove":
            # SOURCE LINE 55
            if thing.editable:
                # SOURCE LINE 56
                __M_writer(u'      ')

                access_required = getattr(thing, 'remove_access_required', True)
                      
                
                # SOURCE LINE 58
                __M_writer(u'\n      ')
                # SOURCE LINE 59
                __M_writer(conditional_websafe(ynbutton(_("remove"), "removed", thing.remove_action,
                 callback="deleteRow",
                 hidden_data = dict(type = thing.type,
                                    id = thing.user._fullname,
                                    container = thing.container_name),
                 access_required=access_required)))
                # SOURCE LINE 64
                __M_writer(u'\n')
                # SOURCE LINE 65
            else:
                # SOURCE LINE 66
                if c.user != thing.user:
                    # SOURCE LINE 67
                    __M_writer(u'        <span class="gray">')
                    __M_writer(conditional_websafe(_("can't remove")))
                    __M_writer(u'</span>\n')
            # SOURCE LINE 70
        elif cell_type == "note":
            # SOURCE LINE 71
            __M_writer(u'    <form action="/post/')
            __M_writer(conditional_websafe(thing.type))
            __M_writer(u'note" id="')
            __M_writer(conditional_websafe(thing.type))
            __M_writer(u'note-')
            __M_writer(conditional_websafe(thing.rel._fullname))
            __M_writer(u'"\n          method="post" class="pretty-form medium-text rel-note ')
            # SOURCE LINE 72
            __M_writer(conditional_websafe(thing.type))
            __M_writer(u'-note"\n          onsubmit="return post_form(this, \'')
            # SOURCE LINE 73
            __M_writer(conditional_websafe(thing.type))
            __M_writer(u'note\');">\n      <input type="hidden" name="name" value="')
            # SOURCE LINE 74
            __M_writer(conditional_websafe(thing.user.name))
            __M_writer(u'" />\n      <input type="text" maxlength="300" name="note"\n             onchange="$(this).parent().addClass(\'edited\')"\n             value="')
            # SOURCE LINE 77
            __M_writer(conditional_websafe(getattr(thing.rel, 'note', '')))
            __M_writer(u'" />\n      <button onclick="$(this).parent().removeClass(\'edited\')" type="submit">\n        ')
            # SOURCE LINE 79
            __M_writer(conditional_websafe(_("submit")))
            __M_writer(u'\n      </button>\n    </form>\n')
            # SOURCE LINE 82
        elif cell_type == "age":
            # SOURCE LINE 83
            __M_writer(u'      ')
            __M_writer(conditional_websafe(timestamp(thing.rel._date, include_tense=True)))
            __M_writer(u'\n')
            # SOURCE LINE 84
        elif cell_type == "permissions":
            # SOURCE LINE 85
            __M_writer(u'      ')
            __M_writer(conditional_websafe(thing.permissions))
            __M_writer(u'\n')
            # SOURCE LINE 86
        elif cell_type == "permissionsctl":
            # SOURCE LINE 87
            if thing.editable:
                # SOURCE LINE 88
                __M_writer(u'      <span class="permissions-edit">\n        (<a class="access-required"\n            href="javascript:void(0)"\n            data-type="account"\n            data-fullname="')
                # SOURCE LINE 92
                __M_writer(conditional_websafe(thing.user._fullname))
                __M_writer(u'"\n            data-event-action="editsettings"\n            data-event-detail="set_permissions"\n            >')
                # SOURCE LINE 95
                __M_writer(conditional_websafe(_('change')))
                __M_writer(u'</a>)\n      </span>\n')
            # SOURCE LINE 98
        elif cell_type == "temp" and hasattr(thing, "tempban"):
            # SOURCE LINE 99
            __M_writer(u'    ')
            __M_writer(conditional_websafe(_('%(time)s days left') % dict(time=thing.tempban)))
            __M_writer(u'\n    ')
            # SOURCE LINE 100
            __M_writer(conditional_websafe(ynbutton(_('make permanent'), _("made permanent"), "friend",
        hidden_data = dict(type=thing.type,
                           name=thing.user.name,
                           container=thing.container_name))))
            # SOURCE LINE 103
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


