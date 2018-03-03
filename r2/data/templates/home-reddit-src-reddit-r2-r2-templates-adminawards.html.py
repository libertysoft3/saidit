# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505799351.190848
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/adminawards.html'
_template_uri = '/adminawards.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['awardbuttons', 'awardtype_radio', 'awardedit']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7ff76f8d3e90', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7ff76f8d3e90')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7ff76f8d3e90')._populate(_import_ns, [u'error_field'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        def awardbuttons(codename):
            return render_awardbuttons(context._locals(__M_locals),codename)
        def awardedit(fullname,title='',awardtype='',codename='',imgurl='',api_ok=False):
            return render_awardedit(context._locals(__M_locals),fullname,title,awardtype,codename,imgurl,api_ok)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n')
        # SOURCE LINE 33
        __M_writer(u'\n\n')
        # SOURCE LINE 41
        __M_writer(u'\n\n')
        # SOURCE LINE 101
        __M_writer(u'\n\n<table class="lined-table">\n <tbody>\n   <tr>\n     <th>fn</th>\n     <th>cn</th>\n     <th>img</th>\n     <th>title</th>\n     <th>type</th>\n     <th>buttons</th>\n   </tr>\n')
        # SOURCE LINE 113
        for award in thing.awards:
            # SOURCE LINE 114
            __M_writer(u'   <tr>\n     <td>')
            # SOURCE LINE 115
            __M_writer(conditional_websafe(award._fullname))
            __M_writer(u'</td>\n     <td>')
            # SOURCE LINE 116
            __M_writer(conditional_websafe(award.codename))
            __M_writer(u'</td>\n     <td><img src="')
            # SOURCE LINE 117
            __M_writer(conditional_websafe(award.imgurl % 40))
            __M_writer(u'"/></td>\n     <td>')
            # SOURCE LINE 118
            __M_writer(conditional_websafe(award.title))
            __M_writer(u'</td>\n     <td>')
            # SOURCE LINE 119
            __M_writer(conditional_websafe(award.awardtype))
            __M_writer(u'</td>\n     <td class="entry">\n       ')
            # SOURCE LINE 121
            __M_writer(conditional_websafe(awardbuttons(award.codename)))
            __M_writer(u'\n       ')
            # SOURCE LINE 122
            __M_writer(conditional_websafe(awardedit(award._fullname, award.title, award.awardtype,
       award.codename, award.imgurl, award.api_ok)))
            # SOURCE LINE 123
            __M_writer(u'\n     </td>\n   </tr>\n')
        # SOURCE LINE 127
        __M_writer(u' </tbody>\n</table>\n\n<button onclick="$(\'#awardedit-NEW\').show()">new award</button>\n\n')
        # SOURCE LINE 132
        __M_writer(conditional_websafe(awardedit("NEW")))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_awardbuttons(context,codename):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7ff76f8d3e90')._populate(_import_ns, [u'error_field'])
        __M_writer = context.writer()
        # SOURCE LINE 25
        __M_writer(u'\n  <ul class="flat-list buttons">\n    <li><a href="#"\n        onclick="$(this).parents(\'td\').find(\'form\').toggle(); return false;">\n        edit</a></li>\n    <li><a href="/admin/awards/')
        # SOURCE LINE 30
        __M_writer(conditional_websafe(codename))
        __M_writer(u'/give">give</a></li>\n    <li><a href="/admin/awards/')
        # SOURCE LINE 31
        __M_writer(conditional_websafe(codename))
        __M_writer(u'/winners">winners</a></li>\n  </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_awardtype_radio(context,val,label,award_fn,current):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7ff76f8d3e90')._populate(_import_ns, [u'error_field'])
        __M_writer = context.writer()
        # SOURCE LINE 35
        __M_writer(u'\n  <input id="awardtype_')
        # SOURCE LINE 36
        __M_writer(conditional_websafe(award_fn))
        __M_writer(u'_')
        __M_writer(conditional_websafe(val))
        __M_writer(u'" class="nomargin"\n         type="radio"  value="')
        # SOURCE LINE 37
        __M_writer(conditional_websafe(val))
        __M_writer(u'" name="awardtype"\n         ')
        # SOURCE LINE 38
        __M_writer(conditional_websafe("checked='checked'" if current == val else ''))
        __M_writer(u' />\n  <label for="awardtype_')
        # SOURCE LINE 39
        __M_writer(conditional_websafe(award_fn))
        __M_writer(u'_')
        __M_writer(conditional_websafe(val))
        __M_writer(u'">')
        __M_writer(conditional_websafe(label))
        __M_writer(u'</label>\n  <br/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_awardedit(context,fullname,title='',awardtype='',codename='',imgurl='',api_ok=False):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7ff76f8d3e90')._populate(_import_ns, [u'error_field'])
        def awardtype_radio(val,label,award_fn,current):
            return render_awardtype_radio(context,val,label,award_fn,current)
        error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 44
        __M_writer(u'\n <form action="/post/editaward" method="post" class="pretty-form medium-text"\n       style="display:none"\n       onsubmit="return post_form(this, \'editaward\');" id="awardedit-')
        # SOURCE LINE 47
        __M_writer(conditional_websafe(fullname))
        __M_writer(u'">\n  <input type="hidden" name="fullname" value="')
        # SOURCE LINE 48
        __M_writer(conditional_websafe(fullname))
        __M_writer(u'" />\n\n  <table class="lined-table borderless">\n    <tr>\n      <td>codename</td>\n      <td>\n        <input type="text" name="codename" value="')
        # SOURCE LINE 54
        __M_writer(conditional_websafe(codename))
        __M_writer(u'" />\n        ')
        # SOURCE LINE 55
        __M_writer(conditional_websafe(error_field("NO_TEXT", "codename", "span")))
        __M_writer(u'\n        ')
        # SOURCE LINE 56
        __M_writer(conditional_websafe(error_field("INVALID_OPTION", "codename", "span")))
        __M_writer(u'\n      </td>\n    </tr>\n    <tr>\n      <td>title</td>\n      <td>\n        <input type="text" name="title" value="')
        # SOURCE LINE 62
        __M_writer(conditional_websafe(title))
        __M_writer(u'" />\n        ')
        # SOURCE LINE 63
        __M_writer(conditional_websafe(error_field("NO_TEXT", "title", "span")))
        __M_writer(u'\n      </td>\n    </tr>\n    <tr>\n      <td>type</td>\n      <td>\n        ')
        # SOURCE LINE 69
        __M_writer(conditional_websafe(awardtype_radio("regular", "regular", fullname, awardtype)))
        __M_writer(u'\n        ')
        # SOURCE LINE 70
        __M_writer(conditional_websafe(awardtype_radio("manual", "manual", fullname, awardtype)))
        __M_writer(u'\n        ')
        # SOURCE LINE 71
        __M_writer(conditional_websafe(awardtype_radio("invisible", "invisible", fullname, awardtype)))
        __M_writer(u'\n        ')
        # SOURCE LINE 72
        __M_writer(conditional_websafe(error_field("NO_TEXT", "awardtype", "span")))
        __M_writer(u'\n      </td>\n    </tr>\n    <tr>\n      <td>API ok?</td>\n      <td>\n        <input name="api_ok" id="award_')
        # SOURCE LINE 78
        __M_writer(conditional_websafe(fullname))
        __M_writer(u'_api_ok"\n          type="checkbox"\n')
        # SOURCE LINE 80
        if api_ok:
            # SOURCE LINE 81
            __M_writer(u'            checked="checked"\n')
        # SOURCE LINE 83
        __M_writer(u'          />\n        <label for="award_')
        # SOURCE LINE 84
        __M_writer(conditional_websafe(fullname))
        __M_writer(u'_api_ok">\n          allow adding/removing this award via API\n        </label>\n      </td>\n    </tr>\n    <tr>\n      <td>img url</td>\n      <td>\n        <input type="text" name="imgurl" value="')
        # SOURCE LINE 92
        __M_writer(conditional_websafe(imgurl))
        __M_writer(u'" />\n        ')
        # SOURCE LINE 93
        __M_writer(conditional_websafe(error_field("NO_TEXT", "imgurl", "span")))
        __M_writer(u'\n        ')
        # SOURCE LINE 94
        __M_writer(conditional_websafe(error_field("BAD_URL", "imgurl", "span")))
        __M_writer(u'\n      </td>\n    </tr>\n  </table>\n  <button class="btn" type="submit">save</button>\n  <span class="status"></span>\n </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


