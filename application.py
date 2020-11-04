from flask import Flask, request, render_template, redirect, url_for 

application = Flask(__name__)

@application.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@application.route('/all-items', methods=['GET'])
def all_items():
    return render_template('items.html')

if __name__ == "__main__":
    application.run(debug=True)
