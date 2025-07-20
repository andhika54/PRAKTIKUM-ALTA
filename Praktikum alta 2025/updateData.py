import sqlite3

koneksi_ke_DB = sqlite3.connect("cars.db")

k = koneksi_ke_DB.cursor()

k.execute("""
          UPDATE TBcars SET
              price = 20000
              Where
              id = 101
              """)
print(k.fetchall())

koneksi_ke_DB.commit()
koneksi_ke_DB.close()