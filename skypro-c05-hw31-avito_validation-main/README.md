# SkyPro.Python course
## HW31. Avito - Validation, tests

### Project is ready to start locally

1. Start postgres database `docker-compose up -d`
2. Database is already populated, volume is in /pg_data
3. To access admin
```
user: skypro
password: 1234
```

### To start project from scratch

1. Delete postgres volume (pg_data)
2. Delete migrations from apps (users, ads)
3. Start postgres database `docker-compose up -d`
4. Create fixtures (run csv_to_json script in /data)
5. Load fixtures (in the order showed)
```
./manage.py loaddata locations.json'
./manage.py loaddata users.json'
./manage.py loaddata categories.json'
./manage.py loaddata ads.json'
```

Kirill Paveliev\
August 2022