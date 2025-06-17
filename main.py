import data
import helpers
from selenium import webdriver
from pages import UrbanRoutesPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")

        # não modifique, pois precisamos do registro adicional habilitado para recuperar o código de confirmação do telefone
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

        cls.driver.get(data.URBAN_ROUTES_URL)
        cls.page = UrbanRoutesPage(cls.driver)

    def test_set_route(self):
        self.page.enter_from_location(data.ADDRESS_FROM)
        self.page.enter_to_location (data.ADDRESS_TO)
        assert self.page.get_from_location_value() == data.ADDRESS_FROM, "Endereço de origem incorreto."
        assert self.page.get_to_location_value() == data.ADDRESS_TO, "Endereço de destino incorreto."

    def test_select_plan(self):
        # Teste anterior
        self.page.enter_from_location(data.ADDRESS_FROM)
        self.page.enter_to_location(data.ADDRESS_TO)

        # Teste para selecionar o plano
        self.page.select_personal_mode()
        self.page.select_taxi_type()
        self.page.click_call_taxi()
        self.page.select_comfort_plan()
        assert self.page.get_selected_plan() == "Comfort", "O plano Comfort não foi selecionado corretamente."

    def test_fill_phone_number(self):
        # Teste anterior
        self.page.enter_from_location(data.ADDRESS_FROM)
        self.page.enter_to_location(data.ADDRESS_TO)
        self.page.select_personal_mode()
        self.page.select_taxi_type()
        self.page.click_call_taxi()
        self.page.select_comfort_plan()

        # Teste para preencher o  número de telefone
        self.page.click_phone_field()
        self.page.enter_phone_number(data.PHONE_NUMBER)
        self.page.submit_phone()
        sms_code = helpers.retrieve_phone_code(self.driver)
        assert sms_code, "Não foi possível recuperar o código SMS"
        self.page.enter_sms_code(sms_code)
        self.page.confirm_sms_code()
        assert self.page.get_displayed_phone_number() == data.PHONE_NUMBER, f"Número exibido incorreto: {displayed_number}"

    def test_fill_card(self):
        # Teste anterior
        self.page.enter_from_location(data.ADDRESS_FROM)
        self.page.enter_to_location(data.ADDRESS_TO)
        self.page.select_personal_mode()
        self.page.select_taxi_type()
        self.page.click_call_taxi()
        self.page.select_comfort_plan()
        self.page.click_phone_field()
        self.page.enter_phone_number(data.PHONE_NUMBER)
        self.page.submit_phone()
        sms_code = helpers.retrieve_phone_code(self.driver)
        self.page.enter_sms_code(sms_code)
        self.page.confirm_sms_code()

        # Teste para preencher o cartão
        self.page.open_payment_field()
        self.page.choose_add_card()
        self.page.enter_card_number(data.CARD_NUMBER)
        self.page.enter_card_cvv(data.CARD_CODE)
        self.page.submit_card()
        assert self.page.get_payment_method_text() == "Cartão", f"Método de pagamento incorreto exibido: {payment_method}"

    def test_comment_for_driver(self):
        # Teste anterior
        self.page.enter_from_location(data.ADDRESS_FROM)
        self.page.enter_to_location(data.ADDRESS_TO)
        self.page.select_personal_mode()
        self.page.select_taxi_type()
        self.page.click_call_taxi()
        self.page.select_comfort_plan()
        self.page.click_phone_field()
        self.page.enter_phone_number(data.PHONE_NUMBER)
        self.page.submit_phone()
        sms_code = helpers.retrieve_phone_code(self.driver)
        self.page.enter_sms_code(sms_code)
        self.page.confirm_sms_code()
        self.page.open_payment_field()
        self.page.choose_add_card()
        self.page.enter_card_number(data.CARD_NUMBER)
        self.page.enter_card_cvv(data.CARD_CODE)
        self.page.submit_card()

        # Teste para adicionar comentário
        self.page.comment_for_driver(data.MESSAGE_FOR_DRIVER)
        assert self.page.get_comment_for_driver() == data.MESSAGE_FOR_DRIVER, "Mensagem ao motorista incorreta."

    def test_order_blanket_and_handkerchiefs(self):
        # Adicionar em S8
        print("Função criada para pedir cobertor e lenços")
        pass

    def test_order_2_ice_creams(self):
        print("Função criada para pedir 2 sorvetes")
        for i in range(2):
            # Adicionar em S8
            pass

    def test_car_search_model_appears(self):
        # Adicionar em S8
        print("Função criada para pesquisar se o modelo do carro aparece")
        pass

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()