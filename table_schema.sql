DROP TABLE IF EXISTS pitchfork_data, spotify_data;

CREATE TABLE pitchfork_data(
	id SERIAL PRIMARY KEY,
	reviewid INT NOT NULL,
	title VARCHAR NOT NULL,
	artist VARCHAR NOT NULL,
	score INT NOT NULL,
	best_new_music INT ,
	pub_date VARCHAR(10) NOT NULL,
	content VARCHAR,
	genre VARCHAR
);

CREATE TABLE spotify_data(
	id SERIAL PRIMARY KEY,
	artist_name VARCHAR NOT NULL,
	popularity_score INT NOT NULL,
	spotify_genres VARCHAR NOT NULL,
	followers INT NOT NULL
);