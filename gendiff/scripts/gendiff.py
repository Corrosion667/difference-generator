#!/usr/bin/env python3
"""This script shows basic info about the progam: its usage and syntax."""
import argparse


def main():
    """Show info for gendiff program."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    main()
