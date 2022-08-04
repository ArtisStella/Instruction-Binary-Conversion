operations = {"add": "0001", "sub": "0010", "equal": "0011", "nequal": "0100", "gequal": "0101", "lequal": "0110", "reg1": "1000", "reg2": "1001"}

data = {'reg1': 0, 'reg2': 0}

filePath = "instructions.txt"

def main():
    with open(filePath) as inFile:
        content = inFile.read().split('\n')
        
        first2Lines = content[:2]
        for line in first2Lines: 
            line = line.split() 
            if line[0] in data.keys():
                data[line[0]] = int(line[1])
        # print(data)
        assert sum(data.values()) < 15, "Data Invalid"    
        
        binaryOut = ""
        for line in content:
            line = line.split()
            for word in line:
                if word in operations.keys():
                    binaryOut += operations[word] + " "
                elif word in data.keys():
                    binaryOut += "{:04b}".format(data[word]) + " "
                else:
                    binaryOut += "{:04b}".format(int(word)) + " "
            binaryOut += "\n"
        print(binaryOut)
        
        
if __name__ == "__main__":
    main()