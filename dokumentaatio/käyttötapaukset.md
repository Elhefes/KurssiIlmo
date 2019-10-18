# KurssiIlmon käyttötapaukset
Sovelluksessa on yhdenlaisia käyttäjiä. Kaikki siis voivat sekä ilmoittautua kursseille, sekä järjestää omia kursseja.

## Sovelluksen käyttäjä voi:
* rekisteröityä ja kirjautua sivulle
```
INSERT INTO account (name, username, password, iban) VALUES (?, ?, ?, ?)
```
```
SELECT account.id AS account_id, account.name AS account_name, account.username AS account_username, account.password AS account_password, account.iban AS account_iban 
FROM account 
WHERE account.username = ? AND account.password = ?
```
* ilmoittautua kursseille sekä poistaa ilmoittautumisiaan
```
INSERT INTO enrolment (date_created, course_id, account_id) VALUES (CURRENT_TIMESTAMP, ?, ?)
```
```
DELETE FROM enrolment WHERE enrolment.id = ?
```
* nähdä listan kaikista kursseista, johon on ilmoittautunut
```
SELECT enrolment.id AS enrolment_id, enrolment.date_created AS enrolment_date_created, enrolment.course_id AS enrolment_course_id, enrolment.account_id AS enrolment_account_id 
FROM enrolment

SELECT name FROM Course WHERE id =? 
```
* selata omia avoimia sekä maksettuja laskujaan
```
SELECT invoice.id AS invoice_id, invoice.enrolment_id AS invoice_enrolment_id, invoice.price AS invoice_price, invoice.paid AS invoice_paid 
FROM invoice 
WHERE invoice.enrolment_id = ?
```
* luoda uusia kursseja sekä poistaa niitä
```
INSERT INTO course (name, location, "startingDate", "endingDate", description, price, "organizerIban", account_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
```
```
DELETE FROM course WHERE course.id = ?
```
* muokata kurssinsa tietoja (esimerkiksi kuvausta tai päivämääriä)
```
UPDATE course SET name=?, location=?, "startingDate"=?, "endingDate"=?, description=?, price=? WHERE course.id = ?
```
* saada yhteenvedon kurssillensa ilmoittautuneiden tiedoista
```
SELECT Account.name FROM Account JOIN Course ON Account.id= Course.account_id WHERE Course.id = ?
```
* nähdä, kuinka paljon ihmisiä on ilmoittautunut kurssille
```
SELECT COUNT(*) FROM Account LEFT JOIN Enrolment ON Enrolment.account_id = Account.id WHERE Enrolment.course_id = ?
```
* poistaa käyttäjänsä
  * tämä poistaa ensiksi kaikki käyttäjän ilmoittautumiset, omat kurssit (ja niihin ilmoittautumiset), jonka jälkeen poistaa vasta käyttäjän.
```
DELETE FROM invoice WHERE invoice.id = ?

DELETE FROM enrolment WHERE enrolment.id = ?

DELETE FROM course WHERE course.id = ?

DELETE FROM account WHERE account.id = ?
```
