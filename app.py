from flask import Flask,render_template,jsonify
import pymysql.cursors

app = Flask(__name__)
connection = pymysql.connect(host='localhost',user='root',password='',db='webscrape',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)

@app.route('/',)
def display_quotes():
    try:
        with connection.cursor() as cursor:
            sql = "SELECT quotes.id,author.name,quotes.quote from quotes,author WHERE quotes.author_id=author.id order by quotes.id"
            cursor.execute(sql) 
            quotes = cursor.fetchall()
        return render_template('test1.html',data=quotes)

    except pymysql.Error as err:
            return render_template('test1.html',error=err)


if __name__ =='__main__':
    print("name",__name__)
    app.run('localhost',1234,debug=True)