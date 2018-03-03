# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1509497068.280538
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/quarantineinterstitial.html'
_template_uri = '/quarantineinterstitial.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['interstitial_image_attrs', 'interstitial_message', 'interstitial_title', 'interstitial_buttons']


# SOURCE LINE 23

from r2.lib.template_helpers import static 


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 28
    ns = runtime.TemplateNamespace(u'utils', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'utils')] = ns

    # SOURCE LINE 27
    ns = runtime.TemplateNamespace('__anon_0x7fddd0a2ced0', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fddd0a2ced0')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'interstitial.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fddd0a2ced0')._populate(_import_ns, [u'submit_form', u'_md', u'_mdf'])
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'\n\n')
        # SOURCE LINE 27
        __M_writer(u'\n')
        # SOURCE LINE 28
        __M_writer(u'\n\n')
        # SOURCE LINE 30
        __M_writer(u'\n\n')
        # SOURCE LINE 35
        __M_writer(u'\n\n')
        # SOURCE LINE 45
        __M_writer(u'\n\n')
        # SOURCE LINE 59
        __M_writer(u'\n\n')
        # SOURCE LINE 78
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_interstitial_image_attrs(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fddd0a2ced0')._populate(_import_ns, [u'submit_form', u'_md', u'_mdf'])
        __M_writer = context.writer()
        # SOURCE LINE 32
        __M_writer(u'\n  src="')
        # SOURCE LINE 33
        __M_writer(conditional_websafe(static('interstitial-image-quarantine.png')))
        __M_writer(u'"\n  alt="')
        # SOURCE LINE 34
        __M_writer(conditional_websafe(_('quarantined')))
        __M_writer(u'"\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_interstitial_message(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fddd0a2ced0')._populate(_import_ns, [u'submit_form', u'_md', u'_mdf'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        _mdf = _import_ns.get('_mdf', context.get('_mdf', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 47
        __M_writer(u'\n  <p>\n    ')
        # SOURCE LINE 49

        quarantine_link = 'https://reddit.zendesk.com/hc/en-us/articles/205701245'
            
        
        # SOURCE LINE 51
        __M_writer(u'\n\n')
        # SOURCE LINE 53
        if thing.can_opt_in:
            # SOURCE LINE 54
            __M_writer(u'      ')
            __M_writer(conditional_websafe(_mdf("Communities that are dedicated to shocking or highly offensive content are [quarantined](%(link)s). Content in this community may be upsetting. Are you certain you want to continue?", link=quarantine_link)))
            __M_writer(u'\n')
            # SOURCE LINE 55
        else:
            # SOURCE LINE 56
            __M_writer(u'      ')
            __M_writer(conditional_websafe(_mdf("Communities that are dedicated to shocking or highly offensive content are [quarantined](%(link)s).", link=quarantine_link)))
            __M_writer(u'\n')
        # SOURCE LINE 58
        __M_writer(u'  </p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_interstitial_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fddd0a2ced0')._populate(_import_ns, [u'submit_form', u'_md', u'_mdf'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        _md = _import_ns.get('_md', context.get('_md', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 37
        __M_writer(u'\n')
        # SOURCE LINE 38
        if thing.can_opt_in:
            # SOURCE LINE 39
            __M_writer(u'    ')
            __M_writer(conditional_websafe(_("Are you sure you want to view this community?")))
            __M_writer(u'\n')
            # SOURCE LINE 40
        elif thing.logged_in:
            # SOURCE LINE 41
            __M_writer(u'    ')
            __M_writer(conditional_websafe(_md("You must have a [verified email](/prefs/update) to view this community")))
            __M_writer(u'\n')
            # SOURCE LINE 42
        else:
            # SOURCE LINE 43
            __M_writer(u'    ')
            __M_writer(conditional_websafe(_("You must log in and have a verified email to view this community")))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_interstitial_buttons(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fddd0a2ced0')._populate(_import_ns, [u'submit_form', u'_md', u'_mdf'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        utils = _mako_get_namespace(context, 'utils')
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 61
        __M_writer(u'\n')
        # SOURCE LINE 62
        if thing.can_opt_in:
            # SOURCE LINE 63
            __M_writer(u'    ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    __M_writer(u'\n      <input type="hidden" name="sr_name" value="')
                    # SOURCE LINE 64
                    __M_writer(conditional_websafe(thing.sr_name))
                    __M_writer(u'" />\n\n      <div class="buttons">\n        <button class="c-btn c-btn-primary" type="submit" name="accept" value="no">\n          ')
                    # SOURCE LINE 68
                    __M_writer(conditional_websafe(_("no thank you")))
                    __M_writer(u'\n        </button>\n        <button class="c-btn c-btn-primary" type="submit" name="accept" value="yes">\n          ')
                    # SOURCE LINE 71
                    __M_writer(conditional_websafe(_("continue")))
                    __M_writer(u'\n        </button>\n      </div>\n    ')
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 63
                __M_writer(conditional_websafe(utils.submit_form(_class=u'pretty-form')))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 74
            __M_writer(u'\n')
            # SOURCE LINE 75
        else:
            # SOURCE LINE 76
            __M_writer(u'    ')
            __M_writer(conditional_websafe(parent.interstitial_buttons()))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


