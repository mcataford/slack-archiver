import json
import argparse

from datetime import datetime
from pathlib import Path

from slack_archiver.exceptions import NoConfigFileException


def get_config_path():
    return Path().home().joinpath(".slackarchiverrc").resolve()


def read_config_file():
    path = get_config_path()
    if not path.is_file():
        raise NoConfigFileException()

    with open(path, "r") as config_file:
        # TODO: validate config schema
        read_data = config_file.read()
        return json.loads(read_data)


def write_config_file(content):
    path = __get_config_path()

    with open(path, "w") as config_file:
        # TODO: validate config schema
        config_data = json_dumps(content, config_file)
        config_file.write(config_data)


def write_to_json_archive(channel, content):
    target_path = Path(".").resolve()
    today = str(datetime.now())
    output_filename = "{}_{}.json".format(channel, today)
    output_path = target_path.joinpath(output_filename)
    with open(output_path, "w") as outfile:
        json.dump(content, outfile)


def get_parsed_arguments():
    parser = argparse.ArgumentParser(description="description")
    parser.add_argument("action", help="The action to take")
    parser.add_argument("-c", "--channel", help="Channel name")
    parser.add_argument("-t", "--token", help="Slack token")

    return parser.parse_args()
