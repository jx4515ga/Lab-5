import sqlite3


conn = sqlite3.connect('record_db.sqlite')


def main():
    creating_table()
    insert_data()
    add_new_row_to_records()
    search_by_id_from_records()
    update_by_name_num_of_catches()
    delete_by_record_holder_name()


# creating table if not exists
def creating_table():
  
    
    conn.execute('CREATE TABLE IF NOT EXISTS records(name text , country text, catches int)')
    conn.commit()
    
# inserting data to records table
def insert_data():
    
    conn.execute('INSERT INTO records values(" Janne Mustonen ", "Finland", 98)')
    conn.execute('INSERT INTO records values("Ian Stewart  ", "Canada", 94)')
    conn.execute('INSERT INTO records values("Aaron Gregg ", "Canada", 88)')
    conn.execute('INSERT INTO records values("Chad Taylor", "USA", 78 )')
    conn.commit()
    


#adding new row to records table  
def add_new_row_to_records():
    
    new_name = input('Enter new name: ')
    new_country = input('Enter country: ')
    new_catch = int(input('Enter the number of catches: '))

    conn.execute(f'INSERT INTO records VALUES(?,?,?)', (new_name, new_country, new_catch))
    conn.commit()

#searching by id from the recorda table
def search_by_id_from_records():
    
    serach_by_name = input("Enter the name you want to search: ")
    serach_by_name = conn.execute('select * from records  WHERE  rowid = ? ', ( serach_by_name ,))


    conn.commit()
    

#update by typing the name in the records table
def update_by_name_num_of_catches():
   
    name_to_update = input("Enter the name you want to update: ")
    update_catches = int(input("Enter the number of catches: "))
    update_catches = conn.execute('UPDATE records SET  catches = ? WHERE  name = ? ', ( update_catches, name_to_update))
    
    conn.commit()


# delete by name from records table
def delete_by_record_holder_name():
    
    delete_by_name = input("Enter the name you want to delete: ")
    
    delete_by_name = conn.execute('delete  from records  WHERE name = ? ', (  delete_by_name ,))
    
    conn.commit()
    conn.close()
    


  
    
if __name__ == '__main__':
    main()