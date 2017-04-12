import os

from model.artifact import Artifact

artifacts_ext = '.feature'


class Documentation(object):
    """
    Docstring for Documentation class
    """
    def __init__(self, path):
        """

        :param path: the feature file path (to retrieve artifacts)
        """
        self.artifacts = self.get_artifacts(path)

    def get_artifacts(self, path):
        """

        Get all artifacts in specified path

        :param path: the directory where feature files are in
        :type path: str
        :return: return a tuple with dir and artifact name
        :rtype: Artifact[]
        """
        found_artifacts = []

        if not os.path.exists(path):
            raise Exception('You must set a valid path')

        for root, sub_dirs, files in os.walk(path):
            for file in files:
                if file.endswith(artifacts_ext):
                    found_artifacts.append(Artifact(root, file))

        if not found_artifacts:
            raise Exception('you must set a path with valid artifacts')

        return found_artifacts
