import mysql.connector


def login(host_name, user_name, user_password, db_name):


    connection = mysql.connector.connect(
        host=host_name,
        user=user_name,
        passwd=user_password,
        database=db_name
        )
    print("Connection to MySQL DB successful")
    cursor=connection.cursor()
    query="SELECT * FROM world.signup;"
    cursor.execute(query)
    result=cursor.fetchall()
    connection.close()
    return(result)


def sign(host_name, user_name, user_password, db_name,fn,us,em,ps):
    connection = mysql.connector.connect(
        host=host_name,
        user=user_name,
        passwd=user_password,
        database=db_name
        )
    print("Connection to MySQL DB successful")
    cursor=connection.cursor()
    query="INSERT INTO `world`.`signup` (`Full Name`, `UserName`, `Email`, `Password`) VALUES (%s,%s,%s,%s);"
    val=fn,us,em,ps
    print(val)
    cursor.execute(query,val)
    connection.commit()
    connection.close()


