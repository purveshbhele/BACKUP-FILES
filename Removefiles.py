import os
import time
import shutil
def main() :
    del_folders = 0
    del_files = 0
    path = input("Enter the path :- ")
    days = int(input("Enter number of Days: "))
    total_seconds = time.time() - (days * 24 * 60 * 60)
    print("Total number of seconds: ","%d"%(total_seconds))
    if os.path.exists(path):
        for root_folder,folders,files in os.walk(path):
            if total_seconds >= get_file_age(root_folder):
                remove_folder(root_folder)
                del_folders = del_folders + 1
            else :
                for folder in folders :               
                   folder_path = os.path.join(root_folder,folder)
                   if total_seconds >= get_file_age(folder_path):
                       remove_folder(folder_path)
                       del_folders = del_folders + 1
                for file1 in files : 
                    file_path = os.path.join(root_folder,file1)

                    if total_seconds >= get_file_age(file_path):
                      remove_file(file_path)
                      del_files = del_files + 1
    else:
        print(" Path does not exist")
    print(f"deleted files:{del_files}")
    print(f"deleted foldes:{del_folders}")
def remove_folder(path):
	if not shutil.rmtree(path):
		print(f"{path} is removed successfully")
	else:
		print(f"Unable to delete the "+path)
def remove_file(path):
	if not os.remove(path):
		print(f"{path} is removed successfully")
	else:
		print("Unable to delete the "+path)
def get_file_age(path):
	ctime = os.stat(path).st_ctime
	return ctime
if __name__ == '__main__':
	main()
