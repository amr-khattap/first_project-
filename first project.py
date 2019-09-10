#first project 
import psycopg2

Database_name="Amr_news"

query_Q1= """select *,
            from log, articles
            where log.status='200 OK'
            and articles.slug = substr(log.path, 10)
            group by articles.title
            order by num desc
            limit 3;"""

Query_Q2 = """select*
            from articles, authors, log
            where log.status='200 OK'
            and authors.id = articles.author
            and articles.slug = substr(log.path, 10)
            group by authors.name
            order by num desc;
            """

Query_Q3 = """select time, percentagefailed
            from percentagecount
            where percentagefailed > 1;
            """


#  open and close the connection
def query_db(Amr_news):
    conect_db = psycopg2.connect(database="Amr_news")
    cursor = conect_db.cursor()
    cursor.execute(Amr_news)
    resu = cursor.fetchall()
    conect_db.close()
    return resu



def title(title):
    print ("\n\t\t" + title + "\n")


# Print  articles 
def articles(Amr_news):
    articles = query_db(query_Q1)
    print_title("Top 3 articles of all time")

    for title, num in articles:
        print(" \"{}\" -- {} views".format(title, num))


# Print authors
def authors():
    authors = query_db(Query_Q2)
    print_title("Top authors of all time")

    for name, num in authors:
        print(" {} -- {} views".format(name, num))


# Print error
def error():
    error = query_db(Query_Q3)
    print_title("Days with more than one percentage of bad requests")

    for day, percentagefailed in error:
        print("""{0:%B %d, %Y}
            -- {1:.2f} % ""rrors""".format(day, percentagefailed))


if __name__ == '':
    articles()
    authors()
    error()
