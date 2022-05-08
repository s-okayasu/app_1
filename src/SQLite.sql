-- SQLite
DELETE FROM problem;
DELETE FROM title;

DELETE FROM problem WHERE id IN (1);
DELETE FROM title WHERE id IN (1);
