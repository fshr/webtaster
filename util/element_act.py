from elements.elements import elements


class element_act:

    def __init__(self, driver):
        self.driver = driver

    def get(self, e_name):
        selectors = elements[e_name.__class__.__name__]

        if e_name.name in selectors["id_selectors"]:
            id_selector = selectors["id_selectors"][e_name.name]
            return self.driver.find_element_by_id(id_selector)

        elif e_name.name in selectors["css_selectors"]:
            css_selector = selectors["css_selectors"][e_name.name]
            return self.driver.find_element_by_css_selector(css_selector)

    def is_displayed(self, e_name):
        return self.get(e_name).is_displayed()

