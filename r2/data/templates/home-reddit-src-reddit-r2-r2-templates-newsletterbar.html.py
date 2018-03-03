# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1508181621.237145
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/newsletterbar.html'
_template_uri = '/newsletterbar.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23

from r2.lib.template_helpers import make_url_https, static


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 26
    ns = runtime.TemplateNamespace('__anon_0x7fb899350890', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fb899350890')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fb899350890')._populate(_import_ns, [u'form_group'])
        form_group = _import_ns.get('form_group', context.get('form_group', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'\n')
        # SOURCE LINE 26
        __M_writer(u'\n\n<section hidden class="infobar newsletterbar newsletter-container">\n  <header>\n    <h1 class="subscribe-callout">\n      <a href="/newsletter"><img src="')
        # SOURCE LINE 31
        __M_writer(conditional_websafe(static('subscribe-header.svg')))
        __M_writer(u'" alt="')
        __M_writer(conditional_websafe(_('subscribe to our newsletter')))
        __M_writer(u'"></a>\n    </h1>\n    <div class="subscribe-thanks"><img src="')
        # SOURCE LINE 33
        __M_writer(conditional_websafe(static('subscribe-header-thanks.svg')))
        __M_writer(u'" alt="_(\'thanks for subscribing\')" /></div>\n    <h2 class="result-message">')
        # SOURCE LINE 34
        __M_writer(conditional_websafe(_('get the best of reddit, delivered once a week')))
        __M_writer(u'</h2>\n  </header>\n  <form class="newsletter-signup form-v2 c-form-inline" method="post" action="')
        # SOURCE LINE 36
        __M_writer(conditional_websafe(make_url_https('/api/newsletter.json')))
        __M_writer(u'">\n    <input type="hidden" name="uh" value="')
        # SOURCE LINE 37
        __M_writer(conditional_websafe(c.modhash))
        __M_writer(u'" />\n    <input type="hidden" name="source" value="newsletterbar">\n    ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                # SOURCE LINE 39
                __M_writer(u'\n      <label for="email" class="screenreader-only">')
                # SOURCE LINE 40
                __M_writer(conditional_websafe(_('email')))
                __M_writer(u':</label>\n      <input value=""\n             name="email"\n             class="c-form-control"\n             type="email"\n             placeholder="')
                # SOURCE LINE 45
                __M_writer(conditional_websafe(_('enter your email')))
                __M_writer(u'"\n             data-validate-url="/api/check_email.json"\n             data-validate-on="change blur">\n    ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 39
            __M_writer(conditional_websafe(form_group('email', 'BAD_EMAIL', show_errors=True, feedback_inside_input=True)))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 48
        __M_writer(u'\n\n    <button type="submit" class="c-btn c-btn-highlight">')
        # SOURCE LINE 50
        __M_writer(conditional_websafe(_('subscribe')))
        __M_writer(u'</button>\n  </form>\n  <a href="#" class="newsletter-close" title="close">&times;</a>\n</section>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


