from flask import Flask, render_template , request 
from textblob import TextBlob

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('form.html')


@app.route('/submit', methods = ['POST'])
def form_data():
   user_data = request.form.get('user_data')
   blob = TextBlob(user_data)
   singu = blob.words.singularize()
   plural = blob.words.pluralize()            

   return render_template('predict.html', data = f'singular of the word is: {singu} , plural of the word is: {plural}')
   
if __name__ == '__main__':
    app.run(app.run(host='0.0.0.0', port=8080))
