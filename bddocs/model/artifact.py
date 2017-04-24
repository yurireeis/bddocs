import re

from bddocs.config.i18n import languages
from bddocs.config.settings import LANGUAGE, FEATURE, INVALID_FEATURE_MSG
from bddocs.model.feature import Feature


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
        self.language = self.__get_language()
        self.__retrieve_feature()

        if not self.feature:
            Exception('You must have at least one feature in file %s' % file)

    def __get_language(self):
        """

        :return: String with language of the artifact
        :rtype: str
        """
        lang_regex = r"({}:)".format(LANGUAGE)
        hash_regex = r"({})".format('#')

        for key, text in self.line_offset:
            if re.search(hash_regex, text) and re.search(lang_regex, text):
                lang = text.strip('\n')
                return lang.split()[-1]
            elif text == '\n':
                return 'en'

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

    def is_feature(self, line):
        """

        :return: bool
        """
        regex = r"({})".format(languages[self.language][FEATURE][0])
        return re.search(regex, line)

    def __retrieve_feature(self):
        """

        :return:
        """
        feature = None

        for pos, text in self.line_offset:
            if self.is_feature(text):
                feature = Feature(text, pos, self.line_offset, self.language)
                break

        if not feature:
            raise Exception(INVALID_FEATURE_MSG)

        self.feature = feature
