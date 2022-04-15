def ReadFromFile(fileNameWithExtension):
    """
    Reads a File
    Args:
        fileNameWithExtension: Name of File
    Outputs:
        Stdout/Stderr
    Returns:
        None
    Raises:
        None
    """
    with open(fileNameWithExtension, 'r') as OpenedFile:
        print(OpenedFile.read())
        
def WriteToFile(fileNameWithExtension, stringToWrite):
    """
    Write stringToWrite in a File, even if file does not exist
    Args:
        fileNameWithExtension: Name of File
        stringToWrite: string to be writtent to the file
    Outputs:
        Stdout/Stderr
    Returns:
        None
    Raises:
        None
    """
    with open(fileNameWithExtension, 'a+') as OpenedFile:
        OpenedFile.write(stringToWrite)

if __name__ == '__main__':
    ReadFromFile("test.txt")
    WriteToFile("write1.text", "Hello, World!")