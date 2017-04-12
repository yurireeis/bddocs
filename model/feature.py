class Feature(object):
    """
    Docstring for Feature class
    """
    title = None
    # regex = r"\b(Feature:)"

    def __init__(self, file_path):
        self.path = file_path
        self.title = self.get_title()
        self.actor, self.objective, self.value = self.get_template()

    def get_title(self):
        """

        :return: a String with Feature title
        :rtype: str
        """
        with open(self.path, 'r') as file:
            for line in file.readlines():
                if line.startswith('Feature:'):
                    return line.replace('Feature:', '')

        raise Exception("This artifact Don't have any feature inside")

    def get_template(self):
        """

        Get the Feature template from document

        :param file_path:
        :return: three way tuple
        :rtype: tuple
        """

        actor = objective = value = None

        with open(self.path, 'r') as file:
            for line in file.readlines():
                if line.startswith('As a'):
                    actor = line.replace('As a', '')

                elif line.startswith('I want'):
                    objective = line.replace('I want', '')

                elif line.startswith('So that'):
                    value = line.replace('So that', '')

        return actor, objective, value
