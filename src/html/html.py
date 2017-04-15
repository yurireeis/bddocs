from src.markup import markup


class HTML(object):
    def __init__(self, documentation):
        self.documentation = documentation
        self.page = markup.page()
        self.set_up()
        self.unordered_list()
        self.paragraphs()

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

    def preview(self):
        return self.page
