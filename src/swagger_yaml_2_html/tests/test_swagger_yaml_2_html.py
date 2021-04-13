import pytest
import swagger_yaml_2_html


def test_project_defines_author_and_version():
    assert hasattr(swagger_yaml_2_html, '__author__')
    assert hasattr(swagger_yaml_2_html, '__version__')
