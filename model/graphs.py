import plotly.tools as config
import plotly.plotly as py
from plotly.graph_objs import *

username = 'yurireis'
credential = 'JS2YQg2NQ7WP1n2OZc8i'


class Graphs(object):
    def __init__(self, user, api_key, readable=False, privacy='private'):
        """

        :param readable:
        :param privacy:
        """
        config.set_credentials_file(username=user, api_key=api_key)
        config.set_config_file(world_readable=readable, sharing=privacy)

    def get

Graphs(username, credential)
