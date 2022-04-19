# CPSC 223p
##  Google Sign In with Your Flask URL Shortener

Remember the book [Flask Web Development](https://csuf-primo.hosted.exlibrisgroup.com/permalink/f/43rjjt/TN_cdi_askewsholts_vlebooks_9781491991718) book by [Miguel Grinberg](https://blog.miguelgrinberg.com/) is available through the [CSUF library](http://www.library.fullerton.edu/). Miguel Grinberg has also written [the Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) for those unwilling to use books.

You've created your URL shortener but you don't want just anyone to use it. If a member of the public wants to expand a URL, that is allowed. However only authenticated users can shorten URLs.

Starting with part-2, your objective is to add in GitHub sign in using the [Flask-Dance](https://pypi.org/project/Flask-Dance/) module. Flask-Dance supports a large number of different [providers](https://flask-dance.readthedocs.io/en/latest/providers.html). In our case, we shall use Google's [OAuth API](https://developers.google.com/identity/sign-in/web/sign-in) to authenticate our app.

To install Flask-Dance which will work with SQLAlchemy, use the `Flask-Dance[sqla]` module.

## Enable OAuth API on Google Cloud
You'll first need to sing up for a Google Cloud developer account. This is your current Gmail account or any Gmail account you would like to use. Go to Google Cloud [https://cloud.google.com/] and start your free trial of the Google cloud services.

Google provides [instructions on how to enable the OAuth API](https://support.google.com/googleapi/answer/6158849?hl=en) however you may find the additional information provided in this prompt useful in navigating the console.

Once you have an account set up, go to the console [https://console.cloud.google.com/] and select a project from the drop down menu that is at the top of the window towards the center. Any project will do.

In the upper left hand corner is what is called a hamburger. It is three vertical lines. Click the following links through the menus: Hamburger -> APIs & Services -> Create Credentials -->> OAuth client ID (at the top). Select Web Application.

Fill in the form with the following information. Make it clear what you are naming things so you can later disable the API should you choose to.

Name: CPSC223P Google Auth App
Authorized JavaScript origins URIs
http://127.0.0.1:5000
http://localhost:5000

Authorized redirect URIs
http://127.0.0.1:5000/
http://localhost:5000/

You will be presented with 'Your client ID' and 'Your client secret'. Copy and paste these strings someplace safe so you can use them in configuring your application.

## Completing your App
Copy your project from part-2 into the part-3 directory. Our goal is the modify the application such that a user may or may not be authenticated. Again, let's keep it simple and assume that anyone that is authenticated has every right to use all the application's features and someone who is not may only use some of the features.

Remember the application will have the following routes. You must use templates with the home and list routes. You can optionally use templates with the url and delete routes. The routes that are only accessible to authenticated users are labeled as authenticated-only.

* home - authenticated-only - This is the index page. Using `GET`, the webform for shortening a URL is presented. Using `POST`, a new ShortUrl object is created and stored. When a URL is successfully created and stored a message is given on the page and the web form is shown again. If a URL is not successfully created (duplicate or malformed), then an error message is shown and the web form is shown again.
* list - authenticated-only - List all shortened URLs as rows in an HTML table. The table shall have five columns. The first column is the ShortUrl id, the second is the ShortUrl original URL, the third is the ShortUrl short URL, the forth is the ShortUrl creation date, and the fifth is a hyperlink to delete/<id> where id is the ShortUrl object's id in the database.
* url/<short_code> - Given the short_code, look up the URL in the database and redirect the web browser to the original URL.
* delete/<id> - authenticated-only - Given the id, remove that object from the database. If successful, the list page reloads otherwise an error message is shown on the list page.

The author of Flask-Dance, David Baumgold, has written several demonstration projects for Google authentication with Flask-Dance. The project [flask-dance-google-security-sqla](https://github.com/singingwolfboy/flask-dance-google-security-sqla) demonstrates using Flask-Dance and Flask-Security with Google authentication. I recommend using this project as inspiration on how to integrate Flask-Dance into your existing URL shortener. Alternatively, the project [flask-dance-google-sqla](https://github.com/singingwolfboy/flask-dance-google-sqla) takes the same approach yet excludes Flask-Security.


