import re

from config.settings import CONTEXT, ACTION, EXPECTED_BEHAVIOR
from model.step import Step


class Scenario(object):
    """
    Docstring for scenario class
    """

    tags = []

    def __init__(self, title, start, line_offset):
        self.title = title
        self.start_line = start
        self.line_offset = line_offset
        self.__get_steps()
        self.__get_tags()

    def __is_context(self, line):
        """

        This private function allows you to retrieve Given (en-us) steps

        :return:
        """
        regex = r"({})".format(CONTEXT)
        return re.search(regex, line)

    def __is_action(self, line):
        """

        This private function allows you to retrieve When (en-us) steps

        :return:
        """
        regex = r"({})".format(ACTION)
        return re.search(regex, line)

    def __is_expected_behavior(self, line):
        """

        This private function allows you to retrieve Then (en-us) steps

        """
        regex = r"({})".format(EXPECTED_BEHAVIOR)
        return re.search(regex, line)

    def __is_tag(self, line):
        """

        :param line:
        :return:
        """
        regex = r"(@)"
        return re.search(regex, line)

    def __get_steps(self):
        """

        :return:
        """
        steps = []
        rows = [x[1] for x in self.line_offset]
        for pos in range(self.start_line, len(self.line_offset)):
            if self.__is_context(rows[pos]):
                steps.append(Step(rows[pos], pos, self.line_offset))
            elif self.__is_action(rows[pos]):
                steps.append(Step(rows[pos], pos, self.line_offset))
            elif self.__is_expected_behavior(rows[pos]):
                steps.append(Step(rows[pos], pos, self.line_offset))
            elif rows[pos].startswith('\n'):
                break

        self.steps = steps

    def __get_tags(self):
        """
        Fill feature tags
        :return:
        """
        rows = [x[1] for x in self.line_offset]
        if self.__is_tag(rows[self.start_line - 1]):
            self.tags = rows[self.start_line - 1].split()
