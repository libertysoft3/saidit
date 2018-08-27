/**
 * Markdown Expandos - SaidIt 2018
 *
 * Supports urls: static images, YouTube
 * Unsupported static image urls:
 *   https://example.com/folder/file.jpg?param.eter#hash=12.345
 *   https://en.wikipedia.org/wiki/Portable_Network_Graphics#/media/File:PNG_transparency_demonstration_1.png
 */
!function(r) {
  $(function() {
    var buttonClass = 'md-expando-button';
    var buttonOpenClass = 'md-expando-open';
    var buttonClosedClass = 'md-expando-closed';
    var reYouTube = /https?:\/\/(?:[0-9A-Z-]+\.)?(?:youtu\.be\/|youtube(?:-nocookie)?\.com\S*?[^\w\s-])([\w-]{11})(?=[^\w-]|$)(?![?=&+%\w.-]*(?:['"][^<>]*>|<\/a>))[?=&+%\w.-]*/ig; // src https://stackoverflow.com/a/5831191

    function initMdExpandosByThingId(thingId) {
      $('#' + thingId).find('.md a').each(function() {
        initMdExpando($(this));
      });
      $('#' + thingId).find('.md a.' + buttonClass).on('click', function(){
        toggleMdExpando($(this));
      });
    }

    function initMdExpando($thing) {
      var check = getImageExtension($thing.attr('href'));
      if (check) {
        $thing.after(' <a class="' + buttonClass + ' ' + buttonClosedClass + '" data-type="image" data-expando-exists="false" href="javascript:void(0);">' + check + '</a> ');
        return;
      }
      check = getYouTubeId($thing.attr('href'));
      if (check) {
        $thing.after(' <a class="' + buttonClass + ' ' + buttonClosedClass + '" data-video-id="' + check  + '" data-type="youtube" data-expando-exists="false" href="javascript:void(0);">YouTube</a> ');
        return;
      }
    }

    function toggleMdExpando($button) {
      // hide expando
      if ($button.hasClass(buttonOpenClass)) {
        $button.addClass(buttonClosedClass).removeClass(buttonOpenClass);
        $button.next().hide();
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
              $button.after('<div class="md-expando"><a href="' + sourceHref + '" draggable="false"><img src="' + sourceHref + '" draggable="false"/></a></div>');
              initMdExpandoImageResize($button.next().find('a'), $button.next().find('img'));
          break;
        case 'youtube':
              $button.after('<div class="md-expando"><iframe width="560" height="315" style="max-width: 100%;" src="https://www.youtube-nocookie.com/embed/' + $button.data('video-id') + '" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe></div>');
          break;
      }
    }

    function getImageExtension(href) {
      if (!href || href.indexOf('#') != -1 || href.indexOf('?') != -1) {
        return false;
      }
      var allowed = ['jpg', 'jpeg', 'gif', 'png'];
      var extIndex = allowed.indexOf(href.split('.').pop().toLowerCase());
      if (extIndex == -1) {
        return false;
      }
      return allowed[extIndex].toUpperCase();
    }

    function getYouTubeId(href) {
      if (!href) {
        return false;
      }
      var match = reYouTube.exec(href);
      if (match) {
        return match[1];
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
        $link.data('dragging', true).data('startX', event.pageX).data('startY', event.pageY);
        $img.data('original-width', $img.width()).css('width', $img.width() + 'px');
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
    $('.md a.' + buttonClass).on('click', function(){
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
