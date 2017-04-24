import re

from bddocs.config.i18n import languages
from bddocs.config.settings import ACTOR, OBJECTIVE, VALUE_PROPOSITION, SCENARIO
from bddocs.model.scenario import Scenario


class Feature(object):
    """
    Docstring for Feature class
    """
    actor = None
    objective = None
    value = None
    line_offset = []
    tags = []

    def __init__(self, title, start, line_offset, language):
        """

        :param title: the feature title
        :type title: str
        :param start: the feature start line
        :type start: int
        :param line_offset:
        :type line_offset:
        """
        self.language = language
        self.title = title
        self.start_line = start
        self.line_offset = line_offset
        self.__get_header()
        self.__get_scenarios()
        self.__get_tags()

    def __is_actor(self, line):
        """
        Set the Actor (or role) from document
        :return:
        """
        regex = r"({})".format(languages[self.language][ACTOR][0])
        return re.search(regex, line)

    def __is_objective(self, line):
        """
        Set the Objective from document
        :return:
        """
        regex = r"({})".format(languages[self.language][OBJECTIVE][0])
        return re.search(regex, line)

    def __is_value_proposition(self, line):
        """
        Set the Value Proposition from document
        :return:
        """
        regex = r"({})".format(languages[self.language][VALUE_PROPOSITION][0])
        return re.search(regex, line)

    def is_scenario(self, line):
        """

        :return:
        """
        regex = r"({})".format(languages[self.language][SCENARIO][0])
        return re.search(regex, line)

    def __is_tag(self, line):
        """

        :param line:
        :return:
        """
        regex = r"(@)"
        return re.search(regex, line)

    def __get_header(self):
        """

        This function scan file looking for patterns and
        fill feature header

        """
        actor, objective, value = None, None, None

        for pos, text in self.line_offset:
            if actor and objective and value:
                break
            elif self.__is_actor(text):
                self.actor = text
            elif self.__is_objective(text):
                self.objective = text
            elif self.__is_value_proposition(text):
                self.value = text

    def __get_scenarios(self):
        """
        Fill feature body
        :return:
        """
        scenarios = []
        rows = [x[1] for x in self.line_offset]
        for pos in range(self.start_line, len(self.line_offset)):
            if self.is_scenario(rows[pos]):
                scenarios.append(Scenario(rows[pos], pos, self.line_offset, self.language))

        self.scenarios = scenarios

    def __get_tags(self):
        """
        Fill feature tags
        :return:
        """
        rows = [x[1] for x in self.line_offset]
        if self.__is_tag(rows[self.start_line - 1]):
            self.tags = rows[self.start_line - 1].split()
