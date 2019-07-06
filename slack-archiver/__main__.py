import json

from datetime import datetime
from pathlib import Path

from app import SlackArchiver
from use_cases import ( read_config_file, write_config_file, get_parsed_arguments, write_to_json_archive )

def run():
    current_config = read_config_file()
    token = current_config.get('slack_token')

    args = get_parsed_arguments()
    print(args)
    if args.action == 'init':
        token = args.token
        init_config = { 'slack_token': token }
        write_config_File(init_config)
        return
   
    archiver = SlackArchiver(token)
   
    if args.action == 'archive':
        result = archiver.get_channel_history(args.channel)
        write_to_json_archive(result)

if __name__ == '__main__':
    run()
