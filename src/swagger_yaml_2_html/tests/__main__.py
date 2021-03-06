import os
import argparse

from swagger_yaml_2_html import __version__


def get_parser():
    """
    Creates a new argument parser.
    """
    parser = argparse.ArgumentParser('swagger-yaml-2-html')
    version = '%(prog)s ' + __version__
    parser.add_argument('--version', '-v', action='version', version=version)
    return parser


def main(args=None):
    """
    Called with ``python -m swagger_yaml_2_html.tests``: run main test suite.
    """

    parser = get_parser()
    args = parser.parse_args(args)

    # Check if pytest is available
    try:
        import pytest
    except ImportError:
        raise SystemExit(
            'You need py.test to run the test suite.\n'
            'You can install it using your distribution package manager or\n'
            '    $ python -m pip install pytest --user'
        )

    # Get data from test_module
    import swagger_yaml_2_html.tests as test_module
    test_path = os.path.abspath(os.path.dirname(test_module.__file__))
    pytest.main([test_path, '-m', 'not documentation'])


if __name__ == '__main__':
    main()