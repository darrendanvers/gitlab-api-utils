import argparse

from .pipeline_delete import pipeline_delete_action
from .artifact_delete import artifact_delete_action


def _parse_args():
    """
    Parses the command line arguments.

    :return: The parsed command-line arguments.
    """
    access_token_instructions = "https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html"
    epilog_text = f"Instructions for generating an access token can be found here: {access_token_instructions}"

    parser = argparse.ArgumentParser(description='GitLab API helper', epilog=epilog_text)

    # Required arguments across all actions.
    parser.add_argument('--token', '-t', nargs='?', dest='token', help='your GitLab access token or - to read from standard input', required=True)
    parser.add_argument('--project', '-p', nargs='?', dest='project', help='your GitLab project', required=True)

    # Add the action sub-parser.
    action_subparser = parser.add_subparsers(title="action", help="action to perform", dest="action", required=True)

    # Add the actions the application supports.
    _add_pipeline_delete(action_subparser)
    _add_artifacts_delete(action_subparser)

    parsed_args = parser.parse_args()
    _reconcile_token(parsed_args)

    return parsed_args


def _add_pipeline_delete(action_subparser):
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

def _add_artifacts_delete(action_subparser):
    """
    Adds the command line configuration for the job artifact delete action.

    :param action_subparser: The subparser for the action command line argument.
    :return: void
    """
    # Add an action to delete job artifacts.
    action_artifact_delete = action_subparser.add_parser("artifact-delete",
                                                         help="deletes artifacts tied to a particular job")
    action_artifact_delete.add_argument("--job", "-j", dest="job", required=True,
                                        help="the ID of the job to delete artifacts from")
    action_artifact_delete.set_defaults(function=artifact_delete_action)

def _reconcile_token(args):
    """
    If the user passes a '-' as the value for the token parameter, the application will try to read
    the value from standard input. This will allow the user to store the token in a file and cat
    that file into this program.

    :param args: The parsed command line arguments. If the token contains a '-', the function will read
    a value from standard input and replace the token property with the value read in.
    :return: void
    """
    if args.token and args.token == '-':
        args.token = input()