# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1512369675.484429
_enable_loop = True
_template_filename = u'/home/reddit/src/reddit/r2/r2/templates/prefoptions.html'
_template_uri = u'/prefoptions.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['checkbox', 'chat_sidebar_size_options', 'comment_sort_options', 'media_radio', 'media_preview_radio', 'link_options', 'text_input', 'num_input', 'text_input_all', 'theme_item']


# SOURCE LINE 23

from r2.config import feature
from r2.lib.errors import error_list
from r2.lib.menus import CommentSortMenu

## CUSTOM
from r2.lib.menus import ChatSidebarSizeMenu

from r2.lib.template_helpers import add_sr, _wsf, format_html, make_url_protocol_relative
from r2.lib.utils import UrlParser
import random


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 35
    ns = runtime.TemplateNamespace('__anon_0x7fa55a395f90', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fa55a395f90')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fa55a395f90')._populate(_import_ns, [u'md', u'error_field', u'language_tool', u'plain_link'])
        capture = _import_ns.get('capture', context.get('capture', UNDEFINED))
        def checkbox(text,name,disabled=False,disabled_text='',prefix='pref_'):
            return render_checkbox(context._locals(__M_locals),text,name,disabled,disabled_text,prefix)
        def chat_sidebar_size_options():
            return render_chat_sidebar_size_options(context._locals(__M_locals))
        def comment_sort_options():
            return render_comment_sort_options(context._locals(__M_locals))
        def media_preview_radio(val,label):
            return render_media_preview_radio(context._locals(__M_locals),val,label)
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        def link_options():
            return render_link_options(context._locals(__M_locals))
        def media_radio(val,label):
            return render_media_radio(context._locals(__M_locals),val,label)
        language_tool = _import_ns.get('language_tool', context.get('language_tool', UNDEFINED))
        def num_input(s,name):
            return render_num_input(context._locals(__M_locals),s,name)
        def text_input_all(s,name,size,disabled):
            return render_text_input_all(context._locals(__M_locals),s,name,size,disabled)
        def theme_item(thumbnail_url,preview_url,id,tagline,checked):
            return render_theme_item(context._locals(__M_locals),thumbnail_url,preview_url,id,tagline,checked)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 34
        __M_writer(u'\n')
        # SOURCE LINE 35
        __M_writer(u'\n\n')
        # SOURCE LINE 52
        __M_writer(u'\n\n')
        # SOURCE LINE 62
        __M_writer(u'\n\n')
        # SOURCE LINE 74
        __M_writer(u'\n\n\n\n')
        # SOURCE LINE 84
        __M_writer(u'\n\n')
        # SOURCE LINE 92
        __M_writer(u'\n\n')
        # SOURCE LINE 97
        __M_writer(u'\n\n')
        # SOURCE LINE 102
        __M_writer(u'\n\n')
        # SOURCE LINE 108
        __M_writer(u'\n\n')
        # SOURCE LINE 110
        if c.user_is_loggedin:
            # SOURCE LINE 111
            if thing.done:
                # SOURCE LINE 112
                __M_writer(u'    <p class="green">')
                __M_writer(conditional_websafe(_("your preferences have been updated")))
                __M_writer(u'</p>\n')
                # SOURCE LINE 113
            elif thing.error_style_override:
                # SOURCE LINE 114
                __M_writer(u'    <p class="error">')
                __M_writer(conditional_websafe(_("we couldn't save the custom stylesheet preference. please see the error below")))
                __M_writer(u'</p>\n')
                # SOURCE LINE 115
            elif thing.generic_error:
                # SOURCE LINE 116
                __M_writer(u'    <p class="error">')
                __M_writer(conditional_websafe(_("your preferences couldn't be saved")))
                __M_writer(u'</p>\n')
        # SOURCE LINE 119
        __M_writer(u'\n')
        # SOURCE LINE 120

        if c.user_is_loggedin:
            action = "/post/options"
        else:
            action = "/post/unlogged_options"
        action = add_sr(action, sr_path=False)
         
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['action'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 126
        __M_writer(u'\n<form action="')
        # SOURCE LINE 127
        __M_writer(conditional_websafe(action))
        __M_writer(u'" method="post" class="pretty-form short-text">\n  <input type="hidden" name="uh" value="')
        # SOURCE LINE 128
        __M_writer(conditional_websafe(c.modhash))
        __M_writer(u'" />\n<table class="content preftable">\n  <tr>\n    <th>')
        # SOURCE LINE 131
        __M_writer(conditional_websafe(_("interface language")))
        __M_writer(u'</th>\n    <td class="prefright">\n      ')
        # SOURCE LINE 133
        __M_writer(conditional_websafe(language_tool(allow_blank = False, show_regions = True,
                      default_lang = c.user.pref_lang)))
        # SOURCE LINE 134
        __M_writer(u'\n      &#32;<span class="details hover">(*) ')
        # SOURCE LINE 135
        __M_writer(conditional_websafe(_("incomplete")))
        __M_writer(u'\n      &#32;<a href="https://www.reddit.com/r/i18n/wiki/getting_started">')
        # SOURCE LINE 136
        __M_writer(conditional_websafe(_("volunteer to translate")))
        __M_writer(u'</a></span>\n    </td>\n  </tr>\n\n')
        # SOURCE LINE 140
        if c.user_is_loggedin:
            # SOURCE LINE 141
            if not c.user.has_subscribed and (c.user.pref_use_global_defaults or c.user.pref_hide_locationbar):
                # SOURCE LINE 142
                __M_writer(u'    <tr>\n      <th>')
                # SOURCE LINE 143
                __M_writer(conditional_websafe(_("location options")))
                __M_writer(u'</th>\n      <td class="prefright">\n        ')
                # SOURCE LINE 145
                __M_writer(conditional_websafe(checkbox(_("use the global default subreddits for my front page"), "use_global_defaults")))
                __M_writer(u'\n        <br/>\n        ')
                # SOURCE LINE 147
                __M_writer(conditional_websafe(checkbox(_("hide the location information bar"), "hide_locationbar")))
                __M_writer(u'\n      </td>\n    </tr>\n')
            # SOURCE LINE 151
            __M_writer(u'\n  <tr>\n    <th>')
            # SOURCE LINE 153
            __M_writer(conditional_websafe(_("clicking options")))
            __M_writer(u'</th>\n    <td class="prefright">\n      ')
            # SOURCE LINE 155
            __M_writer(conditional_websafe(checkbox(_("open links in a new window"), "newwindow")))
            __M_writer(u'\n    </td>\n  </tr>\n')
            # SOURCE LINE 158
            if thing.feature_autoexpand_media_previews:
                # SOURCE LINE 159
                __M_writer(u'    <tr class="preferences-media">\n')
                # SOURCE LINE 160
            else:
                # SOURCE LINE 161
                __M_writer(u'    <tr>\n')
            # SOURCE LINE 163
            __M_writer(u'    <th>')
            __M_writer(conditional_websafe(_("media")))
            __M_writer(u'</th>\n    <td class="prefright">\n')
            # SOURCE LINE 165
            if thing.feature_autoexpand_media_previews:
                # SOURCE LINE 166
                __M_writer(u'        <h6>')
                __M_writer(conditional_websafe(_("thumbnails")))
                __M_writer(u'</h6>\n')
            # SOURCE LINE 168
            if not c.user.pref_compress:
                # SOURCE LINE 169
                __M_writer(u'        ')
                __M_writer(conditional_websafe(media_radio("on", _("show thumbnails next to links"))))
                __M_writer(u'\n        ')
                # SOURCE LINE 170
                __M_writer(conditional_websafe(media_radio("off", _("don't show thumbnails next to links"))))
                __M_writer(u'\n        ')
                # SOURCE LINE 171
                __M_writer(conditional_websafe(media_radio("subreddit", _("show thumbnails based on that subreddit's media preferences"))))
                __M_writer(u'\n')
                # SOURCE LINE 172
            else:
                # SOURCE LINE 173
                __M_writer(u'        <p class="error">')
                __M_writer(conditional_websafe(_("to enable thumbnails, disable compressed link display")))
                __M_writer(u'</p>\n        <input type="hidden" name="media" value="')
                # SOURCE LINE 174
                __M_writer(conditional_websafe(c.user.pref_media))
                __M_writer(u'"/>\n')
            # SOURCE LINE 176
            if thing.feature_autoexpand_media_previews:
                # SOURCE LINE 177
                __M_writer(u'        <br>\n\n        <h6>')
                # SOURCE LINE 179
                __M_writer(conditional_websafe(_("media previews")))
                __M_writer(u'</h6>\n        ')
                # SOURCE LINE 180
                __M_writer(conditional_websafe(media_preview_radio("on", _("auto-expand media previews"))))
                __M_writer(u'\n        ')
                # SOURCE LINE 181
                __M_writer(conditional_websafe(media_preview_radio("off", _("don't auto-expand media previews on comments pages"))))
                __M_writer(u'\n        ')
                # SOURCE LINE 182
                __M_writer(conditional_websafe(media_preview_radio("subreddit", _("expand media previews based on that subreddit's media preferences"))))
                __M_writer(u'\n        <br>\n\n        <h6>')
                # SOURCE LINE 185
                __M_writer(conditional_websafe(_("NSFW content")))
                __M_writer(u'</h6>\n        ')
                # SOURCE LINE 186
                __M_writer(conditional_websafe(checkbox(_("hide images for NSFW/18+ content "), "no_profanity", disabled = not c.user.pref_over_18, disabled_text = "(requires over 18)")))
                __M_writer(u'\n        &#32;\n        <span class="details">\n          ')
                # SOURCE LINE 189
                __M_writer(conditional_websafe(_("(Don't show thumbnails or media previews for anything labeled NSFW)")))
                __M_writer(u'\n        </span>\n')
                # SOURCE LINE 191
            else:
                # SOURCE LINE 192
                __M_writer(u'        ')
                __M_writer(conditional_websafe(checkbox(_("make safe(r) for work "), "no_profanity", disabled = not c.user.pref_over_18, disabled_text = "(requires over 18)")))
                __M_writer(u'\n        <span class="details">\n          ')
                # SOURCE LINE 194
                __M_writer(conditional_websafe(_("(Don't show thumbnails next to anything labeled NSFW)")))
                __M_writer(u'\n        </span>\n')
            # SOURCE LINE 197
            __M_writer(u'    </td>\n  </tr>\n  <tr>\n    <th>')
            # SOURCE LINE 200
            __M_writer(conditional_websafe(_("link options")))
            __M_writer(u'</th>\n    <td class="prefright">\n      <p>\n        ')
            # SOURCE LINE 203
            __M_writer(conditional_websafe(checkbox(_("show the spotlight box on the front page"), "organic")))
            __M_writer(u'\n        &#32;\n        <span class="details">\n          ')
            # SOURCE LINE 206
            __M_writer(conditional_websafe(_("(it shows new and promoted links, and gives you a say in what's spam and what isn't.)")))
            __M_writer(u'\n        </span>\n      </p>\n      <p>\n        ')
            # SOURCE LINE 210
            __M_writer(conditional_websafe(checkbox(_("show trending subreddits on the front page"), "show_trending")))
            __M_writer(u'\n        &#32;\n        <span class="details">\n          ')
            # SOURCE LINE 213
            __M_writer(conditional_websafe(_("(a list of popular and notable subreddits to check out)")))
            __M_writer(u'\n        </span>\n      </p>\n\n      <p>')
            # SOURCE LINE 217
            __M_writer(conditional_websafe(checkbox(_("show me links I've recently viewed"), "clickgadget")))
            __M_writer(u'</p>\n      <p>')
            # SOURCE LINE 218
            __M_writer(conditional_websafe(checkbox(_("compress the link display"), "compress")))
            __M_writer(u'</p>\n      <p>')
            # SOURCE LINE 219
            __M_writer(conditional_websafe(checkbox(_("show additional details in the domain text when available"), "domain_details")))
            __M_writer(u'\n        &#32;\n        <span class="details">\n          ')
            # SOURCE LINE 222
            __M_writer(conditional_websafe(_("(such as the source subreddit or the content author's url/name)")))
            __M_writer(u'\n        </span>\n      </p>\n      <p>')
            # SOURCE LINE 225
            __M_writer(conditional_websafe(checkbox(_("don't show me submissions after I've upvoted them"), "hide_ups")))
            __M_writer(u'\n         &#32;\n         <span class="details">')
            # SOURCE LINE 227
            __M_writer(conditional_websafe(_("(except my own)")))
            __M_writer(u'</span>\n      </p>\n      <p>')
            # SOURCE LINE 229
            __M_writer(conditional_websafe(checkbox(_("don't show me submissions after I've downvoted them"), "hide_downs")))
            __M_writer(u'\n         &#32;\n         <span class="details">')
            # SOURCE LINE 231
            __M_writer(conditional_websafe(_("(except my own)")))
            __M_writer(u'</span>\n      </p>\n      <p>\n        ')
            # SOURCE LINE 234
            __M_writer(conditional_websafe(_wsf("display %(num)s links at once", num=unsafe(capture(link_options)))))
            __M_writer(u'\n      </p>\n      ')
            # SOURCE LINE 236

            input = unsafe(capture(num_input, c.user.pref_min_link_score,
            'min_link_score'))
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['input'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 239
            __M_writer(u'\n      <p>\n      ')
            # SOURCE LINE 241
            __M_writer(conditional_websafe(_wsf("don't show me submissions with a score less than %(num)s", num=input)))
            __M_writer(u'\n      &#32;<span class="details">')
            # SOURCE LINE 242
            __M_writer(conditional_websafe(_("(leave blank to show all submissions)")))
            __M_writer(u'</span>\n      </p>\n    </td>\n  </tr>\n  <tr>\n    <th>')
            # SOURCE LINE 247
            __M_writer(conditional_websafe(_("comment options")))
            __M_writer(u'</th>\n    <td class="prefright">\n    <p>\n      ')
            # SOURCE LINE 250
            __M_writer(conditional_websafe(_wsf("sort comments by %(sort)s", sort=unsafe(capture(comment_sort_options)))))
            __M_writer(u'\n    </p>\n    <p>\n    ')
            # SOURCE LINE 253
            __M_writer(conditional_websafe(checkbox(_(u"ignore suggested sorts"), "ignore_suggested_sort")))
            __M_writer(u'\n    &#32;<span class="details">')
            # SOURCE LINE 254
            __M_writer(conditional_websafe(_("(suggested sorts may be set by community moderators for specific threads or subreddits, like Q&As)")))
            __M_writer(u'</span>\n    </p>\n    <p>\n    ')
            # SOURCE LINE 257
            __M_writer(conditional_websafe(checkbox(_(u"show a dagger (†) on comments voted controversial"), "highlight_controversial")))
            __M_writer(u'\n    &#32;<span class="details">')
            # SOURCE LINE 258
            __M_writer(conditional_websafe(_("(a controversial comment is one that's been both upvoted and downvoted significantly)")))
            __M_writer(u'</span>\n    </p>\n    ')
            # SOURCE LINE 260

            input = unsafe(capture(num_input, c.user.pref_min_comment_score,
                                   'min_comment_score'))
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['input'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 263
            __M_writer(u'\n    <p>\n      ')
            # SOURCE LINE 265
            __M_writer(conditional_websafe(_wsf("don't show me comments with a score less than %(num)s", num=input)))
            __M_writer(u'\n      &#32;<span class="details">')
            # SOURCE LINE 266
            __M_writer(conditional_websafe(_("(leave blank to show all comments)")))
            __M_writer(u'</span>\n    </p>\n    <p>\n      ')
            # SOURCE LINE 269

            input = unsafe(capture(num_input, c.user.pref_num_comments,
                                   'num_comments'))
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['input'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 272
            __M_writer(u'\n    ')
            # SOURCE LINE 273
            s = c.user.pref_num_comments 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['s'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n    ')
            # SOURCE LINE 274
            __M_writer(conditional_websafe(_wsf("display %(num)s comments by default", num=input)))
            __M_writer(u'\n    &#32;\n    <span class="details">\n      (1 - ')
            # SOURCE LINE 277
            __M_writer(conditional_websafe(g.max_comments))
            __M_writer(u');\n      &#32;\n      ')
            # SOURCE LINE 279
            __M_writer(conditional_websafe(_("the smaller the number, the faster your comments pages will load")))
            __M_writer(u'\n    </span>\n    </td>\n  </tr>\n\n\n\n  <tr>\n    <th>')
            # SOURCE LINE 287
            __M_writer(conditional_websafe(_("messaging options")))
            __M_writer(u'</th>\n    <td class="prefright">\n      ')
            # SOURCE LINE 289
            __M_writer(conditional_websafe(checkbox(_("show message conversations in the inbox"), \
         "threaded_messages")))
            # SOURCE LINE 290
            __M_writer(u'\n      &#32;<span class="details">\n        ')
            # SOURCE LINE 292
            __M_writer(conditional_websafe(_("(only applies when you go to the 'messages' panel)")))
            __M_writer(u'\n      </span>\n      <br/>\n')
            # SOURCE LINE 295
            if c.user.pref_threaded_messages:
                # SOURCE LINE 296
                __M_writer(u'        ')
                __M_writer(conditional_websafe(checkbox(_("collapse messages after I've read them"), \
           "collapse_read_messages")))
                # SOURCE LINE 297
                __M_writer(u'\n        &#32;<span class="details">\n          ')
                # SOURCE LINE 299
                __M_writer(conditional_websafe(_("(otherwise, you'll have to collapse them yourself)")))
                __M_writer(u'\n        </span>\n        <br/>\n')
            # SOURCE LINE 303
            __M_writer(u'      ')
            __M_writer(conditional_websafe(checkbox(_("mark messages as read when I open my inbox"), \
         "mark_messages_read")))
            # SOURCE LINE 304
            __M_writer(u'\n      &#32;<span class="details">\n        ')
            # SOURCE LINE 306
            __M_writer(conditional_websafe(_("(otherwise, they will be marked as read when you click them)")))
            __M_writer(u'\n      </span>\n      <br>\n      ')
            # SOURCE LINE 309
            __M_writer(conditional_websafe(checkbox(_("notify me when people say my username"), "monitor_mentions")))
            __M_writer(u'\n')
            # SOURCE LINE 310
            if feature.is_enabled('orangereds_as_emails'):
                # SOURCE LINE 311
                __M_writer(u'        <br>\n        ')
                # SOURCE LINE 312
                __M_writer(conditional_websafe(checkbox(_("send messages as emails"), "email_messages", disabled=(not c.user.email_verified), disabled_text=_("requires a verified email"))))
                __M_writer(u'\n')
            # SOURCE LINE 314
            __M_writer(u'      <br>\n      ')
            # SOURCE LINE 315
            __M_writer(conditional_websafe(checkbox(_("enable threaded modmail display"), "threaded_modmail")))
            __M_writer(u'\n    </td>\n  </tr>\n  <tr>\n    <th>')
            # SOURCE LINE 319
            __M_writer(conditional_websafe(_("display options")))
            __M_writer(u'</th>\n    <td class="prefright">\n      ')
            # SOURCE LINE 321
            __M_writer(conditional_websafe(checkbox(_("allow subreddits to show me custom themes"), "show_stylesheets")))
            __M_writer(u'\n')
            # SOURCE LINE 322
            if feature.is_enabled('stylesheets_everywhere'):
                # SOURCE LINE 323
                __M_writer(u'        &#32;<span class="details reddit-gold">\n          ')
                # SOURCE LINE 324
                __M_writer(conditional_websafe(_("(you can also choose which subreddit themes to disable on an individual level)")))
                __M_writer(u'\n        </span>\n')
            # SOURCE LINE 327
            __M_writer(u'      <br/>\n      ')
            # SOURCE LINE 328
            __M_writer(conditional_websafe(checkbox(_("show user flair"), "show_flair")))
            __M_writer(u'\n      <br/>\n      ')
            # SOURCE LINE 330
            __M_writer(conditional_websafe(checkbox(_("show link flair"), "show_link_flair")))
            __M_writer(u'\n')
            # SOURCE LINE 331
            if c.user.pref_show_promote is not None:
                # SOURCE LINE 332
                __M_writer(u'        <br/>\n        ')
                # SOURCE LINE 333
                __M_writer(conditional_websafe(checkbox(_("show self-serve advertising tab on front page"),
          "show_promote")))
                # SOURCE LINE 334
                __M_writer(u'\n')
            # SOURCE LINE 336
            if feature.is_enabled('legacy_search_pref'):
                # SOURCE LINE 337
                __M_writer(u'        <br>\n        ')
                # SOURCE LINE 338
                __M_writer(conditional_websafe(checkbox(_("show legacy search page"), "legacy_search")))
                __M_writer(u'\n')
            # SOURCE LINE 340
            __M_writer(u'    </td>\n  </tr>\n  <tr>\n    <th>')
            # SOURCE LINE 343
            __M_writer(conditional_websafe(_("content options")))
            __M_writer(u'</th>\n    <td class="prefright">\n      ')
            # SOURCE LINE 345
            __M_writer(conditional_websafe(checkbox(_("I am over eighteen years old and willing to view adult content"), "over_18")))
            __M_writer(u'\n      &#32;<span class="details">(')
            # SOURCE LINE 346
            __M_writer(conditional_websafe(_("required to view some subreddits")))
            __M_writer(u')</span>\n      <br/>\n        ')
            # SOURCE LINE 348
            __M_writer(conditional_websafe(checkbox(_("label posts that are not safe for work (NSFW)"), "label_nsfw", disabled = c.user.pref_no_profanity, disabled_text = "(requires not 'safer for work' mode)")))
            __M_writer(u'\n      <br/>\n        ')
            # SOURCE LINE 350
            __M_writer(conditional_websafe(checkbox(_("enable private RSS feeds"), "private_feeds")))
            __M_writer(u'\n       &#32;<span class="details">\n        ')
            # SOURCE LINE 352
            __M_writer(conditional_websafe(_("(available from the 'RSS feed' tab in prefs)")))
            __M_writer(u'</span>\n    </td>\n  <tr>\n    <th>')
            # SOURCE LINE 355
            __M_writer(conditional_websafe(_("privacy options")))
            __M_writer(u'</th>\n    <td class="prefright">\n      ')
            # SOURCE LINE 357
            __M_writer(conditional_websafe(checkbox(_("make my votes public"), "public_votes")))
            __M_writer(u'\n      &#32;\n      <span class="details">\n        ')
            # SOURCE LINE 360

            link1 = format_html('&#32;<a href="/user/%s/upvoted">/user/%s/upvoted</a>&#32;', c.user.name, c.user.name)
            link2 = format_html('&#32;<a href="/user/%s/downvoted">/user/%s/downvoted</a>', c.user.name, c.user.name)
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['link1','link2'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 363
            __M_writer(u'\n        (')
            # SOURCE LINE 364
            __M_writer(conditional_websafe(_wsf("let everyone see %(link1)s and %(link2)s", link1=link1, link2=link2)))
            __M_writer(u')\n      </span>\n      <br/>\n      ')
            # SOURCE LINE 367
            __M_writer(conditional_websafe(checkbox(_("allow my data to be used for research purposes"), "research")))
            __M_writer(u'\n      &#32;\n      <span class="details">\n       (\n         <a href="https://www.reddit.com/r/redditdev/comments/dtg4j/want_to_help_reddit_build_a_recommender_a_public/">\n           ')
            # SOURCE LINE 372
            __M_writer(conditional_websafe(_("details")))
            __M_writer(u'\n         </a>\n       )\n      </span>\n      <br />\n      ')
            # SOURCE LINE 377
            __M_writer(conditional_websafe(checkbox(_("don't allow search engines to index my user profile"), "hide_from_robots")))
            __M_writer(u'\n      &#32;\n      <span class="details">\n        (\n        <a href="https://www.reddit.com/wiki/noindex">')
            # SOURCE LINE 381
            __M_writer(conditional_websafe(_("details")))
            __M_writer(u'</a>\n        )\n      </span>\n    </td>\n  </tr>\n')
            # SOURCE LINE 386
            if feature.is_enabled('beta_opt_in'):
                # SOURCE LINE 387
                __M_writer(u'  <tr>\n    <th>')
                # SOURCE LINE 388
                __M_writer(conditional_websafe(_("beta options")))
                __M_writer(u'</th>\n    <td class="prefright">\n      ')
                # SOURCE LINE 390
                __M_writer(conditional_websafe(checkbox(_("I would like to beta test features for reddit"), "beta")))
                __M_writer(u'\n      &#32;\n      <span class="details">\n        ')
                # SOURCE LINE 393

                beta_sr_link = format_html('&#32;<a href="/r/%s">/r/%s</a>&#32;', g.beta_sr, g.beta_sr)
                        
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['beta_sr_link'] if __M_key in __M_locals_builtin_stored]))
                # SOURCE LINE 395
                __M_writer(u'\n        (')
                # SOURCE LINE 396
                __M_writer(conditional_websafe(_wsf("by enabling you'll be subscribed to %(beta_sr_link)s automatically.", beta_sr_link=beta_sr_link)))
                __M_writer(u'\n          &#32;\n          <a href="/r/')
                # SOURCE LINE 398
                __M_writer(conditional_websafe(g.beta_sr))
                __M_writer(u'/wiki">')
                __M_writer(conditional_websafe(_("details on the /r/{beta_sr} wiki").format(beta_sr=g.beta_sr)))
                __M_writer(u'</a>)\n      </span>\n    </td>\n  </tr>\n')
        # SOURCE LINE 404
        __M_writer(u'\n')
        # SOURCE LINE 406
        __M_writer(u'  ')
        # SOURCE LINE 416
        __M_writer(u'\n')
        # SOURCE LINE 417
        if feature.is_enabled('chat'):
            # SOURCE LINE 418
            __M_writer(u'  <tr>\n    <th>')
            # SOURCE LINE 419
            __M_writer(conditional_websafe(_("chat")))
            __M_writer(u'</th>\n    <td class="prefright">\n      ')
            # SOURCE LINE 421
            __M_writer(conditional_websafe(checkbox(_("enable chat"), "chat_enabled")))
            __M_writer(u'\n      <br/>\n      <p>\n        ')
            # SOURCE LINE 424
            __M_writer(conditional_websafe(_wsf("sidebar chat width %(sort)s", sort=unsafe(capture(chat_sidebar_size_options)))))
            __M_writer(u'\n      </p>\n      <!-- \n      ')
            # SOURCE LINE 427
            __M_writer(conditional_websafe(checkbox(_("click to load sidebar chats"), "label_nsfw", disabled = c.user.pref_no_profanity, disabled_text = "(coming soon)")))
            __M_writer(u'\n      <br/>\n        ')
            # SOURCE LINE 429
            __M_writer(conditional_websafe(checkbox(_("click to load post chats"), "label_nsfw", disabled = c.user.pref_no_profanity, disabled_text = "(coming soon)")))
            __M_writer(u'\n      <br/>\n        ')
            # SOURCE LINE 431
            __M_writer(conditional_websafe(checkbox(_("click to load comment chats"), "label_nsfw", disabled = c.user.pref_no_profanity, disabled_text = "(coming soon)")))
            __M_writer(u'\n      <br/> -->\n      <p>\n          ')
            # SOURCE LINE 434

            input = unsafe(capture(text_input_all, c.user.pref_chat_user,
                                   'chat_user', 30, False))
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['input'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 437
            __M_writer(u'\n        ')
            # SOURCE LINE 438
            s = c.user.pref_chat_user 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['s'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n        ')
            # SOURCE LINE 439
            __M_writer(conditional_websafe(_wsf("IRC nickname %(chat_user)s", chat_user=input)))
            __M_writer(u'\n        &#32; <span class="details">')
            # SOURCE LINE 440
            __M_writer(conditional_websafe(_("(changing will generate new chat client credentials)")))
            __M_writer(u'</span>\n        <!--\n        &#32;\n         <span class="details">\n          ')
            # SOURCE LINE 444
            __M_writer(conditional_websafe(_("(as well as IRC username and realname)")))
            __M_writer(u'\n        </span> \n        -->\n      </p>\n      <p>\n          ')
            # SOURCE LINE 449

            disabled = True
            input = unsafe(capture(text_input_all, c.user.pref_chat_client_user,
                                   'chat_client_user', 30, disabled))
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['disabled','input'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 453
            __M_writer(u'\n        ')
            # SOURCE LINE 454
            s = c.user.pref_chat_client_user 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['s'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n        ')
            # SOURCE LINE 455
            __M_writer(conditional_websafe(_wsf("chat client username %(val)s", val=input)))
            __M_writer(u'\n        <!-- &#32; <span class="details">')
            # SOURCE LINE 456
            __M_writer(conditional_websafe(_("(clear field and save to generate new credentials)")))
            __M_writer(u'</span> -->\n      </p>\n      <p>\n          ')
            # SOURCE LINE 459

            disabled = True
            input = unsafe(capture(text_input_all, c.user.pref_chat_client_password,
                                   'chat_client_password', 30, disabled))
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['disabled','input'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 463
            __M_writer(u'\n        ')
            # SOURCE LINE 464
            s = c.user.pref_chat_client_password 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['s'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n        ')
            # SOURCE LINE 465
            __M_writer(conditional_websafe(_wsf("chat client password %(val)s", val=input)))
            __M_writer(u'\n      </p>\n\n      <br>\n      <p>')
            # SOURCE LINE 469
            __M_writer(conditional_websafe(_("creating chat widgets")))
            __M_writer(u'</p>\n      ')
            # SOURCE LINE 470
            chat_enabler = g.live_config['chat_enabling_post_content'] 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['chat_enabler'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n      <p>&#8226; ')
            # SOURCE LINE 471
            __M_writer(conditional_websafe(_("post chat:")))
            __M_writer(u' submit a text post with any title and set the optional text to "')
            __M_writer(conditional_websafe(chat_enabler))
            __M_writer(u'". the title of the post will be the chat channel/topic &#32;<span class="details">(if ')
            __M_writer(conditional_websafe(_(g.live_config['name_community'])))
            __M_writer(u' allows)</span></p>\n      <p>&#8226; ')
            # SOURCE LINE 472
            __M_writer(conditional_websafe(_("comment chat:")))
            __M_writer(u' comment "')
            __M_writer(conditional_websafe(chat_enabler))
            __M_writer(u'" followed by your desired chat channel/topic &#32;<span class="details">(if ')
            __M_writer(conditional_websafe(_(g.live_config['name_community'])))
            __M_writer(u' allows)</span></p>\n      \n      <br>\n      <p>')
            # SOURCE LINE 475
            __M_writer(conditional_websafe(_("bring your own IRC client")))
            __M_writer(u'</p>\n      <p>&#8226; connect to: coming soon\n')
            # SOURCE LINE 478
            __M_writer(u'      </p>\n\n      <br>\n      <p>')
            # SOURCE LINE 481
            __M_writer(conditional_websafe(_("troubleshooting")))
            __M_writer(u'</p>\n      <p>&#8226; disconnect from unused IRC channels to improve performance</p>\n      <p>&#8226; "not connected": type and send IRC command "/connect" a few times until you re-connect to the IRC server</p>\n      <p>&#8226; "authentication failed": refresh the page. ensure other browser tabs with chat are closed. try clearing your cache and cookies and login to this site again. if you still get this error, set a new IRC nickname above and click "save options".</p>\n    </td>\n  </tr>\n')
        # SOURCE LINE 488
        __M_writer(u'\n')
        # SOURCE LINE 489
        if c.user.gold:
            # SOURCE LINE 490
            __M_writer(u'  <tr class="gold-accent">\n    <th>')
            # SOURCE LINE 491
            __M_writer(conditional_websafe(_("gold options")))
            __M_writer(u'</th>\n    <td class="prefright">\n        ')
            # SOURCE LINE 493
            __M_writer(conditional_websafe(checkbox(_("hide ads"), "hide_ads")))
            __M_writer(u'\n        <br>\n        ')
            # SOURCE LINE 495
            __M_writer(conditional_websafe(checkbox(_("remember what links I've visited"), "store_visits")))
            __M_writer(u'\n        &#32;<span class="details">(')
            # SOURCE LINE 496
            __M_writer(conditional_websafe(_("we'll remember and mark what links you've already read, even between computers")))
            __M_writer(u')</span>\n        <br>\n        ')
            # SOURCE LINE 498
            __M_writer(conditional_websafe(checkbox(_("highlight new comments"), "highlight_new_comments")))
            __M_writer(u'\n        &#32;<span class="details">\n          (')
            # SOURCE LINE 500
            __M_writer(conditional_websafe(_("we'll remember your visits for 48 hours and show you which comments you haven't seen yet")))
            __M_writer(u')\n        </span>\n        <br>\n        ')
            # SOURCE LINE 503
            __M_writer(conditional_websafe(checkbox(_("show gold expiration"), "show_gold_expiration")))
            __M_writer(u'\n        &#32;<span class="details">\n          (')
            # SOURCE LINE 505
            __M_writer(conditional_websafe(_("show how much gold you have remaining on your userpage")))
            __M_writer(u')\n        </span>\n        <br>\n        ')
            # SOURCE LINE 508
            creddit_link = unsafe('&#32;<a href="/creddits">creddit</a>&#32;') 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['creddit_link'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n        ')
            # SOURCE LINE 509
            __M_writer(conditional_websafe(checkbox(_wsf("use a %(creddit_link)s to automatically renew my gold if it expires", creddit_link=creddit_link), "creddit_autorenew")))
            __M_writer(u'\n    </td>\n  </tr>\n')
            # SOURCE LINE 512
        elif c.user.is_moderator_somewhere:
            # SOURCE LINE 513
            __M_writer(u'  <tr class="gold-accent">\n    <th>')
            # SOURCE LINE 514
            __M_writer(conditional_websafe(_("gold options")))
            __M_writer(u'</th>\n    <td class="prefright">\n      ')
            # SOURCE LINE 516
            __M_writer(conditional_websafe(checkbox(_("highlight new comments"), "highlight_new_comments")))
            __M_writer(u'\n      ')
            # SOURCE LINE 517
            gold_link = unsafe('&#32;<a href="/gold/about">' + _("reddit gold") + '</a>') 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['gold_link'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n      &#32;<span class="details">\n        (')
            # SOURCE LINE 519
            __M_writer(conditional_websafe(_wsf("since you don't have %(gold_link)s, this will only apply in subreddits you moderate", gold_link=gold_link)))
            __M_writer(u')\n      </span>\n    </td>\n  </tr>\n')
        # SOURCE LINE 524
        __M_writer(u'\n\n\n')
        # SOURCE LINE 527
        if feature.is_enabled('stylesheets_everywhere'):
            # SOURCE LINE 528
            __M_writer(u'    <tr class="gold-accent">\n      <th>')
            # SOURCE LINE 529
            __M_writer(conditional_websafe(_("reddit themes")))
            __M_writer(u'</th>\n      <td class="prefright">\n        <div class="reddit-themes-description">\n          <span>\n            ')
            # SOURCE LINE 533
            __M_writer(conditional_websafe(_("reddit themes change the appearance of reddit.  They are used anywhere another custom theme is not present.")))
            __M_writer(u'\n          </span>\n          <br />\n          <span class="details">\n            (')
            # SOURCE LINE 537
            __M_writer(conditional_websafe(_("Note: For security reasons this page will not be changed by themes")))
            __M_writer(u')\n          </span>\n        </div>\n\n        ')
            # SOURCE LINE 541
            __M_writer(conditional_websafe(checkbox(_("use reddit theme"), "enable_default_themes")))
            __M_writer(u'\n        &#32;<span class="details">(')
            # SOURCE LINE 542
            __M_writer(conditional_websafe(_("hover to preview")))
            __M_writer(u')</span>\n\n        <div class="container reddit-themes">\n')
            # SOURCE LINE 545
            if thing.themes:
                # SOURCE LINE 546
                for theme in thing.themes:
                    # SOURCE LINE 547
                    __M_writer(u'              ')
                    __M_writer(conditional_websafe(theme_item(
                thumbnail_url=theme.thumbnail_url,
                preview_url=theme.preview_url,
                id=theme.id,
                tagline=theme.tagline,
                checked=theme.checked,
              )))
                    # SOURCE LINE 553
                    __M_writer(u'\n')
            # SOURCE LINE 556
            __M_writer(u'\n          <div class="theme select-custom-theme">\n            <label><input type="radio" name="theme_selector" id="other_theme_selector" value="" ')
            # SOURCE LINE 558
            __M_writer(conditional_websafe("checked" if thing.use_other_theme else ""))
            __M_writer(u'>use theme from /r/</label>\n              <input type="text" class="text" size="21" maxlength="21" name="other_theme" placeholder="subreddit" ')
            # SOURCE LINE 559
            __M_writer(conditional_websafe("value=" + c.user.pref_default_theme_sr if thing.use_other_theme and c.user.pref_default_theme_sr else ""))
            __M_writer(u'>\n              <span class="details">\n                  (')
            # SOURCE LINE 561
            __M_writer(conditional_websafe(_("warning: use non-featured themes at your own risk")))
            __M_writer(u')\n              </span>\n          </div>\n        </div>\n      </div>\n')
            # SOURCE LINE 566
            if thing.error_style_override:
                # SOURCE LINE 567
                __M_writer(u'        <p class="error">')
                __M_writer(conditional_websafe(_(error_list[thing.error_style_override])))
                __M_writer(u'</p>\n')
            # SOURCE LINE 569
            __M_writer(u'      </td>\n    </tr>\n')
        # SOURCE LINE 572
        __M_writer(u'\n  <tr>\n    <td>\n      <input type="submit" class="btn" value="')
        # SOURCE LINE 575
        __M_writer(conditional_websafe(_('save options')))
        __M_writer(u'"/>\n    </td>\n  </tr>\n</table>\n\n</form>\n\n ')
        # SOURCE LINE 595
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_checkbox(context,text,name,disabled=False,disabled_text='',prefix='pref_'):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fa55a395f90')._populate(_import_ns, [u'md', u'error_field', u'language_tool', u'plain_link'])
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 37
        __M_writer(u'\n    <input name="')
        # SOURCE LINE 38
        __M_writer(conditional_websafe(name))
        __M_writer(u'" id="')
        __M_writer(conditional_websafe(name))
        __M_writer(u'" type="checkbox"\n')
        # SOURCE LINE 39
        if getattr(c.user, prefix + name):
            # SOURCE LINE 40
            __M_writer(u'                 checked="checked"\n')
        # SOURCE LINE 42
        if disabled:
            # SOURCE LINE 43
            __M_writer(u'                 disabled="disabled"\n')
        # SOURCE LINE 45
        __M_writer(u'               />\n    <label class="')
        # SOURCE LINE 46
        __M_writer(conditional_websafe('disabled' if disabled else ''))
        __M_writer(u'" for="')
        __M_writer(conditional_websafe(name))
        __M_writer(u'">\n      ')
        # SOURCE LINE 47
        __M_writer(conditional_websafe(text))
        __M_writer(u'\n    </label>\n')
        # SOURCE LINE 49
        if disabled and disabled_text:
            # SOURCE LINE 50
            __M_writer(u'      &#32;<span class="details">')
            __M_writer(conditional_websafe(disabled_text))
            __M_writer(u'</span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_chat_sidebar_size_options(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fa55a395f90')._populate(_import_ns, [u'md', u'error_field', u'language_tool', u'plain_link'])
        __M_writer = context.writer()
        # SOURCE LINE 406
        __M_writer(u'\n    ')
        # SOURCE LINE 407
        menu = ChatSidebarSizeMenu() 
        
        __M_writer(u'\n    <select name="chat_sidebar_size">\n')
        # SOURCE LINE 409
        for sort in menu._options:
            # SOURCE LINE 410
            __M_writer(u'          <option ')
            __M_writer(conditional_websafe('selected="selected"' if sort == c.user.pref_chat_sidebar_size else ""))
            __M_writer(u'\n                  value="')
            # SOURCE LINE 411
            __M_writer(conditional_websafe(sort))
            __M_writer(u'">\n            ')
            # SOURCE LINE 412
            __M_writer(conditional_websafe(menu.make_title(sort)))
            __M_writer(u'&#32;')
            __M_writer(conditional_websafe(_('(recommended)') if sort == menu._default else ''))
            __M_writer(u'\n          </option>\n')
        # SOURCE LINE 415
        __M_writer(u'    </select>\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_sort_options(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fa55a395f90')._populate(_import_ns, [u'md', u'error_field', u'language_tool', u'plain_link'])
        __M_writer = context.writer()
        # SOURCE LINE 64
        __M_writer(u'\n  ')
        # SOURCE LINE 65
        menu = CommentSortMenu() 
        
        __M_writer(u'\n  <select name="default_comment_sort">\n')
        # SOURCE LINE 67
        for sort in menu.visible_options():
            # SOURCE LINE 68
            __M_writer(u'        <option ')
            __M_writer(conditional_websafe('selected="selected"' if sort == c.user.pref_default_comment_sort else ""))
            __M_writer(u'\n                value="')
            # SOURCE LINE 69
            __M_writer(conditional_websafe(sort))
            __M_writer(u'">\n          ')
            # SOURCE LINE 70
            __M_writer(conditional_websafe(menu.make_title(sort)))
            __M_writer(u'&#32;')
            __M_writer(conditional_websafe(_('(recommended)') if sort == menu._default else ''))
            __M_writer(u'\n        </option>\n')
        # SOURCE LINE 73
        __M_writer(u'  </select>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_media_radio(context,val,label):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fa55a395f90')._populate(_import_ns, [u'md', u'error_field', u'language_tool', u'plain_link'])
        __M_writer = context.writer()
        # SOURCE LINE 78
        __M_writer(u'\n  <input id="media_')
        # SOURCE LINE 79
        __M_writer(conditional_websafe(val))
        __M_writer(u'" class="nomargin"\n         type="radio"  value="')
        # SOURCE LINE 80
        __M_writer(conditional_websafe(val))
        __M_writer(u'" name="media"\n         ')
        # SOURCE LINE 81
        __M_writer(conditional_websafe("checked='checked'" if c.user.pref_media == val else ''))
        __M_writer(u' />\n  <label for="media_')
        # SOURCE LINE 82
        __M_writer(conditional_websafe(val))
        __M_writer(u'">')
        __M_writer(conditional_websafe(label))
        __M_writer(u'</label>\n  <br/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_media_preview_radio(context,val,label):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fa55a395f90')._populate(_import_ns, [u'md', u'error_field', u'language_tool', u'plain_link'])
        __M_writer = context.writer()
        # SOURCE LINE 86
        __M_writer(u'\n  <input id="media_preview_')
        # SOURCE LINE 87
        __M_writer(conditional_websafe(val))
        __M_writer(u'" class="nomargin"\n         type="radio"  value="')
        # SOURCE LINE 88
        __M_writer(conditional_websafe(val))
        __M_writer(u'" name="media_preview"\n         ')
        # SOURCE LINE 89
        __M_writer(conditional_websafe("checked='checked'" if c.user.pref_media_preview == val else ''))
        __M_writer(u'>\n  <label for="media_preview_')
        # SOURCE LINE 90
        __M_writer(conditional_websafe(val))
        __M_writer(u'">')
        __M_writer(conditional_websafe(label))
        __M_writer(u'</label>\n  <br/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_link_options(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fa55a395f90')._populate(_import_ns, [u'md', u'error_field', u'language_tool', u'plain_link'])
        __M_writer = context.writer()
        # SOURCE LINE 54
        __M_writer(u'\n  <select name="numsites">\n')
        # SOURCE LINE 56
        for x in [10, 25, 50, 100]:
            # SOURCE LINE 57
            __M_writer(u'        <option ')
            __M_writer(conditional_websafe(x == c.user.pref_numsites and "selected='selected'" or ""))
            __M_writer(u'>\n          ')
            # SOURCE LINE 58
            __M_writer(conditional_websafe(x))
            __M_writer(u'\n        </option>\n')
        # SOURCE LINE 61
        __M_writer(u'  </select>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_text_input(context,s,name):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fa55a395f90')._populate(_import_ns, [u'md', u'error_field', u'language_tool', u'plain_link'])
        __M_writer = context.writer()
        # SOURCE LINE 99
        __M_writer(u'\n  <input type="text" class="text" size="20" maxlength="20"\n         name="')
        # SOURCE LINE 101
        __M_writer(conditional_websafe(name))
        __M_writer(u'" value="')
        __M_writer(conditional_websafe(s if s is not None else ''))
        __M_writer(u'">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_num_input(context,s,name):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fa55a395f90')._populate(_import_ns, [u'md', u'error_field', u'language_tool', u'plain_link'])
        __M_writer = context.writer()
        # SOURCE LINE 94
        __M_writer(u'\n  <input type="text" class="number" size="4" maxlength="4"\n         name="')
        # SOURCE LINE 96
        __M_writer(conditional_websafe(name))
        __M_writer(u'" value="')
        __M_writer(conditional_websafe(s if s is not None else ''))
        __M_writer(u'">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_text_input_all(context,s,name,size,disabled):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fa55a395f90')._populate(_import_ns, [u'md', u'error_field', u'language_tool', u'plain_link'])
        __M_writer = context.writer()
        # SOURCE LINE 105
        __M_writer(u'\n  <input type="text" class="text" size="')
        # SOURCE LINE 106
        __M_writer(conditional_websafe(size))
        __M_writer(u'" maxlength="')
        __M_writer(conditional_websafe(size))
        __M_writer(u'"\n         name="')
        # SOURCE LINE 107
        __M_writer(conditional_websafe(name))
        __M_writer(u'" value="')
        __M_writer(conditional_websafe(s if s is not None else ''))
        __M_writer(u'" ')
        __M_writer(conditional_websafe("disabled='disabled'" if disabled else ""))
        __M_writer(u' ')
        __M_writer(conditional_websafe("style='width:auto'" if size and size > 20 else ""))
        __M_writer(u'>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_theme_item(context,thumbnail_url,preview_url,id,tagline,checked):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fa55a395f90')._populate(_import_ns, [u'md', u'error_field', u'language_tool', u'plain_link'])
        md = _import_ns.get('md', context.get('md', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 582
        __M_writer(u'\n  <div class="theme ')
        # SOURCE LINE 583
        __M_writer(conditional_websafe('selected' if checked else ''))
        __M_writer(u'" id="')
        __M_writer(conditional_websafe(id))
        __M_writer(u'">\n    <div class="theme-container">\n      <div class="theme-thumbnail">\n        <img src="')
        # SOURCE LINE 586
        __M_writer(conditional_websafe(make_url_protocol_relative(thumbnail_url)))
        __M_writer(u'"/>\n        <div class="theme-preview">\n          <img src="')
        # SOURCE LINE 588
        __M_writer(conditional_websafe(make_url_protocol_relative(preview_url)))
        __M_writer(u'"/>\n        </div>\n      </div>\n      <label><input type="radio" name="theme_selector" value="')
        # SOURCE LINE 591
        __M_writer(conditional_websafe(id))
        __M_writer(u'" ')
        __M_writer(conditional_websafe("checked" if checked else ""))
        __M_writer(u'>\n        ')
        # SOURCE LINE 592
        __M_writer(conditional_websafe(md(tagline)))
        __M_writer(u'</label>\n    </div>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


