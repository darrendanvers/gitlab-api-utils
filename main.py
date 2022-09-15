import getopt
import sys


class Config:
    """
    The application's configuration.
    """
    token = None
    """
    The access token to use to contact GitLab.
    """
    project = None
    """
    The ID of the project being accessed.
    """
    action = None
    """
    The action to take.
    """
    count = 50
    """
    The number of pipelines to delete.
    """

    def in_error(self):
        """
        Returns whether the application's configuration is invalid.

        :return: True if the application's configuration is invalid and false otherwise.
        """
        return self.token is None or self.project is None or self.action is None


def parse_args(args):
    """
    Parses the command line arguments.

    :param args: The command line arguments. It should not include the program's name.
    :return: A Config object containing the parsed arguments.
    """
    config = Config()

    try:
        opts, args = getopt.getopt(args, "t:p:c:a:", ["token=", "project=", "count=", "action="])
    except getopt.GetoptError:
        return config

    for opt, arg in opts:
        if opt in ("-t", "--token"):
            config.token = arg
        if opt in ("-c", "--count"):
            config.count = arg
        if opt in ("-p", "--project"):
            config.project = arg
        if opt in ("-a", "--action"):
            config.action = arg

    return config


def print_usage(program_name):
    """
    Prints the application's usage statement and quits the application. It will retun an error code to the
    operating system.

    :param program_name: The name of the application.
    :return: void
    """
    print(f'{program_name} --action <action> --token <token> --project <project> [--count <count>]', file=sys.stderr)
    print("Action must equal 'pipeline-delete'", file=sys.stderr)
    print("Token is your GitLab access token", file=sys.stderr)
    print("Project is you GitLab project ID", file=sys.stderr)
    print("Count is action dependent. For pipeline-delete, it is the number of pipelines to delete.", file=sys.stderr)
    sys.exit(-1)


if __name__ == '__main__':

    program_config = parse_args(sys.argv[1:])

    if program_config.in_error():
        print_usage(sys.argv[0])

    print(program_config.token)
    print(program_config.project)
    print(program_config.count)
