
import psycopg2

DBNAME = "news"
query_1 = ("select * from article_views limit 3")
query_2 = ("select name, sum(article_views.views) as VIEWS from article_authors, article_views where article_authors.title = article_views.title group by name order by views desc limit 3")
query_3= ("select requests.date,round(100.0*errorresponsecount/requestcount,2) as percent from requests left join ErrorResponse on (requests.date = ErrorResponse.date) where 0.01 * requests.requestCount <= ErrorResponse.ErrorResponseCount")

def connect(query):
  """Connect to the database news and close the connection after getting the necessary data"""
  db = psycopg2.connect(database = DBNAME)
  c = db.cursor()
  c.execute(query)
  posts = c.fetchall()
  db.close()
  return posts


def three_most_popular_articles(query):
  result_1 = connect(query)
  print("\nThis is the list of the three most popular articles: ")
  for n in result_1:
    print(str(n[0]) + ' --- ' +  str(n[1]) + ' views' )


def three_most_popular_authors(query):
  print("\nThis is the list of the three authors with the most articles views:")
  result_2 = connect(query)
  for n in result_2:
    print(str(n[0]) + ' --- ' +  str(n[1]) + ' views' )


def errorlog(query):
  print("\nThis is the list of the days where more than 1 percent of logs received error response: ")
  result_3 = connect(query)
  for n in result_3:
    print(str(n[0]) + '  --  ' + str(n[1]) + ' % ' + 'errors')

if __name__ == '__main__':
  #Printing results
  three_most_popular_articles(query_1)
  three_most_popular_authors(query_2)
  errorlog(query_3)
