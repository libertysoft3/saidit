# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1508265121.40145
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/apihelp.html'
_template_uri = '/apihelp.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['api_uri', 'mode_selector', 'api_method_toc', 'api_uri_with_sr_maybe', 'oauth_toc', 'scope_header', 'section_header', 'api_method_id']


# SOURCE LINE 23

import re
from r2.lib.filters import safemarkdown
from r2.controllers.api_docs import section_info
from r2.models.token import OAuth2Scope
from r2.lib.db.thing import thing_types


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def section_header(section):
            return render_section_header(context._locals(__M_locals),section)
        def api_method_toc(api):
            return render_api_method_toc(context._locals(__M_locals),api)
        def api_uri_with_sr_maybe(uri,in_sr):
            return render_api_uri_with_sr_maybe(context._locals(__M_locals),uri,in_sr)
        def oauth_toc(api,oauth_index):
            return render_oauth_toc(context._locals(__M_locals),api,oauth_index)
        def scope_header(scope):
            return render_scope_header(context._locals(__M_locals),scope)
        thing = context.get('thing', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        def api_method_id(uri,method):
            return render_api_method_id(context._locals(__M_locals),uri,method)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 29
        __M_writer(u'\n\n')
        # SOURCE LINE 31
        __M_writer(u'\n')
        # SOURCE LINE 32
        __M_writer(u'\n')
        # SOURCE LINE 33
        __M_writer(u'\n\n')
        # SOURCE LINE 42
        __M_writer(u'\n\n')
        # SOURCE LINE 66
        __M_writer(u'\n\n')
        # SOURCE LINE 85
        __M_writer(u'\n\n')
        # SOURCE LINE 94
        __M_writer(u'\n\n')
        # SOURCE LINE 104
        __M_writer(u'\n\n')
        # SOURCE LINE 106

        api = thing.api_docs
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['api'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 108
        __M_writer(u'\n\n<div class="sidebar">\n  <div class="head"></div>\n  <div class="toc">\n    <ul>\n      <li>\n')
        # SOURCE LINE 115
        if thing.mode == "oauth":
            # SOURCE LINE 116
            __M_writer(u'          ')
            __M_writer(conditional_websafe(oauth_toc(thing.api_docs, thing.oauth_index)))
            __M_writer(u'\n')
            # SOURCE LINE 117
        else:
            # SOURCE LINE 118
            __M_writer(u'          ')
            __M_writer(conditional_websafe(api_method_toc(thing.api_docs)))
            __M_writer(u'\n')
        # SOURCE LINE 120
        __M_writer(u'      </li>\n    </ul>\n  </div>\n  <div class="feet"></div>\n</div>\n\n<div class="contents">\n  <div class="section introduction">\n    <p>This is automatically-generated documentation for the reddit API.</p>\n    <p>The reddit API and code are&#32;<a href="/code">open source</a>. Found a mistake or interested in helping us improve? Have a gander at&#32;<a href="https://github.com/reddit/reddit/blob/master/r2/r2/controllers/api.py">api.py</a>&#32;and send us a pull request.</p>\n    <p><strong>Please take care to respect our&#32;<a href="https://github.com/reddit/reddit/wiki/API">API access rules</a>.</strong></p>\n  </div>\n\n  <div class="section overview">\n    <h2>overview</h2>\n\n    <h3 id="listings">listings</h3>\n\n    ')
        __M_writer = context._push_writer()
        try:
            # SOURCE LINE 138
            __M_writer(u'\nMany endpoints on reddit use the same protocol for controlling pagination and\nfiltering. These endpoints are called Listings and share five common\nparameters: `after` / `before`, `limit`, `count`, and `show`.\n\nListings do not use page numbers because their content changes so frequently.\nInstead, they allow you to view slices of the underlying data. Listing JSON\nresponses contain `after` and `before` fields which are equivalent to the\n"next" and "prev" buttons on the site and in combination with `count` can be\nused to page through the listing.\n\nThe common parameters are as follows:\n\n* `after` / `before` - only one should be specified. these indicate the\n[fullname](#fullnames) of an item in the listing to use as the anchor point of\nthe slice.\n* `limit` - the maximum number of items to return in this slice of the listing.\n* `count` - the number of items already seen in this listing. on the html site,\nthe builder uses this to determine when to give values for `before` and `after`\nin the response.\n* `show` - optional parameter; if `all` is passed, filters such as "hide links\nthat I have voted on" will be disabled.\n\nTo page through a listing, start by fetching the first page without specifying\nvalues for `after` and `count`. The response will contain an `after` value\nwhich you can pass in the next request. It is a good idea, but not required, to\nsend an updated value for `count` which should be the number of items already\nfetched.\n    ')
        finally:
            __M_buf, __M_writer = context._pop_buffer_and_writer()
            __M_writer(safemarkdown(__M_buf.getvalue()))
        # SOURCE LINE 166
        __M_writer(u'\n\n    <h3 id="modhashes">modhashes</h3>\n\n    ')
        __M_writer = context._push_writer()
        try:
            # SOURCE LINE 170
            __M_writer(u'\nA modhash is a token that the reddit API requires to help prevent\n[CSRF](http://en.wikipedia.org/wiki/CSRF). Modhashes can be obtained via the\n[/api/me.json](#GET_api_me.json) call or in response data of listing endpoints.\n\nThe preferred way to send a modhash is to include an `X-Modhash` custom HTTP\nheader with your requests.\n\nModhashes are not required when authenticated with OAuth.\n    ')
        finally:
            __M_buf, __M_writer = context._pop_buffer_and_writer()
            __M_writer(safemarkdown(__M_buf.getvalue()))
        # SOURCE LINE 179
        __M_writer(u'\n\n    <h3 id="fullnames">fullnames</h3>\n\n    ')
        __M_writer = context._push_writer()
        try:
            # SOURCE LINE 183
            __M_writer(u"\nA fullname is a combination of a thing's type (e.g. `Link`) and its unique ID\nwhich forms a compact encoding of a globally unique ID on reddit.\n\nFullnames start with the type prefix for the object's type, followed by the\nthing's unique ID in [base 36](http://en.wikipedia.org/wiki/Base36).  For\nexample, `t3_15bfi0`.\n    ")
        finally:
            __M_buf, __M_writer = context._pop_buffer_and_writer()
            __M_writer(safemarkdown(__M_buf.getvalue()))
        # SOURCE LINE 190
        __M_writer(u'\n\n    <table class="parameters">\n      <caption>type prefixes</caption>\n')
        # SOURCE LINE 194
        for typeid in sorted(thing_types):
            # SOURCE LINE 195
            __M_writer(u'      <tr>\n        <th scope="row">t')
            # SOURCE LINE 196
            __M_writer(conditional_websafe(typeid))
            __M_writer(u'_</th>\n        <td>')
            # SOURCE LINE 197
            __M_writer(conditional_websafe(thing_types[typeid].__name__))
            __M_writer(u'</td>\n      </tr>\n')
        # SOURCE LINE 200
        __M_writer(u'    </table>\n\n    <h3 id="response_body_encoding">response body encoding</h3>\n\n    ')
        __M_writer = context._push_writer()
        try:
            # SOURCE LINE 204
            __M_writer(u'\nFor legacy reasons, all JSON response bodies currently have `<`, `>`, and `&`\nreplaced with `&lt;`, `&gt;`, and `&amp;`, respectively. If you wish to opt out\nof this behaviour, add a `raw_json=1` parameter to your request.\n    ')
        finally:
            __M_buf, __M_writer = context._pop_buffer_and_writer()
            __M_writer(safemarkdown(__M_buf.getvalue()))
        # SOURCE LINE 208
        __M_writer(u'\n  </div>\n\n  <div class="section methods">\n')
        # SOURCE LINE 212
        for section in sorted(api):
            # SOURCE LINE 213
            if thing.mode == 'oauth':
                # SOURCE LINE 214
                __M_writer(u'        ')
                __M_writer(conditional_websafe(scope_header(section)))
                __M_writer(u'\n')
                # SOURCE LINE 215
            else:
                # SOURCE LINE 216
                __M_writer(u'        ')
                __M_writer(conditional_websafe(section_header(section)))
                __M_writer(u'\n')
            # SOURCE LINE 218
            for uri in sorted(api[section]):
                # SOURCE LINE 219
                for method in sorted(api[section][uri]):
                    # SOURCE LINE 220
                    __M_writer(u'          ')

                    docs = api[section][uri][method]
                    # skip uri variants in the index
                    if docs['uri'] != uri:
                      continue
                    
                    in_subreddit = 'in-subreddit' in docs
                    
                    extends = docs.get('extends')
                              
                    
                    __M_locals_builtin_stored = __M_locals_builtin()
                    __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['docs','in_subreddit','extends'] if __M_key in __M_locals_builtin_stored]))
                    # SOURCE LINE 229
                    __M_writer(u'\n          <div class="endpoint" id="')
                    # SOURCE LINE 230
                    __M_writer(conditional_websafe(api_method_id(uri, method)))
                    __M_writer(u'">\n            <div class="links">\n')
                    # SOURCE LINE 232
                    if docs.get('lineno') and docs.get('relfilepath'):
                        # SOURCE LINE 233
                        __M_writer(u'                <a href="')
                        __M_writer(conditional_websafe(docs["source_root_url"]))
                        __M_writer(conditional_websafe(docs['relfilepath']))
                        __M_writer(u'#L')
                        __M_writer(conditional_websafe(docs['lineno']))
                        __M_writer(u'">view code</a>\n')
                    # SOURCE LINE 235
                    __M_writer(u'              <a href="#')
                    __M_writer(conditional_websafe(api_method_id(uri, method)))
                    __M_writer(u'">#</a>\n            </div>\n            <h3>\n              <span class="method">')
                    # SOURCE LINE 238
                    __M_writer(conditional_websafe(method))
                    __M_writer(u'&nbsp;</span>\n              ')
                    # SOURCE LINE 239
                    __M_writer(conditional_websafe(api_uri_with_sr_maybe(uri, in_subreddit)))
                    __M_writer(u'\n')
                    # SOURCE LINE 240
                    if docs['oauth_scopes']:
                        # SOURCE LINE 241
                        __M_writer(u'                <span class="oauth-scope-list">\n')
                        # SOURCE LINE 242
                        for scope in docs['oauth_scopes']:
                            # SOURCE LINE 243
                            __M_writer(u'                    <a href="https://github.com/reddit/reddit/wiki/OAuth2">\n                        <span class="api-badge oauth-scope">')
                            # SOURCE LINE 244
                            __M_writer(conditional_websafe(scope or "any"))
                            __M_writer(u'</span>\n                    </a>\n')
                        # SOURCE LINE 247
                        __M_writer(u'                </span>\n')
                    # SOURCE LINE 249
                    if docs['supports_rss']:
                        # SOURCE LINE 250
                        __M_writer(u'                <a href="https://www.reddit.com/wiki/rss">\n                    <span class="api-badge rss-support">rss support</span>\n                </a>\n')
                    # SOURCE LINE 254
                    __M_writer(u'            </h3>\n')
                    # SOURCE LINE 255
                    if 'uri_variants' in docs:
                        # SOURCE LINE 256
                        __M_writer(u'              <ul class="uri-variants">\n')
                        # SOURCE LINE 257
                        for variant in docs['uri_variants']:
                            # SOURCE LINE 258
                            __M_writer(u'                <li id="')
                            __M_writer(conditional_websafe(api_method_id(variant, method)))
                            __M_writer(u'">&rarr; ')
                            __M_writer(conditional_websafe(api_uri_with_sr_maybe(variant, in_subreddit)))
                            __M_writer(u'</li>\n')
                        # SOURCE LINE 260
                        __M_writer(u'              </ul>\n')
                    # SOURCE LINE 262
                    __M_writer(u'            <div class="info">\n              ')
                    # SOURCE LINE 263
                    __M_writer(conditional_websafe(unsafe(safemarkdown(docs.get('doc')))))
                    __M_writer(u'\n              ')
                    # SOURCE LINE 264

                    json_model = docs.get('json_model')
                    if json_model:
                      params = None
                      base_params = None
                    else:
                      params = docs.get('parameters')
                      base_params = extends.get('parameters') if extends else None
                                  
                    
                    __M_locals_builtin_stored = __M_locals_builtin()
                    __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['params','json_model','base_params'] if __M_key in __M_locals_builtin_stored]))
                    # SOURCE LINE 272
                    __M_writer(u'\n')
                    # SOURCE LINE 273
                    if params or base_params or json_model:
                        # SOURCE LINE 274
                        __M_writer(u'                <table class="parameters">\n')
                        # SOURCE LINE 275
                        if params:
                            # SOURCE LINE 276
                            for param in sorted(params):
                                # SOURCE LINE 277
                                __M_writer(u'                    <tr>\n                      <th scope="row">')
                                # SOURCE LINE 278
                                __M_writer(conditional_websafe(param))
                                __M_writer(u'</th>\n                      <td>')
                                # SOURCE LINE 279
                                __M_writer(conditional_websafe(unsafe(safemarkdown(params[param], wrap=False))))
                                __M_writer(u'</td>\n                    </tr>\n')
                        # SOURCE LINE 283
                        if base_params:
                            # SOURCE LINE 284
                            for param in sorted(base_params):
                                # SOURCE LINE 285
                                if param not in params:
                                    # SOURCE LINE 286
                                    __M_writer(u'                      <tr class="base-param">\n                        <th scope="row">')
                                    # SOURCE LINE 287
                                    __M_writer(conditional_websafe(param))
                                    __M_writer(u'</th>\n                        <td>')
                                    # SOURCE LINE 288
                                    __M_writer(conditional_websafe(unsafe(safemarkdown(base_params[param], wrap=False))))
                                    __M_writer(u'</td>\n                      </tr>\n')
                        # SOURCE LINE 293
                        if json_model:
                            # SOURCE LINE 294
                            __M_writer(u'                  <tr class="json-model">\n                    <th>')
                            # SOURCE LINE 295
                            __M_writer(conditional_websafe(_("This endpoint expects JSON data of this format")))
                            __M_writer(u'</th>\n                    <td>')
                            # SOURCE LINE 296
                            __M_writer(conditional_websafe(unsafe(safemarkdown(json_model.docs_model(), wrap=False))))
                            __M_writer(u'</td>\n                  </tr>\n')
                        # SOURCE LINE 299
                        __M_writer(u'                </table>\n')
                    # SOURCE LINE 301
                    __M_writer(u'            </div>\n          </div>\n')
        # SOURCE LINE 306
        __M_writer(u'  </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_api_uri(context,uri):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 32
        __M_writer(conditional_websafe(unsafe(re.sub(r'{(\w+)}', r'<em class="placeholder">\1</em>', uri))))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_mode_selector(context,current_mode):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 35
        __M_writer(u'\n  <span class="mode-selector">\n    <a class="mode ')
        # SOURCE LINE 37
        __M_writer(conditional_websafe('mode-current' if current_mode == 'section' else ''))
        __M_writer(u'"\n       href="/dev/api">by section</a>\n    <a class="mode ')
        # SOURCE LINE 39
        __M_writer(conditional_websafe('mode-current' if current_mode == 'oauth' else ''))
        __M_writer(u'"\n       href="/dev/api/oauth">by oauth scope</a>\n  </span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_api_method_toc(context,api):
    __M_caller = context.caller_stack._push_frame()
    try:
        def api_uri(uri):
            return render_api_uri(context,uri)
        sorted = context.get('sorted', UNDEFINED)
        def api_method_id(uri,method):
            return render_api_method_id(context,uri,method)
        def mode_selector(current_mode):
            return render_mode_selector(context,current_mode)
        any = context.get('any', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 44
        __M_writer(u'\n  <strong>API methods</strong>\n  ')
        # SOURCE LINE 46
        __M_writer(conditional_websafe(mode_selector('section')))
        __M_writer(u'\n  <ul>\n')
        # SOURCE LINE 48
        for section in sorted(api):
            # SOURCE LINE 49
            __M_writer(u'    <li>\n      <a href="#section_')
            # SOURCE LINE 50
            __M_writer(conditional_websafe(section))
            __M_writer(u'" class="section">')
            __M_writer(conditional_websafe(section_info[section]['title']))
            __M_writer(u'</a>\n      <ul>\n')
            # SOURCE LINE 52
            for uri in sorted(api[section]):
                # SOURCE LINE 53
                __M_writer(u'          ')

                methods = sorted(api[section][uri].keys())
                has_oauth = any(api[section][uri][method]['oauth_scopes']
                                for method in methods)
                          
                
                # SOURCE LINE 57
                __M_writer(u'\n          <li class="')
                # SOURCE LINE 58
                __M_writer(conditional_websafe('supports-oauth' if has_oauth else ''))
                __M_writer(u'">\n            <a href="#')
                # SOURCE LINE 59
                __M_writer(conditional_websafe(api_method_id(uri, methods[0])))
                __M_writer(u'">')
                __M_writer(conditional_websafe(api_uri(uri)))
                __M_writer(u'</a>\n          </li>\n')
            # SOURCE LINE 62
            __M_writer(u'      </ul>\n    </li>\n')
        # SOURCE LINE 65
        __M_writer(u'  </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_api_uri_with_sr_maybe(context,uri,in_sr):
    __M_caller = context.caller_stack._push_frame()
    try:
        def api_uri(uri):
            return render_api_uri(context,uri)
        __M_writer = context.writer()
        # SOURCE LINE 33
        __M_writer(conditional_websafe(api_uri(("[/r/{subreddit}]" if in_sr else "") + uri)))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_oauth_toc(context,api,oauth_index):
    __M_caller = context.caller_stack._push_frame()
    try:
        def api_uri(uri):
            return render_api_uri(context,uri)
        sorted = context.get('sorted', UNDEFINED)
        def api_method_id(uri,method):
            return render_api_method_id(context,uri,method)
        def mode_selector(current_mode):
            return render_mode_selector(context,current_mode)
        __M_writer = context.writer()
        # SOURCE LINE 68
        __M_writer(u'\n  <strong>API methods</strong>\n  ')
        # SOURCE LINE 70
        __M_writer(conditional_websafe(mode_selector('oauth')))
        __M_writer(u'\n  <ul>\n')
        # SOURCE LINE 72
        for scope, keys in sorted(oauth_index.iteritems()):
            # SOURCE LINE 73
            __M_writer(u'    <li>\n      <a href="#scope_')
            # SOURCE LINE 74
            __M_writer(conditional_websafe(scope))
            __M_writer(u'" class="section">')
            __M_writer(conditional_websafe(scope))
            __M_writer(u'</a>\n      <ul>\n')
            # SOURCE LINE 76
            for section, uri, method in sorted(keys):
                # SOURCE LINE 77
                __M_writer(u'          <li>\n            <a href="#')
                # SOURCE LINE 78
                __M_writer(conditional_websafe(api_method_id(uri, method)))
                __M_writer(u'">')
                __M_writer(conditional_websafe(api_uri(uri)))
                __M_writer(u'</a>\n          </li>\n')
            # SOURCE LINE 81
            __M_writer(u'      </ul>\n    </li>\n')
        # SOURCE LINE 84
        __M_writer(u'  </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_scope_header(context,scope):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 96
        __M_writer(u'\n  <h2 id="scope_')
        # SOURCE LINE 97
        __M_writer(conditional_websafe(scope))
        __M_writer(u'">\n    ')
        # SOURCE LINE 98
        __M_writer(conditional_websafe(OAuth2Scope.scope_info[scope]['name']))
        __M_writer(u'\n    <span class="scope-id">')
        # SOURCE LINE 99
        __M_writer(conditional_websafe(scope))
        __M_writer(u'</span>\n  </h2>\n  <div class="description">\n    ')
        # SOURCE LINE 102
        __M_writer(conditional_websafe(unsafe(safemarkdown(OAuth2Scope.scope_info[scope]['description']))))
        __M_writer(u'\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_section_header(context,section):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 87
        __M_writer(u'\n  <h2 id="section_')
        # SOURCE LINE 88
        __M_writer(conditional_websafe(section))
        __M_writer(u'">')
        __M_writer(conditional_websafe(section_info[section]['title']))
        __M_writer(u'</h2>\n')
        # SOURCE LINE 89
        if 'description' in section_info[section]:
            # SOURCE LINE 90
            __M_writer(u'    <div class="description">\n      ')
            # SOURCE LINE 91
            __M_writer(conditional_websafe(unsafe(safemarkdown(section_info[section]['description']))))
            __M_writer(u'\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_api_method_id(context,uri,method):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 31
        __M_writer(conditional_websafe(method))
        __M_writer(u'_')
        __M_writer(conditional_websafe(uri.replace('/', '_').strip('_')))
        return ''
    finally:
        context.caller_stack._pop_frame()


