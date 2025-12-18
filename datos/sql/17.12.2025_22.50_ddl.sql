CREATE TABLE comments(
    id INTEGER AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    body VARCHAR(255) NOT NULL,
    postId INTEGER NOT NULL,
    
    CONSTRAINT pk_comments PRIMARY KEY (id),
    CONSTRAINT fk_comments_posts FOREIGN KEY (postId) REFERENCES posts(id)
)