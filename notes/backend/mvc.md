MVC - model, view, controller<br>
MVC - UI patter to separate internal representations of data from the ways it is presented to/accepted from the user.
<br>
MVC - образует замкнутый поток управления внутри приложения. 
<h1>Model</h1>
Модель - это сущность для работы с данными. Хранит данные, их целостность и соотвествие между разными моделями и статусом, которое имеет целое приложение в целом.
Модель обрабатывает запросы на чтение и изменение данных. Пример: нельзя сохранить сущность пользователя без e-mail адресса. 
<br>

<h1>View</h1>
Взаимодействие с пользователем. Пользователь - человек, видит через браузер. Пользователь - сервис (микросервис) обращение через jsonAPI. Пользователь работает именно с отображением, не лезет в базу данных. отображения могут быть интерактивные и статичные. 
<br>

<h1>Controller</h1>
Посредник между пользователем, моделью и отображением. "Умный маршрутизатор". Принимает, интерпретирует и валидирует все что вводит пользователь. Создает на основе имеющихся модель отображение и отправляет их пользователю. Принимает от пользователя сообщения и отправляет моделям, вызывая различные методы в моделях или иную бизнес логику. 
<br>

Путь:  пользователь видит отображение (экран, форма) -> отправляет http запрос -> контроллер получает и обрабатывает запрос, интерпритирует его -> Данные, которые ввел пользователь проходят черех защитные конструкции, валидаторы -> запрос превращается в вызов методов в логике приложения -> контроллер вызывает исполнение бизнес логики -> новый статус приложения сохранен в базе данных -> формируется ответ на запрос -> бизнес логика возвращает данные ответа в контроллер ->
контроллер на основании данных формирует и отправляет пользователю отображение модели, которую мы изменили -> отображение показывает пользователю новое состояние модели
<br>

Бизнес логика - обобщенное функциональное наполнение всего приложения.
<br>
http-запрос - stateless запрос 
<br>

По учебнику логика в моделях<br>
Избыточно сложный контроллер - это плохо<br>

