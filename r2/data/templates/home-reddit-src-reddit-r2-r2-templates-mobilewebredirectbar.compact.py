# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1508303897.835576
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/mobilewebredirectbar.compact'
_template_uri = '/mobilewebredirectbar.compact'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23

import urlparse


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'\n\n')
        # SOURCE LINE 27

        def mobile_web_url():
          url = request.environ['FULLPATH']
          scheme, netloc, path, query, fragment = urlparse.urlsplit(url)
          netloc = "%s.%s" % ('m', g.domain)
          path = path.replace('.compact', '')
          return urlparse.urlunsplit((None, netloc, path, query, fragment))
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['mobile_web_url'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 34
        __M_writer(u'\n\n<div hidden class="mobile-web-redirect-bar">\n  <div class="mobile-web-redirect-header">')
        # SOURCE LINE 37
        __M_writer(conditional_websafe(_("You've been invited to try out reddit's new mobile website!")))
        __M_writer(u'</div>\n\n  <a href="')
        # SOURCE LINE 39
        __M_writer(conditional_websafe(mobile_web_url()))
        __M_writer(u'"\n     class="mobile-web-redirect-optin">')
        # SOURCE LINE 40
        __M_writer(conditional_websafe(_("try reddit's mobile website")))
        __M_writer(u'</a>\n\n  <a href="#" class="mobile-web-redirect-optout">')
        # SOURCE LINE 42
        __M_writer(conditional_websafe(_("No thanks")))
        __M_writer(u'</a>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


