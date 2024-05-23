-- Create new table if it doesn't exist, with the id field set to 1 as default
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
