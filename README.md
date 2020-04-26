#### Setup
To install dependencies and enter the pipenv virtual environment:
```bash
pipenv install
pipenv shell
```

To exit the pipenv virtual environment
```bash
exit
```

To initialise the database, use the following commands inside the python interpreter:
```python
from app import db
db.create_all()
```