#!/bin/bash
BACKUP_DIR="/var/backups/postgresql"
DATE=$(date +%Y%m%d%H%M%S)
DB_NAME="mi_base_de_datos"

pg_dump $DB_NAME > $BACKUP_DIR/${DB_NAME}_${DATE}.sql
find $BACKUP_DIR -type f -mtime +7 -exec rm {} \;  # Eliminar backups mayores a 7 días
