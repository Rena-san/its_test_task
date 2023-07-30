from page_object.element.base_element import Element


class Label(Element):

    def get_label_text(self):
        return self.find_element().text
