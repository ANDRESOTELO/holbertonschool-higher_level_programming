/*
fetches and list data (the film name) from URL
*/
$(document).ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    $('#hello').html(data.hello);
  });
});
