-- Create new table if it doesn't exist with the id field set to 1 by defaultand must be unique
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
