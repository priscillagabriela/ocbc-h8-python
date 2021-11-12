# 1
# from os import name
# from markupsafe import escape
# from flask import Flask, request, render_template

# app = Flask(__name__,template_folder='templates')
#     #   Flask('__main__')

# @app.route('/movies')
# @app.route('/books') #will invoke the func if we hit 127.0.0.1/books
# @app.route('/') #will invoke the func if we hit 127.0.0.1/
# def hello_world():
#     sum = a = 19999
#     # return f'Hello, World! {sum}'
#     # return "<h1>Hello, World!</h1> <p>{}</p> <p> <b> lorem ipsum fdfkjfsk </b> </p>".format(sum)
#     page_content = "<h1>Hello, World!</h1> <p>{}</p> <p> <b> lorem ipsum fdfkjfsk </b> </p>".format(sum)
#     page_content += "<i> italic hello </i>"
#     return page_content

# @app.route('/<name>') #127.0.0.1/some_value_bebas
# # @app.route('/name') #127.0.0.1/name
# def hellox(name):
#     # return f"Hello, {name}"
#     return f"Hello, {escape(name)}"

# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)

# # apakah dijalankan sebagai standalone
# if __name__ == '__main__':
#     app.run(debug=True)

# 2
# from markupsafe import escape
# from flask import Flask, url_for
# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p> Hello, World! </p>"

# @app.route("/<name>")
# def hello(name):
#     return f"Hello, <b>{escape(name)}</b>"

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     return f'Post {post_id}'

# @app.route('/')
# def index():
#     return 'Index Page'

# @app.route('/hello')
# def hello():
#     return 'Hello, World'


# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return f'User {escape(username)}'

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return f'Post {post_id}'

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return f'Subpath {escape(subpath)}'

# @app.route('/projects/')
# def projects():
#     return 'The project page'

# @app.route('/about')
# def about():
#     return 'The about page'

# if __name__ == '__main__':
#     app.run()

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))

# 3

from flask import Flask, render_template, request
from author_book import author_books

app = Flask(__name__)

@app.route('/home')
@app.route('/')
def home():
    #return 'Hello, World!'
    return render_template('index.html')

@app.route('/author', methods=['GET','POST'])
def author():
    if 'author_id' in request.form:
        author_books[request.form['author_id']] = []
    #return '<h2> Author Bio </h2> <a href="/"> Home Page </a>'
    return render_template('author.html', author_books=author_books)

@app.route('/books/<int:author_id>')
def books(author_id):
    # html =  f'List of Books authored by {author_id}:'
    # html += '<ul> <li>intro to lyfe</li><li>intro to lyfe 2</li><li>intro to lyfe 3</li></ul>'
    #return html
    # return render_template('book.html', author_id=author_id, book_list=author_books[author_id])
    # if author_id != 400:
    if len(author_books[author_id])==0:
        return render_template('book.html', author_id=author_id)
    else:
        return render_template('book.html', author_id=author_id, book_list=author_books[author_id])

if __name__ == '__main__':
    app.run(debug=True)