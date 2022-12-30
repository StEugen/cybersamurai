DROP TABLE IF EXISTS notes cascade;

--Note Table
CREATE TABLE notes(
    id SERIAL PRIMARY KEY NOT NULL,
    note TEXT,
    done BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP
)