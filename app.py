from flask import Flask,render_template

app = Flask(__name__)

@app.route('/',)
def add_5_6():
    c=5+6
    return render_template('test1.html',name=c)

@app.route('/vinay',)
def displayVinay():
    return "Vinay yolo"    

if __name__ =='__main__':
    print("name",__name__)
    app.run('localhost',1234)