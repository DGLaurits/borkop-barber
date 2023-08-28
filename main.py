from flask import Flask, render_template

print("hello")

# Create a Flask app
app = Flask(__name__)

# Define a route and function to handle the route
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/priser')
def pricing():
    return render_template('pricing.html')

# Run the app if this script is executed
if __name__ == '__main__':
    app.run(debug=True)