import sys

# python main.py 0 va tester en utilisant A-small-practice.in
#                1                        A-large-practice.in

files = [
    "A-small-practice.in",
    "A-large-practice.in"
]

# Lit le fichier et retourne le tableau des cas
def getFileData():
    fileId = int(sys.argv[1])
    data = open(files[fileId]).read().splitlines()
    
    # Get each case as a list of its own
    data = chunks(data[1:], 3)
    cases = []
    
    for case in data:
        cases.append({'initials': case[1].split(' '), 'target': case[2].split()})
    
    return cases

# Separates list l in chunks of n length
# Returns a list of lists, each sublist having n length
def chunks(l, n):
    n = max(1, n)
    return [l[i:i + n] for i in range(0, len(l), n)]
def flip(case,index):
    print(case)
    if case['initials'][index] == '1':
        s = list(case['initials'][index])
        s[index] ='0'
        case['initials'][index] = "".join(s)
    else:
        s = list(case['initials'][index])
        s[index] ='0'
        case['initials'][index] = "".join(s)
    print(case)
    return

# LOLOLOL YA RIEN DE FAIT
def resolveCase(case, flips):
    for i in range(len(case['initials'])) :
        outlet = case['initials'][i]
        target = case['target'][i]
        # Si le outlet est pas dans les targets, on a pas encore la solution
        if outlet != target:
            flip(case,i)
            return resolveCase(case, flips+1)
        
        # Si tous les initials existent dans le target, on a la bonne solution donc on arrête de flipper
        return flips

def main():
    data = getFileData()
    # print data

    for i in range(len(data)):
        case = data[i]
        answer = resolveCase(case, 0)

        print ("Case #" + str(i) + ": " + str(answer))
    
if __name__ == "__main__":
    main()