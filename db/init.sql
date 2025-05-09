-- init.sql

-- Create the 'blog' table
CREATE TABLE IF NOT EXISTS blog (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    content TEXT NOT NULL,
    author_id VARCHAR(36) NOT NULL,
    FOREIGN KEY (author_id) REFERENCES user_attribute(user_id)
);

-- Create the 'comment' table
CREATE TABLE IF NOT EXISTS comment (
    id SERIAL PRIMARY KEY,
    content TEXT NOT NULL,
    blog_id INTEGER NOT NULL,
    author_id VARCHAR(36) NOT NULL,
    FOREIGN KEY (blog_id) REFERENCES blog(id),
    FOREIGN KEY (author_id) REFERENCES user_attribute(user_id)
);
