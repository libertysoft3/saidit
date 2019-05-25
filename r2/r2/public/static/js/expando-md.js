/**
 * Markdown Expandos - SaidIt 2018
 *
 * Unsupported static image url formats:
 *   https://en.wikipedia.org/wiki/Portable_Network_Graphics#/media/File:PNG_transparency_demonstration_1.png
 *   https://example.com/download.php?file=folder/file.jpg
 *
 * Supported static image url formats:
 *   https://example.com/folder/file.jpg
 *   https://example.com/folder/file.jpg?param.eter#hash=12.345
 *
 * Making on click ajax requests for providers:
 *   SoundCloud - oEmbed
 *
 * On click js injected for providers:
 *   imgur
 */
!function(r) {
  $(function() {
    var buttonClass = 'md-expando-button';
    var buttonOpenClass = 'md-expando-open';
    var buttonClosedClass = 'md-expando-closed';
    var destroyOnCloseTypes = ['video', 'audio', 'soundcloud', 'youtube', 'invidious', 'bitchute', 'peertube', 'dtube', 'vimeo'];
    var reValidExpandoUrl = /^https?\:\/\//i;
    var reYouTube = /https?:\/\/(?:[0-9A-Z-]+\.)?(?:youtu\.be\/|youtube(?:-nocookie)?\.com\S*?[^\w\s-])([\w-]{11})(?=[^\w-]|$)(?![?=&+%\w.-]*(?:['"][^<>]*>|<\/a>))[?=&+%\w.-]*/i; // https://stackoverflow.com/a/5831191
    var reInvidious = /^(?:https?:)?\/\/(?:[0-9A-Z-]+\.)?(?:invidio\.us)\/(?:(?:watch\?(?:[^&=]+=[^&]*)*v=)|embed\/)([\w-]{11})/i;
    var reYouTubeTimestampParam = /t=([^&#]*)/; // capture param t
    var reYouTubeTimestampA = /^(\d+h)?(\d+m)?(\d+s)$/i; // 1h6m30s
    var reYouTubeTimestampB = /^(\d+)$/; // 960
    var rePeerTube = /^https?\:\/\/(([^:\/?#]*)(?:\:([0-9]+))?)\/videos\/watch\/(\w{8}\-\w{4}\-\w{4}\-\w{4}\-\w{12})(\?start=(\w+))?$/i; // https://stackoverflow.com/a/21553982/1525014
    var reBitChute = /^https?\:\/\/(www\.)*bitchute\.com\/video\/\w+/i;
    var reDTube = /^https?\:\/\/d\.tube\/(#\!\/)*v\/.+\/\w+/i;
    var reVimeo = /^https?\:\/\/(player\.)*vimeo\.com\/((.+\/.+\/)|(video\/))*(\d+)(#.+)*/i;
    var reSoundCloud = /^https?\:\/\/(www\.)*soundcloud.com\/.+\/.+/i;
    var reImgur = /^https?\:\/\/(www\.)*imgur.com\/(gallery|t\/\w+|user\/\w+\/favorites)\/(\w+)$/i;

    function initMdExpandosByThingId(thingId) {
      $('#' + thingId + ' > .entry .md a').each(function() {
        initMdExpando($(this));
      });
      $('#' + thingId + ' > .entry .md a.' + buttonClass).on('click', function(event) {
        event.preventDefault();
        toggleMdExpando($(this));
      });
    }

    function initMdExpando($thing) {
      if (!$thing.attr('href').length || !reValidExpandoUrl.exec($thing.attr('href'))) {
        return;
      }

      // Images
      var check = getImageExtension($thing.attr('href'));
      if (check) {
        $thing.after(' <a class="' + buttonClass + ' ' + buttonClosedClass + '" data-type="image" data-expando-exists="false" href="javascript:void(0);">' + check + '</a> ');
        return;
      }
      check = getEmbedIdImgur($thing.attr('href'));
      if (check) {
        $thing.after(' <a class="' + buttonClass + ' ' + buttonClosedClass + '" data-type="imgur" data-embed-id="' + check  + '" data-expando-exists="false" href="javascript:void(0);">Imgur</a> ');
        return;
      }

      // Video
      check = getVideoExtension($thing.attr('href'));
      if (check) {
        $thing.after(' <a class="' + buttonClass + ' ' + buttonClosedClass + '" data-type="video" data-expando-exists="false" href="javascript:void(0);">' + check + '</a> ');
        return;
      }
      check = getEmbedUrlYouTube($thing.attr('href'));
      if (check) {
        $thing.after(' <a class="' + buttonClass + ' ' + buttonClosedClass + '" data-type="youtube" data-video-url="' + check  + '" data-expando-exists="false" href="javascript:void(0);">YouTube</a> ');
        return;
      }
      check = getEmbedUrlInvidious($thing.attr('href'));
      if (check) {
        $thing.after(' <a class="' + buttonClass + ' ' + buttonClosedClass + '" data-type="invidious" data-video-url="' + check + '" data-expando-exists="false" href="javascript:void(0);">Invidious</a> ');
        return;
      }
      check = getEmbedUrlPeerTube($thing.attr('href'));
      if (check) {
        $thing.after(' <a class="' + buttonClass + ' ' + buttonClosedClass + '" data-type="peertube" data-video-url="' + check  + '" data-expando-exists="false" href="javascript:void(0);">PeerTube</a> ');
        return;
      }
      check = getEmbedUrlBitChute($thing.attr('href'));
      if (check) {
        $thing.after(' <a class="' + buttonClass + ' ' + buttonClosedClass + '" data-type="bitchute" data-video-url="' + check  + '" data-expando-exists="false" href="javascript:void(0);">BitChute</a> ');
        return;
      }
      check = getEmbedUrlDTube($thing.attr('href'));
      if (check) {
        $thing.after(' <a class="' + buttonClass + ' ' + buttonClosedClass + '" data-type="dtube" data-video-url="' + check  + '" data-expando-exists="false" href="javascript:void(0);">DTube</a> ');
        return;
      }
      check = getEmbedUrlVimeo($thing.attr('href'));
      if (check) {
        $thing.after(' <a class="' + buttonClass + ' ' + buttonClosedClass + '" data-type="vimeo" data-video-url="' + check  + '" data-expando-exists="false" href="javascript:void(0);">Vimeo</a> ');
        return;
      }

      // Audio
      check = getAudioExtension($thing.attr('href'));
      if (check) {
        $thing.after(' <a class="' + buttonClass + ' ' + buttonClosedClass + '" data-type="audio" data-expando-exists="false" href="javascript:void(0);">' + check + '</a> ');
        return;
      }
      check = reSoundCloud.exec($thing.attr('href'))
      if (check) {
        $thing.after(' <a class="' + buttonClass + ' ' + buttonClosedClass + '" data-type="soundcloud" data-url="' + $thing.attr('href')  + '" data-expando-exists="false" href="javascript:void(0);">SoundCloud</a> ');
        return;
      }
    }

    function toggleMdExpando($button) {
      // close expando
      if ($button.hasClass(buttonOpenClass)) {
        $button.addClass(buttonClosedClass).removeClass(buttonOpenClass);
        $button.next().hide();
        if (destroyOnCloseTypes.indexOf($button.data('type')) != -1) {
          $button.data('expando-exists', false).next().remove(); // remove players to make them stop playing
        }
        return;
      }

      // show existing expando
      $button.addClass(buttonOpenClass).removeClass(buttonClosedClass);
      if ($button.data('expando-exists') == true) {
        $button.next().show();
        return;
      }

      // create and show expando
      $button.data('expando-exists', true);
      switch ($button.data('type')) {
        case 'image':
          var sourceHref = $button.prev().attr('href');
          $button.after('<div class="md-expando"><a href="' + sourceHref + '" draggable="false" style="outline: none;"><img src="' + sourceHref + '" draggable="false"/></a></div>');
          initMdExpandoImageResize($button.next().find('a'), $button.next().find('img'));
          break;
        case 'video':
          $button.after('<div class="md-expando"><video controls preload="auto" src="' + $button.prev().attr('href') + '"></video></div>');
          break;
        case 'audio':
          $button.after('<div class="md-expando"><audio controls preload="auto" src="' + $button.prev().attr('href') + '"></audio></div>');
          break;
        case 'imgur':
          var html  = '<blockquote class="imgur-embed-pub" lang="en" data-id="a/' + $button.data('embed-id') + '"><a href="//imgur.com/' + $button.data('embed-id') + '"></a></blockquote><script async src="//s.imgur.com/min/embed.js" charset="utf-8"></script>';
          $button.after('<div class="md-expando">' + html + '</div>');
          break;
        case 'youtube':
          $button.after('<div class="md-expando"><iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/' + $button.data('video-url') + '" frameborder="0" allow="autoplay; encrypted-media" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe></div>');
          break;
        case 'invidious':
          $button.after('<div class="md-expando"><iframe width="560" height="315" src="https://www.invidio.us/embed/' + $button.data('video-url')+ '" frameborder="0" allow="autoplay; encrypted-media" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe></div>');
          break;
        case 'peertube':
          $button.after('<div class="md-expando"><iframe width="560" height="315" sandbox="allow-same-origin allow-scripts" src="' + $button.data('video-url') + '" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe></div>');
          break;
        case 'bitchute':
          $button.after('<div class="md-expando"><iframe width="640" height="360" scrolling="no" frameborder="0" style="border: none;" src="' + $button.data('video-url') + '" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe></div>');
          break;
        case 'dtube':
          $button.after('<div class="md-expando"><iframe width="560" height="315" src="' + $button.data('video-url') + '" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe></div>');
          break;
        case 'vimeo':
          $button.after('<div class="md-expando"><iframe width="640" height="360" src="' + $button.data('video-url') + '" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe></div>');
          break;
        case 'soundcloud':
          $.getJSON('https://soundcloud.com/oembed?url=' + encodeURIComponent($button.data('url')), function(data) {
            $button.after('<div class="md-expando">' + data['html'] + '</div>');
          });
          break;
      }
    }
    
    function getExtension(href) {
      var trimIndex = href.indexOf('#');
      if (trimIndex !== -1) {
        href = href.slice(0, trimIndex);
      }
      trimIndex = href.indexOf('?');
      if (trimIndex !== -1) {
        href = href.slice(0, trimIndex);
      }
      return href.split('.').pop();
    }

    function getImageExtension(href) {
      var allowed = ['jpg', 'jpeg', 'gif', 'png', 'svg', 'ico', 'bmp', 'webp', 'tif', 'tiff'];
      var extIndex = allowed.indexOf(getExtension(href).toLowerCase());
      if (extIndex == -1) {
        return false;
      }
      return allowed[extIndex].toUpperCase();
    }
    
    function getVideoExtension(href) {
      var allowed = ['ogg', 'webm', 'mpg', 'mp2', 'mpeg', 'mpe', 'mpv', 'mp4', 'm4v', 'avi', 'ogv', 'ogx', 'webm',
                     '3gp', '3g2', 'flv', 'f4v', 'f4p', 'f4f', 'hevc'];
      var extIndex = allowed.indexOf(getExtension(href).toLowerCase());
      if (extIndex == -1) {
        return false;
      }
      return allowed[extIndex].toUpperCase();
    }

    function getAudioExtension(href) {
      var allowed = ['wav', 'm4p', 'mp3', 'm4a', 'aac', 'oga', 'mid', 'midi', 'weba', 'f4a', 'f4b', 'opus'];
      var extIndex = allowed.indexOf(getExtension(href).toLowerCase());
      if (extIndex == -1) {
        return false;
      }
      return allowed[extIndex].toUpperCase();
    }

    function getEmbedIdImgur(href) {
      var match = reImgur.exec(href);
      if (match && match[3]) {
        return match[3];
      }
      return false;
    }

    function getEmbedUrlYouTube(href) {
      var match = reYouTube.exec(href);
      if (match) {
        match[1] += '?rel=0';
        var ts = reYouTubeTimestampParam.exec(href);
        if (ts) {
          var parts = reYouTubeTimestampA.exec(ts[1]);
          if (parts) {
            var secs = 0;
            if (parts[3]) {
              secs += parseInt(parts[3].substring(0, parts[3].length - 1));
            }
            if (parts[2]) {
              secs += 60 * parseInt(parts[2].substring(0, parts[2].length - 1));
            }
            if (parts[1]) {
              secs += 60 * 60 * parseInt(parts[1].substring(0, parts[1].length - 1));
            }
            match[1] += '&start=' + secs;
          } else {
            var secs = reYouTubeTimestampB.exec(ts[1]);
            if (secs) {
              match[1] += '&start=' + parseInt(secs[1]);
            }
          }
        }
        return match[1];
      }
      return false;
    }
    function getEmbedUrlInvidious(href) {
      var match = reInvidious.exec(href);
      if (match) {
        match[1] += '?rel=0';
        var ts = reYouTubeTimestampParam.exec(href);
        if (ts) {
          var parts = reYouTubeTimestampA.exec(ts[1]);
          if (parts) {
            var secs = 0;
            if (parts[3]) {
              secs += parseInt(parts[3].substring(0, parts[3].length - 1));
            }
            if (parts[2]) {
              secs += 60 * parseInt(parts[2].substring(0, parts[2].length - 1));
            }
            if (parts[1]) {
              secs += 60 * 60 * parseInt(parts[1].substring(0, parts[1].length - 1));
            }
            match[1] += '&start=' + secs;
          } else {
            var secs = reYouTubeTimestampB.exec(ts[1]);
            if (secs) {
              match[1] += '&start=' + parseInt(secs[1]);
            }
          }
        }
        return match[1];
      }
      return false;
    }
    function getEmbedUrlPeerTube(href) {
      var match = rePeerTube.exec(href);
      if (match) {
        return href.replace('/videos/watch/','/videos/embed/');
      }
      return false;
    }
    function getEmbedUrlBitChute(href) {
      if (reBitChute.exec(href)) {
        return href.replace('/video/','/embed/');
      }
      return false;
    }
    function getEmbedUrlDTube(href) {
      if (reDTube.exec(href)) {
        href = href.replace('d.tube/#!/v/','d.tube/#!/'); // A https://d.tube/#!/v/lagtvgames/7d6495li
        href = href.replace('d.tube/v/', 'd.tube/#!/'); // B https://d.tube/v/lagtvgames/7d6495li
        return href.replace('d.tube/','emb.d.tube/');
      }
      return false;
    }
    function getEmbedUrlVimeo(href) {
      var match = reVimeo.exec(href);
      if (match && match[5]) {
        var url = 'https://player.vimeo.com/video/' + match[5];
        if (match[6]) {
          url += match[6];
        }
        return url;
      }
      return false;
    }

    // mousemoves stop firing if we leave the container. RES' solution is abs
    // positioning, but this is difficult to do in all places. One solution is
    // moving the image to a new div inside body when resizing, like a modal window
    // approach. image max-width: 100% is kept for this same reason, can't leave
    // the container unless using abs positioning.
    function initMdExpandoImageResize($link, $img) {
      var threshold = 3;
      $link.click(function(event){
        event.preventDefault();
      })
      .mousedown(function(event) {
        event.preventDefault(); // prevents FF from overlaying the image with blue
        $link.data('dragging', true).data('startX', event.pageX).data('startY', event.pageY);
        $img.data('original-width', $img.width()).css('width', $img.width() + 'px').css('max-width', 'none');
      })
      .mousemove(function(event) {
        if (!$link.data('dragging')) return;
        $img.css('cursor', 'nwse-resize').css('width', ($img.data('original-width') + event.pageX - $link.data('startX') + event.pageY - $link.data('startY')) + 'px');
       })
      .mouseup(function(event) {
        // detect click not drag, goto link
        if (Math.abs(event.pageX - $link.data('startX') + event.pageY - $link.data('startY')) <= threshold) {
          location.href = $link.attr('href');
        }
        $link.data('dragging', false);
        $img.css('cursor', 'pointer');
      })
      // prevent: leave container, mouse up, re-enter, still resizing
      .mouseenter(function(event){
        $link.data('dragging', false);
      });
    }

    // Add buttons
    $('.md a').each(function() {
      initMdExpando($(this));
    });

    // Handle button clicks
    $('.md a.' + buttonClass).on('click', function(event){
      event.preventDefault();
      toggleMdExpando($(this));
    });

    // Handle new comment, edit comment, edit post, load more comments
    $(document).on('new_thing', function(event, thing){
      initMdExpandosByThingId(thing.getAttribute('id'));
    });

    // Handle selftext expandos
    $(document).on('expando:hashtml', function(event){
      initMdExpandosByThingId('thing_' + event.expando.id);
    });
  });
}(r);
