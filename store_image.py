import gridfs.errors
from pymongo import MongoClient
from dotenv import load_dotenv
from bson import ObjectId
import os
import gridfs
import time

load_dotenv()

mongodb_url = os.getenv("MONGODB_URL")

try:
    client = MongoClient(mongodb_url, tlsAllowInvalidCertificates=True)
except Exception as e:
    f"Esception:{e}"
db=client["ytmanager"]

fs = gridfs.GridFS(db)

def create_image(path):
    image_path=path

    with open(image_path,'rb') as image_file:
        file_id=fs.put(image_file,filename = 'test.jpg')

    print(f"File created !! {file_id}")

def show_all_images():
    for image in fs.find():
        print(f"id: {image._id}, filename: {image.filename}")

def retreve_image(file_id):
    try:
        get_file=fs.get(ObjectId(file_id))
    except Exception as e:
        print(e)
    output_path='F:\python_project\output.jpg'

    with open(output_path,'wb') as output_file:
        output_file.write(get_file.read())

    print(f"Image retrieved and saved to: {output_path}")
    return output_path

def delete_file_from_database(file_id):
    for remaining in range(10, 0, -1):
        print(f"File will be deleted in {remaining} seconds", end='\r')
        time.sleep(1)

    print()

    try:
        fs.delete(ObjectId(file_id))
        print("file deleted!!")
    except gridfs.errors.NoFile:
        print("File not found!!")
    except Exception as e:
        print("error occurred!")

def delete_from_computer(output_path):
    try:
        os.remove(output_path)
        print(f"File {output_path} has been deleted.")
    except FileNotFoundError:
        print(f"File {output_path} not found.")
    except PermissionError:
        print(f"Permission denied: {output_path}")
    except Exception as e:
        print(f"Error occurred: {e}")

def main():
    while True:
        print("\n Youtube manager App")
        print("1. Create Image")
        print("2. Show all Images")
        print("3. Retreve a specifc image")
        print("4. Delete a image from database")
        print("5. Delete a image from computer")
        print("6. Exit the app")
        choice = input("Enter your choice: ")

        if choice == '1':
            path = input("Enter the path of the image: ")
            create_image(path)
        elif choice == '2':
            show_all_images()
        elif choice == '3':
            file_id = input("Enter the file id: ")
            output_path=retreve_image(file_id)
        elif choice == '4':
            file_id = input("Enter the file id: ")
            delete_file_from_database(file_id)
        elif choice == '5':
            delete_from_computer(output_path)
        elif choice == '6':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()