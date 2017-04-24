from bddocs.config.settings import NO_VALUE_MSG, NO_STEPS_MSG, NO_SCENARIOS_MSG
from bddocs.src.pdf.style import Style


class PDF(Style):
    """
    Docstring for PDF class
    """

    def __init__(self, documentation, logo=None):
        """

        :param documentation:
        :param logo:
        """
        Style.__init__(self)
        self.docs = documentation
        self.logo = logo
        self.body()

    # def header(self):
    #     # Logo
    #     if self.logo:
    #         self.image(self.logo, 10, 8, 33)
    #     # Arial bold 15
    #     self.set_font('Arial', 'B', 15)
    #     # Move to the right
    #     self.cell(80)
    #     # Title
    #     # self.cell(30, 10, 'Title', 1, 0, 'C')
    #     # Line break
    #     self.ln(20)

    def body(self):

        self.alias_nb_pages()

        for artifact in self.docs.artifacts:
            feature = artifact.feature

            # feature title
            self.add_page()
            self.feature(feature.title.upper())

            if feature.actor:
                self.value_proposition(feature.actor)
            if feature.objective:
                self.value_proposition(feature.objective)
            if feature.value:
                self.value_proposition(feature.value)

            if not feature.actor and not feature.objective and not feature.value:
                self.value_proposition(NO_VALUE_MSG)

            # break line
            self.break_line()

            if feature.scenarios:

                for scenario in feature.scenarios:
                    self.scenario(scenario.title)

                    if not scenario.steps:
                        self.scenario(NO_STEPS_MSG)
                    else:
                        for step in scenario.steps:
                            self.step(step.title)

                        self.break_line()

            else:
                self.scenario(NO_SCENARIOS_MSG)

            self.break_line()

            # Page footer
            # def footer(self):
            #     # Position at 1.5 cm from bottom
            #     self.set_y(-15)
            #     # Arial italic 8
            #     self.set_font('Arial', 'I', 8)
            #     # Page number
            #     self.cell(0, 10, 'Página ' + str(self.page_no()) + ' de ' + '{nb}', 0, 0, 'C')

