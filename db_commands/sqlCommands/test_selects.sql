WITH yeas AS (
        SELECT COUNT(*) AS y
            FROM vote NATURAL JOIN bill
            WHERE name = 'Bipartisan Background Checks Act' AND vote = 'yea'),
    tot_vote AS (
        SELECT COUNT(*) AS t
        FROM vote NATURAL JOIN bill
        WHERE name = 'Bipartisan Background Checks Act')
SELECT cast(floor((cast(y AS float) * 10000)/(cast(t AS float))) AS float)/100 AS percentage
    FROM yeas, tot_vote;

WITH vs AS(
        SELECT congress_number, district, vote
            FROM bill NATURAL JOIN vote
            WHERE name = 'Bipartisan Background Checks Act'),
    rep AS(
        SELECT congress_number, district
            FROM representative
            WHERE first = 'Denny' and last = 'Heck')
SELECT vote
    FROM vs NATURAL JOIN rep;

WITH sal AS (
        SELECT speaker AS SALARY
            FROM payroll
            WHERE congress_number = 115),
    rep AS(
        SELECT first, last
        FROM chamber_leader NATURAL JOIN representative
        WHERE title = 'speaker' AND congress_number = 115)
SELECT *
    FROM rep, sal;

SELECT (cast (votes_for AS float))/(cast (total_votes AS float)) * 100 as percentage FROM election NATURAL JOIN representative WHERE first = 'Kelly' AND last = 'Ayotte' AND congress_number = 111;

WITH r1 as (
        SELECT first, last, vote, bill_number, congress_number
            FROM vote NATURAL JOIN representative
            WHERE first = 'Ron' AND last = 'Wright'),
    r2 as (
        SELECT first, last, vote, bill_number, congress_number
            FROM vote NATURAL JOIN representative
            WHERE first = 'Ilhan' AND last = 'Omar')
SELECT bill.name, r1.first, r1.last, r1.vote, r2.first, r2.last, r2.vote
    FROM r1, r2, bill
    WHERE r1.bill_number = r2.bill_number
        AND r1.bill_number = bill.bill_number
        AND r2.bill_number = bill.bill_number
        AND r1.vote != r2.vote;


SELECT floor((cast (votes_for AS float) * 10000)/(cast (total_votes AS float))) / 100
    AS percentage
    FROM election NATURAL JOIN representative
    WHERE first = 'Kelly' AND last = 'Ayotte' AND congress_number = 111;

SELECT name
    FROM committee
    WHERE (2019 - cast(date_established AS integer)) > 10;
