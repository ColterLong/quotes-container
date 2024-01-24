-- CREATE DATABASE quotesDb;
USE quotesDb;
CREATE TABLE quotes (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(30),
    quote VARCHAR(300),
    PRIMARY KEY(id)
);

insert into quotes (quote, name)
values ('Fortune favors the bold.', 'Virgil');

insert into quotes (quote, name)
values ('Great minds discuss ideas; average minds discuss events; small minds discuss people.', 'Eleanor Roosevelt');

insert into quotes (quote, name)
values ('We are what we repeatedly do; excellence, then, is not an act but a habit.', 'Aristotle');

insert into quotes (quote, name)
values ('The successful warrior is the average man, with laser-like focus.', 'Bruce Lee');

insert into quotes (quote, name)
values ('You can discover more about a person in an hour of play than in a year of conversation.', 'Plato');