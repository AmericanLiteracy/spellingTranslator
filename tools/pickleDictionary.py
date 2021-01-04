# Convert dictionary csv file to python dictionary and pickle
import pickle

fileNameIn = 'dictionaries/soundSpel/soundSpelWurdList.csv'
fileNameOut = 'dictionaries/soundSpel.pickle'

fileIn = open(fileNameIn, "r")

# ss is the soundSpel dictionary
ss = {}
header = fileIn.readline()
while(True):
    line = fileIn.readline()
    if not line:
        break
    row = line.split(',')
    # remove letter header entries
    if row[0].count('[') == 0:
        ss[row[0]] = row[1]

pickle.dump(ss, open(fileNameOut, 'wb' ) )
