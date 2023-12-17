# Cервис YaCut

Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

###  Установка и настройки
  * Шаг первый: клонируем репозиторий
```python
git clone git@github.com:Nurbek878/yacut.git
```
 * Переходим в папку с проектом 
```sh 
cd yacut
``` 
* Создаем и активируем виртуальное окружение 
```sh 
python -m venv venv 
source venv/bin/activate 
``` 
* Обновляем менеджер пакетов pip
```sh 
pip install --upgrade pip 
``` 
* Устанавливаем необходимые зависимости 
```sh 
pip install -r requirements.txt
``` 
* В корне проекта создаем .env файл
```sh 
FLASK_APP=yacut
FLASK_ENV=development
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=YOUR_SECRET_KEY
``` 
* Создаем файл базы данных и таблицы в нем
```sh 
flask shell
>>> from yacut import db
>>> db.create_all()
``` 
* Запускаем Flask-приложение командой
```sh 
flask run
``` 

### Стек
-   [Python](https://www.python.org/)
-   [Flask](https://flask.palletsprojects.com/)
-   [SQLAlchemy](https://www.sqlalchemy.org/)

### Автор

- [@nurbek878](https://github.com/Nurbek878)