# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505842325.839844
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/modlisting.html'
_template_uri = '/modlisting.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7fe407a38ed0', context._clean_inheritance_tokens(), templateuri=u'printablebuttons.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fe407a38ed0')] = ns

    # SOURCE LINE 25
    ns = runtime.TemplateNamespace('__anon_0x7fe407a9b350', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fe407a9b350')] = ns

    # SOURCE LINE 24
    ns = runtime.TemplateNamespace('__anon_0x7fe407a9ba10', context._clean_inheritance_tokens(), templateuri=u'userlisting.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fe407a9ba10')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fe407a38ed0')._populate(_import_ns, [u'ynbutton'])
        _mako_get_namespace(context, '__anon_0x7fe407a9b350')._populate(_import_ns, [u'error_field'])
        _mako_get_namespace(context, '__anon_0x7fe407a9ba10')._populate(_import_ns, [u'add_form', u'listing'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        ynbutton = _import_ns.get('ynbutton', context.get('ynbutton', UNDEFINED))
        add_form = _import_ns.get('add_form', context.get('add_form', UNDEFINED))
        listing = _import_ns.get('listing', context.get('listing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n')
        # SOURCE LINE 24
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'\n\n<div class="')
        # SOURCE LINE 27
        __M_writer(conditional_websafe(thing._class))
        __M_writer(u' usertable">\n')
        # SOURCE LINE 28
        if thing.can_remove_self:
            # SOURCE LINE 29
            __M_writer(u'      ')
            __M_writer(conditional_websafe(ynbutton(op='unfriend',
                 title=_("leave"),
                 executed=_("you are no longer a moderator"),
                 question=_("stop being a moderator?"),
                 format=_('you are a moderator of this sub. %(action)s'),
                 format_arg='action',
                 _class=thing.type + ' remove-self',
                 hidden_data=dict(
                   id=c.user._fullname,
                   type=thing.type,
                   container=thing.container_name),
                 access_required=False)))
            # SOURCE LINE 40
            __M_writer(u'\n')
        # SOURCE LINE 42
        __M_writer(u'\n')
        # SOURCE LINE 43
        if thing.has_invite:
            # SOURCE LINE 44
            __M_writer(u'    ')
            __M_writer(conditional_websafe(ynbutton(op='accept_moderator_invite',
               title=_("accept"),
               executed=_("you are now a moderator. welcome to the team!"),
               question=_("become a moderator of %s?" % ("/r/" + c.site.name)),
               format=_('you are invited to become a moderator. %(action)s'),
               format_arg='action',
               _class=thing.type + ' accept-invite',
               access_required=False)))
            # SOURCE LINE 51
            __M_writer(u'\n')
        # SOURCE LINE 53
        __M_writer(u'\n')
        # SOURCE LINE 54
        if thing.addable and thing.has_add_form:
            # SOURCE LINE 55
            __M_writer(u'    ')
            def ccall(caller):
                def body():
                    error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
                    __M_writer = context.writer()
                    __M_writer(u'\n      ')
                    # SOURCE LINE 56
                    __M_writer(conditional_websafe(error_field("ALREADY_MODERATOR", "name")))
                    __M_writer(u'\n      ')
                    # SOURCE LINE 57
                    __M_writer(conditional_websafe(error_field("BANNED_FROM_SUBREDDIT", "name")))
                    __M_writer(u'\n      ')
                    # SOURCE LINE 58
                    __M_writer(conditional_websafe(error_field("MUTED_FROM_SUBREDDIT", "name")))
                    __M_writer(u'\n    ')
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 55
                __M_writer(conditional_websafe(add_form(thing.form_title, thing.destination, thing.type, thing.container_name, verb=_('add'))))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 59
            __M_writer(u'\n')
        # SOURCE LINE 61
        __M_writer(u'  ')
        __M_writer(conditional_websafe(listing()))
        __M_writer(u'\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


