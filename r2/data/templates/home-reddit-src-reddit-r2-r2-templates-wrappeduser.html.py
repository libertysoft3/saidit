# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505003062.386668
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/wrappeduser.html'
_template_uri = '/wrappeduser.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['make_distinguish', 'flair']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7f36094246d0', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f36094246d0')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f36094246d0')._populate(_import_ns, [u'plain_link'])
        def make_distinguish(distinguish_tuples):
            return render_make_distinguish(context._locals(__M_locals),distinguish_tuples)
        target = _import_ns.get('target', context.get('target', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        context_deleted = _import_ns.get('context_deleted', context.get('context_deleted', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        def flair(user,enabled=None):
            return render_flair(context._locals(__M_locals),user,enabled)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n')
        # SOURCE LINE 32
        __M_writer(u'\n\n')
        # SOURCE LINE 59
        __M_writer(u'\n\n')
        # SOURCE LINE 61
        if context_deleted and not c.user_is_admin:
            # SOURCE LINE 62
            __M_writer(u'  <span class="author">[deleted]</span>\n')
            # SOURCE LINE 63
        else:
            # SOURCE LINE 64
            if thing.user_deleted:
                # SOURCE LINE 65
                __M_writer(u'    <span class="author">[deleted]</span>\n')
                # SOURCE LINE 66
            elif thing.name == '[blocked]':
                # SOURCE LINE 67
                __M_writer(u'    <span class="author">')
                __M_writer(conditional_websafe(_(thing.thing.original_author.name)))
                __M_writer(u'</span>\n')
                # SOURCE LINE 68
            else:
                # SOURCE LINE 69
                if thing.flair_position == 'left':
                    # SOURCE LINE 70
                    __M_writer(u'      ')
                    __M_writer(conditional_websafe(flair(thing, enabled=thing.force_show_flair)))
                    __M_writer(u'\n')
                # SOURCE LINE 72
                __M_writer(u'    ')

                classes = [thing.author_cls, 'may-blank', 'id-%s' % thing.fullname]
                if thing.include_flair_selector:
                    classes.append('flairselectable')
                    
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['classes'] if __M_key in __M_locals_builtin_stored]))
                # SOURCE LINE 76
                __M_writer(u'\n    ')
                # SOURCE LINE 77
                __M_writer(conditional_websafe(plain_link(thing.name + thing.karma, "/user/%s" % thing.name,
                 _class = ' '.join(classes),
                 _sr_path = False, target=target, title=thing.author_title)))
                # SOURCE LINE 79
                __M_writer(u'\n')
                # SOURCE LINE 80
                if thing.flair_position == 'right':
                    # SOURCE LINE 81
                    __M_writer(u'      ')
                    __M_writer(conditional_websafe(flair(thing, enabled=thing.force_show_flair)))
                    __M_writer(u'\n')
                # SOURCE LINE 83
                if thing.include_flair_selector:
                    # SOURCE LINE 84
                    __M_writer(u'      (<a class="flairselectbtn access-required"\n          data-name="')
                    # SOURCE LINE 85
                    __M_writer(conditional_websafe(thing.name))
                    __M_writer(u'"\n          data-type="account" data-fullname="')
                    # SOURCE LINE 86
                    __M_writer(conditional_websafe(thing.fullname))
                    __M_writer(u'"\n          data-event-action="editflair" data-event-detail="set"\n          href="javascript://void(0)">')
                    # SOURCE LINE 88
                    __M_writer(conditional_websafe(_('edit')))
                    __M_writer(u'</a>)\n      <div class="flairselector drop-choices"></div>\n')
                # SOURCE LINE 91
                __M_writer(u'    ')
                __M_writer(conditional_websafe(make_distinguish(thing.attribs)))
                __M_writer(u'\n')
        # SOURCE LINE 94
        __M_writer(u'\n')
        # SOURCE LINE 95
        if thing.ip_span:
            # SOURCE LINE 96
            __M_writer(u'  ')
            __M_writer(conditional_websafe(unsafe(thing.ip_span)))
            __M_writer(u'\n')
        # SOURCE LINE 98
        __M_writer(u'\n')
        # SOURCE LINE 99
        if thing.show_details_link and thing.context_thing_fullname:
            # SOURCE LINE 100
            __M_writer(u'  &#32;\n  <a class="adminbox" href="/details/')
            # SOURCE LINE 101
            __M_writer(conditional_websafe(thing.context_thing_fullname))
            __M_writer(u'">voting</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_make_distinguish(context,distinguish_tuples):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f36094246d0')._populate(_import_ns, [u'plain_link'])
        target = _import_ns.get('target', context.get('target', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 34
        __M_writer(u'\n<span class="userattrs">\n')
        # SOURCE LINE 36
        if distinguish_tuples:
            # SOURCE LINE 37
            __M_writer(u'  [\n')
            # SOURCE LINE 38
            for priority, abbv, css_class, label, attr_link in distinguish_tuples:
                # SOURCE LINE 39
                if attr_link:
                    # SOURCE LINE 40
                    __M_writer(u'      <a class="')
                    __M_writer(conditional_websafe(css_class))
                    __M_writer(u'" title="')
                    __M_writer(conditional_websafe(label))
                    __M_writer(u'"\n')
                    # SOURCE LINE 41
                    if target:
                        # SOURCE LINE 42
                        __M_writer(u'         target="')
                        __M_writer(conditional_websafe(target))
                        __M_writer(u'"\n')
                    # SOURCE LINE 44
                    __M_writer(u'         href="')
                    __M_writer(conditional_websafe(attr_link))
                    __M_writer(u'">\n        ')
                    # SOURCE LINE 45
                    __M_writer(conditional_websafe(unsafe(abbv)))
                    __M_writer(u'\n      </a>\n')
                    # SOURCE LINE 47
                else:
                    # SOURCE LINE 48
                    __M_writer(u'      <span class="')
                    __M_writer(conditional_websafe(css_class))
                    __M_writer(u'" title="')
                    __M_writer(conditional_websafe(label))
                    __M_writer(u'">')
                    __M_writer(conditional_websafe(abbv))
                    __M_writer(u'</span>\n')
                # SOURCE LINE 50
                __M_writer(u'\n')
                # SOURCE LINE 52
                if priority != distinguish_tuples[-1][0]:
                    # SOURCE LINE 53
                    __M_writer(u'      ,\n')
            # SOURCE LINE 56
            __M_writer(u'  ]\n')
        # SOURCE LINE 58
        __M_writer(u'</span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_flair(context,user,enabled=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f36094246d0')._populate(_import_ns, [u'plain_link'])
        __M_writer = context.writer()
        # SOURCE LINE 25
        __M_writer(u'\n')
        # SOURCE LINE 26
        if enabled is None:
            # SOURCE LINE 27
            __M_writer(u'    ')
            enabled = user.flair_enabled 
            
            __M_writer(u'\n')
        # SOURCE LINE 29
        if user.has_flair and enabled:
            # SOURCE LINE 30
            __M_writer(u'    <span class="flair ')
            __M_writer(conditional_websafe(user.flair_css_class))
            __M_writer(u'" title="')
            __M_writer(conditional_websafe(user.flair_text))
            __M_writer(u'">')
            __M_writer(conditional_websafe(user.flair_text))
            __M_writer(u'</span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


