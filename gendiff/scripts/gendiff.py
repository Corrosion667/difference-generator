#!/usr/bin/env python3
"""This program determines the differences between two files."""
import argparse

from gendiff.gendiff_engine import generate_diff


def main():
    """Execute the diff generator."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f',
        '--format',
        type=str,
        choices='stylished',
        default='stylished',
        help="""set format of output; default: stylished
         (json-like format with - for deleted elements and + for added)
         """,
    )
    args = parser.parse_args()
    print(
        generate_diff
        (
            args.first_file, args.second_file, args.format,
        ),
    )


if __name__ == '__main__':
    main()
