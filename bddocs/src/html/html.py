from bddocs.config.settings import NO_VALID_PROPOSITION_MSG, NO_STEPS_MSG, NO_SCENARIOS_MSG, DEFAULT_FILENAME
from bddocs.src.markup import markup


class HTML(object):
    def __init__(self, documentation):
        self.docs = documentation
        self.html_page = markup.page()
        self.set_up()
        self.set_content()

    def set_up(self):
        self.html_page.init(title="My title",
                            header="Something at the top",
                            footer="The bitter end.")

    def unordered_list(self):
        items = ("Item one", "Item two", "Item three", "Item four")
        self.html_page.ul(class_='mylist')
        self.html_page.li(items, class_='myitem')
        self.html_page.ul.close()

    def paragraphs(self):
        paras = ("This was a fantastic list.", "And now for something completely different.")
        self.html_page.p(paras)

    def images(self):
        """
        Implement later
        :return:
        """
        images = ("thumb1.jpg", "thumb2.jpg", "more.jpg", "more2.jpg")
        self.html_page.img(src=images, width=100, height=80, alt="Thumbnails")

    def set_content(self):
        for artifact in self.docs.artifacts:
            feature = artifact.feature

            # feature title
            self.html_page.p(feature.title)

            if feature.actor:
                self.html_page.p(feature.actor)
            if feature.objective:
                self.html_page.p(feature.objective)
            if feature.value:
                self.html_page.p(feature.value)

            if not feature.actor and not feature.objective and not feature.value:
                self.html_page.p(NO_VALID_PROPOSITION_MSG)

            # break line
            self.html_page.br()

            if feature.scenarios:

                for scenario in feature.scenarios:
                    self.html_page.p(scenario.title)

                    if not scenario.steps:
                        self.html_page.p(NO_STEPS_MSG)
                    else:
                        for step in scenario.steps:
                            self.html_page.p(step.title)

                # break line after scenario
                self.html_page.br()

            else:
                self.html_page.p(NO_SCENARIOS_MSG)

                # break line if you dont have scenarios in this feature
                self.html_page.br()

    def output(self, filename=None):
        if filename:
            with open(filename, 'w') as file:
                return file.writelines(str(self.html_page))

        with open(DEFAULT_FILENAME + '.html', 'w') as file:
            return file.write(str(self.html_page))
