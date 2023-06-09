from domain.User import User
from domain.Post import Post

# data structures for posts and comments
user_1_posts = []
user_1_comments = []
user_2_posts = []
user_2_comments = []

# user entities
u1 = User(1, "johny", "j@example.mail", "123456")
u2 = User(2, "marry", "marry@example.mail", "654321")

# post entities
user_1_posts.append(u1.addPost(1, "Jonnys Post", "some body"))
user_1_posts.append(u1.addPost(2, "Jonnys Post", "some body"))

user_2_posts.append(u2.addPost(3, "Marry Post", "some body"))

# comment entities
user_1_comments.append(u1.addComment(1, "1st comment", user_1_posts[0]))
user_2_comments.append(u1.addComment(2, "2nd comment", user_1_posts[0]))

user_1_comments.append(u1.addComment(3, "1st comment", user_1_posts[1]))
user_2_comments.append(u1.addComment(4, "2nd comment", user_1_posts[1]))


# PRINTING RESULTS
for comment in user_1_comments:
    print(comment)
