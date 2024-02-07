import csv
import sqlite3

def main():
    with sqlite3.connect("tp08/users_db.db") as con:
        cur = con.cursor()

        with open('tp08/MOCK_DATA.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                sql = """
                    INSERT INTO users_tbl(first_name,last_name,gender,email,ip_address) VALUES
                  
                              (?,?,?,?,?)"""
                values = [
                    row['first_name'],
                    row['last_name'],
                    row['gender'],
                    row['email'],
                    row['ip_address']]
                cur.execute(sql,values)




if __name__=='__main__':
    main()
