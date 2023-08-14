-- user signup
INSERT INTO users VALUES(4, 'user4', 'u4@e.d', '1234');

--user signin
SELECT * FROM users WHERE username = 'user4' AND password = '1234';
--or with TRUE or FALSE
SELECT COUNT(*) FROM users WHERE username = 'user4' AND password = '1234'
LIMIT 1;

-- see user profile
SELECT username, email FROM users WHERE id = 4;

-- user blocks another user
INSERT INTO users_to_users VALUES(4,1,'block');
INSERT INTO users_to_users VALUES(4,2,'friend');
INSERT INTO users_to_users VALUES(4,3,'friend');

-- see all user's friends
SELECT username, email FROM users_to_users 
    JOIN users ON users_to_users.to_user_id = users.id
WHERE from_user_id = 2 
AND relation = 'friend'
        UNION
SELECT username, email FROM users_to_users 
    JOIN users ON users_to_users.from_user_id = users.id
WHERE to_user_id = 2 
AND relation = 'friend';

--user adds some posts
INSERT INTO posts VALUES(1, 'First post of user4', '...', 4);
INSERT INTO posts VALUES(2, 'Second post of user4', '...', 4);
INSERT INTO posts VALUES(3, 'First post of johny', '...', 1);

--see all the user's posts
SELECT title, body FROM posts 
WHERE author_id = 4;

-- users comment on user4 post
INSERT INTO comments VALUES(1, 'Great post!', 2, 1);
INSERT INTO comments VALUES(2, 'Enjoyed reading!', 3, 1);
INSERT INTO comments VALUES(3, 'Nice Post!', 4, 1);

--see the comments on a post
SELECT body, username FROM comments
JOIN users on comments.author_id = users.id 
WHERE post_id = 1;
