CREATE TABLE employers (
	employer_id INTEGER PRIMARY KEY,
	employer_name TEXT,
	count_vacancy INTEGER
);

CREATE TABLE vacancies (
	vacancy_id SERIAL PRIMARY KEY,
	employer_id INTEGER,
	employer_name CHARACTER(100),
	job_title CHARACTER(100),
	vacancy_link TEXT,
	salary INTEGER,
	requirement TEXT,
	responsibility TEXT,
	FOREIGN KEY (employer_id) REFERENCES employers(employer_id)
);
