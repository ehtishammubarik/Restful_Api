import sqlite3
import os
import sys


class File(object):

    def __init__(self):
        self.file_name = []

    def load_directory(self, path='C:/Users/isamirkhaan/Downloads/Restful_Api/Restful_Api/Restful_Api/api/pdf'):
        """
        :param path: Provide Path of File Directory
        :return: List of pdf File Names
        """
        for x in os.listdir(path):
            self.file_name.append(x)

        return self.file_name

    def create_database(self, name, file):
        """
        :param name: String
        :param file:  BLOP Data
        :return: None
        """

        conn = sqlite3.connect("pdf.db")
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS pdf_table 
        (name TEXT,file BLOP)""")

        cursor.execute(""" INSERT INTO pdf_table 
        (name, file) VALUES (?,?)""", (name, file))

        conn.commit()
        cursor.close()
        conn.close()


def main():
    obj = File()
    os.chdir("C:/Users/isamirkhaan/Downloads/Restful_Api/Restful_Api/Restful_Api/api/pdf")
    file_names = []
    for x in obj.load_directory():

        if ".pdf" in x:
            file_names.append(x)
            with open(x, "rb") as f:
                data = f.read()
                obj.create_database(name=x, file=data)
                print("{} Added to database ".format(x))
    return file_names




def fetch_data():
    counter = 1
    os.chdir("C:/Users/isamirkhaan/Downloads/Restful_Api/Restful_Api/Restful_Api/api/pdf")
    conn = sqlite3.connect("pdf.db")
    cursor = conn.cursor()

    data = cursor.execute("""SELECT * FROM pdf_table""")
    for x in data.fetchall():
        print(x[1])
        with open("{}.pdf".format(counter), "wb") as f:
            f.write(x[1])
            counter = counter + 1

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
