import uuid
from database import Database
import datetime

class Post(object):
    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow() ,id=None ):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.id = uuid.uuid4().hex if id is None else id
        self.created_date = date

    def save_to_db(self):
        Database.insert(collection='posts',
                        data=self.transform_to_json())

    def transform_to_json(self):
        return {
            "id" : self.id,
            "blog_id" : self.blog_id,
            "author" : self.author,
            "content" : self.content,
            "title" : self.title,
            "created_date" : self.created_date
        }

    @classmethod
    def from_mongo(cls, id):
        post_data = Database.find_one(collection='posts',
                                      query={'id':id})
        return cls(blog_id=post_data['blog_id'],
                   title=post_data['title'],
                   content=post_data['content'],
                   author=post_data['author'],
                   date=post_data['date'],
                   id=post_data['id']
                   )

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts',query={'blog_id':id})]
