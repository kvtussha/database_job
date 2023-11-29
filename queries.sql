CREATE TABLE employers (
	employer_id INTEGER PRIMARY KEY,
	employer_name TEXT,
);

CREATE TABLE vacancies (
	vacancy_id SERIAL PRIMARY KEY,
	employer_id INTEGER,
	employer_name CHARACTER(100),
	job_title CHARACTER(100),
	link TEXT,
	salary INTEGER,
	FOREIGN KEY (employer_id) REFERENCES employers(employer_id)
);