# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1507094869.52536
_enable_loop = True
_template_filename = u'/home/reddit/src/reddit/r2/r2/templates/utils.xml'
_template_uri = u'/utils.xml'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['atom_author', 'atom_content']


# SOURCE LINE 1

from r2.lib.filters import websafe, keep_space
from r2.lib.template_helpers import add_sr


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n')
        # SOURCE LINE 32
        __M_writer(u'\n\n')
        # SOURCE LINE 44
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_atom_author(context,author):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 34
        __M_writer(u'\n')
        # SOURCE LINE 35
        if not author._deleted:
            # SOURCE LINE 36
            __M_writer(u'        <author>\n            <name>/u/')
            # SOURCE LINE 37
            __M_writer(conditional_websafe(author.name))
            __M_writer(u'</name>\n            <uri>')
            # SOURCE LINE 38
            __M_writer(conditional_websafe(add_sr('/user/'+author.name,
                          sr_path=False,
                          force_hostname=True,
                          retain_extension=False)))
            # SOURCE LINE 41
            __M_writer(u'</uri>\n        </author>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_atom_content(context,type='html',tag_name='content'):
    __M_caller = context.caller_stack._push_frame()
    try:
        capture = context.get('capture', UNDEFINED)
        Exception = context.get('Exception', UNDEFINED)
        caller = context.get('caller', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\n')
        # SOURCE LINE 9
        if type == 'xhtml':
            # SOURCE LINE 10
            __M_writer(u'        <')
            __M_writer(conditional_websafe(tag_name))
            __M_writer(u' type="xhtml" xml:base="')
            __M_writer(conditional_websafe(request.fullpath))
            __M_writer(u'">\n')
            # SOURCE LINE 14
            __M_writer(u'            <div xmlns="http://www.w3.org/1999/xhtml">\n                ')
            # SOURCE LINE 15
            __M_writer(conditional_websafe(caller.body()))
            __M_writer(u'\n            </div>\n        </')
            # SOURCE LINE 17
            __M_writer(conditional_websafe(tag_name))
            __M_writer(u'>\n')
            # SOURCE LINE 18
        elif type == 'html':
            # SOURCE LINE 19
            __M_writer(u'        <')
            __M_writer(conditional_websafe(tag_name))
            __M_writer(u' type="html">\n            ')
            # SOURCE LINE 20

                # this must be double escaped
            full_body = capture(caller.body)
            full_body = websafe(full_body)
                        
            
            # SOURCE LINE 24
            __M_writer(u'\n            ')
            # SOURCE LINE 25
            __M_writer(conditional_websafe(full_body))
            __M_writer(u'\n        </')
            # SOURCE LINE 26
            __M_writer(conditional_websafe(tag_name))
            __M_writer(u'>\n')
            # SOURCE LINE 27
        elif type == 'text':
            # SOURCE LINE 28
            __M_writer(u'        <')
            __M_writer(conditional_websafe(tag_name))
            __M_writer(u'>')
            __M_writer(conditional_websafe(keep_space(caller.body())))
            __M_writer(u'</')
            __M_writer(conditional_websafe(tag_name))
            __M_writer(u'>\n')
            # SOURCE LINE 29
        else:
            # SOURCE LINE 30
            __M_writer(u'        ')
            raise Exception("Unknown html type %r" % (type,)) 
            
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


