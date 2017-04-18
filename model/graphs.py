import os

import plotly.tools as config
import plotly.plotly as py
import plotly.graph_objs as go

from config.settings import OVERALL_TESTS_IMPLEMENTATION_LABEL, IMPLEMENTED_LABEL, NOT_IMPLEMENTED_LABEL, \
    CORE_TESTS_IMPLEMENTATION_LABEL
from model.documentation import Documentation


class Graphs(object):
    def __init__(self, document, readable=True, privacy='public'):
        """

        :param document:
        :type document: Documentation
        :param readable:
        :param privacy:
        """
        # self.document = document
        self.document = document
        user = os.getenv('PLOTLY_USER', None)
        api_key = os.getenv('PLOTLY_KEY', None)

        if not user or not api_key:
            raise Exception('You must set Plotly Key user/api_key in environment variables')

        config.set_credentials_file(username=user, api_key=api_key)
        config.set_config_file(world_readable=readable, sharing=privacy)
        self.ids = self.get_stream_ids()

    def get_stream_ids(self):
        """

        :return: list of ids
        :rtype: str[]
        """
        return config.get_credentials_file()['stream_ids']

    def general_feature_coverage(self):
        """

        :return:
        """
        self.stream(0)
        fig = {
            'data': [{
                'labels': [IMPLEMENTED_LABEL, NOT_IMPLEMENTED_LABEL],
                'values': [
                    self.document.get_number_of_features(),
                    self.document.get_number_of_implemented_features()
                ],
                'type': 'pie'}
            ],
            'layout': {'title': OVERALL_TESTS_IMPLEMENTATION_LABEL}
        }

        return py.plot(fig, filename='python-streaming')

    def core_feature_coverage(self):
        """

        :return:
        """
        self.stream(1)
        fig = {
            'data': [{
                'labels': [IMPLEMENTED_LABEL, NOT_IMPLEMENTED_LABEL],
                'values': [
                    self.document.get_number_of_core_features(),
                    self.document.get_number_of_implemented_core_features(),
                ],
                'type': 'pie'}
            ],
            'layout': {'title': CORE_TESTS_IMPLEMENTATION_LABEL}
        }

        return py.plot(fig, filename='python-streaming')

    def stream(self, pos):
        """

        :param pos:
        :return:
        """
        return go.Stream(
            token=self.ids[pos],
        )
