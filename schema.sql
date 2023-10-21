CREATE TABLE Users (
    id SERIAL PRIMARY KEY, 
    username TEXT UNIQUE, 
    password TEXT
);
CREATE TABLE Projects (
    id SERIAL PRIMARY KEY, 
    project_name TEXT UNIQUE
);
CREATE TABLE Feedback_messages (
    id SERIAL PRIMARY KEY,
    content TEXT,
    project_id INTEGER REFERENCES projects,
    receiver_id INTEGER REFERENCES users
);
CREATE TABLE Project_members (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    user_name TEXT,
    user_role TEXT,
    project_id INTEGER REFERENCES projects
);
