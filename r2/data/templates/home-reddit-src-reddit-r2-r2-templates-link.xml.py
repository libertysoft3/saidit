# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1520062243.599149
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/link.xml'
_template_uri = '/link.xml'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23

from r2.lib.template_helpers import add_sr, get_domain
from r2.lib.filters import unsafe, safemarkdown, keep_space
from r2.lib.template_helpers import html_datetime
from r2.lib.template_helpers import make_url_https


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 29
    ns = runtime.TemplateNamespace(u'utils', context._clean_inheritance_tokens(), templateuri=u'utils.xml', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'utils')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        thing = context.get('thing', UNDEFINED)
        utils = _mako_get_namespace(context, 'utils')
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 28
        __M_writer(u'\n')
        # SOURCE LINE 29
        __M_writer(u'\n')
        # SOURCE LINE 30

        domain = get_domain(subreddit=False)
        permalink = add_sr(thing.permalink, force_hostname=True, retain_extension=False)
        use_thumbs = thing.has_thumbnail and thing.thumbnail and not request.GET.has_key("nothumbs")
        use_thumbs = use_thumbs and not thing.thumbnail_sprited
        thumbnail = thing.thumbnail
        if c.secure:
            thumbnail = make_url_https(thumbnail)
        if thing.deleted:
            title = _('[deleted]')
        else:
            title = thing.title
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['thumbnail','domain','title','permalink','use_thumbs'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 42
        __M_writer(u'\n<entry>\n')
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
        __M_writer(u'"/>\n\n    ')
        def ccall(caller):
            def body():
                getattr = context.get('getattr', UNDEFINED)
                __M_writer = context.writer()
                # SOURCE LINE 50
                __M_writer(u'\n')
                # SOURCE LINE 51
                if use_thumbs:
                    # SOURCE LINE 52
                    __M_writer(u'            <table>\n                <tr><td>\n                    <a href="')
                    # SOURCE LINE 54
                    __M_writer(conditional_websafe(permalink))
                    __M_writer(u'">\n                        <img src="')
                    # SOURCE LINE 55
                    __M_writer(conditional_websafe(thumbnail))
                    __M_writer(u'" alt="')
                    __M_writer(conditional_websafe(title))
                    __M_writer(u'" title="')
                    __M_writer(conditional_websafe(title))
                    __M_writer(u'" />\n                    </a>\n                </td><td>\n')
                # SOURCE LINE 59
                __M_writer(u'\n')
                # SOURCE LINE 60
                if getattr(thing, 'selftext', None):
                    # SOURCE LINE 61
                    if thing.expunged:
                        # SOURCE LINE 62
                        __M_writer(u'                ')
                        __M_writer(conditional_websafe(_('[removed]')))
                        __M_writer(u'\n')
                        # SOURCE LINE 63
                    else:
                        # SOURCE LINE 64
                        __M_writer(u'                ')
                        __M_writer(conditional_websafe(unsafe(safemarkdown(thing.selftext))))
                        __M_writer(u'\n')
                # SOURCE LINE 67
                __M_writer(u'\n')
                # SOURCE LINE 68
                if not thing.author._deleted:
                    # SOURCE LINE 69
                    __M_writer(u'            ')
                    __M_writer(conditional_websafe(keep_space(' ')))
                    __M_writer(u' submitted by ')
                    __M_writer(conditional_websafe(keep_space(' ')))
                    __M_writer(u'\n            <a href="')
                    # SOURCE LINE 70
                    __M_writer(conditional_websafe(add_sr('/user/'+thing.author.name,
                              sr_path=False,
                              retain_extension=False,
                              force_hostname=True)))
                    # SOURCE LINE 73
                    __M_writer(u'">\n                /u/')
                    # SOURCE LINE 74
                    __M_writer(conditional_websafe(thing.author.name))
                    __M_writer(u'\n            </a>\n')
                # SOURCE LINE 77
                __M_writer(u'\n')
                # SOURCE LINE 78
                if thing.different_sr:
                    # SOURCE LINE 79
                    __M_writer(u'            ')
                    __M_writer(conditional_websafe(keep_space(' ')))
                    __M_writer(u' to ')
                    __M_writer(conditional_websafe(keep_space(' ')))
                    __M_writer(u'\n            <a href="')
                    # SOURCE LINE 80
                    __M_writer(conditional_websafe(add_sr(thing.subreddit.path,
                              sr_path=False,
                              retain_extension=False,
                              force_hostname=True)))
                    # SOURCE LINE 83
                    __M_writer(u'">\n                /r/')
                    # SOURCE LINE 84
                    __M_writer(conditional_websafe(thing.subreddit.name))
                    __M_writer(u'\n            </a>\n')
                # SOURCE LINE 87
                __M_writer(u'\n        <br/>\n\n        <span><a href="')
                # SOURCE LINE 90
                __M_writer(conditional_websafe(thing.url))
                __M_writer(u'">[')
                __M_writer(conditional_websafe(_("link")))
                __M_writer(u']</a></span>\n        ')
                # SOURCE LINE 91
                __M_writer(conditional_websafe(keep_space(' ')))
                __M_writer(u'\n        <span><a href="')
                # SOURCE LINE 92
                __M_writer(conditional_websafe(permalink))
                __M_writer(u'">[')
                __M_writer(conditional_websafe(_("comments")))
                __M_writer(u']</a></span>\n\n')
                # SOURCE LINE 94
                if use_thumbs:
                    # SOURCE LINE 95
                    __M_writer(u'            </td></tr></table>\n')
                # SOURCE LINE 97
                __M_writer(u'    ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 50
            __M_writer(conditional_websafe(utils.atom_content()))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 97
        __M_writer(u'\n\n    <id>')
        # SOURCE LINE 99
        __M_writer(conditional_websafe(thing._fullname))
        __M_writer(u'</id>\n    <link href="')
        # SOURCE LINE 100
        __M_writer(conditional_websafe(permalink))
        __M_writer(u'" />\n    <updated>')
        # SOURCE LINE 101
        __M_writer(conditional_websafe(html_datetime(thing._date)))
        __M_writer(u'</updated>\n    <title>')
        # SOURCE LINE 102
        __M_writer(conditional_websafe(title))
        __M_writer(u'</title>\n</entry>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


