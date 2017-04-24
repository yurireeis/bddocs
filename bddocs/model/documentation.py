import os
import re

from bddocs.config.settings import NOT_IMPLEMENTED, CORE_FEATURE, INVALID_PATH_MSG, ARTIFACTS_EXTENSION, \
    NO_VALID_ARTIFACTS_MSG
from bddocs.model.artifact import Artifact


class Documentation(object):
    """
    Docstring for Documentation class
    """
    artifacts = []
    total_of_features = None

    def __init__(self, path, name=None):
        """

        :param path: the feature file path (to retrieve artifacts)
        :param name: the name of enterprise (goes in Documentation). Default is None
        :type name: str
        """
        self.name = name
        self.path = path
        self.get_artifacts()

    def __is_implemented(self, tag):
        """

        :return: boolean result
        :rtype: bool
        """
        regex = r"({})".format(NOT_IMPLEMENTED)

        if not re.search(regex, tag):
            return True

        return False

    def __is_core(self, tag):
        """

        :return:
        """
        regex = r"({})".format(CORE_FEATURE)
        return re.search(regex, tag)

    def get_number_of_features(self):
        """

        :return:
        """
        return len(self.artifacts)

    def get_number_of_implemented_features(self):
        """

        :return:
        """
        imp_features = 0
        for artifact in self.artifacts:
            if self.__is_implemented(str(artifact.feature.tags)):
                imp_features += 1

        return imp_features

    def get_number_of_core_features(self):
        """

        :return:
        """
        core_imp_features = 0
        for artifact in self.artifacts:
            if self.__is_core(str(artifact.feature.tags)):
                core_imp_features += 1

        return core_imp_features

    def get_number_of_scenarios(self):
        """

        :return:
        """
        scenarios = 0
        for artifact in self.artifacts:
            if self.__is_implemented(str(artifact.feature.tags)):
                scenarios += len(artifact.feature.scenarios)

        return scenarios

    def get_number_of_core_scenarios(self):
        """

        :return:
        """
        core_scenarios = 0
        for artifact in self.artifacts:
            if self.__is_core(str(artifact.feature.tags)) and self.__is_implemented(str(artifact.feature.tags)):
                core_scenarios += len(artifact.feature.scenarios)

        return core_scenarios

    def get_number_of_implemented_core_features(self):
        """

        :return:
        """
        core_imp_features = 0
        for artifact in self.artifacts:
            if self.__is_core(str(artifact.feature.tags)) and self.__is_implemented(str(artifact.feature.tags)):
                core_imp_features += 1

        return core_imp_features

    def get_number_of_implemented_scenarios(self):
        """

        :return:
        """
        imp_scenarios = 0
        for artifact in self.artifacts:
            if self.__is_implemented(str(artifact.feature.tags)):
                for scenario in artifact.feature.scenarios:
                    if self.__is_implemented(str(scenario.tags)):
                        imp_scenarios += 1

        return imp_scenarios

    def get_number_of_implemented_core_scenarios(self):
        """

        :return:
        """
        imp_core_scenarios = 0
        for artifact in self.artifacts:
            if self.__is_core(str(artifact.feature.tags)) and self.__is_implemented(str(artifact.feature.tags)):
                for scenario in artifact.feature.scenarios:
                    if self.__is_implemented(str(scenario.tags)):
                        imp_core_scenarios += 1

        return imp_core_scenarios

    def get_artifacts(self):
        """

        Get all artifacts in specified path

        :param path: the directory where feature files are in
        :type path: str
        """
        if not os.path.exists(self.path):
            raise Exception(INVALID_PATH_MSG)

        for root, sub_dirs, files in os.walk(self.path):
            for file in files:
                if file.endswith(ARTIFACTS_EXTENSION):
                    self.artifacts.append(Artifact(root, file))

        if not self.artifacts:
            raise Exception(NO_VALID_ARTIFACTS_MSG)
