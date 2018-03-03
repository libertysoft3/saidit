# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1520060827.931079
_enable_loop = True
_template_filename = u'/home/reddit/src/reddit/r2/r2/templates/utils.html'
_template_uri = u'/utils.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['round_field', 'checkbox', 'buffered_timestamp', 'img_link', '_a_buffered', 'form_group', 'pretty_button', 's3_image_upload', 'error_field', 'nsfw_stamp', 'js_setup', 'googleanalytics', 'first_defined', 'thing_timestamp', 'inline_radio_type', 'googletagmanager', 'image_upload', 'post_link', 'block_field', 'quarantine_stamp', 'submit_form', 'percentage', 'plain_link', '_a', 'edited', 'ajax_upload', 'optionalstyle', 'tags', 'timestamp', 'text_with_links', 'radio_type', 'thumbnail_img', 'image_upload_inline', 'line_field', 'logout', 'data', 'md', 'language_tool', 'classes', 'separator', '_mdf', '_md', '_id']


# SOURCE LINE 23

import json
from datetime import datetime

from r2.lib import tracking
from r2.lib.filters import spaceCompress, unsafe, safemarkdown, jssafe, scriptsafe_dumps
from r2.lib.template_helpers import (
    add_sr,
    html_datetime,
    js_config,
    make_url_protocol_relative,
    simplified_timesince,
    static,
)
from r2.lib.utils import long_datetime


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 38
        __M_writer(u'\n')
        # SOURCE LINE 49
        __M_writer(u'\n\n')
        # SOURCE LINE 55
        __M_writer(u'\n\n')
        # SOURCE LINE 59
        __M_writer(u'\n\n\n')
        # SOURCE LINE 65
        __M_writer(u'\n\n')
        # SOURCE LINE 69
        __M_writer(u'\n\n')
        # SOURCE LINE 75
        __M_writer(u'\n\n')
        # SOURCE LINE 89
        __M_writer(u'\n\n')
        # SOURCE LINE 95
        __M_writer(u'\n\n')
        # SOURCE LINE 109
        __M_writer(u'\n\n')
        # SOURCE LINE 119
        __M_writer(u'\n\n')
        # SOURCE LINE 137
        __M_writer(u'\n\n')
        # SOURCE LINE 157
        __M_writer(u'\n\n')
        # SOURCE LINE 175
        __M_writer(u'\n\n\n')
        # SOURCE LINE 189
        __M_writer(u'\n\n')
        # SOURCE LINE 213
        __M_writer(u'\n\n')
        # SOURCE LINE 217
        __M_writer(u'\n\n')
        # SOURCE LINE 223
        __M_writer(u'\n\n')
        # SOURCE LINE 230
        __M_writer(u'\n\n')
        # SOURCE LINE 263
        __M_writer(u'\n\n\n')
        # SOURCE LINE 285
        __M_writer(u'\n\n')
        # SOURCE LINE 318
        __M_writer(u'\n\n')
        # SOURCE LINE 425
        __M_writer(u'\n\n\n')
        # SOURCE LINE 432
        __M_writer(u'\n\n')
        # SOURCE LINE 450
        __M_writer(u'\n\n')
        # SOURCE LINE 528
        __M_writer(u'\n\n')
        # SOURCE LINE 550
        __M_writer(u'\n\n')
        # SOURCE LINE 567
        __M_writer(u'\n\n')
        # SOURCE LINE 573
        __M_writer(u'\n\n')
        # SOURCE LINE 579
        __M_writer(u'\n\n')
        # SOURCE LINE 608
        __M_writer(u'\n\n')
        # SOURCE LINE 623
        __M_writer(u'\n\n')
        # SOURCE LINE 634
        __M_writer(u'\n\n')
        # SOURCE LINE 638
        __M_writer(u'\n\n')
        # SOURCE LINE 644
        __M_writer(u'\n\n')
        # SOURCE LINE 652
        __M_writer(u'\n\n')
        # SOURCE LINE 669
        __M_writer(u'\n\n')
        # SOURCE LINE 677
        __M_writer(u'\n\n')
        # SOURCE LINE 681
        __M_writer(u'\n\n')
        # SOURCE LINE 685
        __M_writer(u'\n\n')
        # SOURCE LINE 689
        __M_writer(u'\n\n')
        # SOURCE LINE 695
        __M_writer(u'\n\n')
        # SOURCE LINE 701
        __M_writer(u'\n\n')
        # SOURCE LINE 720
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_round_field(context,title,description='',css_class='',**kw):
    __M_caller = context.caller_stack._push_frame()
    try:
        def block_field(kind,title,description='',css_class='',**kw):
            return render_block_field(context,kind,title,description,css_class,**kw)
        __M_writer = context.writer()
        # SOURCE LINE 569
        __M_writer(u'\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                # SOURCE LINE 570
                __M_writer(u'\n     ')
                # SOURCE LINE 571
                __M_writer(conditional_websafe(caller.body()))
                __M_writer(u'\n  ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 570
            __M_writer(conditional_websafe(block_field('roundfield', title, description = description, css_class= css_class, **kw)))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 572
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_checkbox(context,name,text,val):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 225
        __M_writer(u'\n  <input type="checkbox" ')
        # SOURCE LINE 226
        __M_writer(conditional_websafe('checked="checked"' if val else ''))
        __M_writer(u'\n    name="')
        # SOURCE LINE 227
        __M_writer(conditional_websafe(name))
        __M_writer(u'">\n    ')
        # SOURCE LINE 228
        __M_writer(conditional_websafe(text))
        __M_writer(u'\n  </input>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_buffered_timestamp(context,date,since=None,live=False,include_tense=False):
    __M_caller = context.caller_stack._push_frame()
    try:
        context._push_buffer()
        def timestamp(date,since=None,live=False,include_tense=False):
            return render_timestamp(context,date,since,live,include_tense)
        __M_writer = context.writer()
        # SOURCE LINE 636
        __M_writer(u'\n  ')
        # SOURCE LINE 637
        __M_writer(conditional_websafe(timestamp(date, since, live, include_tense)))
        __M_writer(u'\n')
    finally:
        __M_buf = context._pop_buffer()
        context.caller_stack._pop_frame()
    return __M_buf.getvalue()


def render_img_link(context,link_text,img,path,_id='',target='',img_id=None,size=None,**kw):
    __M_caller = context.caller_stack._push_frame()
    try:
        def _a(**kw):
            return render__a(context,**kw)
        __M_writer = context.writer()
        # SOURCE LINE 121
        __M_writer(u'\n  ')
        # SOURCE LINE 122
 
        if target:
            kw['target'] = target
        
        path = add_sr(path, sr_path = False)
        kw['target'] = target
        
        if size is None:
            size_str = ""
        else:
            size_str = "width='%d' height='%d'" % (size[0], size[1])
          
        
        # SOURCE LINE 133
        __M_writer(u'\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                # SOURCE LINE 134
                __M_writer(u'\n    <img ')
                # SOURCE LINE 135
                __M_writer(conditional_websafe(("id='%s'" % img_id) if img_id else ''))
                __M_writer(u' src="')
                __M_writer(conditional_websafe(img))
                __M_writer(u'" ')
                __M_writer(conditional_websafe(size_str))
                __M_writer(u' alt="')
                __M_writer(conditional_websafe(link_text))
                __M_writer(u'"/>\n  ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 134
            __M_writer(conditional_websafe(_a(href=path, _id=_id, **kw)))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 136
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render__a_buffered(context,body,**kw):
    __M_caller = context.caller_stack._push_frame()
    try:
        context._push_buffer()
        def tags(**kw):
            return render_tags(context,**kw)
        __M_writer = context.writer()
        # SOURCE LINE 57
        __M_writer(u'\n<a ')
        # SOURCE LINE 58
        __M_writer(conditional_websafe(tags(**kw)))
        __M_writer(u'>')
        __M_writer(conditional_websafe(body))
        __M_writer(u'</a>\n')
    finally:
        __M_buf = context._pop_buffer()
        context.caller_stack._pop_frame()
    return __M_buf.getvalue()


def render_form_group(context,field_name,*args,**kwargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        caller = context.get('caller', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 97
        __M_writer(u'\n  ')
        # SOURCE LINE 98
        error = c.errors.get_first(field_name, *args) 
        
        __M_writer(u'\n  <div class="c-form-group ')
        # SOURCE LINE 99
        __M_writer(conditional_websafe('c-has-feedback c-has-error' if (error and kwargs['show_errors']) else ''))
        __M_writer(u'">\n    ')
        # SOURCE LINE 100
        __M_writer(conditional_websafe(caller.body()))
        __M_writer(u'\n')
        # SOURCE LINE 101
        if kwargs['show_errors']:
            # SOURCE LINE 102
            __M_writer(u'      <div class="c-form-control-feedback-wrapper ')
            __M_writer(conditional_websafe('inside-input' if kwargs.get('feedback_inside_input') else ''))
            __M_writer(u'">\n        <span class="c-form-control-feedback c-form-control-feedback-throbber"></span>\n        <span class="c-form-control-feedback c-form-control-feedback-error" title="')
            # SOURCE LINE 104
            __M_writer(conditional_websafe(_(error.message) if error else ''))
            __M_writer(u'"></span>\n        <span class="c-form-control-feedback c-form-control-feedback-success"></span>\n      </div>\n')
        # SOURCE LINE 108
        __M_writer(u'  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_pretty_button(context,label,func=None,func_vars='',extra_class='',event_action=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 654
        __M_writer(u'\n  <a class="pretty-button access-required ')
        # SOURCE LINE 655
        __M_writer(conditional_websafe(extra_class))
        __M_writer(u'" href="#"\n')
        # SOURCE LINE 656
        if func is None:
            # SOURCE LINE 657
            __M_writer(u'       onclick="alert(\'please don\\\'t do that again\');return false;"\n')
            # SOURCE LINE 658
        elif func_vars:
            # SOURCE LINE 659
            __M_writer(u'       onclick="return ')
            __M_writer(conditional_websafe(func))
            __M_writer(u'($(this), ')
            __M_writer(conditional_websafe(func_vars))
            __M_writer(u')"\n')
            # SOURCE LINE 660
        else:
            # SOURCE LINE 661
            __M_writer(u'       onclick="return ')
            __M_writer(conditional_websafe(func))
            __M_writer(u'($(this))"\n')
        # SOURCE LINE 663
        if event_action:
            # SOURCE LINE 664
            __M_writer(u'       data-event-action="')
            __M_writer(conditional_websafe(event_action))
            __M_writer(u'"\n')
        # SOURCE LINE 666
        __M_writer(u'     >\n       ')
        # SOURCE LINE 667
        __M_writer(conditional_websafe(label))
        __M_writer(u'\n  </a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_s3_image_upload(context,id,width,height,src=None,data=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        caller = context.get('caller', UNDEFINED)
        dict = context.get('dict', UNDEFINED)
        def tags(**kw):
            return render_tags(context,**kw)
        __M_writer = context.writer()
        # SOURCE LINE 287
        __M_writer(u'\n  <form\n      id="')
        # SOURCE LINE 289
        __M_writer(conditional_websafe(id))
        __M_writer(u'"\n      class="c-image-upload"\n      method="POST"\n      enctype="multipart/form-data"\n      target="')
        # SOURCE LINE 293
        __M_writer(conditional_websafe(id))
        __M_writer(u'-frame"\n      ')
        # SOURCE LINE 294
        __M_writer(conditional_websafe(tags(**dict(data=data))))
        __M_writer(u'\n    >\n    <div class="c-image-upload-preview-container">\n      <img\n        alt="')
        # SOURCE LINE 298
        __M_writer(conditional_websafe(id))
        __M_writer(u' preview"\n        class="c-image-upload-preview"\n        style="width: ')
        # SOURCE LINE 300
        __M_writer(conditional_websafe(width))
        __M_writer(u'px; max-height: ')
        __M_writer(conditional_websafe(height))
        __M_writer(u'px"\n')
        # SOURCE LINE 301
        if src:
            # SOURCE LINE 302
            __M_writer(u'          src="')
            __M_writer(conditional_websafe(make_url_protocol_relative(src)))
            __M_writer(u'"\n')
            # SOURCE LINE 303
        else:
            # SOURCE LINE 304
            __M_writer(u'          src="')
            __M_writer(conditional_websafe(static(width + 'x' + height + '-placeholder.png')))
            __M_writer(u'"\n')
        # SOURCE LINE 306
        __M_writer(u'      >\n      <input type="file" name="file" id="')
        # SOURCE LINE 307
        __M_writer(conditional_websafe(id))
        __M_writer(u'-input" class="c-image-upload-input" title="')
        __M_writer(conditional_websafe(_("click to upload")))
        __M_writer(u'">\n      <div class="c-progress">\n        <div class="c-progress-bar"></div>\n      </div>\n    </div>\n    <button class="c-image-upload-btn" type="button">')
        # SOURCE LINE 312
        __M_writer(conditional_websafe(_("select")))
        __M_writer(u'</button>\n  </form>\n  <iframe id="')
        # SOURCE LINE 314
        __M_writer(conditional_websafe(id))
        __M_writer(u'-frame" name="')
        __M_writer(conditional_websafe(id))
        __M_writer(u'-frame" src="about:blank" style="display:none;"></iframe>\n')
        # SOURCE LINE 315
        if caller:
            # SOURCE LINE 316
            __M_writer(u'    ')
            __M_writer(conditional_websafe(caller.body()))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_error_field(context,error_name,field_name,kind='span'):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 111
        __M_writer(u'\n  ')
        # SOURCE LINE 112
        error_key = (error_name, field_name) 
        
        __M_writer(u'\n  <')
        # SOURCE LINE 113
        __M_writer(conditional_websafe(kind))
        __M_writer(u' class="error ')
        __M_writer(conditional_websafe(error_name))
        __M_writer(u' field-')
        __M_writer(conditional_websafe(field_name))
        __M_writer(u'" \n  style="')
        # SOURCE LINE 114
        __M_writer(conditional_websafe('' if error_key in c.errors else 'display:none'))
        __M_writer(u'">\n')
        # SOURCE LINE 115
        if error_key in c.errors:
            # SOURCE LINE 116
            __M_writer(u'     ')
            __M_writer(conditional_websafe(c.errors[error_key].message))
            __M_writer(u'\n')
        # SOURCE LINE 118
        __M_writer(u'  </')
        __M_writer(conditional_websafe(kind))
        __M_writer(u'>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_nsfw_stamp(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 691
        __M_writer(u'\n  <acronym title="')
        # SOURCE LINE 692
        __M_writer(conditional_websafe(_('Adult content: Not Safe For Work')))
        __M_writer(u'">\n    ')
        # SOURCE LINE 693
        __M_writer(conditional_websafe(_("NSFW")))
        __M_writer(u'\n  </acronym>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js_setup(context,extra_config=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 428
        __M_writer(u'\n  <script type="text/javascript" id="config">\n    r.setup(')
        # SOURCE LINE 430
        __M_writer(conditional_websafe(scriptsafe_dumps(js_config(extra_config))))
        __M_writer(u')\n  </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_googleanalytics(context,uitype,is_gold_page=False):
    __M_caller = context.caller_stack._push_frame()
    try:
        thing = context.get('thing', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 452
        __M_writer(u'\n')
        # SOURCE LINE 453
        if (g.googleanalytics or g.googleanalytics_gold) and thing.site_tracking:
            # SOURCE LINE 454
            __M_writer(u'    <script type="text/javascript">\n')
            # SOURCE LINE 455
            if thing.dnt_enabled:
                # SOURCE LINE 456
                __M_writer(u'      if (!window.DO_NOT_TRACK) {\n')
            # SOURCE LINE 458
            __M_writer(u"        window.user_type = '")
            __M_writer(conditional_websafe("guest" if not c.user_is_loggedin else "goldloggedin" if c.user.gold else "loggedin"))
            __M_writer(u"';\n        window.is_gold_page = '")
            # SOURCE LINE 459
            __M_writer(conditional_websafe(is_gold_page))
            __M_writer(u"'.toLowerCase() === 'true';\n")
            # SOURCE LINE 460
            if thing.dnt_enabled:
                # SOURCE LINE 461
                __M_writer(u'      }\n')
            # SOURCE LINE 463
            __M_writer(u'    </script>\n')
        # SOURCE LINE 465
        __M_writer(u'\n')
        # SOURCE LINE 466
        if g.googleanalytics and thing.site_tracking:
            # SOURCE LINE 468
            __M_writer(u'  <script type="text/javascript">\n')
            # SOURCE LINE 469
            if thing.dnt_enabled:
                # SOURCE LINE 470
                __M_writer(u'    if (!window.DO_NOT_TRACK) {\n')
            # SOURCE LINE 472
            __M_writer(u"      var _gaq = _gaq || [];\n      _gaq.push(\n          ['_require', 'inpage_linkid', '//www.google-analytics.com/plugins/ga/inpage_linkid.js'],\n          ['_setAccount', '")
            # SOURCE LINE 475
            __M_writer(conditional_websafe(g.googleanalytics))
            __M_writer(u"'],\n          ['_setDomainName', '")
            # SOURCE LINE 476
            __M_writer(conditional_websafe(g.domain))
            __M_writer(u"'],\n          ['_setCustomVar', 1, 'site', '")
            # SOURCE LINE 477
            __M_writer(conditional_websafe(tracking.get_site()))
            __M_writer(u"', 3],\n          ['_setCustomVar', 2, 'srpath', '")
            # SOURCE LINE 478
            __M_writer(conditional_websafe(tracking.get_srpath()))
            __M_writer(u"', 3],\n          ['_setCustomVar', 3, 'usertype', user_type, 2],\n          ['_setCustomVar', 4, 'uitype', '")
            # SOURCE LINE 480
            __M_writer(conditional_websafe(uitype))
            __M_writer(u"', 3],\n          ['_setCustomVar', 5, 'style_override', '")
            # SOURCE LINE 481
            __M_writer(conditional_websafe(jssafe(c.user.pref_default_theme_sr)))
            __M_writer(u"', 2],\n")
            # SOURCE LINE 482
            if g.googleanalytics_sample_rate:
                # SOURCE LINE 483
                __M_writer(u"          ['_setSampleRate', '")
                __M_writer(conditional_websafe(g.googleanalytics_sample_rate))
                __M_writer(u"'],\n")
            # SOURCE LINE 485
            __M_writer(u"          ['_trackPageview']\n      );\n\n      (function() {\n        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;\n        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';\n        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);\n      })();\n")
            # SOURCE LINE 493
            if thing.dnt_enabled:
                # SOURCE LINE 494
                __M_writer(u'    }\n')
            # SOURCE LINE 496
            __M_writer(u'  </script>\n')
        # SOURCE LINE 498
        __M_writer(u'\n')
        # SOURCE LINE 499
        if g.googleanalytics_gold and thing.site_tracking:
            # SOURCE LINE 501
            __M_writer(u'  <script type="text/javascript">\n')
            # SOURCE LINE 502
            if thing.dnt_enabled:
                # SOURCE LINE 503
                __M_writer(u'    if (!window.DO_NOT_TRACK) {\n')
            # SOURCE LINE 505
            __M_writer(u"      (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){\n      (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),\n      m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)\n      })(window,document,'script','//www.google-analytics.com/analytics.js','_ga');\n\n      window._ga('create', '")
            # SOURCE LINE 510
            __M_writer(conditional_websafe(g.googleanalytics_gold))
            __M_writer(u"', {\n        'name': 'goldTracker',\n        'cookieDomain': '")
            # SOURCE LINE 512
            __M_writer(conditional_websafe(g.domain))
            __M_writer(u"',\n        '1': '")
            # SOURCE LINE 513
            __M_writer(conditional_websafe(tracking.get_site()))
            __M_writer(u"',\n        '2': '")
            # SOURCE LINE 514
            __M_writer(conditional_websafe(tracking.get_srpath()))
            __M_writer(u"',\n        '3': window.user_type,\n        '4': '")
            # SOURCE LINE 516
            __M_writer(conditional_websafe(uitype))
            __M_writer(u"',\n        'sampleRate': ")
            # SOURCE LINE 517
            __M_writer(conditional_websafe(g.googleanalytics_sample_rate_gold))
            __M_writer(u"\n      });\n\n      if (window.is_gold_page) {\n        window._ga('goldTracker.send', 'pageview');\n      }\n")
            # SOURCE LINE 523
            if thing.dnt_enabled:
                # SOURCE LINE 524
                __M_writer(u'    }\n')
            # SOURCE LINE 526
            __M_writer(u'  </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_first_defined(context,*kw):
    __M_caller = context.caller_stack._push_frame()
    try:
        def first_defined(*kw):
            return render_first_defined(context,*kw)
        __M_writer = context.writer()
        # SOURCE LINE 91
        __M_writer(u'\n')
        # SOURCE LINE 92
        if not kw or kw[0] == UNDEFINED or not kw[0]:
            # SOURCE LINE 93
            __M_writer(conditional_websafe(first_defined(kw[1:])))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_thing_timestamp(context,thing,since=None,live=False,include_tense=False):
    __M_caller = context.caller_stack._push_frame()
    try:
        def timestamp(date,since=None,live=False,include_tense=False):
            return render_timestamp(context,date,since,live,include_tense)
        __M_writer = context.writer()
        # SOURCE LINE 640
        __M_writer(u'\n')
        # SOURCE LINE 643
        __M_writer(u'  ')
        __M_writer(conditional_websafe(timestamp(thing._date, since=since, live=live, include_tense=include_tense)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_inline_radio_type(context,field_name,val_name,text=None,checked=False):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 610
        __M_writer(u'\n\t')
        # SOURCE LINE 611
        full_name = field_name + "_" + val_name 
        
        __M_writer(u'\n\t<label>\n\t<input class="nomargin" type="radio" name="')
        # SOURCE LINE 613
        __M_writer(conditional_websafe(field_name))
        __M_writer(u'"\n\t\tid="')
        # SOURCE LINE 614
        __M_writer(conditional_websafe(full_name))
        __M_writer(u'" value="')
        __M_writer(conditional_websafe(val_name))
        __M_writer(u'"\n')
        # SOURCE LINE 615
        if checked:
            # SOURCE LINE 616
            __M_writer(u'\t\t\tchecked="checked"\n')
        # SOURCE LINE 618
        __M_writer(u'\t>\n')
        # SOURCE LINE 619
        if text:
            # SOURCE LINE 620
            __M_writer(u'\t\t')
            __M_writer(conditional_websafe(text))
            __M_writer(u'\n')
        # SOURCE LINE 622
        __M_writer(u'\t</label>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_googletagmanager(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        thing = context.get('thing', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 434
        __M_writer(u'\n')
        # SOURCE LINE 435
        if g.googletagmanager and thing.site_tracking and thing.dnt_enabled:
            # SOURCE LINE 436
            __M_writer(u"    <script>\n      if (!window.DO_NOT_TRACK) {\n        var frame = document.createElement('iframe');\n\n        frame.style.display = 'none';\n        frame.referrer = 'no-referrer';\n        frame.id = 'gtm-jail';\n        frame.name = JSON.stringify({ subreddit: r.config.post_site });\n        frame.src = '//' + ")
            # SOURCE LINE 444
            __M_writer(conditional_websafe(scriptsafe_dumps(g.media_domain)))
            __M_writer(u" + '/gtm/jail';\n\n        document.body.appendChild(frame);\n      }\n    </script>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_image_upload(context,post_target,current_image=None,onsubmit='',onchange='',label='',form_id='image-upload',ask_type=False,hidden_data=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        caller = context.get('caller', UNDEFINED)
        def error_field(error_name,field_name,kind='span'):
            return render_error_field(context,error_name,field_name,kind)
        __M_writer = context.writer()
        # SOURCE LINE 322
        __M_writer(u'\n  <form id="')
        # SOURCE LINE 323
        __M_writer(conditional_websafe(form_id))
        __M_writer(u'" enctype="multipart/form-data"\n        class="image-upload"\n        target="upload-iframe"\n')
        # SOURCE LINE 326
        if onsubmit:
            # SOURCE LINE 327
            __M_writer(u'           onsubmit="')
            __M_writer(conditional_websafe(onsubmit))
            __M_writer(u'"\n')
        # SOURCE LINE 329
        __M_writer(u'        action="')
        __M_writer(conditional_websafe(post_target))
        __M_writer(u'" method="post">\n')
        # SOURCE LINE 330
        if label:
            # SOURCE LINE 331
            __M_writer(u'         <label for="file">')
            __M_writer(conditional_websafe(label))
            __M_writer(u'</label>\n         <br>\n')
        # SOURCE LINE 334
        __M_writer(u'          <input type="hidden" name="uh" value="')
        __M_writer(conditional_websafe(c.modhash))
        __M_writer(u'" />\n')
        # SOURCE LINE 335
        if not c.default_sr:
            # SOURCE LINE 336
            __M_writer(u'            <input type="hidden" name="r"  value="')
            __M_writer(conditional_websafe(c.site.name))
            __M_writer(u'" />\n')
        # SOURCE LINE 338
        __M_writer(u'          <input type="hidden" name="formid" value="')
        __M_writer(conditional_websafe(form_id))
        __M_writer(u'" />\n')
        # SOURCE LINE 339
        if hidden_data:
            # SOURCE LINE 340
            for name, value in hidden_data.iteritems():
                # SOURCE LINE 341
                __M_writer(u'              <input type="hidden" name="')
                __M_writer(conditional_websafe(name))
                __M_writer(u'" value="')
                __M_writer(conditional_websafe(value))
                __M_writer(u'" />\n')
        # SOURCE LINE 344
        if ask_type:
            # SOURCE LINE 345
            __M_writer(u'            <label for="img_type">')
            __M_writer(conditional_websafe(_("Type: ")))
            __M_writer(u'</label>\n            <label><input type="radio" name="img_type" value="jpg" />JPEG</label>\n            &nbsp;&nbsp;\n            <label><input type="radio" name="img_type" checked value="png" />PNG</label>\n            <br/>\n')
        # SOURCE LINE 351
        __M_writer(u'          <input type="file" name="file" id="file" \n                 onchange="$(this).next().prop(\'disabled\', false); ')
        # SOURCE LINE 352
        __M_writer(conditional_websafe(onchange))
        __M_writer(u'"/>\n          <button id="submit-img" class="submit-img primary-button"\n                  type="submit" name="upload" \n                  onclick="$(this).parent().addClass(\'uploading\').find(\'.img-status\').show().text(\'')
        # SOURCE LINE 355
        __M_writer(conditional_websafe(jssafe(_('uploading'))))
        __M_writer(u'\'); return true;"\n                  disabled>\n            ')
        # SOURCE LINE 357
        __M_writer(conditional_websafe(_('upload')))
        __M_writer(u'\n          </button>\n\n          <span style="display: none;" class="error img-status"></span>\n          ')
        # SOURCE LINE 361
        __M_writer(conditional_websafe(error_field("IMAGE_ERROR", "span")))
        __M_writer(u'\n          <script type="text/javascript">\n       function on_image_success(img) {}\n       function create_new_image(name) {}\n\n       function completedUploadImage(status, img_src, name, errors, form_id) {\n           var form = form_id ? $("#" + form_id) : $(\'form.image-upload.uploading\');\n           form.removeClass(\'uploading\');\n\n           if (status) \n               form.find(".img-status").show().html(status);\n           else\n               form.find(".img-status").hide().html("");\n           $.map(errors, function(e) {\n                   if(e[1]) \n                       form.find("." + e[0]).html(e[1]).show();\n                   else\n                       form.find("." + e[0]).html(\'\').hide();\n               });\n           if(img_src) {\n              form.get(0).reset();\n              var img = (name) ? $("#img-preview-" + name) :\n                  form.find("img.img-preview:first");\n              if(!$.defined(img) || img.length == 0) \n                  img = create_new_image(name);\n              if(img)\n                  img.attr("src", "").attr("src", img_src);\n              img.show().parent().show();\n              form.find(".delete-img").show();\n              on_image_success(img);\n          }\n       }\n          </script>\n          \n          <iframe src="about:blank" width="600" height="200" \n                  style="display: none;"\n                  name="upload-iframe" id="upload-iframe"></iframe>\n\n          <div id="img-preview-container" class="img-preview-container"\n               style="')
        # SOURCE LINE 400
        __M_writer(conditional_websafe('' if current_image else 'display:none;'))
        __M_writer(u'">\n            <img id="img-preview-upload" alt="header preview" \n                 class="img-preview"\n')
        # SOURCE LINE 403
        if current_image:
            # SOURCE LINE 404
            __M_writer(u'                   src="')
            __M_writer(conditional_websafe(make_url_protocol_relative(current_image)))
            __M_writer(u'"\n')
            # SOURCE LINE 405
        else:
            # SOURCE LINE 406
            __M_writer(u'                   src="')
            __M_writer(conditional_websafe(static('kill.png')))
            __M_writer(u'"\n')
        # SOURCE LINE 408
        __M_writer(u'                 /><br />\n          </div>\n')
        # SOURCE LINE 410
        if caller:
            # SOURCE LINE 411
            __M_writer(u'       ')
            __M_writer(conditional_websafe(caller.body()))
            __M_writer(u'\n')
        # SOURCE LINE 413
        __M_writer(u'  </form>\n  <script type="text/javascript">\n    $(function() {\n      var max_width = 0;\n      $(".preftable th *").each(function() {\n        max_width = Math.max(max_width, $(this).width());\n      }).each(function() {\n        $(this).width(max_width);\n      });\n    });\n       \n  </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_post_link(context,link_text,post_path,redir_path,params,_sr_path=True,nocname=False,fmt='',target='',**kw):
    __M_caller = context.caller_stack._push_frame()
    try:
        def _a_buffered(body,**kw):
            return render__a_buffered(context,body,**kw)
        __M_writer = context.writer()
        # SOURCE LINE 160
        __M_writer(u'\n  ')
        # SOURCE LINE 161

        action = add_sr(post_path, sr_path=_sr_path)
        href = add_sr(redir_path, sr_path=_sr_path)
        if target:
            kw['target'] = target
        onclick = "$(this).parent().submit(); return false;"
        link = _a_buffered(link_text, href=href, onclick=onclick, **kw)
          
        
        # SOURCE LINE 168
        __M_writer(u'\n  <form method="POST" action="')
        # SOURCE LINE 169
        __M_writer(conditional_websafe(action))
        __M_writer(u'">\n')
        # SOURCE LINE 170
        for k, v in params.iteritems():
            # SOURCE LINE 171
            __M_writer(u'      <input type="hidden" name="')
            __M_writer(conditional_websafe(k))
            __M_writer(u'" value="')
            __M_writer(conditional_websafe(v))
            __M_writer(u'">\n')
        # SOURCE LINE 173
        __M_writer(u'    ')
        __M_writer(conditional_websafe(unsafe((fmt % link) if fmt else link)))
        __M_writer(u'\n  </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_block_field(context,kind,title,description='',css_class='',**kw):
    __M_caller = context.caller_stack._push_frame()
    try:
        caller = context.get('caller', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 552
        __M_writer(u'\n  <div class="')
        # SOURCE LINE 553
        __M_writer(conditional_websafe(kind))
        __M_writer(u' ')
        __M_writer(conditional_websafe(css_class))
        __M_writer(u'"\n')
        # SOURCE LINE 554
        for k, v in kw.iteritems():
            # SOURCE LINE 555
            __M_writer(u'         ')
            __M_writer(conditional_websafe(k))
            __M_writer(u'="')
            __M_writer(conditional_websafe(v))
            __M_writer(u'"\n')
        # SOURCE LINE 557
        __M_writer(u'       >\n    <span class="title">')
        # SOURCE LINE 558
        __M_writer(conditional_websafe(title))
        __M_writer(u'</span>\n    &#32;\n')
        # SOURCE LINE 560
        if description:
            # SOURCE LINE 561
            __M_writer(u'      <span class="little gray ')
            __M_writer(conditional_websafe(kind))
            __M_writer(u'-description">')
            __M_writer(conditional_websafe(description))
            __M_writer(u'</span>\n')
        # SOURCE LINE 563
        __M_writer(u'    <div class="')
        __M_writer(conditional_websafe(kind))
        __M_writer(u'-content">\n      ')
        # SOURCE LINE 564
        __M_writer(conditional_websafe(caller.body()))
        __M_writer(u'\n    </div>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_quarantine_stamp(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 697
        __M_writer(u'\n  <span title="')
        # SOURCE LINE 698
        __M_writer(conditional_websafe(_('Quarantined content: Content may be highly offensive')))
        __M_writer(u'">\n    ')
        # SOURCE LINE 699
        __M_writer(conditional_websafe(_("Quarantined")))
        __M_writer(u'\n  </span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_submit_form(context,onsubmit='',action='',_class='',method='post',_id='',**params):
    __M_caller = context.caller_stack._push_frame()
    try:
        caller = context.get('caller', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 77
        __M_writer(u'\n<form class="')
        # SOURCE LINE 78
        __M_writer(conditional_websafe(_class or ''))
        __M_writer(u'" onsubmit="')
        __M_writer(conditional_websafe(onsubmit or ''))
        __M_writer(u'" \n      action="')
        # SOURCE LINE 79
        __M_writer(conditional_websafe(action or ''))
        __M_writer(u'" ')
        __M_writer(conditional_websafe(_id and "id='" + _id + "'" or ""))
        __M_writer(u' method="')
        __M_writer(conditional_websafe(method))
        __M_writer(u'"\n      >\n')
        # SOURCE LINE 81
        if c.user_is_loggedin:
            # SOURCE LINE 82
            __M_writer(u'     <input type="hidden" name="uh" value="')
            __M_writer(conditional_websafe(c.modhash))
            __M_writer(u'">\n')
        # SOURCE LINE 84
        for key, value in params.iteritems():
            # SOURCE LINE 85
            __M_writer(u'  <input type="hidden" name="')
            __M_writer(conditional_websafe(key))
            __M_writer(u'" value="')
            __M_writer(conditional_websafe(value))
            __M_writer(u'" />\n')
        # SOURCE LINE 87
        __M_writer(u'  ')
        __M_writer(conditional_websafe(caller.body()))
        __M_writer(u'\n</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_percentage(context,slice,total):
    __M_caller = context.caller_stack._push_frame()
    try:
        int = context.get('int', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 646
        __M_writer(u'\n')
        # SOURCE LINE 647
        if total is None or total == "" or total == 0 or slice is None or slice == "":
            # SOURCE LINE 648
            __M_writer(u'    --\n')
            # SOURCE LINE 649
        else:
            # SOURCE LINE 650
            __M_writer(u'    ')
            __M_writer(conditional_websafe(int(100 * slice / total)))
            __M_writer(u'%\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_plain_link(context,link_text,path,_sr_path=True,nocname=False,fmt='',target='',**kw):
    __M_caller = context.caller_stack._push_frame()
    try:
        def _a_buffered(body,**kw):
            return render__a_buffered(context,body,**kw)
        __M_writer = context.writer()
        # SOURCE LINE 139
        __M_writer(u'\n')
        # SOURCE LINE 147
        __M_writer(u'  ')
 
        if target:
            kw['target'] = target
        
        link = _a_buffered(link_text, 
                           href=path and add_sr(path, sr_path=_sr_path),
                           **kw) 
          
        
        # SOURCE LINE 154
        __M_writer(u'\n\n  ')
        # SOURCE LINE 156
        __M_writer(conditional_websafe(unsafe((fmt % link) if fmt else link)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render__a(context,**kw):
    __M_caller = context.caller_stack._push_frame()
    try:
        caller = context.get('caller', UNDEFINED)
        def tags(**kw):
            return render_tags(context,**kw)
        __M_writer = context.writer()
        # SOURCE LINE 53
        __M_writer(u'\n<a ')
        # SOURCE LINE 54
        __M_writer(conditional_websafe(tags(**kw)))
        __M_writer(u'>')
        __M_writer(conditional_websafe(caller.body()))
        __M_writer(u'</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_edited(context,thing,lastedited=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        isinstance = context.get('isinstance', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 671
        __M_writer(u'\n')
        # SOURCE LINE 672
        if isinstance(thing.editted, datetime):
            # SOURCE LINE 673
            __M_writer(u'    <time class="edited-timestamp" title="')
            __M_writer(conditional_websafe(_('last edited')))
            __M_writer(u' ')
            __M_writer(conditional_websafe(unsafe(lastedited or simplified_timesince(thing.editted))))
            __M_writer(u'" datetime="')
            __M_writer(conditional_websafe(html_datetime(thing.editted)))
            __M_writer(u'">*</time>\n')
            # SOURCE LINE 674
        elif thing.editted:
            # SOURCE LINE 675
            __M_writer(u'    <em>*</em>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_ajax_upload(context,target,form_id):
    __M_caller = context.caller_stack._push_frame()
    try:
        caller = context.get('caller', UNDEFINED)
        def error_field(error_name,field_name,kind='span'):
            return render_error_field(context,error_name,field_name,kind)
        __M_writer = context.writer()
        # SOURCE LINE 232
        __M_writer(u'\n  <form method="post" enctype="multipart/form-data" target="')
        # SOURCE LINE 233
        __M_writer(conditional_websafe(form_id))
        __M_writer(u'-iframe"\n        id="')
        # SOURCE LINE 234
        __M_writer(conditional_websafe(form_id))
        __M_writer(u'" class="ajax-upload-form pretty-form" action="')
        __M_writer(conditional_websafe(target))
        __M_writer(u'"\n        onsubmit="return post_multipart_form(this, \'')
        # SOURCE LINE 235
        __M_writer(conditional_websafe(target))
        __M_writer(u'\')">\n    <input type="hidden" name="id" value="#')
        # SOURCE LINE 236
        __M_writer(conditional_websafe(form_id))
        __M_writer(u'" />\n    <input type="hidden" name="uh" value="')
        # SOURCE LINE 237
        __M_writer(conditional_websafe(c.modhash))
        __M_writer(u'" />\n    <input type="file" name="file" />\n    <button type="submit">\n      ')
        # SOURCE LINE 240
        __M_writer(conditional_websafe(_('upload')))
        __M_writer(u'\n    </button>\n    ')
        # SOURCE LINE 242
        __M_writer(conditional_websafe(error_field('IMAGE_ERROR', '')))
        __M_writer(u'\n')
        # SOURCE LINE 243
        if caller:
            # SOURCE LINE 244
            __M_writer(u'      ')
            __M_writer(conditional_websafe(caller.body()))
            __M_writer(u'\n')
        # SOURCE LINE 246
        __M_writer(u'    <span class="status"></span>\n    <script type="text/javascript">\n      function completedUploadImage (status, img_src, name, errors, form_id) {\n        /* should only be called when the uploaded file is too large */\n        form_id = $.with_default(form_id, "')
        # SOURCE LINE 250
        __M_writer(conditional_websafe(form_id))
        __M_writer(u'");\n        if (status == "failed") {\n          $("#')
        # SOURCE LINE 252
        __M_writer(conditional_websafe(form_id))
        __M_writer(u'").find(".status").html("");\n          for (var i in errors) {\n            $("#')
        # SOURCE LINE 254
        __M_writer(conditional_websafe(form_id))
        __M_writer(u'").find(".error." + errors[i][0])\n                .show().text(errors[i][1]);\n          }\n        }\n      }\n    </script>\n    <iframe src="about:blank" name="')
        # SOURCE LINE 260
        __M_writer(conditional_websafe(form_id))
        __M_writer(u'-iframe" id="')
        __M_writer(conditional_websafe(form_id))
        __M_writer(u'-iframe">\n    </iframe>\n  </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_optionalstyle(context,style):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 219
        __M_writer(u'\n')
        # SOURCE LINE 220
        if request.GET.get('style') != "off":
            # SOURCE LINE 221
            __M_writer(u'    style="')
            __M_writer(conditional_websafe(style))
            __M_writer(u'"\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tags(context,**kw):
    __M_caller = context.caller_stack._push_frame()
    try:
        def data(**data_attrs):
            return render_data(context,**data_attrs)
        __M_writer = context.writer()
        # SOURCE LINE 39
        __M_writer(u'\n')
        # SOURCE LINE 40
        for k, v in kw.iteritems():
            # SOURCE LINE 41
            if v:
                # SOURCE LINE 42
                if k == "data":
                    # SOURCE LINE 43
                    __M_writer(u'      ')
                    __M_writer(conditional_websafe(data(**v)))
                    __M_writer(u'\n')
                    # SOURCE LINE 44
                else:
                    # SOURCE LINE 45
                    __M_writer(u'      ')
                    __M_writer(conditional_websafe(k.strip('_')))
                    __M_writer(u'="')
                    __M_writer(conditional_websafe(v))
                    __M_writer(u'" ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_timestamp(context,date,since=None,live=False,include_tense=False):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 625
        __M_writer(u'\n')
        # SOURCE LINE 628
        __M_writer(u'  ')

        timestamp_class = unsafe(' class="live-timestamp"') if live else ''
          
        
        # SOURCE LINE 630
        __M_writer(u'\n  <time title="')
        # SOURCE LINE 631
        __M_writer(conditional_websafe(long_datetime(date)))
        __M_writer(u'" datetime="')
        __M_writer(conditional_websafe(html_datetime(date)))
        __M_writer(u'"')
        __M_writer(conditional_websafe(timestamp_class))
        __M_writer(u'>\n    ')
        # SOURCE LINE 632
        __M_writer(conditional_websafe((since or simplified_timesince(date, include_tense))))
        __M_writer(u'\n  </time>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_text_with_links(context,txt,_sr_path=False,nocname=False,**kw):
    __M_caller = context.caller_stack._push_frame()
    try:
        capture = context.get('capture', UNDEFINED)
        def plain_link(link_text,path,_sr_path=True,nocname=False,fmt='',target='',**kw):
            return render_plain_link(context,link_text,path,_sr_path,nocname,fmt,target,**kw)
        __M_writer = context.writer()
        # SOURCE LINE 178
        __M_writer(u'\n')
        # SOURCE LINE 179

        from r2.lib.filters import conditional_websafe
        for key, link_args in kw.iteritems():
           link_args.setdefault("_sr_path", _sr_path)
           kw[key]=spaceCompress(capture(plain_link, **link_args))
        txt = conditional_websafe(txt) % kw
        txt = txt.replace(" <", "&#32;<").replace("> ", ">&#32;")
        
        
        
        # SOURCE LINE 187
        __M_writer(u'\n')
        # SOURCE LINE 188
        __M_writer(conditional_websafe(unsafe(txt)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_radio_type(context,field_name,val_name,title,text=None,checked=False,disabled=False,hover_title='[?]',hover_text=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 581
        __M_writer(u'\n  ')
        # SOURCE LINE 582
        full_name = field_name + "_" + val_name 
        
        __M_writer(u'\n  <tr>\n    <td class="nowrap nopadding">\n      <input name="')
        # SOURCE LINE 585
        __M_writer(conditional_websafe(field_name))
        __M_writer(u'" type="radio" id="')
        __M_writer(conditional_websafe(full_name))
        __M_writer(u'"\n             value="')
        # SOURCE LINE 586
        __M_writer(conditional_websafe(val_name))
        __M_writer(u'" class="nomargin"\n')
        # SOURCE LINE 587
        if checked:
            # SOURCE LINE 588
            __M_writer(u'               checked="checked"\n')
        # SOURCE LINE 590
        if disabled:
            # SOURCE LINE 591
            __M_writer(u'               disabled="disabled"\n')
        # SOURCE LINE 593
        __M_writer(u'             />\n      <label for="')
        # SOURCE LINE 594
        __M_writer(conditional_websafe(full_name))
        __M_writer(u'">')
        __M_writer(conditional_websafe(title))
        __M_writer(u'</label>\n')
        # SOURCE LINE 595
        if hover_text:
            # SOURCE LINE 596
            __M_writer(u'      <span class="help help-hoverable">\n        <sup>')
            # SOURCE LINE 597
            __M_writer(conditional_websafe(hover_title))
            __M_writer(u'</sup>\n        <div class="hover-bubble help-bubble anchor-top-left">\n          <p>')
            # SOURCE LINE 599
            __M_writer(conditional_websafe(hover_text))
            __M_writer(u'</p>\n        </div>\n      </span>\n')
        # SOURCE LINE 603
        __M_writer(u'    </td>\n')
        # SOURCE LINE 604
        if text:
            # SOURCE LINE 605
            __M_writer(u'      <td class="leftpad"><span class="gray">')
            __M_writer(conditional_websafe(text))
            __M_writer(u'</span></td>\n')
        # SOURCE LINE 607
        __M_writer(u'  </tr>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_thumbnail_img(context,thing):
    __M_caller = context.caller_stack._push_frame()
    try:
        hasattr = context.get('hasattr', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 703
        __M_writer(u'\n')
        # SOURCE LINE 704
        if thing.thumbnail and not thing.thumbnail_sprited:
            # SOURCE LINE 705
            __M_writer(u'    ')

            if hasattr(thing, 'thumbnail_size'):
                scaling_factor = 1
                if thing.thumbnail_size[0] > g.thumbnail_size[0]:
                  # hidpi scaling, calculate in case hidpi changes definition in the future and
                  # we have multiple sets of image dimensions. Currently should always be 1 or 2.
                  # Width is always the maximum allowed, so we don't need to check height.
                  scaling_factor = thing.thumbnail_size[0] // g.thumbnail_size[0]
            
                size_str = "width='%d' height='%d'" % (thing.thumbnail_size[0] // scaling_factor, thing.thumbnail_size[1] // scaling_factor)
            else:
                size_str = ""
                
            
            # SOURCE LINE 717
            __M_writer(u'\n    <img src="')
            # SOURCE LINE 718
            __M_writer(conditional_websafe(make_url_protocol_relative(thing.thumbnail)))
            __M_writer(u'" ')
            __M_writer(conditional_websafe(size_str))
            __M_writer(u' alt="">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_image_upload_inline(context,form_id='file',field_id='inline-file'):
    __M_caller = context.caller_stack._push_frame()
    try:
        def error_field(error_name,field_name,kind='span'):
            return render_error_field(context,error_name,field_name,kind)
        __M_writer = context.writer()
        # SOURCE LINE 266
        __M_writer(u'\n  <div id="')
        # SOURCE LINE 267
        __M_writer(conditional_websafe(field_id))
        __M_writer(u'">\n    <input type="file" name="')
        # SOURCE LINE 268
        __M_writer(conditional_websafe(form_id))
        __M_writer(u'" id="')
        __M_writer(conditional_websafe(form_id))
        __M_writer(u'">\n    ')
        # SOURCE LINE 269
        __M_writer(conditional_websafe(error_field("IMAGE_ERROR", "span")))
        __M_writer(u"\n    <script>\n      function completedUploadImage (status, img_src, name, errors, form_id) {\n        if (status == 'failed') {\n          var $form = $('#")
        # SOURCE LINE 273
        __M_writer(conditional_websafe(field_id))
        __M_writer(u"');\n          $form.find('.status').html('');\n          for (var i in errors) {\n            $form.find('.error.' + errors[i][0])\n                .show().text(errors[i][1]);\n          }\n          var top = $form.position().top;\n          $(window).scrollTop(top);\n        }\n      }\n    </script>\n  </div>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_line_field(context,title,description='',css_class='',**kw):
    __M_caller = context.caller_stack._push_frame()
    try:
        def block_field(kind,title,description='',css_class='',**kw):
            return render_block_field(context,kind,title,description,css_class,**kw)
        __M_writer = context.writer()
        # SOURCE LINE 575
        __M_writer(u'\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                # SOURCE LINE 576
                __M_writer(u'\n     ')
                # SOURCE LINE 577
                __M_writer(conditional_websafe(caller.body()))
                __M_writer(u'\n  ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 576
            __M_writer(conditional_websafe(block_field('linefield', title, description = description, css_class= css_class, **kw)))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 578
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_logout(context,top=False,dest=None,a_class=''):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 530
        __M_writer(u'\n  <form method="post" action="')
        # SOURCE LINE 531
        __M_writer(conditional_websafe(add_sr('/logout', sr_path=False)))
        __M_writer(u'" class="logout hover"\n')
        # SOURCE LINE 532
        if top:
            # SOURCE LINE 533
            __M_writer(u'      target="_top"\n')
        # SOURCE LINE 535
        __M_writer(u'    >\n    <input type="hidden" name="uh" value="')
        # SOURCE LINE 536
        __M_writer(conditional_websafe(c.modhash))
        __M_writer(u'"/>\n    <input type="hidden" name="top" value="')
        # SOURCE LINE 537
        __M_writer(conditional_websafe('on' if top else 'off'))
        __M_writer(u'"/>\n')
        # SOURCE LINE 538
        if dest:
            # SOURCE LINE 539
            __M_writer(u'      <input type="hidden" name="dest" value="')
            __M_writer(conditional_websafe(dest))
            __M_writer(u'"/>\n')
        # SOURCE LINE 541
        __M_writer(u'    \n    <a href="javascript:void(0)" onclick="$(this).parent().submit()"\n')
        # SOURCE LINE 543
        if a_class:
            # SOURCE LINE 544
            __M_writer(u'         class="')
            __M_writer(conditional_websafe(a_class))
            __M_writer(u'" \n')
        # SOURCE LINE 546
        __M_writer(u'    >\n      ')
        # SOURCE LINE 547
        __M_writer(conditional_websafe(_("logout")))
        __M_writer(u'\n    </a>\n  </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_data(context,**data_attrs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 71
        __M_writer(u'\n')
        # SOURCE LINE 72
        for name, value in data_attrs.iteritems():
            # SOURCE LINE 73
            __M_writer(u'data-')
            __M_writer(conditional_websafe(name))
            __M_writer(u'="')
            __M_writer(conditional_websafe(value))
            __M_writer(u'"\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_md(context,text,wrap=False,**kwargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 679
        __M_writer(u'\n  ')
        # SOURCE LINE 680
        __M_writer(conditional_websafe(unsafe(safemarkdown(text, wrap=wrap, **kwargs))))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_language_tool(context,name='lang',allow_blank=False,default_lang=g.lang,show_regions=False,all_langs=False):
    __M_caller = context.caller_stack._push_frame()
    try:
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 194
        __M_writer(u'\n')
        # SOURCE LINE 195
 
        langs = g.all_languages if all_langs else g.languages 
        if not show_regions:
            langs = [x for x in langs if len(x) == 2]
        
        
        # SOURCE LINE 199
        __M_writer(u'\n')
        # SOURCE LINE 200
        if langs:
            # SOURCE LINE 201
            __M_writer(u'<select id="')
            __M_writer(conditional_websafe(name))
            __M_writer(u'" name="')
            __M_writer(conditional_websafe(name))
            __M_writer(u'">\n')
            # SOURCE LINE 202
            if allow_blank:
                # SOURCE LINE 203
                __M_writer(u'  <option ')
                __M_writer(conditional_websafe((not default_lang) and "selected='selected'" or ""))
                __M_writer(u'>\n  </option>\n')
            # SOURCE LINE 206
            for x in langs:
                # SOURCE LINE 207
                __M_writer(u'  <option ')
                __M_writer(conditional_websafe(x == default_lang  and "selected='selected'" or ""))
                __M_writer(u' value="')
                __M_writer(conditional_websafe(x))
                __M_writer(u'">\n    ')
                # SOURCE LINE 208
                __M_writer(conditional_websafe(g.lang_name[x][0]))
                __M_writer(u' [')
                __M_writer(conditional_websafe(x))
                __M_writer(u'] ')
                __M_writer(conditional_websafe(g.lang_name[x][1]))
                __M_writer(u'\n  </option>\n')
            # SOURCE LINE 211
            __M_writer(u'</select>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_classes(context,*class_names):
    __M_caller = context.caller_stack._push_frame()
    try:
        filter = context.get('filter', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 67
        __M_writer(u'\nclass="')
        # SOURCE LINE 68
        __M_writer(conditional_websafe(" ".join(filter(None, class_names))))
        __M_writer(u'"\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_separator(context,separator_char):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 215
        __M_writer(u'\n  <span class="separator">')
        # SOURCE LINE 216
        __M_writer(conditional_websafe(separator_char))
        __M_writer(u'</span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render__mdf(context,text,wrap=False,**kwargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def md(text,wrap=False,**kwargs):
            return render_md(context,text,wrap,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 687
        __M_writer(u'\n  ')
        # SOURCE LINE 688
        __M_writer(conditional_websafe(md(_(text) % kwargs, wrap=wrap)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render__md(context,text,wrap=False):
    __M_caller = context.caller_stack._push_frame()
    try:
        def md(text,wrap=False,**kwargs):
            return render_md(context,text,wrap,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 683
        __M_writer(u'\n  ')
        # SOURCE LINE 684
        __M_writer(conditional_websafe(md(_(text), wrap=wrap)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render__id(context,arg):
    __M_caller = context.caller_stack._push_frame()
    try:
        thing = context.get('thing', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 63
        __M_writer(u'\nid="')
        # SOURCE LINE 64
        __M_writer(conditional_websafe(arg))
        __M_writer(u'_')
        __M_writer(conditional_websafe(thing and thing._fullname or ''))
        __M_writer(u'"\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


