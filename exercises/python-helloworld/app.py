from flask import Flask
from flask import json
from logging.config import dictConfig
import logging


dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


app = Flask(__name__)

logging.basicConfig(filename='app.log',
                        level=logging.DEBUG,
                        format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')



@app.route('/status')
def healthcheck():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )

    ## log line
    app.logger.info('Status request successfull')
    app.logger.warning('Status warning log')
    app.logger.error('Status error log')
    return response

@app.route('/metrics')
def metrics():
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )

    ## log line
    app.logger.info('Metrics request successfull')
    app.logger.warning('Metrics warning log')
    app.logger.error('Metrics error log')
    return response

@app.route("/")
def hello():
    ## log line
    app.logger.info('Main request successfull')

    return "Hello World!"

if __name__ == "__main__":

    ## stream logs to app.log file
    #logging.basicConfig(filename='app.log',level=logging.DEBUG)

    app.run(host='0.0.0.0')