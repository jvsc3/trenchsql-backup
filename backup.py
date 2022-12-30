import os
import time
import datetime

MYSQL_HOST = "localhost"
MYSQL_USERNAME = "root"
DATABASE_NAME = "trenches"
BACKUP_DIRECTORY = "~/Desktop"
BACKUP_INTERVAL = 43200 # 12 saat

while True:
    now = datetime.datetime.now()
    filename = f"{DATABASE_NAME}_{now:%Y-%m-%d_%H-%M-%S}.sql"
    filepath = os.path.join(BACKUP_DIRECTORY, filename)

    command = f"mysqldump -h {MYSQL_HOST} -u {MYSQL_USERNAME} {DATABASE_NAME} > {filepath}"
    os.system(command)

    time.sleep(BACKUP_INTERVAL)
