function getLikes() {
    fetch('/apple/orange')
    .then( (response) => { 
      return response.json();
    }).then( (data) => {
      $('.badge').html(data);
    });
    
  }

  $("#likeBtn").on("click", function(){
    fetch('/api/link', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify("1")
    }).then( (response) => { 
      alert(response.text());
      getLikes();
    })
  });