# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505844486.660141
_enable_loop = True
_template_filename = u'/home/reddit/src/reddit/r2/r2/templates/prefapps.html'
_template_uri = u'/prefapps.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['authorized_app', 'sr_list', 'developed_app', 'editable_developer', 'scope_details', 'app_type_selector', 'developers', 'icon']


# SOURCE LINE 23

from r2.lib.filters import jssafe
from r2.lib.template_helpers import static, make_url_protocol_relative
from r2.lib.utils import timeuntil


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 30
    ns = runtime.TemplateNamespace('__anon_0x7f211ae2cf10', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f211ae2cf10')] = ns

    # SOURCE LINE 29
    ns = runtime.TemplateNamespace(u'utils', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'utils')] = ns

    # SOURCE LINE 32
    ns = runtime.TemplateNamespace('__anon_0x7f211ad16250', context._clean_inheritance_tokens(), templateuri=u'printablebuttons.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f211ad16250')] = ns

    # SOURCE LINE 31
    ns = runtime.TemplateNamespace('__anon_0x7f211ae2ce50', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f211ae2ce50')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f211ae2cf10')._populate(_import_ns, [u'_md'])
        _mako_get_namespace(context, '__anon_0x7f211ad16250')._populate(_import_ns, [u'ajax_ynbutton', u'ynbutton'])
        _mako_get_namespace(context, '__anon_0x7f211ae2ce50')._populate(_import_ns, [u'error_field', u'plain_link'])
        def authorized_app(app_data):
            return render_authorized_app(context._locals(__M_locals),app_data)
        def developed_app(app,collapsed=True):
            return render_developed_app(context._locals(__M_locals),app,collapsed)
        def app_type_selector(selection='web'):
            return render_app_type_selector(context._locals(__M_locals),selection)
        _md = _import_ns.get('_md', context.get('_md', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 27
        __M_writer(u'\n\n')
        # SOURCE LINE 29
        __M_writer(u'\n')
        # SOURCE LINE 30
        __M_writer(u'\n')
        # SOURCE LINE 31
        __M_writer(u'\n')
        # SOURCE LINE 32
        __M_writer(u'\n\n')
        # SOURCE LINE 40
        __M_writer(u'\n\n')
        # SOURCE LINE 59
        __M_writer(u'\n\n')
        # SOURCE LINE 71
        __M_writer(u'\n\n')
        # SOURCE LINE 82
        __M_writer(u'\n\n')
        # SOURCE LINE 214
        __M_writer(u'\n\n')
        # SOURCE LINE 223
        __M_writer(u'\n\n')
        # SOURCE LINE 270
        __M_writer(u'\n\n')
        # SOURCE LINE 298
        __M_writer(u'\n\n')
        # SOURCE LINE 300
        if thing.my_apps:
            # SOURCE LINE 301
            __M_writer(u'  <h1>')
            __M_writer(conditional_websafe(_("authorized applications")))
            __M_writer(u'</h1>\n\n')
            # SOURCE LINE 303
            for app_data in thing.my_apps.values():
                # SOURCE LINE 304
                __M_writer(u'    ')
                __M_writer(conditional_websafe(authorized_app(app_data)))
                __M_writer(u'\n')
        # SOURCE LINE 307
        __M_writer(u'\n<div id="developed-apps">\n  <h1 style="')
        # SOURCE LINE 309
        __M_writer(conditional_websafe('' if thing.developed_apps else 'display:none'))
        __M_writer(u'">\n    ')
        # SOURCE LINE 310
        __M_writer(conditional_websafe(_("developed applications")))
        __M_writer(u'\n  </h1>\n  <ul>\n')
        # SOURCE LINE 313
        for app in thing.developed_apps:
            # SOURCE LINE 314
            __M_writer(u'      ')
            __M_writer(conditional_websafe(developed_app(app)))
            __M_writer(u'\n')
        # SOURCE LINE 316
        __M_writer(u'  </ul>\n</div>\n\n<div class="edit-app-form">\n  <button id="create-app-button" class="submit-img">\n')
        # SOURCE LINE 321
        if thing.developed_apps:
            # SOURCE LINE 322
            __M_writer(u'      ')
            __M_writer(conditional_websafe(_('create another app...')))
            __M_writer(u'\n')
            # SOURCE LINE 323
        else:
            # SOURCE LINE 324
            __M_writer(u'      ')
            __M_writer(conditional_websafe(_('are you a developer? create an app...')))
            __M_writer(u'\n')
        # SOURCE LINE 326
        __M_writer(u'  </button>\n  <form method="post" action="/api/updateapp" class="pretty-form" id="create-app"\n   onsubmit="')
        # SOURCE LINE 328
        __M_writer(conditional_websafe("return post_form(this, 'updateapp', function(x) {return '%s'})" % jssafe(_("creating..."))))
        __M_writer(u'">\n    <h1>')
        # SOURCE LINE 329
        __M_writer(conditional_websafe(_("create application")))
        __M_writer(u'</h1>\n    <p>')
        # SOURCE LINE 330
        __M_writer(conditional_websafe(_md("Please [read the API usage guidelines](/wiki/api) before creating your application. After creating, you will be required to [register](/wiki/api) for production API use.")))
        __M_writer(u'\n    <input type="hidden" name="uh" value="')
        # SOURCE LINE 331
        __M_writer(conditional_websafe(c.modhash))
        __M_writer(u'" />\n    <table class="content preftable">\n      <tr>\n        <th>')
        # SOURCE LINE 334
        __M_writer(conditional_websafe(_("name")))
        __M_writer(u'</th>\n        <td class="prefright">\n          <input class="text" name="name">\n          ')
        # SOURCE LINE 337
        __M_writer(conditional_websafe(error_field("NO_TEXT", "name")))
        __M_writer(u'\n        </td>\n      </tr>\n      ')
        # SOURCE LINE 340
        __M_writer(conditional_websafe(app_type_selector()))
        __M_writer(u'\n      <tr>\n        <th>')
        # SOURCE LINE 342
        __M_writer(conditional_websafe(_("description")))
        __M_writer(u'</th>\n        <td class="prefright">\n          <textarea name="description"></textarea>\n        </td>\n      </tr>\n      <tr>\n        <th>')
        # SOURCE LINE 348
        __M_writer(conditional_websafe(_("about url")))
        __M_writer(u'</th>\n        <td class="prefright">\n          <input class="text" name="about_url">\n          ')
        # SOURCE LINE 351
        __M_writer(conditional_websafe(error_field("BAD_URL", "about_url")))
        __M_writer(u'\n        </td>\n      </tr>\n      <tr>\n        <th>')
        # SOURCE LINE 355
        __M_writer(conditional_websafe(_("redirect uri")))
        __M_writer(u'</th>\n        <td class="prefright">\n          <input class="text" name="redirect_uri">\n          ')
        # SOURCE LINE 358
        __M_writer(conditional_websafe(error_field("NO_URL", "redirect_uri")))
        __M_writer(u'\n          ')
        # SOURCE LINE 359
        __M_writer(conditional_websafe(error_field("BAD_URL", "redirect_uri")))
        __M_writer(u'\n          ')
        # SOURCE LINE 360
        __M_writer(conditional_websafe(error_field("INVALID_SCHEME", "redirect_uri")))
        __M_writer(u'\n        </td>\n      </tr>\n    </table>\n    <button type="submit">')
        # SOURCE LINE 364
        __M_writer(conditional_websafe(_('create app')))
        __M_writer(u'</button>\n    <span class="status"></span>\n  </form>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_authorized_app(context,app_data):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f211ae2cf10')._populate(_import_ns, [u'_md'])
        _mako_get_namespace(context, '__anon_0x7f211ad16250')._populate(_import_ns, [u'ajax_ynbutton', u'ynbutton'])
        _mako_get_namespace(context, '__anon_0x7f211ae2ce50')._populate(_import_ns, [u'error_field', u'plain_link'])
        ynbutton = _import_ns.get('ynbutton', context.get('ynbutton', UNDEFINED))
        def scope_details(scope,compact=False,expiration=None):
            return render_scope_details(context,scope,compact,expiration)
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        sorted = _import_ns.get('sorted', context.get('sorted', UNDEFINED))
        def developers(app):
            return render_developers(context,app)
        def icon(app):
            return render_icon(context,app)
        __M_writer = context.writer()
        # SOURCE LINE 272
        __M_writer(u'\n  <div id="authorized-app-')
        # SOURCE LINE 273
        __M_writer(conditional_websafe(app_data['client']._id))
        __M_writer(u'" class="authorized-app rounded">\n    ')
        # SOURCE LINE 274
        __M_writer(conditional_websafe(icon(app_data['client'])))
        __M_writer(u'\n    <div class="app-details">\n      <h2>\n')
        # SOURCE LINE 277
        if app_data['client'].about_url:
            # SOURCE LINE 278
            __M_writer(u'        <a href="')
            __M_writer(conditional_websafe(app_data['client'].about_url))
            __M_writer(u'">')
            __M_writer(conditional_websafe(app_data['client'].name))
            __M_writer(u'</a>\n')
            # SOURCE LINE 279
        else:
            # SOURCE LINE 280
            __M_writer(u'        ')
            __M_writer(conditional_websafe(app_data['client'].name))
            __M_writer(u'\n')
        # SOURCE LINE 282
        __M_writer(u'      </h2>\n')
        # SOURCE LINE 284
        for sr in sorted(app_data['scopes']):
            # SOURCE LINE 285
            __M_writer(u'        ')
            __M_writer(conditional_websafe(scope_details(app_data['scopes'][sr], compact=True)))
            __M_writer(u'<br>\n')
        # SOURCE LINE 287
        __M_writer(u'    </div>\n    <div class="app-description">')
        # SOURCE LINE 288
        __M_writer(conditional_websafe(app_data['client'].description))
        __M_writer(u'</div>\n    ')
        # SOURCE LINE 289
        __M_writer(conditional_websafe(developers(app_data['client'])))
        __M_writer(u'\n    ')
        # SOURCE LINE 290
        __M_writer(conditional_websafe(ynbutton(_("revoke access"),
               _("revoked"),
               "revokeapp",
               callback="r.apps.revoked",
               hidden_data=dict(client_id=app_data['client']._id),
               _class="revoke-app-button",
               access_required=False)))
        # SOURCE LINE 296
        __M_writer(u'\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sr_list(context,srs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f211ae2cf10')._populate(_import_ns, [u'_md'])
        _mako_get_namespace(context, '__anon_0x7f211ad16250')._populate(_import_ns, [u'ajax_ynbutton', u'ynbutton'])
        _mako_get_namespace(context, '__anon_0x7f211ae2ce50')._populate(_import_ns, [u'error_field', u'plain_link'])
        sorted = _import_ns.get('sorted', context.get('sorted', UNDEFINED))
        enumerate = _import_ns.get('enumerate', context.get('enumerate', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 216
        __M_writer(u'\n')
        # SOURCE LINE 217
        for i, name in enumerate(sorted(srs)):
            # SOURCE LINE 218
            if i:
                # SOURCE LINE 219
                __M_writer(u'      ,&#32;\n')
            # SOURCE LINE 221
            __M_writer(u'    <a href="/r/')
            __M_writer(conditional_websafe(name))
            __M_writer(u'">/r/')
            __M_writer(conditional_websafe(name))
            __M_writer(u'</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_developed_app(context,app,collapsed=True):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f211ae2cf10')._populate(_import_ns, [u'_md'])
        _mako_get_namespace(context, '__anon_0x7f211ad16250')._populate(_import_ns, [u'ajax_ynbutton', u'ynbutton'])
        _mako_get_namespace(context, '__anon_0x7f211ae2ce50')._populate(_import_ns, [u'error_field', u'plain_link'])
        def editable_developer(app,dev):
            return render_editable_developer(context,app,dev)
        utils = _mako_get_namespace(context, 'utils')
        ynbutton = _import_ns.get('ynbutton', context.get('ynbutton', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        sorted = _import_ns.get('sorted', context.get('sorted', UNDEFINED))
        def developers(app):
            return render_developers(context,app)
        error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
        def icon(app):
            return render_icon(context,app)
        __M_writer = context.writer()
        # SOURCE LINE 84
        __M_writer(u'\n  <li id="developed-app-')
        # SOURCE LINE 85
        __M_writer(conditional_websafe(app._id))
        __M_writer(u'"\n      class="developed-app rounded ')
        # SOURCE LINE 86
        __M_writer(conditional_websafe('collapsed' if collapsed else ''))
        __M_writer(u'">\n    ')
        # SOURCE LINE 87
        __M_writer(conditional_websafe(icon(app)))
        __M_writer(u'\n    <a class="edit-app-button ')
        # SOURCE LINE 88
        __M_writer(conditional_websafe('' if collapsed else 'collapsed'))
        __M_writer(u'"\n       href="javascript:void(0)">\n       ')
        # SOURCE LINE 90
        __M_writer(conditional_websafe(_("edit")))
        __M_writer(u'\n    </a>\n    <div class="app-details">\n      <h2>\n')
        # SOURCE LINE 94
        if app.about_url:
            # SOURCE LINE 95
            __M_writer(u'        <a href="')
            __M_writer(conditional_websafe(app.about_url))
            __M_writer(u'">')
            __M_writer(conditional_websafe(app.name))
            __M_writer(u'</a>\n')
            # SOURCE LINE 96
        else:
            # SOURCE LINE 97
            __M_writer(u'        ')
            __M_writer(conditional_websafe(app.name))
            __M_writer(u'\n')
        # SOURCE LINE 99
        __M_writer(u'      </h2>\n      <h3>\n')
        # SOURCE LINE 101
        if app.app_type == 'web':
            # SOURCE LINE 102
            __M_writer(u'          ')
            __M_writer(conditional_websafe(_("web app")))
            __M_writer(u'\n')
            # SOURCE LINE 103
        elif app.app_type == 'installed':
            # SOURCE LINE 104
            __M_writer(u'          ')
            __M_writer(conditional_websafe(_("installed app")))
            __M_writer(u'\n')
            # SOURCE LINE 105
        elif app.app_type == 'script':
            # SOURCE LINE 106
            __M_writer(u'          ')
            __M_writer(conditional_websafe(_("personal use script")))
            __M_writer(u'\n')
        # SOURCE LINE 108
        __M_writer(u'      </h3>\n      <h3>')
        # SOURCE LINE 109
        __M_writer(conditional_websafe(app._id))
        __M_writer(u'</h3>\n    </div>\n    <div class="app-description">')
        # SOURCE LINE 111
        __M_writer(conditional_websafe(app.description))
        __M_writer(u'</div>\n')
        # SOURCE LINE 112
        if collapsed:
            # SOURCE LINE 113
            __M_writer(u'      ')
            __M_writer(conditional_websafe(developers(app)))
            __M_writer(u'\n')
        # SOURCE LINE 115
        __M_writer(u'    <div class="edit-app ')
        __M_writer(conditional_websafe('collapsed' if collapsed else ''))
        __M_writer(u'">\n      <a class="edit-app-icon-button" href="javascript:void(0)">\n        change icon\n      </a>\n      ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                # SOURCE LINE 120
                __M_writer(u'\n        <input type="hidden" name="client_id" value="')
                # SOURCE LINE 121
                __M_writer(conditional_websafe(app._id))
                __M_writer(u'" />\n        ')
                # SOURCE LINE 122
                __M_writer(conditional_websafe(error_field('TOO_LONG', 'file')))
                __M_writer(u'\n        ')
                # SOURCE LINE 123
                __M_writer(conditional_websafe(error_field('BAD_IMAGE', 'file')))
                __M_writer(u'\n      ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 119
            __M_writer(conditional_websafe(utils.ajax_upload(target=u'/api/setappicon',form_id=u'app-icon-upload-' + (app._id))))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 124
        __M_writer(u'\n      <div class="edit-app-form">\n        <form method="post" action="/api/updateapp" class="pretty-form"\n         id="update-app-')
        # SOURCE LINE 127
        __M_writer(conditional_websafe(app._id))
        __M_writer(u'"\n         onsubmit="')
        # SOURCE LINE 128
        __M_writer(conditional_websafe("return post_form(this, 'updateapp', function(x) {return '%s'})" % jssafe(_("updating..."))))
        __M_writer(u'">\n          <input type="hidden" name="uh" value="')
        # SOURCE LINE 129
        __M_writer(conditional_websafe(c.modhash))
        __M_writer(u'" />\n          <input type="hidden" name="client_id" value="')
        # SOURCE LINE 130
        __M_writer(conditional_websafe(app._id))
        __M_writer(u'" />\n          <input type="hidden" name="app_type" value="')
        # SOURCE LINE 131
        __M_writer(conditional_websafe(app.app_type))
        __M_writer(u'" />\n          <table class="preftable">\n')
        # SOURCE LINE 133
        if app.is_confidential():
            # SOURCE LINE 134
            __M_writer(u'              <tr>\n                <th>')
            # SOURCE LINE 135
            __M_writer(conditional_websafe(_("secret")))
            __M_writer(u'</th>\n                <td class="prefright">')
            # SOURCE LINE 136
            __M_writer(conditional_websafe(app.secret))
            __M_writer(u'</td>\n              </tr>\n')
        # SOURCE LINE 139
        __M_writer(u'            <tr>\n              <th>')
        # SOURCE LINE 140
        __M_writer(conditional_websafe(_("name")))
        __M_writer(u'</th>\n              <td class="prefright">\n                <input class="text" name="name" value="')
        # SOURCE LINE 142
        __M_writer(conditional_websafe(app.name))
        __M_writer(u'">\n                ')
        # SOURCE LINE 143
        __M_writer(conditional_websafe(error_field("NO_TEXT", "name")))
        __M_writer(u'\n              </td>\n            </tr>\n            <tr>\n              <th>')
        # SOURCE LINE 147
        __M_writer(conditional_websafe(_("description")))
        __M_writer(u'</th>\n              <td class="prefright">\n                <textarea name="description">')
        # SOURCE LINE 149
        __M_writer(conditional_websafe(app.description))
        __M_writer(u'</textarea>\n              </td>\n            </tr>\n            <tr>\n              <th>')
        # SOURCE LINE 153
        __M_writer(conditional_websafe(_("about url")))
        __M_writer(u'</th>\n              <td class="prefright">\n                <input class="text" name="about_url" value="')
        # SOURCE LINE 155
        __M_writer(conditional_websafe(app.about_url))
        __M_writer(u'">\n                ')
        # SOURCE LINE 156
        __M_writer(conditional_websafe(error_field("BAD_URL", "about_url")))
        __M_writer(u'\n              </td>\n            </tr>\n            <tr>\n              <th>')
        # SOURCE LINE 160
        __M_writer(conditional_websafe(_("redirect uri")))
        __M_writer(u'</th>\n              <td class="prefright">\n                <input class="text" name="redirect_uri"\n                 value="')
        # SOURCE LINE 163
        __M_writer(conditional_websafe(app.redirect_uri if app.redirect_uri else ''))
        __M_writer(u'">\n                ')
        # SOURCE LINE 164
        __M_writer(conditional_websafe(error_field("NO_URL", "redirect_uri")))
        __M_writer(u'\n                ')
        # SOURCE LINE 165
        __M_writer(conditional_websafe(error_field("BAD_URL", "redirect_uri")))
        __M_writer(u'\n                ')
        # SOURCE LINE 166
        __M_writer(conditional_websafe(error_field("INVALID_SCHEME", "redirect_uri")))
        __M_writer(u'\n              </td>\n            </tr>\n          </table>\n          <button type="submit">')
        # SOURCE LINE 170
        __M_writer(conditional_websafe(_('update app')))
        __M_writer(u'</button>\n          <span class="status"></span>\n        </form>\n      </div>\n      <div class="edit-app-form pretty-form">\n        <table class="preftable">\n          <tr>\n            <th>')
        # SOURCE LINE 177
        __M_writer(conditional_websafe(_("developers")))
        __M_writer(u'</th>\n            <td class="prefright">\n              <ul>\n')
        # SOURCE LINE 180
        for dev in sorted(app._developers, key=lambda d: d.name):
            # SOURCE LINE 181
            __M_writer(u'                  ')
            __M_writer(conditional_websafe(editable_developer(app, dev)))
            __M_writer(u'\n')
        # SOURCE LINE 183
        __M_writer(u'              </ul>\n              <br>\n              <form method="post" action="/api/adddeveloper"\n               class="pretty-form" id="app-developer-')
        # SOURCE LINE 186
        __M_writer(conditional_websafe(app._id))
        __M_writer(u'"\n               onsubmit="')
        # SOURCE LINE 187
        __M_writer(conditional_websafe("return post_form(this, 'adddeveloper', function(x) {return '%s'})" % jssafe(_("adding..."))))
        __M_writer(u'">\n                <input type="hidden" name="uh" value="')
        # SOURCE LINE 188
        __M_writer(conditional_websafe(c.modhash))
        __M_writer(u'" />\n                <input type="hidden" name="client_id" value="')
        # SOURCE LINE 189
        __M_writer(conditional_websafe(app._id))
        __M_writer(u'" />\n                ')
        # SOURCE LINE 190
        __M_writer(conditional_websafe(_('add developer')))
        __M_writer(u': <input class="text" name="name">\n                <br>\n                ')
        # SOURCE LINE 192
        __M_writer(conditional_websafe(error_field('TOO_MANY_DEVELOPERS', '')))
        __M_writer(u'\n                ')
        # SOURCE LINE 193
        __M_writer(conditional_websafe(error_field('OAUTH2_INVALID_CLIENT', 'client_id')))
        __M_writer(u'\n                ')
        # SOURCE LINE 194
        __M_writer(conditional_websafe(error_field('DEVELOPER_ALREADY_ADDED', 'name')))
        __M_writer(u'\n                ')
        # SOURCE LINE 195
        __M_writer(conditional_websafe(error_field('USER_DOESNT_EXIST', 'name')))
        __M_writer(u'\n                ')
        # SOURCE LINE 196
        __M_writer(conditional_websafe(error_field('NO_USER', 'name')))
        __M_writer(u'\n                ')
        # SOURCE LINE 197
        __M_writer(conditional_websafe(error_field('DEVELOPER_FIRST_PARTY_APP', 'name')))
        __M_writer(u'\n                ')
        # SOURCE LINE 198
        __M_writer(conditional_websafe(error_field('DEVELOPER_PRIVILEGED_ACCOUNT', 'name')))
        __M_writer(u'\n                <span class="status"></span>\n              </form>\n            </td>\n          </tr>\n        </table>\n      </div>\n      <div class="delete-app-button">\n        ')
        # SOURCE LINE 206
        __M_writer(conditional_websafe(ynbutton(_("delete app"),
                   "deleted",
                   "deleteapp",
                   callback="r.apps.deleted",
                   hidden_data=dict(client_id=app._id))))
        # SOURCE LINE 210
        __M_writer(u'\n      </div>\n    </div>\n  </li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_editable_developer(context,app,dev):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f211ae2cf10')._populate(_import_ns, [u'_md'])
        _mako_get_namespace(context, '__anon_0x7f211ad16250')._populate(_import_ns, [u'ajax_ynbutton', u'ynbutton'])
        _mako_get_namespace(context, '__anon_0x7f211ae2ce50')._populate(_import_ns, [u'error_field', u'plain_link'])
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        ajax_ynbutton = _import_ns.get('ajax_ynbutton', context.get('ajax_ynbutton', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 73
        __M_writer(u'\n  <li id="app-dev-')
        # SOURCE LINE 74
        __M_writer(conditional_websafe(app._id))
        __M_writer(u'-')
        __M_writer(conditional_websafe(dev._id))
        __M_writer(u'">\n    ')
        # SOURCE LINE 75
        __M_writer(conditional_websafe(dev.name))
        __M_writer(u'&#32;\n')
        # SOURCE LINE 76
        if c.user == dev:
            # SOURCE LINE 77
            __M_writer(u'      <span class="gray">')
            __M_writer(conditional_websafe(_("(that's you!)")))
            __M_writer(u'</span>&#32;\n')
        # SOURCE LINE 79
        __M_writer(u'    ')
        __M_writer(conditional_websafe(ajax_ynbutton(_("remove"), "removedeveloper",
                    hidden_data=dict(client_id=app._id, name=dev.name))))
        # SOURCE LINE 80
        __M_writer(u'\n  </li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_scope_details(context,scope,compact=False,expiration=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f211ae2cf10')._populate(_import_ns, [u'_md'])
        _mako_get_namespace(context, '__anon_0x7f211ad16250')._populate(_import_ns, [u'ajax_ynbutton', u'ynbutton'])
        _mako_get_namespace(context, '__anon_0x7f211ae2ce50')._populate(_import_ns, [u'error_field', u'plain_link'])
        def sr_list(srs):
            return render_sr_list(context,srs)
        __M_writer = context.writer()
        # SOURCE LINE 225
        __M_writer(u'\n  <div class="app-permissions">\n    <ul>\n')
        # SOURCE LINE 228
        if scope.subreddit_only:
            # SOURCE LINE 229
            if compact:
                # SOURCE LINE 230
                __M_writer(u'\t  ')
                __M_writer(conditional_websafe(_("Only in:")))
                __M_writer(u'&#32;\n\t  ')
                # SOURCE LINE 231
                __M_writer(conditional_websafe(sr_list(scope.subreddits)))
                __M_writer(u'\n\t  <br>\n')
                # SOURCE LINE 233
            else:
                # SOURCE LINE 234
                __M_writer(u'          <li>\n            ')
                # SOURCE LINE 235
                __M_writer(conditional_websafe(_("Only in the subreddits:")))
                __M_writer(u'&#32;\n            ')
                # SOURCE LINE 236
                __M_writer(conditional_websafe(sr_list(scope.subreddits)))
                __M_writer(u'.\n          </li>\n')
        # SOURCE LINE 240
        for name, scope_info in scope.details():
            # SOURCE LINE 241
            __M_writer(u'        <li>\n')
            # SOURCE LINE 242
            if compact:
                # SOURCE LINE 243
                __M_writer(u'            ')
                __M_writer(conditional_websafe(scope_info['name']))
                __M_writer(u'\n            <span class="app-scope">')
                # SOURCE LINE 244
                __M_writer(conditional_websafe(scope_info['description']))
                __M_writer(u'</span>\n')
                # SOURCE LINE 245
            else:
                # SOURCE LINE 246
                __M_writer(u'            ')
                __M_writer(conditional_websafe(scope_info['description']))
                __M_writer(u'\n')
            # SOURCE LINE 248
            __M_writer(u'        </li>\n')
        # SOURCE LINE 250
        if not compact:
            # SOURCE LINE 251
            __M_writer(u'        <li>\n')
            # SOURCE LINE 252
            if expiration:
                # SOURCE LINE 253
                __M_writer(u'            ')
                __M_writer(conditional_websafe(_("Expires in:")))
                __M_writer(u'&#32;\n            ')
                # SOURCE LINE 254
                __M_writer(conditional_websafe(timeuntil(expiration)))
                __M_writer(u'\n')
                # SOURCE LINE 255
            else:
                # SOURCE LINE 256
                __M_writer(u'            ')
                __M_writer(conditional_websafe(_("Maintain this access indefinitely"
                " (or until manually revoked).")))
                # SOURCE LINE 257
                __M_writer(u'\n')
            # SOURCE LINE 259
            __M_writer(u'        </li>\n')
        # SOURCE LINE 261
        __M_writer(u'    </ul>\n')
        # SOURCE LINE 262
        if compact and expiration:
            # SOURCE LINE 263
            __M_writer(u'      <div class="app-permissions-details">\n        ')
            # SOURCE LINE 264
            __M_writer(conditional_websafe(_("Expires in:")))
            __M_writer(u'&#32;\n        ')
            # SOURCE LINE 265
            __M_writer(conditional_websafe(timeuntil(expiration)))
            __M_writer(u'\n        <br>\n      </div>\n')
        # SOURCE LINE 269
        __M_writer(u'  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_app_type_selector(context,selection='web'):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f211ae2cf10')._populate(_import_ns, [u'_md'])
        _mako_get_namespace(context, '__anon_0x7f211ad16250')._populate(_import_ns, [u'ajax_ynbutton', u'ynbutton'])
        _mako_get_namespace(context, '__anon_0x7f211ae2ce50')._populate(_import_ns, [u'error_field', u'plain_link'])
        utils = _mako_get_namespace(context, 'utils')
        __M_writer = context.writer()
        # SOURCE LINE 61
        __M_writer(u'\n')
        # SOURCE LINE 62
        __M_writer(conditional_websafe(utils.radio_type('app_type', "web", _("web app"),
                   _("A web based application"),
                   selection == "web")))
        # SOURCE LINE 64
        __M_writer(u'\n')
        # SOURCE LINE 65
        __M_writer(conditional_websafe(utils.radio_type('app_type', "installed", _("installed app"),
                   _("An app intended for installation, such as on a mobile phone"),
                   selection == "installed")))
        # SOURCE LINE 67
        __M_writer(u'\n')
        # SOURCE LINE 68
        __M_writer(conditional_websafe(utils.radio_type('app_type', "script", _("script"),
                   _("Script for personal use. Will only have access to the developers accounts"),
                   selection == "script")))
        # SOURCE LINE 70
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_developers(context,app):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f211ae2cf10')._populate(_import_ns, [u'_md'])
        _mako_get_namespace(context, '__anon_0x7f211ad16250')._populate(_import_ns, [u'ajax_ynbutton', u'ynbutton'])
        _mako_get_namespace(context, '__anon_0x7f211ae2ce50')._populate(_import_ns, [u'error_field', u'plain_link'])
        sorted = _import_ns.get('sorted', context.get('sorted', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        enumerate = _import_ns.get('enumerate', context.get('enumerate', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 42
        __M_writer(u'\n  ')
        # SOURCE LINE 43
        devs = app._developers 
        
        __M_writer(u'\n')
        # SOURCE LINE 44
        if devs:
            # SOURCE LINE 45
            __M_writer(u'    <div class="app-developers">\n      Developers:&#32;\n')
            # SOURCE LINE 47
            for i, dev in enumerate(sorted(devs, key=lambda d: d.name)):
                # SOURCE LINE 48
                if i:
                    # SOURCE LINE 49
                    if i == len(devs) - 1:
                        # SOURCE LINE 50
                        __M_writer(u'            &#32;and&#32;\n')
                        # SOURCE LINE 51
                    else:
                        # SOURCE LINE 52
                        __M_writer(u'            ,&#32;\n')
                # SOURCE LINE 55
                __M_writer(u'        ')
                __M_writer(conditional_websafe(plain_link(dev.name, "/u/" + dev.name)))
                __M_writer(u'\n')
            # SOURCE LINE 57
            __M_writer(u'    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_icon(context,app):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f211ae2cf10')._populate(_import_ns, [u'_md'])
        _mako_get_namespace(context, '__anon_0x7f211ad16250')._populate(_import_ns, [u'ajax_ynbutton', u'ynbutton'])
        _mako_get_namespace(context, '__anon_0x7f211ae2ce50')._populate(_import_ns, [u'error_field', u'plain_link'])
        __M_writer = context.writer()
        # SOURCE LINE 34
        __M_writer(u'\n  <div class="app-icon">\n    &nbsp;\n    <img src="')
        # SOURCE LINE 37
        __M_writer(conditional_websafe(make_url_protocol_relative(app.icon_url) or static('defaultapp.png')))
        __M_writer(u'">\n    &nbsp;\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


