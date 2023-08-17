import psycopg2
from .model import Model
from .user import User

## using ONLY static vars and func

# adding/removing to blacklist can only the user that wants to block/remove someone
# a user can not add/remove himself from a blacklist of someone
# no update function, only create and delete

class UserToUserRelation(Model):
    # static variables of type tuple -> can not be changed
    types      = ('friend', 'block')
    block_type = ('from_user_id', 'to_user_id')
    
    # CRUD
    def create(from_user, to_user, relation):
        if from_user != None and to_user != None and relation != None:
            conn, cursor = Model.connect()
            cursor.execute(f"INSERT INTO users_to_users VALUES({from_user},{to_user},'{relation}');")
            conn.commit()


    def all():
        relations = []
        _, cursor = Model.connect()
        cursor.execute("SELECT * FROM users_to_users;")
        relation_data = cursor.fetchall()
        for item in relation_data:
            from_user_id = User.get(item[0])
            to_user_id   = User.get(item[1])
            relation = UserToUserRelation(from_user_id, to_user_id, item[2],)
            relations.append(relation)
        return relations
    
    def getFriends(user_id):
        _, cursor = Model.connect()
        cmd = ( "SELECT id FROM users_to_users "                             +               
                "JOIN users ON users_to_users.to_user_id = users.id "        +
               f"WHERE from_user_id = {user_id} "                            +           
                "AND relation = 'friend' "                                   +                             
                "UNION "                                                     +                       
                "SELECT id FROM users_to_users "                             +                   
                "JOIN users ON users_to_users.from_user_id = users.id "      +                         
               f"WHERE to_user_id = {user_id} "                              +         
                "AND relation = 'friend';")    
        cursor.execute(cmd)                                       
        friends = cursor.fetchall()
        return friends
    
    # block_type to return the list with other users that: 
    # block_type = from_user_id  --->           have been blocked by the user_id
    # block_type = to_user_id    --->           blocked the user_id
    def getUserBlocked(user_id, block_type):
        if block_type == UserToUserRelation.block_type[0]:
            read_type = UserToUserRelation.block_type[1]
        else:
            read_type = UserToUserRelation.block_type[0]

        _, cursor = Model.connect()
        cmd = ( "SELECT id FROM users_to_users "                             +               
               f"JOIN users ON users_to_users.{read_type} = users.id "       +
               f"WHERE {block_type} = {user_id} "                            +           
                "AND relation = 'block';")    
        cursor.execute(cmd)                                       
        blocked = cursor.fetchall()
        return blocked

    def delete(from_user_id, to_user_id, relation):
        cmd = ""
        if from_user_id == None:
            if to_user_id == None:
                if relation == None:
                    return
                else:
                    cmd = f"DELETE FROM users_to_users WHERE relation = '{relation}';"
            else:
                if relation == None:
                    cmd = f"DELETE FROM users_to_users WHERE to_user_id = {to_user_id};"
                else:
                    cmd = f"DELETE FROM users_to_users WHERE to_user_id = {to_user_id} AND relation = '{relation}';"
        else:
            if to_user_id == None:
                if relation == None:
                    cmd = f"DELETE FROM users_to_users WHERE from_user_id = {from_user_id};"
                else:
                    cmd = f"DELETE FROM users_to_users WHERE from_user_id = {from_user_id} AND relation = '{relation}';"
            else:
                if relation == None:
                    cmd = f"DELETE FROM users_to_users WHERE from_user_id = {from_user_id} AND to_user_id = {to_user_id};"
                else:
                    cmd = f"DELETE FROM users_to_users WHERE from_user_id = {from_user_id} AND to_user_id = {to_user_id} AND relation = '{relation}';"

        conn, cursor = Model.connect()
        cursor.execute(cmd)
        conn.commit()

    # BEHAVIOUR
