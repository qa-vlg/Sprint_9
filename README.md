## Проект Авто-тестов [Сервиса Продуктовый помощник](https://foodgram-frontend-1.prakticum-team.ru/ "Продуктовый помощник")
### Реализованные тесты:
1. Создание аккаунта:
  * test_user_sign_up_true
2. Авторизация:
  * test_user_login_valid_data_true
3. Создание рецепта:
  * test_create_recipe_true

### Запустить тесты и сгенерировать Allure отчет из репозитория:
  * `pytest tests/test_view_answer_true.py --alluredir=allure_results` пример запуска индивидуального теста
  * `pytest tests/ --alluredir=allure_results` пример запуска всех тестов последовательно
  * `allure serve allure_results` сгенерировать отчет, при условии что результаты тестов находятся в папке `allure_results`

### Используя Docker:
  * `docker compose up` запустит тесты внутри собранного контейнера

### Реализация CI/CD:
  * `push` в `develop` запустит GitHub Actions пайплайн