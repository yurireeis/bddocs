import os
from model.artifact import Artifact
from src.html.html import HTML
from src.pdf.pdf import PDF

artifacts_ext = '.feature'


class Documentation(HTML, PDF):
    """
    Docstring for Documentation class
    """
    artifacts = []

    def __init__(self, path, name=None):
        """

        :param path: the feature file path (to retrieve artifacts)
        :param name: the name of enterprise (goes in Documentation). Default is None
        :type name: str
        """
        self.name = name
        self.path = path
        self.get_artifacts()
        # FIXME: eliminate this aproach above ASAP (when you find the correct manner to solve)
        doc = self
        PDF.__init__(self, doc)
        HTML.__init__(self, doc)

    def preview(self):
        return self.page

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

    def html_output(self, filename=None):
        if filename:
            with open(filename + '.html', 'w') as file:
                return file.writelines(str(self.html_page))

        with open('default.html', 'w') as file:
            return file.write(str(self.html_page))

    def pdf_output(self):
        """

        :return:
        """
        if self.name:
            return self.output(self.name, 'F')

        return self.output('default.pdf', 'F')
