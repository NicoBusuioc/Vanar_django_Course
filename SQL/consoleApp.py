
from orm.user import User
from orm.post import Post
from orm.comment import Comment

#post = Post.create(5, 'fifth Post', '.....')
posts = Post.all()
for item in posts:
    print(item)



