# 🚖 Testes Automatizados - Urban Routes

Este projeto foi desenvolvido dentro da Sprint 7 e 8 do curso de QA, e contém uma suíte de testes automatizados para o sistema *Urban Routes*, utilizando **Selenium WebDriver**, **Python**, e o padrão **Page Object Model (POM)**.

Os testes cobrem o fluxo de solicitação de corrida, incluindo:  
✅ Configuração da rota  
✅ Seleção de plano  
✅ Preenchimento de telefone  
✅ Adição de método de pagamento  
✅ Comentário para motorista  
✅ Seleção de itens adicionais (cobertor, sorvete)  
✅ Início da busca por carro  

---

## 🛠 Tecnologias utilizadas

- Python 3.x  
- Selenium WebDriver  
- pytest 
- ChromeDriver  
- Page Object Model (POM)

---

## ▶️ Como executar

1️⃣ Clone o repositório:
```bash
git clone <seu-repo-url>
cd urban-routes-tests
```

2️⃣ Crie e ative o ambiente virtual:
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate
```

3️⃣ Instale as dependências:
```bash
pip install -r requirements.txt
```

4️⃣ Execute os testes:
```bash
pytest test_urban_routes.py
```

## ⚡ Testes disponíveis

| Teste                               | Descrição                                              |
|-------------------------------------|--------------------------------------------------------|
| `test_set_route`                    | Verifica o preenchimento dos endereços da rota        |
| `test_select_plan`                  | Seleciona o plano Comfort                             |
| `test_fill_phone_number`            | Preenche e confirma o número de telefone              |
| `test_fill_card`                    | Adiciona um cartão como método de pagamento           |
| `test_comment_for_driver`           | Adiciona um comentário para o motorista               |
| `test_order_blanket_and_handkerchiefs` | Seleciona cobertor e lenços                        |
| `test_order_2_ice_creams`           | Adiciona 2 sorvetes ao pedido                         |
| `test_car_search_model_appears`     | Executa o fluxo completo até a busca do carro         |

---

## 💡 Boas práticas adotadas

✅ Page Object Model (POM) para separar lógica dos testes e interações com a interface.  
✅ Uso de `WebDriverWait` para garantir maior estabilidade dos testes com elementos dinâmicos.  
✅ Modularização dos testes, com métodos auxiliares para evitar duplicação de código.  
✅ Separação clara entre lógica de teste (`main.py`), interações (`pages.py`), dados (`data.py`) e helpers (`helpers.py`).  

---

## 📌 Observações

- É necessário que o servidor **Urban Routes** esteja ativo para que os testes funcionem corretamente.
- O projeto utiliza os logs de performance do Chrome para capturar automaticamente o código SMS.
- Recomenda-se o uso do **ChromeDriver** compatível com a versão do navegador instalado na máquina.
