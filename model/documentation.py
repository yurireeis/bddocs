import os
import re
from config.constants import ARTIFACTS_EXTENSION, DEFAULT_FILENAME, INVALID_PATH_MSG, NO_VALID_ARTIFACTS_MSG, \
    NOT_IMPLEMENTED, CORE_FEATURE
from model.artifact import Artifact
from src.html.html import HTML
from src.pdf.pdf import PDF


class Documentation(HTML, PDF):
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
        # FIXME: eliminate this approach above ASAP (when you find the correct manner to solve)
        doc = self
        PDF.__init__(self, doc)
        HTML.__init__(self, doc)
        self.get_number_of_features()
        self.get_number_of_implemented_features()

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

    def preview(self):
        return self.page

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

    def get_number_of_implemented_core_features(self):
        """

        :return:
        """
        core_imp_features = 0
        for artifact in self.artifacts:
            if self.__is_core(str(artifact.feature.tags)) and self.__is_implemented(str(artifact.feature.tags)):
                core_imp_features += 1

        return core_imp_features

    def get_artifacts(self):
        """

        Get all artifacts in specified path

        :param path: the directory where feature files are in
        :type path: str
        """
        if not os.path.exists(self.path):
            raise Exception(NO_VALID_ARTIFACTS_MSG)

        for root, sub_dirs, files in os.walk(self.path):
            for file in files:
                if file.endswith(ARTIFACTS_EXTENSION):
                    self.artifacts.append(Artifact(root, file))

        if not self.artifacts:
            raise Exception(INVALID_PATH_MSG)

    def html_output(self, filename=None):
        if filename:
            with open(filename, 'w') as file:
                return file.writelines(str(self.html_page))

        with open(DEFAULT_FILENAME + '.html', 'w') as file:
            return file.write(str(self.html_page))

    def pdf_output(self):
        """

        :return:
        """
        if self.name:
            return self.output(self.name, 'F')

        return self.output(DEFAULT_FILENAME + '.pdf', 'F')
