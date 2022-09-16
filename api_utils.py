import sys


class HttpError(Exception):
    """
    Error to throw when receiving a response from an API call.
    """
    body = ''
    msg = ''

    def __init__(self, msg, body=''):
        self.msg = msg
        self.body = body
        Exception.__init__(self, msg)

    def __str__(self):
        return self.msg


def get_common_headers(config):
    """
    Returns the headers that are common to all API requests.

    :param config: The application configuration.
    :return: The headers that are common to all API requests.
    """
    return {"PRIVATE-TOKEN": config.token}


def is_success(response):
    """
    Determines if an HTTP response is in the success range.

    :param response: The HTTP response to check.
    :return: True if the response is in the success range and false otherwise.
    """
    return 200 <= response.status_code <= 299


def create_http_error(url, response):
    """
    Returns an HttpError constructed from the URL passed in and the HTTP response.

    :param url: The URL that triggered the fatal error.
    :param response: The HTTP response.
    :return: An HttpError.
    """
    msg = f"Error ${response.status_code} calling uri {url}:"
    return HttpError(msg, response.text)


def fatal_http_error(http_error):
    """
    Common fatal HTTP error handling routine. It prints a message to standard error and exits with an error code.

    :param http_error: The HttpError to log.
    :return: void
    """
    print(f"{http_error}:", file=sys.stderr)
    print(http_error.body, file=sys.stderr)
    sys.exit(-1)
