import requests
from backup_func import *
from datetime import *
import os, time
import shutil
DELETE_OLD_BACKUPS_AFTER_DAYS= 3 #you can change this if you want
def discordnotify(message):
    url = "discord webhook url"


    data = {
        "content": f"{message}",
        "username": "Backup",
    }


    result = requests.post(url, json=data)
    if 200 <= result.status_code < 300:
        print(f"Webhook sent {result.status_code}")
    else:
        print(f"Webhook not sent with {result.status_code}, response:\n{result.json()}")
today = str(date.today())
now = time.time()
backup_location = "/media/data/Backups"
print(f"{today} and {now}")
directory_contents = os.listdir(backup_location)
print(directory_contents)
print(f"The date today is `{today}`. Comparing the backup folders to today's date.")
list_of_datetimes = []
# delete old backups
for name in directory_contents:
    year, month, day = name.split('-')
    list_of_datetimes.append(datetime(int(year), int(month), int(day)))

today = datetime.now()
discordnotify(f"Checking for backups older than {DELETE_OLD_BACKUPS_AFTER_DAYS} day(s)...")
for date in list_of_datetimes:
    if (today - date).days >= DELETE_OLD_BACKUPS_AFTER_DAYS:
        date = date.strftime('%Y-%m-%d')
        print(date, "is overdue and will be deleted.")
        discordnotify(f"The backup `{date}` is over {DELETE_OLD_BACKUPS_AFTER_DAYS} day(s) old and will be deleted.")
        deletepath = f"{backup_location}/{date}"
        shutil.rmtree(deletepath, ignore_errors=False, onerror=None)
        print("Old backup destroyed!")
    else:
        print("No old backups found.")
        discordnotify(f"No backups were found that were older than {DELETE_OLD_BACKUPS_AFTER_DAYS} day(s), skipping to download.")
'''
for filename in os.listdir(backup_location):
    filestamp = os.stat(os.path.join(backup_location, filename)).st_mtime
    filecompare = now - 3 * 86400
    if  filestamp < filecompare:
        print(filename)
        time.sleep(0.5)
        discordnotify(f"Deleting file: `{filename}.`")
        filepath = f"{os.path.join(backup_location, filename)}"
        try:
            #os.remove(filepath)
            print(f"{now} is now and {filestamp} is file age")
        except PermissionError:
            print("File failed to delete.")
            discordnotify(f"`{filepath}` failed to delete.")
'''
# download backups
try:
    print ("Backup starting.")
    discordnotify(f"Backup starting, the time is currently `{datetime.utcnow()}`")
    backup_func()
    discordnotify(f"Backup completed at `{datetime.utcnow()}`")
    os.system("pm2 stop Backup")
except OSError as err:
    discordnotify(f"Backup failed with error: `{err}`!")
    discordnotify("Trying again...")
    deletepath = f"{backup_location}/{date}"
    shutil.rmtree(deletepath, ignore_errors=False, onerror=None)
    try:
        print("Backup starting.")
        discordnotify(f"Backup starting, the time is currently `{datetime.utcnow()}`")
        backup_func()
        discordnotify(f"Backup completed at `{datetime.utcnow()}`")
        os.system("pm2 stop Backup")
    except:
        discordnotify(f"Backup failed with error: `{err}`!")
        discordnotify("Cancelling the backup.")
        os.system("pm2 stop Backup")