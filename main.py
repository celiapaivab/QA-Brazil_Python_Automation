import time

import data
import helpers
from selenium import webdriver
from pages import UrbanRoutesPage

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

    def setup_method(self):
        self.page = UrbanRoutesPage(self.driver)

    def setup_common_route_flow(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        self.page.enter_from_location(data.ADDRESS_FROM)
        self.page.enter_to_location(data.ADDRESS_TO)
        self.page.select_personal_mode()
        self.page.select_taxi_type()
        self.page.click_call_taxi()
        self.page.select_comfort_plan()

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        self.page = UrbanRoutesPage(self.driver)
        self.page.enter_from_location(data.ADDRESS_FROM)
        self.page.enter_to_location (data.ADDRESS_TO)
        assert self.page.get_from_location_value() == data.ADDRESS_FROM, "Endereço de origem incorreto."
        assert self.page.get_to_location_value() == data.ADDRESS_TO, "Endereço de destino incorreto."

    def test_select_plan(self):
        # Teste selecionar rota e plano
        self.setup_common_route_flow()
        assert self.page.get_selected_plan() == "Comfort", "O plano Comfort não foi selecionado corretamente."

    def test_fill_phone_number(self):
        # Teste selecionar rota e plano
        self.setup_common_route_flow()

        # Teste para preencher o  número de telefone
        self.page.click_phone_field()
        self.page.enter_phone_number(data.PHONE_NUMBER)
        self.page.submit_phone()
        sms_code = helpers.retrieve_phone_code(self.driver)
        assert sms_code, "Não foi possível recuperar o código SMS"
        self.page.enter_sms_code(sms_code)
        self.page.confirm_sms_code()
        assert self.page.get_displayed_phone_number() == data.PHONE_NUMBER, "Número exibido incorreto"

    def test_fill_card(self):
        # Teste selecionar rota e plano
        self.setup_common_route_flow()

        # Teste para preencher o cartão
        self.page.open_payment_field()
        self.page.choose_add_card()
        self.page.enter_card_number(data.CARD_NUMBER)
        self.page.enter_card_cvv(data.CARD_CODE)
        self.page.submit_card()
        self.page.close_payment_modal()
        assert self.page.get_payment_method_text() == "Cartão", "Método de pagamento incorreto."

    def test_comment_for_driver(self):
        # Teste selecionar rota e plano
        self.setup_common_route_flow()

        # Teste para adicionar comentário
        self.page.comment_for_driver(data.MESSAGE_FOR_DRIVER)
        assert self.page.get_comment_for_driver() == data.MESSAGE_FOR_DRIVER, "Mensagem ao motorista incorreta."

    def test_order_blanket_and_handkerchiefs(self):
        # Teste selecionar rota e plano
        self.setup_common_route_flow()

        # Teste para pedir cobertor e lenços
        self.page.order_blanket_and_handkerchiefs()
        assert self.page.is_blanket_and_handkerchiefs_selected(), "O cobertor e lenços não foram selecionados."

    def test_order_2_ice_creams(self):
        # Teste selecionar rota e plano
        self.setup_common_route_flow()

        # Teste para adicionar sorvetes
        self.page.order_ice_creams(2)
        assert self.page.get_ice_cream_count() == 2, "Os 2 sorvetes não foram selecionados"


    def test_car_search_model_appears(self):
        # Teste selecionar rota e plano
        self.setup_common_route_flow()
        # Teste para preencher o  número de telefone
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
        self.page.close_payment_modal()
        # Teste para adicionar comentário
        self.page.comment_for_driver(data.MESSAGE_FOR_DRIVER)
        # Teste para pedir cobertor e lenços
        self.page.order_blanket_and_handkerchiefs()
        # Teste para adicionar sorvetes
        self.page.order_ice_creams(2)

        # Teste para procurar carro
        self.page.click_final_call_taxi_button()
        assert self.page.wait_for_search_modal().is_displayed(), "O modal de busca do carro não apareceu."

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()