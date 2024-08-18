"""
Define the argument parser
"""

import argparse


class ArgNamespace(argparse.Namespace):
    """Typing"""
    subdomain: str
    port: int


def get_args() -> ArgNamespace:
    """Define an argument parser and return it."""
    parser = argparse.ArgumentParser(description='The nDeploy manager')
    parser.add_argument(
        '-d',
        type=str,
        dest='subdomain',
        required=True,
        help='Define the subdomain to register',
    )
    parser.add_argument(
        '-p',
        type=str,
        dest='port',
        required=True,
        help='Define the local port to expose',
    )
    args = parser.parse_args()
    return args
