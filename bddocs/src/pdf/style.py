from fpdf import FPDF


class Style(FPDF):
    """
    A simple static class to set default style content
    """

    def feature(self, text):
        """

        :param self: PDF self. to set style
        :param text: text to be molded
        :return:
        """
        self.set_font('Times', '', 10)
        self.set_fill_color(r=231, g=216, b=213)
        return self.cell(w=0, h=8, txt=text, border=0, ln=1,
                         align='L', fill=True, link='')

    def value_proposition(self, text):
        """

        :param self: PDF self. to set style
        :param text: text to be molded
        :return:
        """
        self.set_font('Times', '', 10)
        return self.cell(w=0, h=8, txt=text, border=0, ln=1,
                         align='L', fill=False, link='')

    def scenario(self, text):
        """

        :param self.: PDF self. to set style
        :param text: text to be molded
        :return:
        """
        self.set_font('Times', '', 12)
        self.set_fill_color(r=67, g=67, b=68)
        self.set_text_color(r=247, g=247, b=247)
        return self.cell(w=0, h=6, txt=text, border=0, ln=1,
                           align='L', fill=True, link='')

    def step(self, text):
        """

        :param self.: PDF self. to set style
        :param text: text to be molded
        :return:
        """
        self.set_font('Times', '', 10)
        self.set_text_color(r=0, g=0, b=0)
        return self.cell(w=0, h=6, txt=text, border=0, ln=1,
                           align='L', fill=False, link='')

    def break_line(self):
        """

        :return:
        """
        return self.cell(w=0, h=6, txt='', border=0, ln=1,
                           align='L', fill=False, link='')
