#!/bin/bash
source $HOME/bin/script-settings-INSERT_PROJECTNAME.sh
BACKUPFOLDER='backups_locale_'$PROJECTNAME
mkdir -p $HOME/$BACKUPFOLDER

KEEP=60
BACKUPS=`find $HOME/$BACKUPFOLDER -name "locale-*.tgz" | wc -l | sed 's/\ //g'`
while [ $BACKUPS -ge $KEEP ]
do
ls -tr1 $HOME/$BACKUPFOLDER/locale-*.gz | head -n 1 | xargs rm -f
BACKUPS=`expr $BACKUPS - 1`
done

DATE=`date +%Y%m%d%H%M%S`
rm -f $HOME/$BACKUPFOLDER/.locale-${DATE}.tgz_INPROGRESS
tar -cvzpf $HOME/$BACKUPFOLDER/.locale-${DATE}.tgz_INPROGRESS ~/webapps/$DJANGO_APP_NAME/myproject/locale
mv -f $HOME/$BACKUPFOLDER/.locale-${DATE}.tgz_INPROGRESS $HOME/$BACKUPFOLDER/locale-${DATE}.tgz
exit 0
