# SVAR. A new fast and lite data type. Created by Jake.

def loads(data, strip_white_space=True):
    '''Loads SVAR data into a dict() format.'''
    comment = "#"
    splitter = ":"
    data_parsed = dict()
    for line in data.split("\n"):
        if line.startswith(comment):
            pass
        elif line == "":
            pass
        elif not splitter in line:
            raise Exception("File not formatted properly.")
        else:
            title = line.split(splitter)[0]
            data = splitter.join(line.split(splitter)[1:len(line)-1])
            if strip_white_space:
                title = title.lstrip(' ').rstrip(' ')
                data = data.lstrip(' ').rstrip(' ')
            if data == "":
                data = None
            elif data.isdigit():
                data = int(data)
            elif data.lower() == "true":
                data = True
            elif data.lower() == "false":
                data = False
            data_parsed[title] = data
    return data_parsed
# Loads the data into a dict() type.

def load(data, strip_white_space=True):
    '''Similar to svar.loads but allows you to load from a text file.'''
    return loads(data.read(), strip_white_space)
# Loads data from a text file.
