# Selenium.WebDriver.Allure
Автотесты на классическом варианте Selenium WebDriver

1. Открыть проект в Visual Studio Code
2. Установить необходимые модули:

pip install pytest

pip install selenium

pip install webdriver_manager

pip install allure-pytest

3. Открыть файлы в папке tests/

Запуск теста можно осуществить двумя способами: 
- Через дерево тестов в Visual Studio Code, вкладка TESTING
- Из командной строки: pytest <название теста>

4. Скачать Allure по ссылке https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.19.0/allure-commandline-2.19.0.zip
5. Посмотреть отчёты в Allure. Находятся в папке my_allure_resalts
- в командной строке ввести:

cd <путь до каталога allure\bin>

.\allure.bat

.\allure serve <путь до каталога с результатами>
