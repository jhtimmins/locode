$(document).ready(function(){

  $("#search").on('click', function() {
    var repo = $("#search-field").val()
    $.get('/repos/search?route=' + repo, function(data, status) {
      console.log(data);
    })
  })
});
