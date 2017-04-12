from model.feature import Feature


class Artifact(object):
    """
    Docstring for Artifact class
    """

    def __init__(self, _dir, file):
        """

        :param _dir: a file directory to know where you can find the Artifact
        :type _dir: str
        :param file: a feature file name to open and read
        :type file_directory: str
        """
        self.file_path = './%s/%s' % (_dir, file)
        self.feature = Feature(self.file_path)
