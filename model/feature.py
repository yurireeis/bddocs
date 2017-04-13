import re

from model.scenario import Scenario


class Feature(object):
    """
    Docstring for Feature class
    """
    actor = None
    objective = None
    value = None
    line_offset = []

    def __init__(self, title, start, line_offset):
        """

        :param title: the feature title
        :type title: str
        :param start: the feature start line
        :type start: int
        :param file_path: the file path from Artifact
        :type file_path: str
        """
        self.title = title
        self.start_line = start
        self.line_offset = line_offset
        self.__fill_header()
        self.scenarios = self.__retrieve_scenarios()

    def __is_actor(self, line):
        """
        Set the Actor (or role) from document
        :return:
        """
        regex = r"(As a)\b"
        return re.search(regex, line)

    def __is_objective(self, line):
        """
        Set the Objective from document
        :return:
        """
        regex = r"(I want)\b"
        return re.search(regex, line)

    def __is_value_proposition(self, line):
        """
        Set the Value Proposition from document
        :return:
        """
        regex = r"(So that)\b"
        return re.search(regex, line)

    def __is_scenario(self, line):
        """

        :return:
        """
        regex = r"(Scenario:)"
        return re.search(regex, line)

    def __fill_header(self):
        """

        This function scan file looking for patterns and
        fill feature header

        :return:
        """
        actor, objective, value = None, None, None

        for pos, text in self.line_offset:
            if self.__is_actor(text):
                actor = text
            elif self.__is_objective(text):
                objective = text
            elif self.__is_value_proposition(text):
                value = text
            elif actor and objective and value:
                break

    def __retrieve_scenarios(self):
        """
        Fill feature body
        :return:
        """
        scenarios = []
        rows = [x[1] for x in self.line_offset]
        for pos in range(self.start_line, len(self.line_offset)):
            if self.__is_scenario(rows[pos]):
                scenarios.append(Scenario(rows[pos], pos, self.line_offset))

        return scenarios
