from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h2>Enter Your Name</h2>
        <form action="/welcome" method="post">
            <input type="text" name="username" placeholder="Enter name">
            <input type="submit" value="Submit">
        </form>
    '''

@app.route('/welcome', methods=['POST'])
def welcome():
    name = request.form['username']
    return f"<h1>Welcome, {name}!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
