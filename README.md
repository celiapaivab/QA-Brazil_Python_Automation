# Automated Tests – Urban Routes

![QA](https://img.shields.io/badge/Tests-Automated-blue)
![Framework](https://img.shields.io/badge/Selenium-WebDriver-green)
![Language](https://img.shields.io/badge/Python-3.x-yellow)
![Pattern](https://img.shields.io/badge/POM-Page%20Object%20Model-lightgrey)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/celia-bruno)

---

## 📌 Project Overview

This project was developed during **Sprints 7 and 8** of the QA course as part of a hands-on learning experience in test automation. It features a comprehensive **automated test suite** for the **Urban Routes** application, which simulates a ride-request system.  

The automation is implemented using **Selenium WebDriver** with **Python** and follows the **Page Object Model (POM)** design pattern to ensure code maintainability and scalability. The test suite covers critical user flows, validating the functionality and stability of key features through end-to-end testing.


---

## 🎯 Project Goal

- Validate the Urban Routes ride request flow through automated tests  
- Apply best practices in automation using Selenium and POM  
- Increase efficiency and repeatability for web UI tests

---

## 🔧 Technologies and Tools

- **Python**  
- **Selenium WebDriver**  
- **pytest**  
- **ChromeDriver**  
- **Page Object Model (POM)**

---

## ▶️ How to Run

1️⃣ Clone the repository:
```bash
git clone https://github.com/celiapaivab/QA-Brazil_Python_Automation
cd QA-Brazil_Python_Automation
```

2️⃣ Create and activate a virtual environment:
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate
```

3️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```

4️⃣ Run the tests:
```bash
pytest test_urban_routes.py
```

---

## 🧾 Results

- Successfully automated the ride request flow in Urban Routes  
- Tests covered critical steps including route setup, plan selection, phone number input, payment, comments, and additional items  
- Complete flow finalized with car search initiation  
- Scripts organized by pages (POM) with best practices for stability and maintainability
- No real bugs were detected during execution, as this project’s primary goal was to design and validate the automation framework for practice purposes only

---

## 📚 What I Learned

- Hands-on practice with end-to-end test automation using **Selenium WebDriver** and **Python**  
- Application of the **Page Object Model (POM)** to improve code maintainability and readability  
- Use of **WebDriverWait** to handle dynamic elements reliably  
- Modular structure for scalable and maintainable automated tests

---

## 💡 Future Improvements

- Add more alternative scenarios (input errors, route cancellation, edge cases)  
- Implement cross-browser testing  
- Integrate the test suite with CI/CD pipelines (e.g., GitHub Actions)  
- Add automatic generation of test execution reports

---

## ✅ Notes

- The **Urban Routes** server must be running for the tests to execute correctly.  
- The project uses Chrome performance logs to automatically capture the SMS code.  
- It is recommended to use a **ChromeDriver** version that matches the installed Chrome browser.
