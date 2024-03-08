# INTRODUCTION TO SQL

## 0. List databases
This is a statement that displays of all database on my MySQL sever
SHOW DATABASES

## 1. Create a database
A way of creating a database only if it does not exit;
this is done by using the "IF NOT EXISTING" statmenent inbetween
the create stament and the database name

## 2. Delete a database
A way to delete a database from MySQL sever
you can use "IF NOT EXISTS"
the key word here is DROP.
DROP is use to get rid of unwanted objects

## 3. List tables
Show is used to do so.
SHOW TABLES;

## 4. First table
Creating an table and giving discription to the table. ie the columsyou use CREAT TABLE `name`
then add the discription(columns) by (giving the variable name and it type seperated by a comma) check code to understand more
### REMEMBER TO ALWAYS USE "IF NOT EXISTS"

## 5. Full description
Getting the full description of the table. This is acheived by usingSHOW CREATE TABLE `table_name`;
Note that EXPLAIN and DESCRIBE can do similar things. Read more on that.
What is the difference in SHOW CREAT TABLE and SHOW TABLE

## 6. List all in table
Listing all the row in a table. You get this with the SHOW *
in effect it shows everything

## 7. First add
To add a new row you use the inser. Each insert must be done separately

## 8. Count 89
This is to count the number of records with id 89 in the table
You will need to use SELECT COUNT(*) then choose the table and use WHERE to give the condition

## 9. Full creation
Creates a new table with directions and valuse
you need to insert 4 rows
use CREATE TABLE add the name then give the discreption
remeber to use "IF NOT EXISTS"
then you can now use INSERT INTO to do the insertion

## 10. List by best
List all the result with the hights being first
You do this by using SELECT the score column then indicate the tableto get it.
Now use ORDER BY to set it to descending order DESC

## 11. Select the best
This list all the record of scores with than name
but there is a condition of score being greated than 10
this is acheived by using WHERE score >= 10

## 12. Cheating is bad
Updating the score of one of the members
you can do this by using UPDATE
then SET
you use WHERE name = BOb to get the target of the to be changed

## 13. Score too low
This removes any record with scores lower or equal to 5
you delete it by using the WHERE to get the condition right

## 14. Average
This get the average of the scores  in to a column call average
You do this by SELECT and using the average function  with score as a parameter to get the average and put it in a variable call averageusing he AS key word
check code for more understanding

## 15. Number by score
Get th list number of records with the same score
You can archeive this by using COUNT(*) and GROUP BY
Use SELECT the column then use the COUNT(*) and put it value in a
variable call number
use GROUP BY to get the number of occurance
Use ORDER BY to make is descending order

## 16. Say my name
List all the name and score in the table
with the condition of name not being empy
also with it being ordered descending
SELECT is used

## 17. Go to UTF8
Use USE to get the database
Use ALTER to get the table
then CONVER TO CHARACTER SET ......

This is important for
Data intergrity
Compatibility with other database,systems etc
Future-proofing
Internationalization
Multilingual support


## 18. Temperatures #0
Getting the average temperature for cities
use SELECT TO the city column then use AVG function with value as parameter and us AS to put it value in avg_temp
Indicate from which table
use group to get the group
then order it in descending order

## 19. Temperatures #1
Same as 18 but this time you are getting the highest temperature between some month.
Use WHERE to get the condition
Group and order it
then USE LIMIT
Read more on LIMIT

## 20. Temperatures #2
displaying max temperature of each state
Select the sate and use MAX funtion to get the max temp and put it in max_temp
indicate from which table
GROUP BY State
ORDER By state
