$(document).ready(function () {
  $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const movies = data.results;
    const $list = $('UL#list_movies');
    $.each(movies, function (index, movies) {
      $list.append('<li>' + movies.title + '</li>');
    });
  });
});
