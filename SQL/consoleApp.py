
from orm.user import User
from orm.post import Post
from orm.comment import Comment
from orm.users_to_users import UserToUserRelation

print("Friends of user with id 2")
friends = UserToUserRelation.getFriends(2)
for id in friends:
    user = User.get(id[0])
    print('\t',user)

print("Users have been blocked by user with id: 4")
users_that_blocked_user = UserToUserRelation.getUserBlocked(4, UserToUserRelation.block_type[0])
for id in users_that_blocked_user:
    user = User.get(id[0])
    print('\t',user)

print("Users that blocked user with id: 1")
users_that_blocked_user = UserToUserRelation.getUserBlocked(1, UserToUserRelation.block_type[1])
for id in users_that_blocked_user:
    user = User.get(id[0])
    print('\t',user)

print("==========================================================================================================")
print("==========================================================================================================")
print("==========================================================================================================")
print("==========================================================================================================")

UserToUserRelation.create(3,2,UserToUserRelation.types[0])
print("Friends of user with id 2")
friends = UserToUserRelation.getFriends(2)
for id in friends:
    user = User.get(id[0])
    print('\t',user)
UserToUserRelation.delete(3,2,UserToUserRelation.types[0])
print("Friends of user with id 2")
friends = UserToUserRelation.getFriends(2)
for id in friends:
    user = User.get(id[0])
    print('\t',user)


