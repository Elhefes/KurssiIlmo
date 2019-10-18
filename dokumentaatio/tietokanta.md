```CREATE TABLE account (
	id INTEGER NOT NULL, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	iban VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
);```
```
CREATE TABLE course (
	id INTEGER NOT NULL, 
	name VARCHAR(144) NOT NULL, 
	location VARCHAR(144) NOT NULL, 
	"startingDate" DATE, 
	"endingDate" DATE, 
	description VARCHAR(144) NOT NULL, 
	price FLOAT, 
	"organizerIban" VARCHAR(144) NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id) ON DELETE CASCADE
);```
```
CREATE TABLE enrolment (
	id INTEGER NOT NULL, 
	date_created DATE, 
	course_id INTEGER NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(course_id) REFERENCES course (id) ON DELETE CASCADE, 
	FOREIGN KEY(account_id) REFERENCES account (id) ON DELETE CASCADE
);```
```
CREATE TABLE invoice (
	id INTEGER NOT NULL, 
	enrolment_id INTEGER NOT NULL, 
	price FLOAT, 
	paid BOOLEAN NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(enrolment_id) REFERENCES enrolment (id) ON DELETE CASCADE, 
	CHECK (paid IN (0, 1))
);```

