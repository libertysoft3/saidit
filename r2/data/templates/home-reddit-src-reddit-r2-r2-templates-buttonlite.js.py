# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1510145475.410203
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/buttonlite.js'
_template_uri = '/buttonlite.js'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['submiturl']


# SOURCE LINE 23

from r2.lib.filters import jssafe, websafe
from r2.lib.template_helpers import static, get_domain
from r2.lib.utils import query_string
from r2.lib.strings import Score
 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        thing = context.get('thing', UNDEFINED)
        def submiturl(url,title=''):
            return render_submiturl(context._locals(__M_locals),url,title)
        str = context.get('str', UNDEFINED)
        capture = context.get('capture', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 28
        __M_writer(u'\n\n')
        # SOURCE LINE 30
        __M_writer(u'\n\n')
        # SOURCE LINE 32
 
        if thing._fullname:
            path = thing.make_permalink_slow(force_domain=True)
        else:
            path = capture(submiturl, thing.url, thing.title)
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['path'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 37
        __M_writer(u'\n(function() {\n       \n    var styled_submit = \'<a style="color: #369; text-decoration: none;" href="')
        # SOURCE LINE 40
        __M_writer(conditional_websafe(path))
        __M_writer(u'" target="')
        __M_writer(conditional_websafe(thing.target))
        __M_writer(u'">\';\n    var unstyled_submit = \'<a href="')
        # SOURCE LINE 41
        __M_writer(conditional_websafe(submiturl(thing.url)))
        __M_writer(u'" target="')
        __M_writer(conditional_websafe(path))
        __M_writer(u'">\';\n    var write_string=\'<span class="reddit_button" style="\';\n')
        # SOURCE LINE 43
        if thing.styled:    
            # SOURCE LINE 44
            __M_writer(u"    write_string += 'color: grey;';\n")
        # SOURCE LINE 46
        __M_writer(u'    write_string += \'">\';\n')
        # SOURCE LINE 47
        if thing.image > 0:
            # SOURCE LINE 48
            __M_writer(u'    write_string += unstyled_submit + \'<img style="height: 2.3ex; vertical-align:top; margin-right: 1ex" src="')
            __M_writer(conditional_websafe(static('spreddit' + str(thing.image) + '.gif')))
            __M_writer(u'">\' + "</a>";\n')
        # SOURCE LINE 50
        if thing._fullname:
            # SOURCE LINE 51
            __M_writer(u"    write_string += '")
            __M_writer(conditional_websafe(jssafe(websafe(Score.safepoints(thing.score)))))
            __M_writer(u"';\n")
            # SOURCE LINE 52
            if thing.styled:  
                # SOURCE LINE 53
                __M_writer(u"        write_string += ' on ' + styled_submit + 'reddit</a>';\n")
                # SOURCE LINE 54
            else:
                # SOURCE LINE 55
                __M_writer(u"        write_string += ' on ' + unstyled_submit + 'reddit</a>';\n")
            # SOURCE LINE 57
        else:
            # SOURCE LINE 58
            if thing.styled:
                # SOURCE LINE 59
                __M_writer(u"    write_string += styled_submit + 'submit';\n")
                # SOURCE LINE 60
            else:
                # SOURCE LINE 61
                __M_writer(u"    write_string += unstyled_submit + 'submit';\n")
            # SOURCE LINE 63
            if thing.image > 0:
                # SOURCE LINE 64
                __M_writer(u"    write_string += '</a>';\n")
                # SOURCE LINE 65
            else:
                # SOURCE LINE 66
                __M_writer(u"    write_string += ' to reddit</a>';\n")
        # SOURCE LINE 69
        __M_writer(u"    write_string += '</span>';\n\ndocument.write(write_string);\n})()\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_submiturl(context,url,title=''):
    __M_caller = context.caller_stack._push_frame()
    try:
        dict = context.get('dict', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 30
        __M_writer(conditional_websafe(("%s://%s/submit" % (g.default_scheme, get_domain(subreddit=True))) + query_string(dict(url=url, title=title))))
        return ''
    finally:
        context.caller_stack._pop_frame()


