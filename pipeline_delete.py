import requests

from api_utils import get_common_headers

PIPELINE_FETCH_URI = "https://gitlab.com/api/v4/projects/{project}/pipelines?sort=asc"
PIPELINE_DELETE_URI = "https://gitlab.com/api/v4/projects/{project}/pipelines/{pipeline}"


def delete_single_pipeline(config, pipeline_id):
    """
    Deletes a single pipeline.

    :param config: The application configuration.
    :param pipeline_id: The ID of the pipeline to delete.
    :return: void
    """
    print(f"Deleting pipeline {pipeline_id}...", end="")
    delete_url = PIPELINE_DELETE_URI.format(project=config.project, pipeline=pipeline_id)
    headers = get_common_headers(config)
    response = requests.delete(delete_url, headers=headers)
    response.raise_for_status()
    print("OK")


def delete_pipelines(config, pipelines):
    """
    Deletes an array of pipelines.

    :param config: The application configuration.
    :param pipelines: The array of pipelines to delete
    :return: The number of pipelines deleted
    """
    for pipeline in pipelines:
        delete_single_pipeline(config, pipeline["id"])
    return len(pipelines)


def pipeline_delete_action(config):
    """
    Handles deleting build pipelines in a GitLab project. It will delete up to the number of pipelines passed in
    as the count parameter of the application configuration.

    :param config: The application configuration.
    :return: void
    """
    count_deleted = 0

    fetch_url = PIPELINE_FETCH_URI.format(project=config.project)
    headers = get_common_headers(config)

    try:
        while count_deleted < config.count:

            # Get the next batch of pipelines to delete.
            response = requests.get(fetch_url, headers=headers)
            response.raise_for_status()

            all_pipelines = response.json()

            # Figure out how many pipelines to delete. If there are enough pipelines
            # in the response to make the total count deleted exceed the requested amount,
            # then just delete enough to get to the requested amount. Otherwise, delete
            # all pipelines in the response.
            total_to_delete = len(all_pipelines)
            if total_to_delete + count_deleted > config.count:
                total_to_delete = config.count - count_deleted

            # Delete the pipelines and update the running total.
            count_deleted += delete_pipelines(config, all_pipelines[:total_to_delete])
            print(f"Deleted {count_deleted} pipelines")
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
