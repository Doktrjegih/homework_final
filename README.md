# Итоговая работа на курсе "Автоматизация тестирования на языке Python"

Для запуска тестов нужно установить зависимости:
* pip install -r requirements.txt

Далее выполнить команду:
* pytest autotests

Также можно передать следующие аргументы:
* --browser - chrome, firefox или opera
* --bv - версия браузера
* --executor - исполнитель, "local" или адрес selenoid-сервера в формате ip:port
* --vnc - включить трансляцию в selenoid UI
* --videos - включать запись видео в selenoid
* --mobile - прогон на мобильной версии браузера (только chrome)
* --headless - запуск браузера в headless-режиме (без окна)

Результат прогона сохраняется в директории allure-result и доступен для просмотра
при помощи команды:
* allure serve allure-result

Для проверки качества кода можно установить инструменты разработчика:
* pip install -r requirements.dev.txt

И далее после изменения кода выполнить команду:
* make format lint