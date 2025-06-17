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

        cls.driver.get(data.URBAN_ROUTES_URL)
        cls.page = UrbanRoutesPage(cls.driver)

    def test_set_route(self):
        self.page.enter_from_location(data.ADDRESS_FROM)
        self.page.enter_to_location (data.ADDRESS_TO)
        assert self.page.get_from_location_value() == data.ADDRESS_FROM
        assert self.page.get_to_location_value() == data.ADDRESS_TO

    def test_select_plan(self):
        self.page.enter_from_location(data.ADDRESS_FROM)
        self.page.enter_to_location(data.ADDRESS_TO)
        self.page.select_personal_mode()
        self.page.select_taxi_type()
        self.page.click_call_taxi()
        self.page.select_comfort_plan()
        assert self.page.get_selected_plan() == "Comfort", "O plano Comfort não foi selecionado corretamente."

    def test_fill_phone_number(self):
        pass

    def test_fill_card(self):
        # Adicionar em S8
        print("Função criada para preencher o cartão")
        pass

    def test_comment_for_driver(self):
        # Adicionar em S8
        print("Função criada para comentar para o motorista")
        pass

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