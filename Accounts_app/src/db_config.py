from mysql.connector import pooling
from config import BaseConfig

def create_connection_pool():
    dbconfig=BaseConfig.DB_SETTINGS
    connection_pool=pooling.MySQLConnectionPool(pool_name='account_pool',
                                                pool_size=20,**dbconfig)
    return connection_pool


