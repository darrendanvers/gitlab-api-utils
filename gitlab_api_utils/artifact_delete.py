import requests

from .api_utils import get_common_headers
from .api_utils import get_base_uri

ARTIFACTS_DELETE_URI = "{base}/projects/{project}/jobs/{job}/artifacts"

def artifact_delete_action(config):
    """
    Handles deleting build artifacts for a single job in a GitLab project. The project and job ID are pulled
    from the supplied configuration.

    :param config: The application configuration.
    :return: void
    """
    print(f"Deleting artifacts for job {config.job}...", end="")
    delete_url = ARTIFACTS_DELETE_URI.format(base=get_base_uri(config), project=config.project, job=config.job)
    headers = get_common_headers(config)
    response = requests.delete(delete_url, headers=headers)
    response.raise_for_status()
    print("OK")