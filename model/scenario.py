class Scenario(object):
    """
    Docstring for scenario class
    """
    # feature_regex = r"\b(Feature:)"
    # scenario_regex = r"\b(Scenario:)"

    steps = []
    title = None

    def set_title(self, line):
        """

        :return:
        """
        self.title = line.replace('Scenario:', '')

    def __is_context(self, line):
        """

        This private function allows you to retrieve Given (en-us) steps

        :return:
        """
        if line.startswith('Given'):
            self.steps.append(line.replace('Given', ''))

    def __is_action(self, line):
        """

        This private function allows you to retrieve When (en-us) steps

        :return:
        """
        if line.startswith('Given'):
            self.steps.append(line.replace('When', ''))

    def __is_expected_behavior(self, line):
        """

        This private function allows you to retrieve Then (en-us) steps

        """
        if line.startswith('Given'):
            self.steps.append(line.replace('Then', ''))

    def __fill_scenario(self):
        """
        This private method fills scenario info
        :return:
        """
        pass

