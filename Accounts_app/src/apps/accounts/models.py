from db_config import create_connection_pool

def create_user_table():
    try:
        connection_pool=create_connection_pool()
        connection=connection_pool.get_connection()
        cursor=connection.cursor()
        cursor.execute("CREATE TABLE users3 (id int , first_name varchar(250) ,"
                       " phone_number varchar(11));")
        print("table create successfully!")
        connection.close()
    except Exception as e:
        print(str(e))
        connection.close()


def main():
    create_user_table()