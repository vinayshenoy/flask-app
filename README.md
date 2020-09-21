# flask-app

Introduction
Basic example for flask to display contents in webpage from database.


Setup

To install this modules, type the following commands in cmd:
>pip install Flask,render_template

After connection to mysql, write the query to fetch data from database
    >sql = "SELECT quotes.id,author.name,quotes.quote from quotes,author WHERE quotes.author_id=author.id order by quotes.id"
    
Output:
>Displays id, author names and quotes into a webpage. 







