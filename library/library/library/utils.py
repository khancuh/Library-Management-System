# library/utils.py
import MySQLdb

def connect_to_newdb():
    db = MySQLdb.connect(
        host="localhost",
        user="imran",  # Replace with your actual database user
        passwd="Hello123456",  # Replace with your actual database password
        db="newdb"  # The name of your database
    )
    return db
