/*
fetches and list data (the film name) from URL
*/
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $.each(data.results, function (key, value) {
    const title = '<li>' + value.title + '</li>';
    $('#list_movies').append(title);
  });
});
