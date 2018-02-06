import psycopg2

# Define Database name
DBNAME = "news"


# Create query function
def try_query(query):
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute(query)
        return c.fetchall()
        db.commit()
        db.close()
    except:
        print("There was an error completing the query")


def create_views(query):
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute(query)
        db.commit()
        db.close()
    except:
        print("There was an error creating the " + str(query) + " view")

# 1) What are the 3 most popular articles of all time?
question1 = "\nWhat are the 3 most popular articles of all time?\n"
query1 = """
    select full_details.title, count(log.path) as views
    from (full_details join log
    on log.path like '%' || full_details.slug || '%')
    group by full_details.title
    order by views desc
    limit 3;"""

# 2) Who are the three most popular authors of all time?
question2 = "\nWho are the three most popular authors of all time?\n"
query2 = """
    select full_details.name, count(log.path) as views
    from (full_details join log
    on log.path like '%' || full_details.slug || '%')
    group by full_details.name
    order by views desc
    limit 3;"""

# 3) On what days did more than 1% of requests lead to errors?
question3 = "\nOn what days did more than 1% of requests lead to errors?\n"
query3 = """
    select date, (round((num * 1.0 / views) * 100.0, 2)) as percent
    from errorlog
    where (num * 1.0 / views) > .01;
    """

# Queries to create views
full_details = """
    create or replace view full_details as
    select articles.title, articles.slug, authors.name, authors.id
    from articles join authors
    on articles.author = authors.id;
    """

errors = """
    create or replace view errors as
    select date(time), count(status) as num
    from log
    where status like '%404%'
    group by date(time);
    """

daily_views = """
    create or replace view daily_views as
    select date(time), count(status) as views
    from log
    group by date(time);
    """

errorlog = """
    create or replace view errorlog as
    select errors.date, errors.num, daily_views.views
    from errors join daily_views
    on errors.date = daily_views.date;
    """


# Execute Queries for each question
def get_results_1(query):
    results = try_query(query)
    for e in results:
        print ('\t' + str(e[0]) + ' --> ' + str(e[1]) + ' views')


def get_results_2(query):
    results = try_query(query)
    for e in results:
        print ('\t' + str(e[0]) + ' --> ' + str(e[1]) + ' views')


def get_results_3(query):
    results = try_query(query)
    for e in results:
        print ('\t' + str(e[0]) + ' --> ' + str(e[1]) + '%')


# Print all Results from queries above
if __name__ == '__main__':
    create_views(full_details)
    create_views(errorlog)
    create_views(daily_views)
    print question1
    get_results_1(query1)
    print question2
    get_results_2(query2)
    print question3
    get_results_3(query3)
    print('\nSuccess!\n')
