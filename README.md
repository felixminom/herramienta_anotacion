# Annotation tool

## Backend

1. Initiate a migration folder using init command for alembic to perform the migrations.

```bash
python manage.py db init
```
2. Create a migration script from the detected changes in the model using the migrate command. This doesn’t affect the database yet.

```bash
python manage.py db migrate --message 'initial database migration'
```

3. Apply the migration script to the database by using the upgrade command

```bash
python manage.py db upgrade
```
