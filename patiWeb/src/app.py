from flask import Flask, render_template, request, session, make_response

from src.models.blog import Blog
from src.models.post import Post
from src.models.user import User
from src.common.database import Database

app =Flask(__name__) #'__main__'
app.secret_key = "michal"

@app.route("/")
def home_template():
    return render_template('index.html')

@app.route('/login') #endpoint:www.site.com/api
def login_template():
    return render_template('login.html')

@app.route('/register') #endpoint:www.site.com/api
def register_template():
    return render_template('register.html')

#decorator causing always run as first
@app.before_first_request
def initialize_database():
    Database.initialize()

@app.route('/auth/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    if User.login_valid(email, password):
        User.login(email)
    else:
        session['email'] = None

    return render_template("profile.html", email=session['email'])

@app.route('/auth/register', methods=['POST'])
def register_user():
    email = request.form['email']
    password = request.form['password']

    User.register(email,password)
    #session['email'] = email

    return render_template("profile.html", email=session['email'])

@app.route('/blogs/<string:user_id>')
@app.route('/blogs')
def user_blogs(user_id=None):
    if user_id is not None:
        user = User.get_by_id(user_id)
        print("by user")
    else:
        user = User.get_by_email(session['email'])
        print("by mail")

    blogs = user.get_blogs()
    print(f"user : {user._id}, blogs : {blogs}")

    return render_template("user_blogs.html", blogs=blogs, email=user.email)

@app.route('/blogs/new', methods=['POST','GET'])
def create_new_blog():
    if request.method == 'GET':
        return render_template("new_blog.html")
    else:
        title = request.form['title']
        description = request.form['description']
        user = User.get_by_email(session['email'])

        new_blog = Blog(user.email, title, description, user._id)
        new_blog.save_to_mongo()
        #
        return make_response(user_blogs(user._id))

@app.route('/posts/<string:blog_id>')
def blog_posts(blog_id):
    blog = Blog.from_mongo(blog_id)
    posts = blog.get_posts()
    #print(f"blog : {blog._id}, blogs : {posts}")
    return render_template('post.html', posts=posts, blog_title = blog.title)

@app.route('/posts/<string:blog_id>')
def create_new_post(blog_id):
    print(f"blog : {blog_id}")

    if request.method == 'GET':
        return render_template('new_post.html', blog_id=blog_id)
    else:
        title = request.form['title']
        content = request.form['content']
        user = User.get_by_email(session['email'])

        new_post = Post(blog_id, title, content, user.email)
        new_post.save_to_mongo()

        return make_response(blog_posts(blog_id))



if __name__ == '__main__':
    app.run(port=4995, debug=True)















