import json
import argparse

from datetime import datetime
from pathlib import Path

from slack_archiver.exceptions import NoConfigFileException


def read_config_file():
    path = Path().home().joinpath(".slackarchiverrc").resolve()

    if not path.is_file():
        raise NoConfigFileException()

    with open(path, "r") as config_file:
        return json.load(config_file)


def write_config_file(content):
    path = Path().home().joinpath(".slackarchiverrc").resolve()

    with open(path, "w") as config_file:
        json_dump(content, config_file)


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
