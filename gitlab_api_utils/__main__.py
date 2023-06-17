from gitlab_api_utils.parse_command_line import _parse_args

def main():
    program_config = _parse_args()

    try:
        program_config.function(program_config)
    except AttributeError as err:
        raise SystemExit("No action defined")


if __name__ == '__main__':
    main()
