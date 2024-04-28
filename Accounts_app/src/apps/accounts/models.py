from db_config import create_connection_pool


# migrations here :
def create_user_table():
    try:
        connection_pool=create_connection_pool()
        connection = connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE users (first_name varchar(250),"
                       "last_name varchar(250),"
                       "phone_number varchar(11) NOT NULL,"
                       "password varchar(255),"
                       "PRIMARY KEY (phone_number));")
        print("table create successfully!")
        connection.close()
    except Exception as e:
        print(str(e))
        connection.close()


def main():
    create_user_table()


# model methods here:
def is_user_exists(phone_number):
    try:
        connection_pool=create_connection_pool()
        connection=connection_pool.get_connection()
        cursor=connection.cursor()
        cursor.execute(f"""
        SELECT * FROM users WHERE(phone_number={phone_number});
        """)
        result=cursor.fetchall()
        connection.close()
        return result
    except Exception as e:
        print(str(e))
        connection.close()