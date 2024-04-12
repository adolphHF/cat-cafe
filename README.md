This is a webpage example for a cat cafe with basic functions, like visit the restaurant menu, adopt and view the cats searching a family.
Currently exists two diferent views, one for admin and one for visitors.

Technologies used:
-flask v3.0.X
-python v3.0
-sqlite3

Definitions for project layout
flaskr/, a Python package containing your application code and files.
database/, a directory used for all related to creating and managing db.
repository/, a directory used for all related to queries
routes/, a directory to create routes
templates/, a directory containing the html files
static/, directory containing css an js files used in html files
tests/, a directory containing test modules.
.venv/, a Python virtual environment where Flask and other dependencies are installed



Project Layout:
/catCafe
├── flaskr/
│   ├── __init__.py
│   ├── database/
│   ├── repository/
│   ├── routes/
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── blog/
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── .venv/
├── pyproject.toml


main.py is responsible of execute the flask project, taking from routes/blueprint the corresponding routes
