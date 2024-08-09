// Fetch and list the title for all movies by using this URL
$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  method: 'GET',
  success: function (data) {
    $.each(data.results, function (index, movie) {
      $('UL#list_movies').append('<li>' + movie.title + '</li>');
    });
  }
});
