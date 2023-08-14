-- INSERT data
INSERT INTO users
VALUES(1, 'johny', 'j@e.d', '123');
INSERT INTO users
VALUES(2, 'marry', 'm@e.d', '321');
INSERT INTO users
VALUES(3, 'peter', 'p@e.d', '333');
-- OR
INSERT INTO users
VALUES
    (1, 'johny', 'j@e.d', '123'),
    (2, 'marry', 'm@e.d', '321'),
    (3, 'peter', 'p@e.d', '333');
-- OR
INSERT INTO users(username, email)
VALUES ('anonymus', 'anno');

-- SELECT all the cols for users
SELECT * FROM users;
--OR
SELECT username, email FROM users;
--OR
SELECT username AS name, email FROM users;
--OR
SELECT * FROM users WHERE id>0;
--OR
SELECT * FROM users 
WHERE id>0
ORDER BY id ASC;

-- UPDATE data
UPDATE users 
SET password = '111' 
WHERE username = 'peter';

DELETE FROM users 
WHERE username = 'peter';


-----------------------------------------------------------
--  REST OF CODE ---
-----------------------------------------------------------


INSERT INTO posts VALUES(1, 'Peters Post', 'Post Body', 3);


INSERT INTO users_to_users VALUES(1,2);