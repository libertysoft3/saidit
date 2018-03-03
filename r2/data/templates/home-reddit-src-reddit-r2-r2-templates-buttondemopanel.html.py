# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505017380.46088
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/buttondemopanel.html'
_template_uri = '/buttondemopanel.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['draw_interactive_example', 'demo', 'drawbadge', 'draw_interactive', 'point_option_example', 'drawoption', 'draw_point_button']


# SOURCE LINE 23

from pylons import app_globals as g

from r2.lib.template_helpers import get_domain
 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        capture = context.get('capture', UNDEFINED)
        def draw_interactive_example():
            return render_draw_interactive_example(context._locals(__M_locals))
        xrange = context.get('xrange', UNDEFINED)
        def drawbadge(image):
            return render_drawbadge(context._locals(__M_locals),image)
        def draw_interactive(type):
            return render_draw_interactive(context._locals(__M_locals),type)
        def point_option_example():
            return render_point_option_example(context._locals(__M_locals))
        dict = context.get('dict', UNDEFINED)
        def drawoption(option,val):
            return render_drawoption(context._locals(__M_locals),option,val)
        def demo(content):
            return render_demo(context._locals(__M_locals),content)
        def draw_point_button(image):
            return render_draw_point_button(context._locals(__M_locals),image)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 27
        __M_writer(u'\n\n')
        # SOURCE LINE 29
        domain = get_domain(subreddit=False) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['domain'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n<div class="instructions">\n  <h1>')
        # SOURCE LINE 32
        __M_writer(conditional_websafe(_("put %(site)s buttons on your site") % dict(site=c.site.name)))
        __M_writer(u'</h1>\n    <p>')
        # SOURCE LINE 33
        __M_writer(conditional_websafe(_('the reddit button is the smart way to get your content submitted to\
      and discussed on reddit.  pick the button you like from below, and then\
      copy/paste the code into your HTML editor.')))
        # SOURCE LINE 35
        __M_writer(u'</p>\n\n    <h2>')
        # SOURCE LINE 37
        __M_writer(conditional_websafe(_("commonly used buttons")))
        __M_writer(u'</h2>\n    <p>')
        # SOURCE LINE 38
        __M_writer(conditional_websafe(_('use one of these buttons to quickly add reddit links to your site, or \
      see below for more options.')))
        # SOURCE LINE 39
        __M_writer(u'</p>\n    <ul class="buttons">\n      ')
        # SOURCE LINE 41
        __M_writer(conditional_websafe(demo(capture(drawbadge, 1))))
        __M_writer(u'\n      ')
        # SOURCE LINE 42
        __M_writer(conditional_websafe(demo(capture(drawbadge, 7))))
        __M_writer(u'\n      ')
        # SOURCE LINE 43
        __M_writer(conditional_websafe(demo(capture(draw_point_button, 0))))
        __M_writer(u'\n      ')
        # SOURCE LINE 44
        __M_writer(conditional_websafe(demo(capture(draw_point_button, 1))))
        __M_writer(u'\n      ')
        # SOURCE LINE 45
        __M_writer(conditional_websafe(demo(capture(draw_interactive, 1))))
        __M_writer(u'\n    </ul>\n      \n\n    <h2>')
        # SOURCE LINE 49
        __M_writer(conditional_websafe(_("buttons with points")))
        __M_writer(u'</h2>\n    <ul class="buttons">\n')
        # SOURCE LINE 51
        for x in xrange(0,6):
            # SOURCE LINE 52
            __M_writer(u'       ')
            __M_writer(conditional_websafe(demo(capture(draw_point_button, x))))
            __M_writer(u'\n')
        # SOURCE LINE 54
        __M_writer(u'    </ul>\n    <h2>')
        # SOURCE LINE 55
        __M_writer(conditional_websafe(_("customizing the look of your buttons")))
        __M_writer(u'</h2>\n    <p>')
        # SOURCE LINE 56
        __M_writer(conditional_websafe(_('the buttons with points have three additional options.')))
        __M_writer(u'</p>\n    <ul class="buttons" >\n      <li><strong>styled=off</strong><br />\n        ')
        # SOURCE LINE 59
        __M_writer(conditional_websafe(_('no styles will be added, so you can style it yourself')))
        __M_writer(u'</li>\n      <li><strong>url=[URL]</strong><br />\n        ')
        # SOURCE LINE 61
        __M_writer(conditional_websafe(_('specify a url to use instead of the current url')))
        __M_writer(u'</li>\n      <li><strong>newwindow=1</strong><br />\n        ')
        # SOURCE LINE 63
        __M_writer(conditional_websafe(_('opens links in a new window')))
        __M_writer(u'</li>\n    </ul>\n    <p>')
        # SOURCE LINE 65
        __M_writer(conditional_websafe(_('Example:')))
        __M_writer(u'</p>\n    <code>\n      ')
        # SOURCE LINE 67
        __M_writer(conditional_websafe(point_option_example()))
        __M_writer(u'\n    </code>\n\n\n    <h2>')
        # SOURCE LINE 71
        __M_writer(conditional_websafe(_('simple interactive button')))
        __M_writer(u'</h2>\n    <p>')
        # SOURCE LINE 72
        __M_writer(conditional_websafe(_('put this code on your page:')))
        __M_writer(u'</p>\n    <code>\n      ')
        # SOURCE LINE 74
        __M_writer(conditional_websafe(capture(draw_interactive,False)))
        __M_writer(u'\n    </code>\n      <p>')
        # SOURCE LINE 76
        __M_writer(conditional_websafe(_("and you'll get something like this:")))
        __M_writer(u'</p>\n        <span style="margin-left: 10px;">\n          ')
        # SOURCE LINE 78
        __M_writer(conditional_websafe(draw_interactive(False)))
        __M_writer(u'\n        </span>\n\n    <h2>')
        # SOURCE LINE 81
        __M_writer(conditional_websafe(_("more interactive buttons")))
        __M_writer(u'</h2>\n    <ul class="buttons">\n')
        # SOURCE LINE 83
        for x in xrange(1,4):
            # SOURCE LINE 84
            __M_writer(u'        ')
            __M_writer(conditional_websafe(demo(capture(draw_interactive, x))))
            __M_writer(u'\n')
        # SOURCE LINE 86
        __M_writer(u'    </ul>\n\n    <h2>')
        # SOURCE LINE 88
        __M_writer(conditional_websafe(_('interactive button advanced settings')))
        __M_writer(u'</h2>\n    <div class="box buttonsettings">\n      <ul>\n        <li>\n          <p><strong>')
        # SOURCE LINE 92
        __M_writer(conditional_websafe(_("specify a url")))
        __M_writer(u'</strong><br />\n            ')
        # SOURCE LINE 93
        __M_writer(conditional_websafe(_("useful in places like blogs, where you want to link to the post's permalink")))
        __M_writer(u'</p>\n          <code>')
        # SOURCE LINE 94
        __M_writer(conditional_websafe(drawoption('url','[URL]')))
        __M_writer(u'</code>\n        </li>\n        <li>\n          <p><strong>')
        # SOURCE LINE 97
        __M_writer(conditional_websafe(_("specify a community to target")))
        __M_writer(u'</strong></p>\n          <code>')
        # SOURCE LINE 98
        __M_writer(conditional_websafe(drawoption('target','[COMMUNITY]')))
        __M_writer(u'</code>\n        </li>\n        <li>\n          <p><strong>')
        # SOURCE LINE 101
        __M_writer(conditional_websafe(_("specify a title")))
        __M_writer(u'</strong></p>\n          <code>')
        # SOURCE LINE 102
        __M_writer(conditional_websafe(drawoption('title','[TITLE]')))
        __M_writer(u'</code>\n        </li>\n        <li>\n          <p><strong>')
        # SOURCE LINE 105
        __M_writer(conditional_websafe(_("open links in a new window")))
        __M_writer(u'</strong></p>\n          <code>')
        # SOURCE LINE 106
        __M_writer(conditional_websafe(drawoption('newwindow','1')))
        __M_writer(u'</code>\n        </li>\n        <li>\n          <p><strong>')
        # SOURCE LINE 109
        __M_writer(conditional_websafe(_("specify the color")))
        __M_writer(u'</strong></p>\n          <code>')
        # SOURCE LINE 110
        __M_writer(conditional_websafe(drawoption('bgcolor','[COLOR]')))
        __M_writer(u'</code>\n        </li>\n        <li>\n          <p><strong>')
        # SOURCE LINE 113
        __M_writer(conditional_websafe(_("specify a border color")))
        __M_writer(u'</strong></p>\n          <code>')
        # SOURCE LINE 114
        __M_writer(conditional_websafe(drawoption('bordercolor','[COLOR]')))
        __M_writer(u'</code>\n        </li>\n      </ul>\n      <p style="font-weight: bold">')
        # SOURCE LINE 117
        __M_writer(conditional_websafe(_('Example:')))
        __M_writer(u'</p>\n      <p>')
        # SOURCE LINE 118
        __M_writer(conditional_websafe(_('to make this button:')))
        __M_writer(u'</p>\n      <span style="margin-left: 10px;">')
        # SOURCE LINE 119
        __M_writer(conditional_websafe(draw_interactive_example()))
        __M_writer(u'</span>\n      <p>')
        # SOURCE LINE 120
        __M_writer(conditional_websafe(_('use this code:')))
        __M_writer(u'</p>\n      <code>\n        ')
        # SOURCE LINE 122

        ex = websafe(capture(draw_interactive_example))
        ex = ex.replace("\n", "<br/>").replace(" ", "&nbsp;")
                 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['ex'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 125
        __M_writer(u'\n      ')
        # SOURCE LINE 126
        __M_writer(conditional_websafe(unsafe(ex)))
        __M_writer(u'\n      </code>\n    </div>\n\n    <h2>')
        # SOURCE LINE 130
        __M_writer(conditional_websafe(_("more badges and buttons")))
        __M_writer(u'</h2>\n    <ul class="buttons">\n')
        # SOURCE LINE 132
        for x in xrange(1,15):
            # SOURCE LINE 133
            __M_writer(u'        ')
            __M_writer(conditional_websafe(demo(capture(drawbadge, x))))
            __M_writer(u'\n')
        # SOURCE LINE 135
        __M_writer(u'    </ul>\n\n\n</div>\n\n<script type="text/javascript">\n$(function() {\n $(".view-code").click(function(evt) { \n    $(this).parent().addClass("show-demo"); \n });\n $(".hide-code").click(function(evt) { \n    $(this).parent().removeClass("show-demo"); \n });\n});\n</script>\n\n')
        # SOURCE LINE 157
        __M_writer(u'\n\n')
        # SOURCE LINE 169
        __M_writer(u'\n\n')
        # SOURCE LINE 174
        __M_writer(u'\n\n')
        # SOURCE LINE 179
        __M_writer(u'\n\n')
        # SOURCE LINE 188
        __M_writer(u'\n\n')
        # SOURCE LINE 192
        __M_writer(u'\n\n')
        # SOURCE LINE 201
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_draw_interactive_example(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        domain = context.get('domain', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 194
        __M_writer(u'<script type="text/javascript">\n  reddit_url = "//')
        # SOURCE LINE 195
        __M_writer(conditional_websafe(domain))
        __M_writer(u'/buttons";\n  reddit_title = "Buttons!";\n  reddit_bgcolor = "FF3";\n  reddit_bordercolor = "00F";\n</script>\n<script type="text/javascript" src="//')
        # SOURCE LINE 200
        __M_writer(conditional_websafe(g.static_domain))
        __M_writer(u'/button/button3.js"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_demo(context,content):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 159
        __M_writer(u'\n<li class="button-demo">\n  <a class="view-code" href="javascript:void(0)">')
        # SOURCE LINE 161
        __M_writer(conditional_websafe(_("view code")))
        __M_writer(u'</a>\n  <a class="hide-code" href="javascript:void(0)">')
        # SOURCE LINE 162
        __M_writer(conditional_websafe(_("hide code")))
        __M_writer(u'</a>\n  ')
        # SOURCE LINE 163
        __M_writer(conditional_websafe(unsafe(content)))
        __M_writer(u'\n  <br />\n  <code>\n    ')
        # SOURCE LINE 166
        __M_writer(conditional_websafe(content))
        __M_writer(u'\n  </code>\n</li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_drawbadge(context,image):
    __M_caller = context.caller_stack._push_frame()
    try:
        domain = context.get('domain', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 151
        __M_writer(u'\n  <a href="//')
        # SOURCE LINE 152
        __M_writer(conditional_websafe(domain))
        __M_writer(u'/submit"\n    onclick="window.location = \'//')
        # SOURCE LINE 153
        __M_writer(conditional_websafe(domain))
        __M_writer(u'/submit?url=\' + encodeURIComponent(window.location); return false">\n   <img src="//')
        # SOURCE LINE 154
        __M_writer(conditional_websafe(g.static_domain))
        __M_writer(u'/spreddit')
        __M_writer(conditional_websafe(image))
        __M_writer(u'.gif"\n        alt="submit to SaidIt" border="0" />\n   </a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_draw_interactive(context,type):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 181
        __M_writer(u'\n')
        # SOURCE LINE 182
        if type:
            # SOURCE LINE 183
            __M_writer(u'  <script type="text/javascript" \n          src="//')
            # SOURCE LINE 184
            __M_writer(conditional_websafe(g.static_domain))
            __M_writer(u'/button/button')
            __M_writer(conditional_websafe(type))
            __M_writer(u'.js"></script>\n')
            # SOURCE LINE 185
        else:
            # SOURCE LINE 186
            __M_writer(u'  <script type="text/javascript" src="//')
            __M_writer(conditional_websafe(g.static_domain))
            __M_writer(u'/button/button1.js"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_point_option_example(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        context._push_buffer()
        domain = context.get('domain', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 176
        __M_writer(u'\n   <script type="text/javascript" \n        src="//')
        # SOURCE LINE 178
        __M_writer(conditional_websafe(domain))
        __M_writer(u'/buttonlite.js?i=1&styled=off&url=foo.com&newwindow=1"></script>\n')
    finally:
        __M_buf = context._pop_buffer()
        context.caller_stack._pop_frame()
    return __M_buf.getvalue()


def render_drawoption(context,option,val):
    __M_caller = context.caller_stack._push_frame()
    try:
        context._push_buffer()
        __M_writer = context.writer()
        # SOURCE LINE 190
        __M_writer(u'\n  <script type="text/javascript">reddit_')
        # SOURCE LINE 191
        __M_writer(conditional_websafe(option))
        __M_writer(u"='")
        __M_writer(conditional_websafe(val))
        __M_writer(u"'</script>\n")
    finally:
        __M_buf = context._pop_buffer()
        context.caller_stack._pop_frame()
    return __M_buf.getvalue()


def render_draw_point_button(context,image):
    __M_caller = context.caller_stack._push_frame()
    try:
        domain = context.get('domain', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 171
        __M_writer(u'\n  <script type="text/javascript" \n          src="//')
        # SOURCE LINE 173
        __M_writer(conditional_websafe(domain))
        __M_writer(u'/buttonlite.js?i=')
        __M_writer(conditional_websafe(image))
        __M_writer(u'"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


