# Run the Script - 
#Ensure the malware file is in the same directory.
#Ensure you use the correct file path, since the script deleted the file that was detected.
#Also note that This is a simple pattern matching strategy that might not work every time, 
#particularly if the malware employs obfuscation or if the markers are found in a context that is harmless. 

import os

def isFileMalicious(file_path, mal_signature):
    try:
        # Attempt to open the file for reading
        with open(file_path, "r") as file:
            # Read the content of the file
            file_content = file.read()
            
            # Check for each marker in the malicious signature
            for mal_marker in mal_signature:
                # If a marker is found in the file content, consider it malicious
                if mal_marker in file_content:
                    return True
            
            # If none of the markers are found, the file is not malicious
            return False
    except FileNotFoundError:
        # Handle the case where the file is not found
        print('File not Found')
        return False
    
if __name__ == "__main__":
    # List of markers indicative of malicious content
    mal_signature = ["create_new_malware", "copy_existing_files", ".malware.py", "list_directories", "self.path =path"]

    # Prompt user to enter the file path
    file_path = input("Enter your file path: ")

    # Check if the file is malicious based on the provided signature
    if isFileMalicious(file_path, mal_signature):
        print("Potential Malicious file has been detected.")
        # If malicious, delete the file
        os.remove(file_path)
    else:
        print("File is virus-free.")


    

