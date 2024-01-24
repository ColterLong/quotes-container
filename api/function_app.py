import json, logging, os, mysql.connector
import azure.functions as func


app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)
hostString = os.environ['HOST_STRING']
databaseString = os.environ['DATABASE_STRING']
userString = os.environ['USER_STRING']
passwordString = os.environ['PASSWORD_STRING']

quotesArr = []

@app.route(route="getQuotes")
def getQuotes(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    global quotesArr
    try:
        connection = mysql.connector.connect(host=hostString,database=databaseString,user=userString,password=passwordString)
        cursor = connection.cursor()
        cursor.execute('SELECT name,quote FROM quotes;')
        quotes = cursor.fetchall()
        logging.info(quotes)
        quotesArr = []
        for quote in quotes:
          logging.info(quote)
          quotesArr.append({
            "name": quote[0],
            "text": quote[1]
          })
        logging.info(quotesArr)
        logging.info("executed select statement")
        return func.HttpResponse(json.dumps(quotesArr))
    except mysql.connector.Error as error:
        logging.info("select statement error: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            logging.info("connection closed")