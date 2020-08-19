from flask import Flask, jsonify
import os
import logging
import pprint
from str2bool import str2bool

pp = pprint.PrettyPrinter(indent=4)

app = Flask(__name__)
from routes import apiroutes

logging.basicConfig(level=logging.DEBUG)


def main():
    """
    Main method, creates app and initializes database.

    :return:
    """
    # these routes have been migrated to use decorators in lieu of the older add_url_rule syntax
    #app.add_url_rule('/api/kpivlive/connectiontest', 'connectiontest', apiroutes.connectiontest())
    #app.add_url_rule('/api/kpivlive/checkformodel', 'checkformodel', apiroutes.checkformodel, methods=['POST'])
    #app.add_url_rule('/api/kpivlive/publishkpivdata', 'publishkpivdata', apiroutes.publishkpivdata, methods=['POST'])
    #configure_app()

    #app.logger.debug('current config:')
    #app.logger.debug(get_output_config())
    app.logger.debug('Starting app')
    debug = os.environ.get('DEBUG', True)
    debug = debug if isinstance(debug, bool) else str2bool(debug)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=debug)
    app.logger.debug('Starting app')


main()