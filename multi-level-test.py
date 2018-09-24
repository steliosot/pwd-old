import json, csv
def main():
    '''
    importing
    JSON / CSV, data, with eval, no json
    '''

    file_name = 'YOUR_DIRECTORY/sample-multi-level.json'

    get_data(file_name)


def get_data(file_name):
    '''
    gets data from multi level files
    '''
    data = ''

    with open(file_name, "r") as data_file:
        # read the file
        data = eval(data_file.read())

        # iterate the first level as key,value pair
        for key, value in data.items():
            print(key, ":", value)

            # iterate the data from the values of first level
            for vs in value:
                # extract values and keys at this level
                for k, v in vs.items():
                    print(k, ":", v)

main()
