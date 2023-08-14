-- CREATE a new DB
CREATE DATABASE mini_social_ddd;

-- DELETE a new DB
DROP DATABASE mini_social_ddd;

-- CREATE a new table to store users
CREATE TABLE users(
    id integer PRIMARY KEY,
    username varchar(30) UNIQUE,
    email varchar(30) 
);

-- DELETE a table
DROP TABLE users;

-- MODIFICATE table
ALTER TABLE users
ADD COLUMN password varchar(30);



-----------------------------------------------------------
--  REST OF CODE ---
-----------------------------------------------------------

-- Posts
CREATE TABLE posts(
    id integer PRIMARY KEY,
    title varchar(100),
    body varchar(50000),
    author_id integer 
);
ALTER TABLE posts
ADD FOREIGN KEY(author_id) REFERENCES users(id);

-- Comments
CREATE TABLE comments(
    id integer PRIMARY KEY,
    body varchar(50000),
    author_id integer, 
    post_id integer 
);
ALTER TABLE comments
ADD FOREIGN KEY(author_id) REFERENCES users(id);
ALTER TABLE comments
ADD FOREIGN KEY(post_id) REFERENCES posts(id);


-- Users to users
CREATE TABLE users_to_users(
    from_user_id integer,
    to_user_id integer
);
ALTER TABLE users_to_users
ADD COLUMN relation varchar(10);
ALTER TABLE users_to_users
ADD FOREIGN KEY(from_user_id) REFERENCES users(id);
ALTER TABLE users_to_users
ADD FOREIGN KEY(to_user_id) REFERENCES users(id);