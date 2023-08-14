from domain.User import User
from domain.Post import Post
from domain.Message import Message

from time import sleep

# # data structures for posts and comments
# user_1_posts = []
# user_1_comments = []
# user_2_posts = []
# user_2_comments = []

# # user entities
# u1 = User(1, "johny", "j@example.mail", "123456")
# u2 = User(2, "marry", "marry@example.mail", "654321")

# # post entities
# user_1_posts.append(u1.addPost(1, "Jonnys Post1", "some body1"))
# user_1_posts.append(u1.addPost(2, "Jonnys Post2", "some body2"))
# user_1_posts.append(u1.addPost(3, "Jonnys Post3", "some body3"))

# user_2_posts.append(u2.addPost(3, "Marry Post", "some body"))

# # comment entities
# user_1_comments.append(u1.addComment(1, "1st comment", user_1_posts[0]))
# user_2_comments.append(u2.addComment(2, "2nd comment", user_1_posts[0]))

# user_1_comments.append(u1.addComment(3, "1st comment", user_1_posts[1]))
# user_2_comments.append(u2.addComment(4, "2nd comment", user_1_posts[1]))


# # PRINTING RESULTS

# # ATTENTION:
# #   from user_1_posts woudnt be any posts deleted
# #   from user_1_comments woudnt be any comments deleted
# u1.removePost(user_1_posts[1])
# u1.removeComment(user_1_comments[0])

# print("Comments of the u1(list from the User object):")
# for comment in u1.comments:
#     print(f"ID: {comment.id} with ADDRESS: {id(comment)}")

# ###
# print("user_1_comments(consoleAPP.py list):")
# for comment in user_1_comments:
#     print(f"ID: {comment.id} with ADDRESS: {id(comment)}")


# Message.send("Hi!", None, None)
# Message.send("Hi, how are you!", None, None)

# sleep(1)
# print(Message.all[0].body)
# sleep(1)
# print(Message.all[0].body)
# print(Message.all[0].created)
# print(Message.all[0].viewed)
# print("===============================================")
# print(Message.all)
# print("===============================================")


u1 = User(1, "johny", "j@d.e", "123")
u2 = User(2, "marry", "m@d.e", "123")

m1 = Message.send("Hi", u1, u2)

print(f"{u1.username} wrote: {m1} to {u2.username}")
