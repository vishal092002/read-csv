import csv
#from Fileutilities.absolutepath import absolutepath
from pathlib import Path

def ClassFactory(class_name, dictionary):
    return type(class_name, (object,), dictionary)



class ReadCSV:
    data = []

    def __init__(self, filepath):
        self.data = []

       # with open(absolutepath(filepath)) as text_data:
        with open(Path(filepath).absolute()) as text_data:

            csv_data = csv.DictReader(text_data, delimiter=',')
            for row in csv_data:
                self.data.append(row)
        pass

    def return_data_as_class(self, class_name):
        objects = []
        for row in self.data:
            objects.append(ClassFactory(class_name, row))
        return objects