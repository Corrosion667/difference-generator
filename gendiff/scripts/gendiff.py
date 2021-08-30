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
        choices=['stylish', 'plain', 'json'],
        default='stylish',
        help="""set format of output; default: stylish
         (json-like format with - for deleted elements and + for added);
         also usable: plain
         (thesis-like format with satements about adding, updating and removal);
         also usable: json
         (classic json: list of lists with [key, value_file1, value_file2])
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
