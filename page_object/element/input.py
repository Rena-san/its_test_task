from page_object.element.base_element import Element


class Input(Element):

    def send_text(self, text):
        input = self.find_element()
        input.send_keys(text)

