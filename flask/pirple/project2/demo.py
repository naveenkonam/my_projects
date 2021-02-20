from flask import Flask,render_template

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return render_template('demo.html')

@app.route('/aboutme',methods=['GET'])
def about():
    return render_template('about.html')
if __name__ == '__main__':
    app.run(port=7000, debug= True)
