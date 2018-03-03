# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1508265059.79594
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/subreddit.xml'
_template_uri = '/subreddit.xml'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 22

from r2.lib.template_helpers import html_datetime
from r2.lib.template_helpers import get_domain, header_url
from r2.lib.utils import UrlParser


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 27
    ns = runtime.TemplateNamespace(u'utils', context._clean_inheritance_tokens(), templateuri=u'utils.xml', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'utils')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        thing = context.get('thing', UNDEFINED)
        getattr = context.get('getattr', UNDEFINED)
        utils = _mako_get_namespace(context, 'utils')
        __M_writer = context.writer()
        # SOURCE LINE 26
        __M_writer(u'\n')
        # SOURCE LINE 27
        __M_writer(u'\n')
        # SOURCE LINE 28

        domain = get_domain(subreddit=False)
        url = g.default_scheme+"://"+domain+thing.path
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['url','domain'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 31
        __M_writer(u'\n<entry>\n')
        # SOURCE LINE 33
        if getattr(thing, 'author', None):
            # SOURCE LINE 34
            __M_writer(u'        ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                __M_writer(conditional_websafe(utils.atom_author(author=(thing.author))))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n')
        # SOURCE LINE 36
        __M_writer(u'\n    ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                # SOURCE LINE 37
                __M_writer(u'\n')
                # SOURCE LINE 38
                if thing.header:
                    # SOURCE LINE 39
                    __M_writer(u'            <img src="')
                    __M_writer(conditional_websafe(header_url(thing.header, c.secure)))
                    __M_writer(u'" />\n')
                # SOURCE LINE 41
                __M_writer(u'\n')
                # SOURCE LINE 42
                if thing.public_description:
                    # SOURCE LINE 43
                    __M_writer(u'            <div>\n                ')
                    # SOURCE LINE 44
                    __M_writer(conditional_websafe(thing.public_description))
                    __M_writer(u'\n            </div>\n')
                # SOURCE LINE 47
                __M_writer(u'        <div>\n            <a href="')
                # SOURCE LINE 48
                __M_writer(conditional_websafe(url))
                __M_writer(u'">')
                __M_writer(conditional_websafe(_("[link]")))
                __M_writer(u'</a>\n        </div>\n    ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 37
            __M_writer(conditional_websafe(utils.atom_content()))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 50
        __M_writer(u'\n\n    <id>')
        # SOURCE LINE 52
        __M_writer(conditional_websafe(thing._fullname))
        __M_writer(u'</id>\n    <link href="')
        # SOURCE LINE 53
        __M_writer(conditional_websafe(url))
        __M_writer(u'" />\n    <updated>')
        # SOURCE LINE 54
        __M_writer(conditional_websafe(html_datetime(thing._date)))
        __M_writer(u'</updated>\n    <title>')
        # SOURCE LINE 55
        __M_writer(conditional_websafe(thing.title))
        __M_writer(u'</title>\n</entry>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


