CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    username TEXT UNIQUE, 
    password TEXT
);
CREATE TABLE projects (
    id SERIAL PRIMARY KEY, 
    project_name TEXT UNIQUE
);
CREATE TABLE feedback_messages (
    id SERIAL PRIMARY KEY,
    content TEXT,
    project_id INTEGER REFERENCES projects,
    receiver_id INTEGER REFERENCES users
);
CREATE TABLE project_members (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    user_name TEXT,
    user_role TEXT,
    project_id INTEGER REFERENCES projects
);
