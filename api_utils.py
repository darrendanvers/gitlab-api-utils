def get_common_headers(config):
    """
    Returns the headers that are common to all API requests.

    :param config: The application configuration.
    :return: The headers that are common to all API requests.
    """
    return {"PRIVATE-TOKEN": config.token}
