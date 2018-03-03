# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1508265633.967223
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/comment.xml'
_template_uri = '/comment.xml'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23

from r2.lib.filters import safemarkdown
from r2.lib.template_helpers import html_datetime
from r2.lib.template_helpers import add_sr


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 28
    ns = runtime.TemplateNamespace(u'utils', context._clean_inheritance_tokens(), templateuri=u'utils.xml', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'utils')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        thing = context.get('thing', UNDEFINED)
        utils = _mako_get_namespace(context, 'utils')
        hasattr = context.get('hasattr', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 27
        __M_writer(u'\n')
        # SOURCE LINE 28
        __M_writer(u'\n')
        # SOURCE LINE 29

        if thing.deleted:
            author = _('[deleted]')
            comment_body = _('[deleted]')
        else:
            if thing.author._deleted:
                author = _('[deleted]')
            else:
                author = thing.author.name
            comment_body = thing.body
        
        permalink = add_sr(thing.permalink, force_hostname=True)
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['comment_body','permalink','author'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 41
        __M_writer(u'\n\n<entry>\n')
        # SOURCE LINE 44
        if not thing.deleted:
            # SOURCE LINE 45
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
        # SOURCE LINE 47
        __M_writer(u'\n    <category term="')
        # SOURCE LINE 48
        __M_writer(conditional_websafe(thing.subreddit.name))
        __M_writer(u'" label="/r/')
        __M_writer(conditional_websafe(thing.subreddit.name))
        __M_writer(u'" />\n\n    ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                # SOURCE LINE 50
                __M_writer(u'\n        ')
                # SOURCE LINE 51
                __M_writer(conditional_websafe(unsafe(safemarkdown(comment_body))))
                __M_writer(u'\n    ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 50
            __M_writer(conditional_websafe(utils.atom_content()))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 52
        __M_writer(u'\n\n    <id>')
        # SOURCE LINE 54
        __M_writer(conditional_websafe(thing._fullname))
        __M_writer(u'</id>\n    <link href="')
        # SOURCE LINE 55
        __M_writer(conditional_websafe(thing.permalink))
        __M_writer(u'"/>\n    <updated>')
        # SOURCE LINE 56
        __M_writer(conditional_websafe(html_datetime(thing._date)))
        __M_writer(u'</updated>\n    <title>/u/')
        # SOURCE LINE 57
        __M_writer(conditional_websafe(author))
        __M_writer(u' ')
        __M_writer(conditional_websafe(_("on")))
        __M_writer(u' ')
        __M_writer(conditional_websafe(thing.link.title))
        __M_writer(u'</title>\n</entry>\n\n')
        # SOURCE LINE 60
        __M_writer(conditional_websafe(hasattr(thing, "child") and thing.child or ''))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


