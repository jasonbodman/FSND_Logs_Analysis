import psycopg2

#COMMENT
DBNAME = "news"

#COMMENT
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
        
#Print all Results from queries above
if __name__ == '__main__':
    print question1
    get_results_1(query1)
    print question2
    get_results_2(query2)
    print question3
    get_results_3(query3)
    print('\nSuccess!\n')

