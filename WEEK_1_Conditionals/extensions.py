def main():
    file = input("Enter the file name: ").lower().strip()
    if file[-3:] == "gif":
        print("image/gif")
    elif file[-3:] == "jpg" or file[-4:].lower() == "jpeg":
        print("image/jpeg")
    elif file[-3:] == "png":
        print("image/png")
    elif file[-3:] == "pdf":
        print("application/pdf")
    elif file[-3:] == "txt":
        print("text/plain")
    elif file[-3:] == "zip":
        print("application/zip")
    else:
        print("application/octet-stream")


main()
