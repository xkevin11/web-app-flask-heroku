

# Reference: http://flask.pocoo.org/docs/1.0/quickstart/#quickstart



from flask import Flask, url_for, render_template, request
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'


# Routing
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()



# Variable Rules
# You can add variable sections to a URL by marking sections with <variable_name>. 
# Your function then receives the <variable_name> as a keyword argument. 
# Optionally, you can use a converter to specify the type of the argument like <converter:variable_name>.


@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath



with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))


# Rendering Templates
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('headings.html', name=name)


@app.route('/hi', methods=['GET','POST'])
def hi():
    if request.method == 'GET':
        return render_template('hi_get.html')
    else:
        name=request.form.get("name")
        return render_template('hi.html', name=name)




if __name__ == "__main__":
  app.run(host='0.0.0.0')

# If without app.run(), need the following to Run:
# 	export FLASK_APP=hello.py
#	flask run

# Debug mode lets web app refresh without having to restart server every time
# export FLASK_ENV=development


