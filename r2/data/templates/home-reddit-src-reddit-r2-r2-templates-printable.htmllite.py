# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1520060829.87095
_enable_loop = True
_template_filename = u'/home/reddit/src/reddit/r2/r2/templates/printable.htmllite'
_template_uri = u'/printable.htmllite'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['iframe_arrows', 'parent', 'real_arrows', 'arrows', 'Child', 'entry', 'static_arrows']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7fc7c7784310', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fc7c7784310')] = ns

    # SOURCE LINE 24
    ns = runtime.TemplateNamespace('__anon_0x7fc7c7784ad0', context._clean_inheritance_tokens(), templateuri=u'printable.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fc7c7784ad0')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7784310')._populate(_import_ns, [u'optionalstyle'])
        _mako_get_namespace(context, '__anon_0x7fc7c7784ad0')._populate(_import_ns, [u'arrow'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n')
        # SOURCE LINE 24
        __M_writer(u'\n\n')
        # SOURCE LINE 26

        like_cls = "unvoted"
        if getattr(thing, "likes", None):
            like_cls = "likes"
        elif getattr(thing, "likes", None) is False:
            like_cls = "dislikes"
        thing.like_cls = like_cls
         
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['like_cls'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 33
        __M_writer(u'\n')
        # SOURCE LINE 34
        __M_writer(conditional_websafe(self.parent()))
        __M_writer(u'\n')
        # SOURCE LINE 35
        __M_writer(conditional_websafe(self.entry()))
        __M_writer(u'\n')
        # SOURCE LINE 36
        __M_writer(conditional_websafe(self.Child()))
        __M_writer(u'\n\n\n')
        # SOURCE LINE 40
        __M_writer(u'\n\n')
        # SOURCE LINE 44
        __M_writer(u'\n\n')
        # SOURCE LINE 47
        __M_writer(u'\n\n\n')
        # SOURCE LINE 68
        __M_writer(u'\n\n')
        # SOURCE LINE 93
        __M_writer(u'\n\n')
        # SOURCE LINE 100
        __M_writer(u'\n\n\n')
        # SOURCE LINE 111
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_iframe_arrows(context,thing):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7784310')._populate(_import_ns, [u'optionalstyle'])
        _mako_get_namespace(context, '__anon_0x7fc7c7784ad0')._populate(_import_ns, [u'arrow'])
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        optionalstyle = _import_ns.get('optionalstyle', context.get('optionalstyle', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 70
        __M_writer(u'\n  ')
        # SOURCE LINE 71
 
        from r2.lib.template_helpers import get_domain
        
        
        # SOURCE LINE 73
        __M_writer(u'\n  <div class="reddit-voting-arrows" \n     ')
        # SOURCE LINE 75
        __M_writer(conditional_websafe(optionalstyle("float:left; margin: 1px;")))
        __M_writer(u'>\n    <script type="text/javascript">\n      var reddit_bordercolor="FFFFFF";\n    </script>\n    ')
        # SOURCE LINE 79

        from r2.models import FakeSubreddit
        url = ("%s://%s/static/button/button4.html?t=4&id=%s&sr=%s" %
                (g.default_scheme, get_domain(subreddit=False), thing._fullname,
                c.site.name if not isinstance(c.site, FakeSubreddit) else ""))
        if c.bgcolor:
           url += "&bgcolor=%s&bordercolor=%s" % (c.bgcolor, c.bgcolor)
        else:
           url += "&bgcolor=FFFFFF&bordercolor=FFFFFF"
             
        
        # SOURCE LINE 88
        __M_writer(u'\n    <iframe src="')
        # SOURCE LINE 89
        __M_writer(conditional_websafe(url))
        __M_writer(u'" height="55" width="51" scrolling="no" frameborder="0"\n            ')
        # SOURCE LINE 90
        __M_writer(conditional_websafe(optionalstyle("margin:0px;")))
        __M_writer(u'>\n    </iframe>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_parent(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7784310')._populate(_import_ns, [u'optionalstyle'])
        _mako_get_namespace(context, '__anon_0x7fc7c7784ad0')._populate(_import_ns, [u'arrow'])
        __M_writer = context.writer()
        # SOURCE LINE 39
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_real_arrows(context,thing):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7784310')._populate(_import_ns, [u'optionalstyle'])
        _mako_get_namespace(context, '__anon_0x7fc7c7784ad0')._populate(_import_ns, [u'arrow'])
        arrow = _import_ns.get('arrow', context.get('arrow', UNDEFINED))
        optionalstyle = _import_ns.get('optionalstyle', context.get('optionalstyle', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 95
        __M_writer(u'\n  <div class="midcol ')
        # SOURCE LINE 96
        __M_writer(conditional_websafe(thing.like_cls))
        __M_writer(u'" ')
        __M_writer(conditional_websafe(optionalstyle("width: 15px")))
        __M_writer(u'>\n    ')
        # SOURCE LINE 97
        __M_writer(conditional_websafe(arrow(thing, 1, thing.likes)))
        __M_writer(u'\n    ')
        # SOURCE LINE 98
        __M_writer(conditional_websafe(arrow(thing, 0, thing.likes == False)))
        __M_writer(u'\n </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_arrows(context,thing):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7784310')._populate(_import_ns, [u'optionalstyle'])
        _mako_get_namespace(context, '__anon_0x7fc7c7784ad0')._populate(_import_ns, [u'arrow'])
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 103
        __M_writer(u'\n')
        # SOURCE LINE 104
        if getattr(thing, 'embed_voting_style',None) == 'votable':
            # SOURCE LINE 105
            __M_writer(u'    ')
            __M_writer(conditional_websafe(self.real_arrows(thing)))
            __M_writer(u'\n')
            # SOURCE LINE 106
        elif request.GET.get("expanded") or getattr(thing, 'embed_voting_style', None) == 'expanded':
            # SOURCE LINE 107
            __M_writer(u'    ')
            __M_writer(conditional_websafe(self.iframe_arrows(thing)))
            __M_writer(u'\n')
            # SOURCE LINE 108
        else:
            # SOURCE LINE 109
            __M_writer(u'    ')
            __M_writer(conditional_websafe(self.static_arrows(thing)))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_Child(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7784310')._populate(_import_ns, [u'optionalstyle'])
        _mako_get_namespace(context, '__anon_0x7fc7c7784ad0')._populate(_import_ns, [u'arrow'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 42
        __M_writer(u'\n  ')
        # SOURCE LINE 43
        __M_writer(conditional_websafe(getattr(thing, "child", '')))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_entry(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7784310')._populate(_import_ns, [u'optionalstyle'])
        _mako_get_namespace(context, '__anon_0x7fc7c7784ad0')._populate(_import_ns, [u'arrow'])
        __M_writer = context.writer()
        # SOURCE LINE 46
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_static_arrows(context,thing):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc7c7784310')._populate(_import_ns, [u'optionalstyle'])
        _mako_get_namespace(context, '__anon_0x7fc7c7784ad0')._populate(_import_ns, [u'arrow'])
        optionalstyle = _import_ns.get('optionalstyle', context.get('optionalstyle', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 50
        __M_writer(u'\n  ')
        # SOURCE LINE 51

        from r2.lib.template_helpers import get_domain
        domain = get_domain(subreddit=False)
        permalink = "%s://%s%s" % (g.default_scheme, domain, thing.permalink)
        if thing.likes == False:
           arrow = "%s://%s/static/widget_arrows_down.gif"
        elif thing.likes:
           arrow = "%s://%s/static/widget_arrows_up.gif"
        else:
           arrow = "%s://%s/static/widget_arrows.gif"
        arrow = arrow % (g.default_scheme, domain)
        
        
        # SOURCE LINE 62
        __M_writer(u'\n  <a href="')
        # SOURCE LINE 63
        __M_writer(conditional_websafe(permalink))
        __M_writer(u'" class="reddit-voting-arrows" target="_blank"\n     ')
        # SOURCE LINE 64
        __M_writer(conditional_websafe(optionalstyle("float:left; display:block;")))
        __M_writer(u'>\n    <img src="')
        # SOURCE LINE 65
        __M_writer(conditional_websafe(arrow))
        __M_writer(u'" alt="vote" \n         ')
        # SOURCE LINE 66
        __M_writer(conditional_websafe(optionalstyle("border:none;margin-top:3px;")))
        __M_writer(u'/>\n  </a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


