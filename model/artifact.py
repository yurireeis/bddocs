import re
from config.settings import FEATURE
from model.feature import Feature


class Artifact(object):
    """
    Docstring for Artifact class
    """

    feature = None

    line_offset = []

    def __init__(self, _dir, file):
        """

        :param _dir: a file directory to know where you can find the Artifact
        :type _dir: str
        :param file: a feature file name to open and read
        :type file_directory: str
        """
        self.file_path = './%s/%s' % (_dir, file)
        self.line_offset = self.__get_line_offset()
        self.__retrieve_feature()

        if not self.feature:
            Exception('You must have at least one feature in file %s' % file)

    def __get_line_offset(self):
        """

        :return: list with tuples
        :rtype: list
        """
        line_offset = []
        with open(self.file_path, 'r') as file:
            for i, line in enumerate(file):
                line_offset.append((i, line))

        return line_offset

    def __is_feature(self, line):
        """

        :return: bool
        """
        regex = r"({})".format(FEATURE)
        return re.match(regex, line)

    def __retrieve_feature(self):
        """

        :return:
        """
        for pos, text in self.line_offset:
            if self.__is_feature(text):
                self.feature = Feature(text, pos, self.line_offset)
                break
