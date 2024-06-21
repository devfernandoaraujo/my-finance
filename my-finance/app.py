from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

app.route('/')
def home():
     print("Home route hit")
     return render_template('home/index.html') 

@app.route('/test')
def test():
    return "Test route is working!"

if __name__ == '__main__':
    app.run(debug=True)