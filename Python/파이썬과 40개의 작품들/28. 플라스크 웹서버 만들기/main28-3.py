from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"

@app.route('/form')
def map():
    return render_template("form.html")

def main():
    app.run(debug=True,port=80)
    
if __name__== '__main__':
    main()