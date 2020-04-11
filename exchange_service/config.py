
class Config():
    HOST = '0.0.0.0'
    PORT = 8080
    LOG_FILE = None
    LOG_LEVEL = 'INFO'
    RATE_API_URL = 'https://www.cbr-xml-daily.ru/daily_json.js'
    RATE_TIMEOUT = 60 * 60

class TestingConfig(Config):
    LOG_LEVEL = 'DEBUG'
    RATE_TIMEOUT = 2