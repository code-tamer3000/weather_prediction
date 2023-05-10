import get_data
import regresion
import contact
import os

if __name__ == '__main__':
    current_dir = os.getcwd()
    current_dir = current_dir.replace("\\","\\\\")
    get_data.get_data(dir_path=current_dir)
    contact.merge_excel_files(dir_path=current_dir + r'\datatables')
    regresion.make_suggestion(file_path=(current_dir + r'\datatables\database.xlsx'))