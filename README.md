# Annotation tool

## Backend

### Running the project locally

1. Install Python3 (>=3.6 <=3.8.6)

2. Go to the `backend` dir, create a virtual environment and activate it.
You can follow this [guide](https://docs.python.org/3/library/venv.html)

3. Install libraries by running:

```bash
pip install -r requirements.txt
```

4. You need to intall mysql locally. Project works with version 8.

5. Update your string connection in `backend/app/main/config.py` accordingly.

6. Run migrations as detailed in Migration section.

7. To run the project execute this at root `/backend` level:

```bash
python manage.py run
```

### Making migrations
1. Create a migration script from the detected changes in the model using the migrate command. This doesn’t affect the database yet.

```bash
python manage.py db migrate --message 'initial database migration'
```

2. Apply the migration script to the database by using the upgrade command

```bash
python manage.py db upgrade
```
3. To undo the last migration run:

```bash
python manage.py db upgrade
```

## Frontend

1. Install angular-cli following [this guide](https://angular.io/guide/setup-local)

2. Go to `administracion` and run:

```bash
npm install
```
3. To start the website run:

```bash
ng serve
```

### Notes:
1. do the same with the `visualizacion`

2. If you want to run both projects at the same time you should specify a different
port when running the third step, ie: `ng serve --port=4201`
