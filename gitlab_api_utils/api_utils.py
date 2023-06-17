def get_common_headers(config):
    """
    Returns the headers that are common to all API requests.

    :param config: The application configuration.
    :return: The headers that are common to all API requests.
    """
    return {"PRIVATE-TOKEN": config.token}


def get_base_uri(config):
    """
    Returns the base URI for accessing GitLab.

    :param config: The application configuration.
    :return: The base URI for accessing GitLab.
    """
    # Config is currently unused. It's there in anticipation of future functionality.
    return "https://gitlab.com/api/v4"
