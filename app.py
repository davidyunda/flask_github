from flask import Flask, render_template, request
from github_api import get_github_user_info  # NOT the same as requests 

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/about')
def about():
    author = 'David'
    concepts = ['flask', 'web', 'html']
    return render_template('about.html', author=author, concepts=concepts)

@app.route('/get_user')
def get_github_user():
    print(request.args)
    username = request.args.get('username')
    if username:
        user_info = get_github_user_info(username)
        return render_template('github.html', username=username, user_info=user_info)
    else:
        return "error"

    
if __name__ == '__main__':
    app.run()