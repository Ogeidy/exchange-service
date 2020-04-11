import json
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

from exchange_service import config
from exchange_service.exchange import exchange


class ExchangeHandler(BaseHTTPRequestHandler):

    def _process_exchenge(self, params):
        response = {}
        if 'amount' not in params or 'from' not in params or 'to' not in params:
            response['status'] = 'fail'
            response['msg'] = 'Wrong parameters'
            self.send_response(405)
        else:
            exchanged = exchange(amount=float(params['amount']),
                                    cur_from=params['from'],
                                    cur_to=params['to'])
            response['currency'] = params['to']
            response['amount'] = exchanged
            self.send_response(200)

        self.send_header('content-type', 'application/json')
        self.end_headers
        self.wfile.write(bytes(json.dumps(response), encoding='utf-8'))

    def do_GET(self):
        params = parse_qs(urlparse(self.path).query)
        params = {k:v[0] for k, v in params.items()}
        self._process_exchenge(params)
    
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        try:
            json_data = json.loads(post_data)
        except:
            self._process_exchenge({})
            return
        self._process_exchenge(json_data)

    def log_message(self, format, *args):
        logging.info("%s - - %s" %
                    (self.address_string(),
                    format%args))

    def log_request(self, code='-', size='-'):
        self.log_message('"%s" %s %s',
                         self.requestline, str(code), str(size))


def run(server_clsss=HTTPServer, handler_class=ExchangeHandler, conf=config.Config):
    logging.basicConfig(format='%(levelname)s [%(asctime)s] %(message)s',
                        filename=conf.LOG_FILE,
                        datefmt='%m/%d/%Y %H:%M:%S',
                        level=conf.LOG_LEVEL)

    serv = server_clsss((conf.HOST, conf.PORT), handler_class)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass
    serv.server_close()
    logging.info('Stopping the server...')
