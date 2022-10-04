#!/usr/bin/env python3

from parse_command_line import parse_args

if __name__ == '__main__':

    program_config = parse_args()

    try:
        program_config.function(program_config)
    except AttributeError as err:
        raise SystemExit("No action defined")
