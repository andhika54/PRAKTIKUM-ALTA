import sqlite3

koneksi_ke_DB = sqlite3.connect("cars.db")

k = koneksi_ke_DB.cursor()

k.execute("""
          DELETE FROM TBcars
          Where
          id = 102
          """)


koneksi_ke_DB.commit()
koneksi_ke_DB.close()