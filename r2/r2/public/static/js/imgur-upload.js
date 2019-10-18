!function(r) {
  if (!r.config.imgur_client_id.length) {
    return;
  }
  $(function() {
    $('#imgur-upload').on("click", function (e) {
      if ($('#url').val()) {
        if (!confirm("This will replace your existing url, proceed?")) {
          e.preventDefault();
          return;
        }
      }
    });
    $('#imgur-upload').on("change", function () {
      var files = $(this).get(0).files;
      if(files.length) {
        $('#url-field .title-status').css('display','block').text('uploading...');
        var formData = new FormData();
        formData.append("image", files[0]);
        $.ajax({
          crossDomain: true,
          processData: false,
          contentType: false,
          data: formData,
          dataType: 'json',
          type: 'POST',
          url: 'https://api.imgur.com/3/image',
          headers: {
            Authorization: 'Client-ID ' + r.config.imgur_client_id
          },
          mimeType: 'multipart/form-data'
        }).done(function (response) {
          if(response.success == true && response.status == 200) {
            $('#url-field .title-status').css('display','block').text('');
            $('#url').val(response.data.link);
          } else {
            $('#url-field .title-status').css('display','block').html('upload failed, try again or visit <a href="https://imgur.com/upload">https://imgur.com/upload</a>');
            $('#url').val('');
          }
        }).fail(function (xhr, textStatus, error) {
          $('#url-field .title-status').css('display','block').html('upload failed, try again or visit <a href="https://imgur.com/upload">https://imgur.com/upload</a>');
          $('#url').val('');
        });
      }
    });
  });
}(r);
