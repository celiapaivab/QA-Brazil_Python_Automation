from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import data

class UrbanRoutesPage:
    # Localizadores
    FROM_INPUT = (By.ID, "from")
    TO_INPUT = (By.ID, "to")
    PERSONAL_OPTION = (By.XPATH, '//div[@class="mode" and text()="Personal"]')
    TAXI_OPTION = (By.XPATH, '//div[contains(@class, "type") and .//img[contains(@src, "taxi")]]')
    CALL_TAXI_BUTTON = (By.CSS_SELECTOR, 'button.button.round')
    COMFORT_OPTION = (By.XPATH, "//div[contains(@class, 'tcard') and .//button[@data-for='tariff-card-4']]")
    COMFORT_TITLE = (By.XPATH, "//div[contains(@class, 'tcard-title') and text()='Comfort']")
    PHONE_FIELD = (By.CSS_SELECTOR, "div.np-button > div.np-text")
    PHONE_INPUT = (By.ID, "phone")
    PHONE_SUBMIT = (By.XPATH, '//button[@type="submit" and text()="Próximo"]')
    SMS_CODE_INPUT = (By.XPATH, '//div[contains(@class, "modal")]//div[contains(@class, "section") and contains(@class, "active")]//input[@id="code"]')#ID igual ao card code
    SMS_CONFIRM = (By.XPATH, '//button[@type="submit" and text()="Confirmar"]')
    PHONE_FIELD_AFTER = (By.CSS_SELECTOR, "div.np-button.filled > div.np-text")
    PAYMENT_FIELD = (By.CSS_SELECTOR, 'div.pp-button div.pp-text')
    PAYMENT_CARD_OPTION = (By.XPATH, '//div[@class="pp-title" and text()="Adicionar cartão"]')
    CARD_NUMBER_INPUT = (By.ID, "number")
    CARD_CODE_INPUT = (By.XPATH, '//div[contains(@class, "section") and contains(@class, "active")]//input[@id="code"]') #ID igual ao SMS
    CARD_ADD_BUTTON = (By.XPATH, '//button[@type="submit" and text()="Adicionar"]')
    CLOSE_MODAL_BUTTON = (By.CSS_SELECTOR, ".payment-picker.open .section.active .close-button.section-close")
    PAYMENT_FIELD_VALUE = (By.CSS_SELECTOR, "div.pp-button.filled div.pp-value-text")
    COMMENT_INPUT = (By.ID, "comment")
    BLANKET_OPTION = ( By.XPATH, '//div[contains(@class, "r-sw-container")]//div[contains(@class, "r-sw")]//div[contains(@class, "switch")]//span[contains(@class, "slider")]')
    BLANKET_CHECKBOX = (By.XPATH, '//div[contains(@class, "r-sw-container")]//div[contains(@class, "r-sw")]//div[contains(@class, "switch")]//input[@type="checkbox"]')
    ICE_CREAM_OPTION = (By.XPATH, '(//div[contains(@class, "r-group-items")]//div[contains(@class, "r-counter-container")])[1]//div[contains(@class, "counter-plus")]')
    ICE_CREAM_COUNTER = (By.XPATH, '(//div[contains(@class, "r-group-items")]//div[contains(@class, "r-counter-container")])[1]//div[contains(@class, "counter-value")]')
    FINAL_CALL_TAXI_BUTTON = (By.XPATH, '//button[@class="smart-button"]')
    SEARCH_MODAL = (By.CSS_SELECTOR, ".order.shown")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 3)

    # SET ROUTE
    def enter_from_location(self, from_location):
        from_input = self.wait.until(EC.visibility_of_element_located(self.FROM_INPUT))
        from_input.clear()
        from_input.send_keys(from_location)

    def enter_to_location(self, to_location):
        to_input = self.wait.until(EC.visibility_of_element_located(self.TO_INPUT))
        to_input.clear()
        to_input.send_keys(to_location)

    def get_from_location_value(self):
        from_input = self.wait.until(EC.visibility_of_element_located(self.FROM_INPUT))
        return from_input.get_attribute("value")

    def get_to_location_value(self):
        to_input = self.wait.until(EC.visibility_of_element_located(self.TO_INPUT))
        return to_input.get_attribute("value")

    # SELECT PLAN
    def select_personal_mode(self):
        personal = self.wait.until(EC.visibility_of_element_located(self.PERSONAL_OPTION))
        if "active" not in personal.get_attribute("class"):
            personal.click()

    def select_taxi_type(self):
        taxi_div = self.wait.until(EC.visibility_of_element_located(self.TAXI_OPTION))
        if "active" not in taxi_div.get_attribute("class"):
            taxi_div.click()

    def click_call_taxi(self):
        button = self.wait.until(EC.element_to_be_clickable(self.CALL_TAXI_BUTTON))
        button.click()

    def select_comfort_plan(self):
        comfort = self.wait.until(EC.visibility_of_element_located(self.COMFORT_OPTION))
        if "active" not in comfort.get_attribute("class"):
            comfort.click()

    def get_selected_plan(self):
        comfort_title = self.wait.until(EC.visibility_of_element_located(self.COMFORT_TITLE))
        return comfort_title.text.strip()

    # FILL PHONE NUMBER
    def click_phone_field(self):
        field = self.wait.until(EC.element_to_be_clickable(self.PHONE_FIELD))
        field.click()

    def enter_phone_number(self, phone):
        phone_input = self.wait.until(EC.visibility_of_element_located(self.PHONE_INPUT))
        phone_input.send_keys(phone)

    def submit_phone(self):
        submit_btn = self.wait.until(EC.element_to_be_clickable(self.PHONE_SUBMIT))
        submit_btn.click()

    def enter_sms_code(self, sms_code):
        code_input = self.wait.until(EC.visibility_of_element_located(self.SMS_CODE_INPUT))
        code_input.send_keys(sms_code)

    def confirm_sms_code(self):
        confirm_btn = self.wait.until(EC.element_to_be_clickable(self.SMS_CONFIRM))
        confirm_btn.click()

    def get_displayed_phone_number(self):
        phone_field = self.wait.until(EC.visibility_of_element_located(self.PHONE_FIELD_AFTER))
        return phone_field.text.strip()

    # FILL CARD NUMBER
    def open_payment_field(self):
        payment = self.wait.until(EC.element_to_be_clickable(self.PAYMENT_FIELD))
        payment.click()

    def choose_add_card(self):
        add_card = self.wait.until(EC.element_to_be_clickable(self.PAYMENT_CARD_OPTION))
        add_card.click()

    def enter_card_number(self, card_number):
        number_input = self.wait.until(EC.visibility_of_element_located(self.CARD_NUMBER_INPUT))
        number_input.send_keys(card_number)

    def enter_card_cvv(self, card_cvv):
        cvv_input = self.wait.until(EC.visibility_of_element_located(self.CARD_CODE_INPUT))
        cvv_input.send_keys(card_cvv)
        cvv_input.send_keys(Keys.TAB)

    def submit_card(self):
        add_btn = self.wait.until(EC.element_to_be_clickable(self.CARD_ADD_BUTTON))
        add_btn.click()

    def close_payment_modal(self):
        close_btn = self.wait.until(EC.element_to_be_clickable(self.CLOSE_MODAL_BUTTON))
        close_btn.click()

    def get_payment_method_text(self):
        pay_field = self.wait.until(EC.visibility_of_element_located(self.PAYMENT_FIELD_VALUE))
        return pay_field.text.strip()

    # TEST COMMENT
    def comment_for_driver(self, comment):
        comment_input = self.wait.until(EC.visibility_of_element_located(self.COMMENT_INPUT))
        comment_input.send_keys(comment)

    def get_comment_for_driver(self):
        comment_input = self.wait.until(EC.visibility_of_element_located(self.COMMENT_INPUT))
        return comment_input.get_attribute("value")

    # TEST ORDER BLANKET
    def order_blanket_and_handkerchiefs(self):
        slider = self.wait.until(EC.element_to_be_clickable(self.BLANKET_OPTION))
        slider.click()

    def is_blanket_and_handkerchiefs_selected(self):
        checkbox = self.wait.until(EC.presence_of_element_located(self.BLANKET_CHECKBOX))
        return checkbox.is_selected()

    # TEST ORDER ICE CREAM
    def order_ice_creams(self, quantity):
        plus_btn = self.wait.until(EC.element_to_be_clickable(self.ICE_CREAM_OPTION))
        for _ in range(quantity):
            plus_btn.click()

    def get_ice_cream_count(self):
        counter = self.wait.until(EC.visibility_of_element_located(self.ICE_CREAM_COUNTER))
        return int(counter.text.strip())

    # TEST SEARCH CAR
    def click_final_call_taxi_button(self):
        call_btn = self.wait.until(EC.element_to_be_clickable(self.FINAL_CALL_TAXI_BUTTON))
        call_btn.click()

    def wait_for_search_modal(self):
        modal = self.wait.until(EC.visibility_of_element_located(self.SEARCH_MODAL))
        return modal
