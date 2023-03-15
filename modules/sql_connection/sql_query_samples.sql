-- Companies table DDL

CREATE TABLE companies (
    ticker varchar,
    name varchar,
    website varchar
);


-- Inserting a few lines of data into companies

INSERT INTO companies (ticker, name, website) VALUES
('AAPL', 'Apple Inc.', 'https://www.capple.com'),
('AMZN', 'Amazon.Com Inc', 'https://www.amazon.com'),
('TSLA', 'Tesla, Inc. Common Stock', 'https://www.tesla.com'),
('GOOGL', 'Alphabet Inc. Class A Common Stock', 'https://www.abc.xyz');


-- Inserting a single line of data into companies

INSERT INTO companies (ticker, name, website) VALUES ('META', 'Meta Platforms Inc', 'https://www.meta.com/');


-- Delete record example

DELETE FROM companies WHERE ticker LIKE '%TSL%'; 

-- NOTE TO THE ABOVE! A % symbol is considered a special character by Python. In order to avoid having issues 
-- executing that as a query you will need to escape the character using a second % symbol. The query will look like this:
DELETE FROM companies WHERE ticker LIKE '%%TSL%%'; 



-- Single value output example

SELECT COUNT(*) FROM companies;


-- Full table output example

SELECT * FROM companies;


-- List output example

SELECT DISTINCT ticker FROM companies;


