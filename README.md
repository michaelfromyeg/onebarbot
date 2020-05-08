# onebarbot
This is a  Twitter bot that posts lyrics intended to be used as Instagram captions. The application uses [LyricsGenius](https://github.com/johnwmillr/LyricsGenius), a Python client for the Genius API to gather lyrics and the replies to the user with a line. User's may query by artist, album, or song.

## Usage 
A user tweets "@onebarbot" and receives a caption back. See it in action [here](https://twitter.com/captionsbydrake).

## Installation
I'll leave these instructions here in case you want to reconfigure the bot to work for your favourite artist. Perhaps maybe I'll extend it so that a user is able to request their favourite artist.

### Python
1. Run `pip install -U virtualenv`
2. Create a virtual environment by running `virtualenv env` in the root directory
3. Activate it by running `.\env\Scripts\activate`
4. Run `pip install requirements.txt`
5. If you add any modules, run `pip freeze > requirements.txt`

### Twitter
1. Create a [Twitter](https://twitter.com/) account; choose a fun handle!
2. Go to [Twitter for Developers](https://developer.twitter.com/en) and register an app
3. Once Twitter confirms that your app has been created, navigate to it and find the "details" section
4. Create a file in `src/` called `credentials.py`
5. Go to keys and tokens and copy-paste the values into `credentials.py`; you'll have to generate the access token and access token secret

`# Twitter`

`twitter_consumer_key = ""`

`twitter_consumer_secret = ""`

`twitter_access_token = ""`

`twitter_access_token_secret = ""`

`# Genius`

`genius_client_id = ""`

`genius_client_secret = ""`

`genius_client_access_token = ""`


## Deployment

### PythonAnywhere [[source]](https://www.twilio.com/blog/build-deploy-twitter-bots-python-tweepy-pythonanywhere)
1. Register an account [here](https://www.pythonanywhere.com/)
2. Click on files in the navigation bar
3. Upload the files from this directory
4. Select tasks from the navigation bar
5. Set the file path to `/home/<your username>/bot.py` and schedule the bot
6. ...and you're done!

### Heroku
TBD

### Raspberry Pi
TBD