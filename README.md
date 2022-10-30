# Selenium.WebDriver.Allure
Автотесты на классическом варианте Selenium WebDriver

Открываем проект в Visual Studio Code
Устанавливаем необходимые модули
pip install pytest
pip install selenium
pip install webdriver_manager
pip install allure-pytest

Тесты находятся в папке tests/

Запуск теста можно осуществить двумя способами: 
1. Через дерево тестов в Visual Studio Code, вкладка TESTING
2. Из командной строки: pytest <название теста>
3. Посмотреть отчёты в Allure, в командной строке:

cd <путь до каталога allure\bin>
(Allure можно скачать по ссылке https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.19.0/allure-commandline-2.19.0.zip)

.\allure.bat

.\allure serve <путь до каталога с результатами>
