# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1505003802.168484
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/thingupdater.html'
_template_uri = '/thingupdater.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        thing = context.get('thing', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23

        from r2.lib.filters import scriptsafe_dumps
         
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['scriptsafe_dumps'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 25
        __M_writer(u'\n<script type="text/javascript">\n  (function() {\n    var updates = ')
        # SOURCE LINE 28
        __M_writer(conditional_websafe(scriptsafe_dumps(thing.updates)))
        __M_writer(u";\n\n    if (!updates || !updates.length) {\n      return;\n    }\n\n    var delayedUpdates = [];\n    var update;\n\n    updates.forEach(function(update) {\n      var thing = document.getElementById('thing_' + update.id);\n\n      if (!thing) {\n        return;\n      }\n\n      $(thing).updateThing(update);\n\n      if (update.gilded) {\n        delayedUpdates.push(update);\n      }\n    });\n\n    /* Delay until dom ready because this may be called before r.gold is defined otherwise. */\n    $(function() {\n      delayedUpdates.forEach(function(update) {\n        var gilding_data = update.gilded;\n\n        r.gold.gildThing(update.id, gilding_data[0], gilding_data[1]);\n      });\n    });\n  })();\n</script>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


