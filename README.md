# Testes Automatizados - Urban Routes

![QA](https://img.shields.io/badge/Testes-Automatizados-blue)
![Framework](https://img.shields.io/badge/Selenium-WebDriver-green)
![Linguagem](https://img.shields.io/badge/Python-3.x-yellow)
![Padrão](https://img.shields.io/badge/POM-Page%20Object%20Model-lightgrey)

---

## 📌 Sobre o Projeto

Este projeto foi desenvolvido dentro da Sprint 7 e 8 do curso de QA, e contém uma suíte de testes automatizados para o sistema *Urban Routes*, utilizando **Selenium WebDriver**, **Python**, e o padrão **Page Object Model (POM)**.

---

## 🎯 Objetivo do Projeto

- Validar de forma automatizada o fluxo de solicitação de corrida no Urban Routes  
- Implementar boas práticas de automação com Selenium e POM  
- Aumentar a eficiência e repetibilidade dos testes de interface web

---

## 🔧 Tecnologias e Ferramentas

- **Python**  
- **Selenium WebDriver**  
- **pytest**  
- **ChromeDriver**  
- **Page Object Model (POM)**

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

---

## 🧾 Resultado

- Automação bem-sucedida do fluxo de solicitação de corrida no Urban Routes;
- Testes cobriram etapas críticas de cadastro de rota, plano, telefone, pagamento, comentários e itens adicionais;
- Fluxo completo finalizado com busca de carro iniciada;
- Scripts organizados por páginas (POM) e com boas práticas de estabilidade.

---

## 📚 Aprendizados

- Prática de automação de testes ponta a ponta usando **Selenium WebDriver** e **Python**;
- Aplicação do **Page Object Model (POM)** para melhorar a manutenção e a legibilidade do código;
- Uso de **WebDriverWait** para lidar com elementos dinâmicos;
- Estruturação modular dos testes automatizados.

---

## 💡 Melhorias Futuras

- Incluir mais cenários alternativos (erros de preenchimento, cancelamento de rota);
- Implementar testes em múltiplos navegadores (cross-browser);
- Integrar a suíte de testes a pipelines de CI/CD (ex: GitHub Actions);
- Adicionar geração automática de relatórios de execução.

---

## ✅ Observações

- É necessário que o servidor **Urban Routes** esteja ativo para que os testes funcionem corretamente.
- O projeto utiliza os logs de performance do Chrome para capturar automaticamente o código SMS.
- Recomenda-se o uso do **ChromeDriver** compatível com a versão do navegador instalado na máquina.

---

## 🇺🇸 Project Summary

This project automates the main ride request flow of **Urban Routes**, using **Selenium WebDriver**, **Python**, and the **Page Object Model** pattern.  
The suite covers critical steps: setting the route, selecting a plan, adding phone and payment method, driver comments, extra items, and starting the car search.  
All scripts are modular and follow best practices for maintainability and stability.
