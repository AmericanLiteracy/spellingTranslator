# Convert dictionary csv file to python dictionary and pickle
import pickle

fileNameIn = 'dictionaries/soundSpel/soundSpelWurdList.csv'
fileNameOut = 'dictionaries/soundSpel.pickle'
fileNameOutcsv = 'dictionaries/twoColSoundSpel.csv'

fileIn = open(fileNameIn, 'r')
fileOutcsv = open(fileNameOutcsv, 'w')

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
        lineOut = ','.join((row[0],row[1]))+'\n'
        fileOutcsv.write(lineOut)

fileOutcsv.close
pickle.dump(ss, open(fileNameOut, 'wb' ) )


## Open file of entries for American (reform) spelling.
#t0 = time.time()
#dictFileName = 'DIAMBG'
#f = open(dictFileName, 'r')
#rawString = f.read()
#f.close()
#
## Create a python dictionary relating each
## standard word and it's reform version
#a = rawString.split()
#standardToReform = {}
#for i in range(int(len(a)/2)):
#    standardToReform[a[2*i]] = a[2*i+1]
#
#t1 = time.time()
#print('dictionary read and create:',t1-t0)
#pickle.dump( standardToReform, open( dictFileName+'.p', 'wb' ) )
