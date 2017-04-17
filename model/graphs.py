import plotly.tools as config
import plotly.plotly as py
import plotly.graph_objs as go

username = 'yurireeis'
credential = 'JS2YQg2NQ7WP1n2OZc8i'


class Graphs(object):
    def __init__(self, user, api_key, readable=True, privacy='public'):
        """

        :param document:
        :type document: Documentation
        :param readable:
        :param privacy:
        """
        # self.document = document
        config.set_credentials_file(username=user, api_key=api_key)
        config.set_config_file(world_readable=readable, sharing=privacy)
        self.ids = self.get_stream_ids()

    def get_stream_ids(self):
        """

        :return: list of ids
        :rtype: str[]
        """
        return config.get_credentials_file()['stream_ids']

    def general_coverage(self, title=None):
        """

        :return:
        """
        trace0 = go.Scatter(
            x=[1, 2, 3, 4],
            y=[10, 15, 13, 17]
        )
        trace1 = go.Scatter(
            x=[1, 2, 3, 4],
            y=[16, 5, 11, 9]
        )
        data = go.Data([trace0, trace1])

        if title:
            layout = go.Layout(title=title)
            fig = go.Figure(data=data, layout=layout)
            return py.plot(fig, filename='python-streaming')

        return py.plot(data, filename='python-streaming')

    def stream(self, pos):
        """

        :param pos:
        :param max_points:
        :return:
        """
        return go.Stream(
            token=self.ids[pos],
        )


test = Graphs(username, credential)
test.stream(0)
test.general_coverage('Novo título')
pass
