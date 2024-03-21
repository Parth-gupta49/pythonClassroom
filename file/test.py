try:
    # Read Only mode ('r')
    with open("test.txt","r") as f:
        data = f.read()
        print("Read Only Mode:\n",data)
    
    # Read and Write mode ('r+')
    with open("test.txt","r+") as f:
        data = f.read()
        print("\nRead and Write Mode:\n",data)
        f.write("\nHey mate!")
        f.seek(0)
        data = f.read()
        print(data)
    
    # Write Only mode ('w')
    with open("test.txt","w") as f:
        f.write("Hey mate!")
    
    # Write and Read mode ('w+')
    with open("test.txt","w+") as f:
        f.write("Hey mate!")
        f.seek(0)
        data = f.read()
        print("\nWrite and Read Mode:\n",data)
    
    # Append Only mode ('a')
    with open("test.txt","a") as f:
        f.write("\nHey mate!")
    
    # Append and Read mode ('a+')
    with open("test.txt","a+") as f:
        f.write("\nHey mate!")
        f.seek(0)
        data = f.read()
        print("\nAppend and Read Mode:\n",data)
    
    # File operation using split()
    with open("test.txt","r") as f:
        data = f.read()
        split_data = data.split("\n")
        print("\nFile data after split:\n",split_data)
    
    # File operation using seek()
    with open("test.txt","r") as f:
        f.seek(10)
        data = f.read()
        print("\nFile data after seek(10):\n",data)
    
      # File operation using writinglines()
    with open("test.txt","r") as f:
        data = f.readlines()
    with open("BCA_copy.txt","w") as f:  # Corrected filename here
        f.writelines(data)

    
    # File operation using exception handling
    try:
        with open("non_existent_file.txt","r") as f:
            data = f.read()
    except FileNotFoundError:
        print("\nFile not found!")
    
    # File operation using tell()
    with open("test.txt","r") as f:
        f.seek(10)
        location = f.tell()
        print("\nCurrent file location after seek(10):",location)
except Exception as e:
    print("An error occurred:", str(e))
