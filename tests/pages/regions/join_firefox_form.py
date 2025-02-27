# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pypom import Region
from selenium.webdriver.common.by import By


class JoinFirefoxForm(Region):

    _root_locator = (By.ID, 'fxa-email-form')
    _email_locator = (By.ID, 'fxa-email-field')
    _continue_button_locator = (By.ID, 'fxa-email-form-submit')

    @property
    def is_displayed(self):
        return self.page.is_element_displayed(*self._root_locator)

    @property
    def email(self):
        el = self.find_element(*self._email_locator)
        return el.get_attribute('value')

    def type_email(self, value):
        self.find_element(*self._email_locator).send_keys(value)

    def click_continue(self):
        self.find_element(*self._continue_button_locator).click()
        self.wait.until(lambda s: '/signup?action=email' in s.current_url)
