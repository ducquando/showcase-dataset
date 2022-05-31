import csv
import sqlite3

# Create new file if not exist
con = sqlite3.connect('showcase.sqlite')        
cur = con.cursor()

# Create table USER
cur.execute('''CREATE TABLE IF NOT EXISTS USER
               (ID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT NOT NULL,
               Email TEXT NOT NULL, Password TEXT NOT NULL)''')
# Create table ARTICLE
cur.execute('''CREATE TABLE IF NOT EXISTS ARTICLE
               (ID INTEGER PRIMARY KEY AUTOINCREMENT, Title TEXT NOT NULL,
               Author TEXT NOT NULL, FieldID INTEGER NOT NULL,
               ImageURL TEXT DEFAULT "https://picsum.photos/400/480",
               Abstract TEXT, Introduction TEXT, Methodology TEXT,
               Findings TEXT, Discussion TEXT, Conclusion TEXT)''') 
# Create table FIELD
cur.execute('''CREATE TABLE IF NOT EXISTS FIELD
               (ID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT NOT NULL)''')
# Create table ARTICLE_POINT
cur.execute('''CREATE TABLE IF NOT EXISTS ARTICLE_POINT
               (ArticleID INTEGER NOT NULL, UserID INTEGER NOT NULL,
               Point INTEGER DEFAULT 0,
               PRIMARY KEY(ArticleID, UserID),
               FOREIGN KEY(ArticleID) REFERENCES ARTICLE(ID),
               FOREIGN KEY(UserID) REFERENCES USER(ID))''')
# Create table FIELD_POINT
cur.execute('''CREATE TABLE IF NOT EXISTS FIELD_POINT
               (FieldID INTEGER NOT NULL, UserID INTEGER NOT NULL,
               Point REAL DEFAULT 1,
               PRIMARY KEY(FieldID, UserID),
               FOREIGN KEY(FieldID) REFERENCES FIELD(ID),
               FOREIGN KEY(UserID) REFERENCES USER(ID))''')

# Insert data into FIELD table
field_name = ["Computer Science", "Integrated Science", "Arts & Humanities",
              "Social Sciences"]
field_id = [0,1,2,3]
for (i,j) in zip(field_id, field_name):
    cur.execute('''INSERT INTO FIELD VALUES ({0}, "{1}")'''.format(i,j))

# Insert data into ARTICLE table
with open('ShowcaseArticle.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Insert a row of data
        cur.execute('''INSERT INTO ARTICLE (Title, Author, FieldID, Abstract,
                    Introduction, Methodology, Findings, Discussion,
                    Conclusion) VALUES ("{0}","{1}","{2}","{3}","{4}",
                                        "{5}","{6}","{7}","{8}")'''
                    .format(row['Title'], row['Author'], row['FieldID'],
                            row['Abstract'], row['Introduction'],
                            row['Methodology'], row['Findings'],
                            row['Discussion'], row['Conclusion']))

# Insert data into USER table
with open('ShowcaseUser.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Insert a row of data
        cur.execute('''INSERT INTO USER VALUES ("{0}","{1}","{2}","{3}")'''
                    .format(row['ID'], row['Name'], row['Email'], row['Password']))

# Insert data into ARTICLE_POINT table
with open('ShowcaseUserArticlePoint.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Insert a row of data
        cur.execute('''INSERT INTO ARTICLE_POINT VALUES ("{0}","{1}","{2}")'''
                    .format(row['Article'], row['User'], row['Point']))

# Insert data into FIELD_POINT table
with open('ShowcaseUserFieldPoint.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Insert a row of data
        cur.execute('''INSERT INTO FIELD_POINT VALUES ("{0}","{1}","{2}")'''
                    .format(row['Field'], row['User'], row['Point']))

# Save the changes
con.commit()

# Close the connection
con.close()