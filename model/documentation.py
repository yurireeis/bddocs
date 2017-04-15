import os
from model.artifact import Artifact
from pdf import PDF

artifacts_ext = '.feature'


class Documentation(PDF):
    """
    Docstring for Documentation class
    """
    artifacts = []

    def __init__(self, path):
        """

        :param path: the feature file path (to retrieve artifacts)
        """
        self.path = path
        self.get_artifacts()
        super(Documentation, self).__init__(self)

    def get_artifacts(self):
        """

        Get all artifacts in specified path

        :param path: the directory where feature files are in
        :type path: str
        """
        if not os.path.exists(self.path):
            raise Exception('You must set a valid path')

        for root, sub_dirs, files in os.walk(self.path):
            for file in files:
                if file.endswith(artifacts_ext):
                    self.artifacts.append(Artifact(root, file))

        if not self.artifacts:
            raise Exception('you must set a path with valid artifacts')
