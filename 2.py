import sqlite3

# 从文件中读取数据并保存到列表中
with open('stephen_king_adaptations.txt', 'r') as file:
    stephen_king_adaptations_list = file.readlines()

# 建立与SQLite数据库的连接
conn = sqlite3.connect('stephen_king_adaptations.db')

# 创建一个游标对象
cursor = conn.cursor()

# 创建一个新表
cursor.execute("""
CREATE TABLE stephen_king_adaptations_table (
    movieID TEXT PRIMARY KEY,
    movieName TEXT,
    movieYear INTEGER,
    imdbRating FLOAT
)
""")

# 将列表中的数据插入到表中
# 假设列表中的每一行都是一个电影数据，格式为：movieID, movieName, movieYear, imdbRating
for line in stephen_king_adaptations_list:
    data = line.strip().split(',')
    cursor.execute("INSERT INTO stephen_king_adaptations_table VALUES (?, ?, ?, ?)", data)

# 提交事务
conn.commit()

# 用户交互
while True:
    print("1. Movie name")
    print("2. Movie year")
    print("3. Movie rating")
    print("4. STOP")
    option = input("Select an option: ")
    
    if option == '1':
        movie_name = input("Enter the movie name: ")
        cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieName = ?", (movie_name,))
        result = cursor.fetchone()
        if result:
            print("Movie Details: ", result)
        else:
            print("No such movie exists in our database")

    elif option == '2':
        movie_year = int(input("Enter the movie year: "))
        cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieYear = ?", (movie_year,))
        results = cursor.fetchall()
        if results:
            for result in results:
                print("Movie Details: ", result)
        else:
            print("No movies were found for that year in our database.")

    elif option == '3':
        rating = float(input("Enter the rating: "))
        cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE imdbRating >= ?", (rating,))
        results = cursor.fetchall()
        if results:
            for result in results:
                print("Movie Details: ", result)
        else:
            print("No movies at or above that rating were found in the database.")
            
    elif option == '4':
        break

# 关闭连接
conn.close()