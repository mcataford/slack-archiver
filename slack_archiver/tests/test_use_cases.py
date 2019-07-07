from pytest_mock import mocker
from pytest import raises

import json

from slack_archiver.use_cases import read_config_file
from slack_archiver.exceptions import NoConfigFileException


def test_read_config_file_raises_no_config_exception_if_config_missing(mocker):
    mocker.patch("pathlib.Path.is_file").return_value = False
    with raises(NoConfigFileException) as excinfo:
        config = read_config_file()


def test_read_config_file_returns_json_decoded_file_if_config_exists(mocker):
    mock_config_str = '{ "mock": "json" }'
    mocker.patch("pathlib.Path.is_file").return_value = True
    mocker.patch("builtins.open", mocker.mock_open(read_data=mock_config_str))
    mock_config = read_config_file()
    assert mock_config == json.loads(mock_config_str)
