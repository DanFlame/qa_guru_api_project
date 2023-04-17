## Проект API автотестов

<!-- Технологии -->

### Используемые технологии
<p  align="center">
  <code><img width="5%" title="Pycharm" src="./attachments/logo/pycharm.svg"></code>
  <code><img width="5%" title="Python" src="./attachments/logo/Python-logo-notext.svg"></code>
  <code><img width="5%" title="Pytest" src="./attachments/logo/pytest.png"></code>
  <code><img width="5%" title="Selene" src="./attachments/logo/selene.png"></code>
  <code><img width="5%" title="GitHub" src="./attachments/logo/git-logo.svg"></code>
  <code><img width="5%" title="Allure Report" src="./attachments/logo/allure-Report-logo.svg"></code>
  <code><img width="5%" title="Jenkins" src="./attachments/logo/jenkins-logo.svg"></code>
  <code><img width="5%" title="Requests" src="./attachments/logo/requests.png"></code>
  <code><img width="5%" title="Selenoid" src="./attachments/logo/selenoid-logo.svg"></code>
  <code><img width="5%" title="Requests" src="./attachments/logo/Telegram.svg"></code>
</p>

### Что проверяется в тестах:
#### Для сайта reqres.in:
- [x] Успешное создание пользователя
- [x] Успешное обновление данных пользователя методом PATCH
- [x] Успешное обновление данных пользователя методом PUT
- [x] Успешное удаление пользователя
- [x] Успешная регистрация
- [x] Безуспешная регистрация из-за отсутствия пароля
- [x] Безуспешная регистрация из-за отсутствия электронной почты
#### Для сайта demowebshop.tricentis.com:
- [x] Успешный логин
- [x] Успешный логин посредством апи
- [x] Добавление товара в Корзину
- [x] Добавление товара в Желаемое
- [x] Удаление товара из Корзины
- [x] Удаление товара из Желаемого


В проекте используется встроенный logger:
![This is an image](attachments/screenshot/logger.jpg)

<!-- Jenkins -->

### <img width="3%" title="Jenkins" src="attachments/logo/jenkins-logo.svg"> Запуск проекта в Jenkins

### [Job](https://jenkins.autotests.cloud/job/fazylov_api_project/)

##### При нажатии на кнопку "Собрать сейчас" начинается сборка тестов и их прохождение
![This is an image](attachments/screenshot/jenkins.jpg)

<!-- Allure report -->

### <img width="3%" title="Allure Report" src="attachments/logo/allure-Report-logo.svg"> Allure report

##### После прохождения тестов, результаты автоматически сохраняются. Чтобы посмотреть Allure отчет, нужно нажать на иконку allure report у сборки.
![This is an image](attachments/screenshot/allure.jpg)

##### Во вкладке Suites находятся подробные данные о прохождении теста с приложенными логами и скриншотами/видео о прохождении
![This is an image](attachments/screenshot/allure_suites.jpg)

##### Видео-прохождение теста
![This is an image](attachments/video/selenoid.gif)

##### В канал в мессенджере telegram приходит краткая версия отчёта с ссылкой на полноценную версию в аллюре
![This is an image](attachments/screenshot/telegram_report.jpg)
