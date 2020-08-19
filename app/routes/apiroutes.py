from flask import Flask, url_for, redirect
import logging
from __main__ import app
from framework import messaging
import pprint
pp = pprint.PrettyPrinter(indent=4)

logging.basicConfig(level=logging.DEBUG)

@app.route("/")
def index():
    """
    Act as a generic landing page that redirects to /index

    :return: redirect to index
    """
    app.logger.debug('Redirecting from /')
    return redirect(url_for('hello_world'))

@app.route("/health", methods=['GET'])
def health():
    """
    Perform a health check and return true or false and an http code as appropriate.

    A real health check should ensure required backend systems are created etc.

    :return: JSONified message in JSend format.
    """
    app.logger.debug("Performing health check")
    return messaging.create_success_fail_payload(
        {"healthy": True},
        True, status_code=200)


@app.route('/index', methods=['GET'])
def hello_world():
    """
    Return a friendly "Hello, World!" message.

    :return: string
    """
    app.logger.debug('Hello, World!')
    return 'Hello, World!'
