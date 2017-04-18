class Step(object):
    """
    Docstring for Step class
    """
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
