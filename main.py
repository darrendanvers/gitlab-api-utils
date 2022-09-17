import argparse
import sys

from pipeline_delete import pipeline_delete_action


def parse_args():
    """
    Parses the command line arguments.

    :return: The parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(description='GitLab API helper')
    parser.add_argument('--token', '-t', nargs='?', dest='token', help='Your GitLab access token', required=True)
    parser.add_argument('--project', '-p', nargs='?', dest='project', help='Your GitLab project', required=True)
    parser.add_argument('--action', '-a', nargs='?', dest='action', help='Your GitLab access token', required=True)
    parser.add_argument('--count', '-c', nargs='?', dest='count', help='Action dependent count of things to do',
                        type=int, default=50)

    return parser.parse_args()


def action_factory(action):
    """
    Factory method to return the function that will handle the specific action requested by the user.

    :param action: The action requested by the user.
    :return: The function that will handle that action. If there is no match, will return None.
    """
    if action == "pipeline-delete":
        return pipeline_delete_action
    else:
        return None


if __name__ == '__main__':

    program_config = parse_args()

    func = action_factory(program_config.action)

    if func is None:
        print(f"Unknown action: '{program_config.action}'", file=sys.stderr)
        sys.exit(-1)
    else:
        func(config=program_config)
