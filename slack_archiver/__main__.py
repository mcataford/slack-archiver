import json

from datetime import datetime
from pathlib import Path

from slack_archiver.app import SlackArchiver
from slack_archiver.use_cases import (
    read_config_file,
    write_config_file,
    get_parsed_arguments,
    write_to_json_archive,
)


def run():
    current_config = read_config_file()
    token = current_config.get("slack_token")

    args = get_parsed_arguments()
    if args.action == "init":
        token = args.token
        init_config = {"slack_token": token}
        write_config_File(init_config)
        return

    archiver = SlackArchiver(token)

    if args.action == "archive":
        result = archiver.get_channel_history(args.channel)
        print("Archiving {count} messages.".format(count=len(result)))
        write_to_json_archive(args.channel, result)


if __name__ == "__main__":
    run()
