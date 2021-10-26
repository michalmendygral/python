import uuid
import datetime
from database import Database
from models.post import Post

class Blog(object):
    def __init__(self, author, title, description, id=None):
        self.author= author,
        self.title=title,
        self.description=description
        self.id=uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = input("Enter post title: ")
        content = input("Enter your content: ")
        date = input("Enter today date(DDMMYY): ")
        if date == "":
            date = datetime.datetime.utcnow()
        else:
            date = datetime.datetime.strptime(date, "%d%m%Y")
        post = Post(blog_id=self.id,
                    author=self.author,
                    title=title,
                    content=content,
                    date=date)
        post.save_to_db()


    def get_posts(self):
        return Post.from_blog(self.id)

    def save_to_mongo(self):
        Database.insert(collection='blogs',
                        data=self.transform_to_json())

    def transform_to_json(self):
        return {
            'author':self.author,
            'title':self.title,
            'description':self.description,
            'id':self.id
        }


    # classmethod instead of staticmethod to use 'cls' instead of name('Blog')
    # after change class name(Blog) we still have cls,
    # better to improve in future, coz have no impact if changes needed
    @classmethod
    def get_from_mongo(cls, id):
        blog_data = Database.find_one(collection='blogs',
                                        query={'id':id})
        return cls(author=blog_data['author'],
                   title=blog_data['title'],
                   description=blog_data['description'],
                   id=blog_data['id']
                   )

