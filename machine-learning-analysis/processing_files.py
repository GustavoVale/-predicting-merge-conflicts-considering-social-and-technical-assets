def get_file_content(file_name):
    """
    Returns the content of a file
        
        Parameters:
            file_name (str): name of file

        Returns:
            File content
    """
    try:
        f = open(file_name)
        return f.read()

    except:
        print('Failing opening file')
        raise 