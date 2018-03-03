# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505144068.196378
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/newsletter.html'
_template_uri = '/newsletter.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['bodyContent', 'viewport', 'Title']


# SOURCE LINE 23

from r2.lib.template_helpers import make_url_https, static
from r2.models.admintools import wiki_template


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 27
    ns = runtime.TemplateNamespace('__anon_0x7fb219db5290', context._clean_inheritance_tokens(), templateuri=u'less.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fb219db5290')] = ns

    # SOURCE LINE 28
    ns = runtime.TemplateNamespace('__anon_0x7fb219db59d0', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fb219db59d0')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'reddit.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fb219db5290')._populate(_import_ns, [u'less_stylesheet'])
        _mako_get_namespace(context, '__anon_0x7fb219db59d0')._populate(_import_ns, [u'form_group', u'md'])
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 26
        __M_writer(u'\n')
        # SOURCE LINE 27
        __M_writer(u'\n')
        # SOURCE LINE 28
        __M_writer(u'\n\n')
        # SOURCE LINE 30
        __M_writer(u'\n\n')
        # SOURCE LINE 34
        __M_writer(u'\n\n')
        # SOURCE LINE 38
        __M_writer(u'\n\n')
        # SOURCE LINE 78
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bodyContent(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fb219db5290')._populate(_import_ns, [u'less_stylesheet'])
        _mako_get_namespace(context, '__anon_0x7fb219db59d0')._populate(_import_ns, [u'form_group', u'md'])
        md = _import_ns.get('md', context.get('md', UNDEFINED))
        form_group = _import_ns.get('form_group', context.get('form_group', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 40
        __M_writer(u'\n\n<section class="newsletter-box newsletter-container">\n  <header>\n    <h1 class="subscribe-callout">')
        # SOURCE LINE 44
        __M_writer(conditional_websafe(_("subscribe to reddit's official newsletter,")))
        __M_writer(u'&#32;<span class="upvoted-weekly-logo"><span class="screenreader-only">')
        __M_writer(conditional_websafe(_('upvoted weekly')))
        __M_writer(u'</span></span></h1>\n    <div class="subscribe-thanks"><img src="')
        # SOURCE LINE 45
        __M_writer(conditional_websafe(static('subscribe-header-thanks-black.svg')))
        __M_writer(u'" alt="_(\'thanks for subscribing\')" /></div>\n    <h2 class="result-message">\n      ')
        # SOURCE LINE 47
        __M_writer(conditional_websafe(_("Enter your email to get the very best of reddit's content curated, packaged, and delivered to your inbox once a week. It's free and we'll never spam you.")))
        __M_writer(u'\n    </h2>\n    <div class="subscribe-thanks"><a href="/" class="c-btn c-btn-primary">')
        # SOURCE LINE 49
        __M_writer(conditional_websafe(_('back to reddit')))
        __M_writer(u'</a></div>\n  </header>\n  <form class="newsletter-signup form-v2 c-form-inline" method="post" action="')
        # SOURCE LINE 51
        __M_writer(conditional_websafe(make_url_https('/api/newsletter.json')))
        __M_writer(u'">\n    <input type="hidden" name="uh" value="')
        # SOURCE LINE 52
        __M_writer(conditional_websafe(c.modhash))
        __M_writer(u'" />\n    <input type="hidden" name="source" value="standalone">\n    ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                # SOURCE LINE 54
                __M_writer(u'\n      <label for="email" class="screenreader-only">')
                # SOURCE LINE 55
                __M_writer(conditional_websafe(_('email')))
                __M_writer(u':</label>\n      <input value=""\n             name="email"\n             class="c-form-control"\n             type="email"\n             placeholder="')
                # SOURCE LINE 60
                __M_writer(conditional_websafe(_('enter your email')))
                __M_writer(u'"\n             data-validate-url="/api/check_email.json"\n             data-validate-on="change blur">\n    ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 54
            __M_writer(conditional_websafe(form_group('email', 'BAD_EMAIL', show_errors=True, feedback_inside_input=True)))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 63
        __M_writer(u'\n    <button type="submit" class="c-btn c-btn-primary">')
        # SOURCE LINE 64
        __M_writer(conditional_websafe(_('subscribe')))
        __M_writer(u'</button>\n  </form>\n\n  <a class="faq-toggle" href="#">')
        # SOURCE LINE 67
        __M_writer(conditional_websafe(_('More Info')))
        __M_writer(u'&#32;</a>\n\n  <div class="faq md">\n  ')
        # SOURCE LINE 70

        md(wiki_template('newsletter_faq'))
          
        
        # SOURCE LINE 72
        __M_writer(u'\n  </div>\n</section>\n\n<div class="upvoted-gradient" role="presentation"></div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_viewport(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fb219db5290')._populate(_import_ns, [u'less_stylesheet'])
        _mako_get_namespace(context, '__anon_0x7fb219db59d0')._populate(_import_ns, [u'form_group', u'md'])
        __M_writer = context.writer()
        # SOURCE LINE 36
        __M_writer(u'\n<meta name="viewport" content="width=device-width, initial-scale=1">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_Title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fb219db5290')._populate(_import_ns, [u'less_stylesheet'])
        _mako_get_namespace(context, '__anon_0x7fb219db59d0')._populate(_import_ns, [u'form_group', u'md'])
        __M_writer = context.writer()
        # SOURCE LINE 32
        __M_writer(u'\n')
        # SOURCE LINE 33
        __M_writer(conditional_websafe(_('reddit newsletter - upvoted weekly')))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


