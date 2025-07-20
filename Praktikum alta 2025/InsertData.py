import sqlite3

koneksi_ke_DB = sqlite3.connect("cars.db")

k = koneksi_ke_DB.cursor()

k.execute("""
          INSERT INTO TBcars(
              id,
              name,
              brand,
              model,
              price
        )
        VALUES(
            '101',
            'Red Car',
            'Honda',
            'CRV',
            12000
        )    
          """)

koneksi_ke_DB.commit()
koneksi_ke_DB.close()