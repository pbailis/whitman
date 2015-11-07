from flask import Flask, request, send_file
import pickle
import random

poems = pickle.load(open( "whitman-log/log.pkl"))

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

@app.route('/get_image')
def get_image():
    filename = 'pbj.png'
    return send_file(filename, mimetype='image/png')

@app.route('/')
def hello_world():
    title = random.choice(poems.keys())
    print title
    return '<font face="sans-serif"><h3>%s</h3></font><p>%s</p> <p><img src="get_image" /></p>' % (title, "<br />".join(poems[title]))

    
if __name__ == "__main__":
    app.run(debug=True)
