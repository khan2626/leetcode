def calpoints(ops: list):

    record = []

    for i in range(len(ops)):
        
        if ops[i] == "C":
            record.pop()  
        elif ops[i] == "D":
            record.append(2 * record[-1])  
        elif ops[i] == "+":
            record.append(record[-1] + record[-2])  
        else:
            record.append(int(ops[i]))  
    
    return sum(record)
print(calpoints(["5", "2", "C", "D", "+"]))
print(calpoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))
