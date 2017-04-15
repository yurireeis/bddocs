from fpdf import FPDF


class PDF(FPDF):
    def __init__(self, documentation, logo=None):
        super(PDF, self).__init__()
        self.docs = documentation
        self.logo = logo
        self.body()

    def header(self):
        # Logo
        if self.logo:
            self.image(self.logo, 10, 8, 33)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, 'Title', 1, 0, 'C')
        # Line break
        self.ln(20)

    def body(self):
        self.alias_nb_pages()
        self.add_page()

        for artifact in self.docs.artifacts:
            feature = artifact.feature

            # feature title
            self.set_font('Times', 'B', 12)
            self.cell(0, 10, feature.title.upper(), 0, 1)

            self.set_font('Times', '', 10)
            if feature.actor:
                self.cell(0, 10, feature.actor, 0, 1)
            if feature.objective:
                self.cell(0, 10, feature.objective, 0, 1)
            if feature.value:
                self.cell(0, 10, feature.value, 0, 1)

            if not feature.actor and not feature.objective and not feature.value:
                self.cell(0, 10, 'No value description', 0, 1)

            # break line
            self.cell(0, 10, '', 0, 1)

            if feature.scenarios:

                for scenario in feature.scenarios:
                    self.set_font('Times', 'B', 12)
                    self.cell(0, 10, scenario.title, 0, 1)

                    if not scenario.steps:
                        self.cell(0, 10, '[This scenario Dont have steps yet]', 0, 1)
                    else:
                        self.set_font('Times', '', 10)
                        for step in scenario.steps:
                            self.cell(0, 10, step.title, 0, 1)

                # break line after scenario
                self.cell(0, 10, '', 0, 1)

            else:
                self.cell(0, 10, 'This feature Dont Have scenarios', 0, 1)

                # break line if you dont have scenarios in this feature
                self.cell(0, 10, '', 0, 1)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')
