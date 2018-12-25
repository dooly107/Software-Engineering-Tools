from localBank import *

def loadBankData(dataFileName):
    filedir = "labfiles/"+dataFileName
    with open(filedir, 'r') as myFile:
        lines = myFile.readlines()
        for i in range(3,len(lines)):
            detail = lines[i].split('|')
            name = detail[0].split()
            firstname = name[0].strip()
            lastname = name[1].strip()
            accountID = detail[1].strip()
            trans = detail[2].strip()
            person = Person.__init__(firstname,lastname)
            bank = Bank.__init__()

def getTotalBalanceByPerson(bank, person):
    pass

def getBalances(bank):
    pass

if __name__ == "__main__":
    loadBankData("transactions.txt")