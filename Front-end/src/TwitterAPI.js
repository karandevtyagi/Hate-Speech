// Returns a collection of the most recent Tweets posted by the user indicated by the screen_name or user_id parameters.
let user_timeline = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=twitterapi&count=2";


// https://stackoverflow.com/questions/4152841/twitter-api-to-get-recent-tweets-of-a-particular-user

var Twit = require('twit');


var T = new Twit({
    consumer_key: ''
  , consumer_secret: ''
  , access_token: ''
  , access_token_secret: ''
})

var options = { screen_name: '',
                count: 3 };

T.get('statuses/user_timeline', options , function(err, data) {
  for (var i = 0; i < data.length ; i++) {
    console.log(data[i].text);
  }
})



