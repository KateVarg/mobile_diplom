# Дипломный проект QA.GURU (mobile-тестирование)

Данный репозиторий содержит проект - mobile-тестирование для мобильного приложения Wikipedia. Данный проект является частью дипломной работы, выполненной в рамках обучения на курсах QA.GURU. Проект разработан с целью продемонстрировать полученные навыки и знания в области тестирования программного обеспечения.

## Используемые инструменты
<div>
<img src="https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png" title="python" alt="python" width="40" height="40"/>&nbsp
<img src="https://user-images.githubusercontent.com/25181517/184117132-9e89a93b-65fb-47c3-91e7-7d0f99e7c066.png" title="pytest" alt="pytest" width="40" height="40"/>&nbsp
<img src="wikipedia_app_tests/resources/appium.png" alt="Appium" title="Appium" width="40" height="40"/>&nbsp
<img src="wikipedia_app_tests/resources/android_studio.png" width="40" height="40"  alt="Android studio" title="Android Studio"/>&nbsp
<img src="https://img.icons8.com/?size=100&id=3tC9EQumUAuq&format=png&color=000000" title="github" alt="github" width="40" height="40"/>&nbsp
<img src="https://user-images.githubusercontent.com/25181517/179090274-733373ef-3b59-4f28-9ecb-244bea700932.png" title="jenkins" alt="jenkins" width="40" height="40"/>&nbsp
<img src="https://camo.githubusercontent.com/501c9d05b6660ba5e1a8753b8461e60d7ff1614656102c254ab800e14a6b19fa/68747470733a2f2f616c6c7572657265706f72742e6f72672f7075626c69632f696d672f616c6c7572652d7265706f72742e737667" title="allure" alt="allure" width="40" height="40"/>&nbsp
<img src="wikipedia_app_tests/resources/AllureTestOps.png" width="40" height="40"  alt="Allure TestOps"/> 
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pycharm/pycharm-original.svg" title="pycharm" alt="pycharm" width="40" height="40"/>&nbsp
<img src="https://cdn-icons-png.flaticon.com/512/2111/2111646.png" title="telegram" alt="telegram" width="40" height="40"/>&nbsp
</div>

## Список автоматизированных тест-кейсов:
1. Переход по страницам на приветственном экране
2. Успешный поиск статьи
3. Неуспешный поиск статьи
4. Открытие статьи из результатов поиска

## Запуск тестов и получение отчета

### **Локально**

<summary>1. Открыть Android Studio и запустить эмулятор</summary>

<summary>2. В терминале запустить Appium</summary>

<details><summary>3. Склонировать репозиторий</summary>

```
git clone https://github.com/KateVarg/mobile_diplom
```
</details>

<details><summary>4. Установить зависимости и запустить тесты</summary>

```
python -m venv .venv
source .venv/bin/activate
pip install poetry
poetry install
pytest --context=emulator
```
</details>

<details><summary>5. Получить отчет о прохождении тестов в allure</summary>

```
allure serve allure-results/
```
</details>

<details><summary>6. После выполнения команды откроется браузер с отчетом</summary>
    
<img src="wikipedia_app_tests/resources/allure.png">

</details>

### **Удалённо**

Удаленный запуск автотестов осуществляется при помощи Jenkins. Все тесты выполняются на облачной платформе BrowserStack. Для запуска тестов необходимо выполнить следующие действия:

1. Открыть [проект на Jenkins](https://jenkins.autotests.cloud/job/mobile_diplom/)

<details><summary>2. Нажать на Build now</summary>

<img src="wikipedia_app_tests/resources/jenkins1.png">

</details>

<details><summary>3. Дождаться окончания выполнения автотестов и нажать на иконку allure <img src="https://camo.githubusercontent.com/501c9d05b6660ba5e1a8753b8461e60d7ff1614656102c254ab800e14a6b19fa/68747470733a2f2f616c6c7572657265706f72742e6f72672f7075626c69632f696d672f616c6c7572652d7265706f72742e737667" title="allure" alt="allure" width="20" height="20"/> для просмотра отчета</summary>

<img src="wikipedia_app_tests/resources/jenkins2.png">

</details>

## <img src="https://camo.githubusercontent.com/501c9d05b6660ba5e1a8753b8461e60d7ff1614656102c254ab800e14a6b19fa/68747470733a2f2f616c6c7572657265706f72742e6f72672f7075626c69632f696d672f616c6c7572652d7265706f72742e737667" title="allure" alt="allure" width="30" height="30"/> Отчет в <a href = "https://jenkins.autotests.cloud/job/mobile_diplom/allure/">Allure report</a>

<details><summary>Основной отчет</summary>

<img src="wikipedia_app_tests/resources/jenkins_base_report.png">

</details>
<details><summary>Тесты</summary>

<img src="wikipedia_app_tests/resources/jenkins_tests.png">

</details>

## <img src="wikipedia_app_tests/resources/AllureTestOps.png" width="30" height="30"  alt="Allure TestOps"/> Отчет в <a href = "https://allure.autotests.cloud/project/4374/dashboards">Allure TestOps</a>

<details><summary>Основной отчет</summary>

<img src="wikipedia_app_tests/resources/testOps_base_report.png">

</details>

<details><summary>Тесты</summary>

<img src="wikipedia_app_tests/resources/testOps_tests.png">

</details>

## **Дополнительно**

Реализована отправка результатов тестирования в Telegram <img src="https://cdn-icons-png.flaticon.com/512/2111/2111646.png" title="telegram" alt="telegram" width="20" height="20"/>  
<details><summary>Пример отчета</summary>

<img src="wikipedia_app_tests/resources/telegram.png" alt="report Telegram">

</details>
