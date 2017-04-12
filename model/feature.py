from model.scenario import Scenario


class Feature(object):
    """
    Docstring for Feature class
    """

    title = None
    actor = None
    objective = None
    value = None
    scenarios = []

    def __init__(self, file_path):
        self.path = file_path
        self.fill_title()
        self.fill_header()
        self.fill_scenarios()

    def __is_title(self, line):
        """

        :return: bool
        """
        if line.startswith('Feature:'):
            self.title = line.replace('Feature:', '')
            return True

        return False

    def __is_actor(self, line):
        """
        Set the Actor (or role) from document
        :return:
        """
        if line.startswith('As a'):
            self.actor = line.replace('As a', '')

    def __is_objective(self, line):
        """
        Set the Objective from document
        :return:
        """
        if line.startswith('As a'):
            self.objective = line.replace('I want', '')

    def ___value_proposition(self, line):
        """
        Set the Objective from document
        :return:
        """
        if line.startswith('As a'):
            self.objective = line.replace('So that', '')

    def fill_title(self):
        """
        A feature must have a title (otherwise is invalid)
        """
        with open(self.path, 'r') as file:
            for line in file.readlines():
                if self.__is_title(line):
                    return True

        # TODO: create class with no pattern found specific exceptions
        raise Exception("This artifact Don't have any feature inside")

    def fill_header(self):
        """

        This function scan file looking for patterns and
        fill feature header

        :return:
        """
        with open(self.path, 'r') as file:
            for line in file.readlines():
                # get feature header
                self.__is_title(line)
                self.__is_actor(line)
                self.__is_objective(line)
                self.___value_proposition(line)

    def fill_scenarios(self):
        """
        This functions set a list of scenarios objects
        """
        # fill if scenario is not null
        with open(self.path, 'r') as file:
            scenario = Scenario()
            for line in file.readlines():
                # fill scenarios list
                if scenario.is_valid(line):
                    self.scenarios.append(scenario)
                    scenario = Scenario()
