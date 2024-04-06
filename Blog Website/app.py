from flask import Flask, render_template

app = Flask(__name__)

# Define your routes and other Flask-related code here

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/single')
def single():
    return render_template('single.html')


@app.route('/search', methods=['POST'])
def search():

    pass

@app.route('/topics/<topic>')
def topic(topic):
   
    pass

@app.route('/contact', methods=['POST'])
def contact():

    pass


# Other routes and Flask-related code

if __name__ == '__main__':
    app.run(debug=True)
