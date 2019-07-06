import argparse
import json

from datetime import datetime
from pathlib import Path

from app import SlackArchiver
 
if __name__ == '__main__':
    token = None
    config_path = Path().home().joinpath('.slackarchiverrc').resolve()
    if config_path.is_file():
        with open(config_path, 'r') as infile:
            config = json.load(infile)
            token = config.get('slack_token')

    parser = argparse.ArgumentParser(description='description')
    parser.add_argument('action', help='The action to take', )
    parser.add_argument('-c', '--channel', help='Channel name')
    parser.add_argument('-t', '--token', help='Slack token')

    args = parser.parse_args()

    if args.action == 'init':
        token = args.token
        init_config = { 'slack_token': token }
        home_path = Path().home().resolve()
        config_file = home_path.joinpath('.slackarchiverrc')
        with open(config_file, 'w') as outfile:
            json.dump(init_config, outfile)
    archiver = SlackArchiver(token)
   
    if args.action == 'archive':
        result = archiver.get_channel_history('project-leads')
        target_path = Path('.').resolve()
        today = str(datetime.now())
        output_filename = '{}_{}.json'.format(args.channel, today)
        output_path = target_path.joinpath(output_filename)
        with open(output_path, 'w') as outfile:
            json.dump(result, outfile)
