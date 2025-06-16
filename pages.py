from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UrbanRoutesPage:
    # Localizadores
    FROM_INPUT = (By.ID, "from")
    TO_INPUT = (By.ID, "to")
    PERSONAL_OPTION = (By.XPATH, '//div[@class="mode" and text()="Personal"]')
    TAXI_OPTION = (By.XPATH, '//div[@class="type"]//img[contains(@src, "taxi")]')
    CALL_TAXI_BUTTON = (By.XPATH, '//button[contains(@class, "button") and contains(@class, "round") and text()="Chamar um táxi"]')
    COMFORT_BUTTON = (By.XPATH, '//button[@data-for="tariff-card-4"]')
    PHONE_FIELD = (By.XPATH, '//div[@class="np-button"]//div[@class="np-text" and text()="Número de telefone"]')
    PHONE_INPUT = (By.ID, "phone")
    PHONE_SUBMIT = (By.XPATH, '//button[@type="submit" and text()="Próximo"]')
    SMS_CODE_INPUT = (By.XPATH, '//div[contains(@class, "modal")]//div[contains(@class, "section") and contains(@class, "active")]//input[@id="code"]')
    SMS_CONFIRM = (By.XPATH, '//button[@type="submit" and text()="Confirmar"]')
    PAYMENT_FIELD = (By.XPATH, '//div[contains(@class, "pp-button")]//div[@class="pp-text" and text()="Método de pagamento"]')
    PAYMENT_CARD_OPTION = (By.XPATH, '//div[@class="pp-title" and text()="Adicionar cartão"]')
    CARD_NUMBER_INPUT = (By.ID, "number")
    CARD_CODE_INPUT = (By.XPATH, '//div[contains(@class, "section") and contains(@class, "active")]//input[@id="code"]')
    CARD_ADD_BUTTON = (By.XPATH, '//button[@type="submit" and text()="Adicionar"]')
    COMMENT_INPUT = (By.ID, "comment")
    BLANKET_OPTION = (By.XPATH, '//div[@class="r-sw-label" and text()="Cobertor e lençóis"]/following-sibling::div//input[@type="checkbox"]')
    ICE_CREAM_OPTION = (By.XPATH, '//div[@class="r-counter-label" and text()="Sorvete"]/following-sibling::div//div[@class="counter-plus"]')
    FINAL_CALL_TAXI_BUTTON = (By.XPATH, '//button[@class="smart-button"]')

    def __init__(self, driver):
        self.driver = driver

    def set_route(self, from_location, to_location):
        self.driver.find_element(*self.FROM_INPUT).send_keys(from_location)
        self.driver.find_element(*self.TO_INPUT).send_keys(to_location)
        self.driver.find_element(*self.PERSONAL_OPTION).click()
        self.driver.find_element(*self.TAXI_OPTION).click()

    def select_plan(self):
        self.driver.find_element(*self.CALL_TAXI_BUTTON).click()
        self.driver.find_element(*self.COMFORT_BUTTON).click()

    def fill_phone_number(self, phone, sms_code):
        self.driver.find_element(*self.PHONE_FIELD).click()
        self.driver.find_element(*self.PHONE_INPUT).send_keys(phone)
        self.driver.find_element(*self.PHONE_SUBMIT).click()
        self.driver.find_element(*self.SMS_CODE_INPUT).send_keys(sms_code)
        self.driver.find_element(*self.SMS_CONFIRM).click()

    def fill_card(self, card_number, card_code):
        self.driver.find_element(*self.PAYMENT_FIELD).click()
        self.driver.find_element(*self.PAYMENT_CARD_OPTION).click()
        self.driver.find_element(*self.CARD_NUMBER_INPUT).send_keys(card_number)
        self.driver.find_element(*self.CARD_CODE_INPUT).send_keys(card_code)
        self.driver.find_element(*self.CARD_ADD_BUTTON).click()

    def comment_for_driver(self, comment):
        self.driver.find_element(*self.COMMENT_INPUT).send_keys(comment)

    def order_blanket_and_handkerchiefs(self):
        self.driver.find_element(*self.BLANKET_OPTION).click()

    def order_ice_creams(self, quantity):
        for _ in range(quantity):
            self.driver.find_element(*self.ICE_CREAM_OPTION).click()

    def finalize_order(self):
        self.driver.find_element(*self.FINAL_CALL_TAXI_BUTTON).click()

