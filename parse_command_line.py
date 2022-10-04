import argparse

from pipeline_delete import pipeline_delete_action


def parse_args():
    """
    Parses the command line arguments.

    :return: The parsed command-line arguments.
    """
    access_token_instructions = "https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html"
    epilog_text = f"Instructions for generating an access token can be found here: {access_token_instructions}"

    parser = argparse.ArgumentParser(description='GitLab API helper', epilog=epilog_text)

    # Required arguments across all actions.
    parser.add_argument('--token', '-t', nargs='?', dest='token', help='your GitLab access token', required=True)
    parser.add_argument('--project', '-p', nargs='?', dest='project', help='your GitLab project', required=True)

    # Add the action sub-parser.
    action_subparser = parser.add_subparsers(title="action", help="action to perform", dest="action", required=True)

    # Add the actions the application supports.
    add_pipeline_delete(action_subparser)

    return parser.parse_args()


def add_pipeline_delete(action_subparser):
    """
    Adds the command line configuration for the pipeline-delete action.

    :param action_subparser: The subparser for the action command line argument.
    :return: void
    """
    # An action to delete old pipelines.
    action_pipeline_delete = action_subparser.add_parser("pipeline-delete",
                                                         help="deletes build pipelines in reverse chronological order")
    action_pipeline_delete.add_argument("--count", "-c", nargs="?", dest="count",
                                        help="the number of pipelines to delete", type=int, default=50)
    # Calls the pipeline_delete_action function to process this action.
    action_pipeline_delete.set_defaults(function=pipeline_delete_action)
