# BackupScript
A py backup script that backups up a dir every day, putting the files in a folder with the days date and deletes old backups after 3 days.   
## This is meant for usage with PM2 as the script will stop itself with PM2 by default.
# Setup:
1. Download all the files.
2. Change the values in `backup_func.py` to what you need and change `url = "discord webhook url"` in `main.py` to your Discord Webhook URL.
3. Run this with PM2, assuming you have Python 3 already installed, and the cron time is at which you want it.  
 For example:  
`pm2 start main.py --watch --name="Backup" --interpreter python3 --cron "*0 1 * * *"`
   would run the backup script once a day at 1am.
# Info:
1. The discord webhook is set in the main py file.
2. The amount of days that backups stay before deletion is set in the main file, with the int variable `DELETE_OLD_BACKUPS_AFTER_DAYS`.  


### You can fork and modify this code as you wish, I will update it in this repo as I see fit. Suggestions/Feature requests and bug reports in the GitHub issues, please.