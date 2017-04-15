from src.markup import markup


class HTML(object):
    def __init__(self, documentation):
        self.bdd = documentation
        self.page = markup.page()
        self.set_up()
        # self.unordered_list()
        # self.paragraphs()
        self.set_content()

    def set_up(self):
        self.page.init(title="My title",
                       header="Something at the top",
                       footer="The bitter end.")

    def unordered_list(self):
        items = ("Item one", "Item two", "Item three", "Item four")
        self.page.ul(class_='mylist')
        self.page.li(items, class_='myitem')
        self.page.ul.close()

    def paragraphs(self):
        paras = ("This was a fantastic list.", "And now for something completely different.")
        self.page.p(paras)

    def images(self):
        """
        Implement later
        :return:
        """
        images = ("thumb1.jpg", "thumb2.jpg", "more.jpg", "more2.jpg")
        self.page.img(src=images, width=100, height=80, alt="Thumbnails")

    def set_content(self):
        for artifact in self.bdd.artifacts:
            feature = artifact.feature

            # feature title
            self.page.p(feature.title)

            if feature.actor:
                self.page.p(feature.actor)
            if feature.objective:
                self.page.p(feature.objective)
            if feature.value:
                self.page.p(feature.value)

            if not feature.actor and not feature.objective and not feature.value:
                self.page.p('No value proposition found')

            # break line
            self.page.br()

            if feature.scenarios:

                for scenario in feature.scenarios:
                    self.page.p(scenario.title)

                    if not scenario.steps:
                        self.page.p('[This scenario dont have steps yet]')
                    else:
                        for step in scenario.steps:
                            self.page.p(step.title)

                # break line after scenario
                self.page.br()

            else:
                self.page.p('This feature Dont have scenarios')

                # break line if you dont have scenarios in this feature
                self.page.br()

    def preview(self):
        return self.page
