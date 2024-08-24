from flask import Flask, render_template, request
import util

app = Flask(__name__)
util.load_data()

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/Get-data',methods=['GET','POST'])
def get_result():
    if request.method=='POST':
        message = str(request.form['message'])
        result = util.predict(message)
        return render_template('index.html',result=result)
    return render_template('index.html')
if __name__=='__main__':
    app.run()