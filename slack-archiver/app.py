import slack

from datetime import datetime

def load_config():
    pass

class SlackArchiver():
    def __init__(self, token: str):
        self.client = self.__get_api_client(token)
        self.channels = self.__get_channel_map()

    def __get_api_client(self, token: str):
        return slack.WebClient(token=token)

    def __get_channel_map(self):
        response = self.client.channels_list()
        return { channel.get('name'):channel.get('id') for channel in response.get('channels') }

    def get_channel_history(self, channel_name: str, start=None, end=None):
        channel_id = self.channels.get(channel_name)
        raw_history = self.client.channels_history(channel=channel_id, count=1000)

        return [ (message.get('text'), str(datetime.fromtimestamp(float(message.get('ts'))))) for message in raw_history.get('messages') ]

