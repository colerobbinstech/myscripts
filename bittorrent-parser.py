captureset = {}

with open("stack.out") as f:
    for l in f:
        #Each line will contain 1 or more indices that are comma separated followed by a + then the comma separated data
        split = l.rsplit('+') #Separate indices from data
        idxes = split[0].rsplit(',') #Will turn any number of indices into a list of them
        datas = split[1].rsplit(',') #Will turn any
        for index in range(len(idxes)):
            idx = idxes[index]
            datum = datas[index]
            if(datum[-1] == '\n'):
                datum = datum[:-1]
            captureset[idx] = datum #Set each index to the data, stripping the newline character at the end


#Now need to output everything to a file
with open("parsed.out2", 'w') as f:
    for num in range(8460): # I knew this was close. Could be set higher if unknown
        padded_hex = f"{num:#0{10}x}" #takes int and pads to length of 10 including 0x at start to match given idx
        data = captureset.get(padded_hex,'') #if index does not exist, just append blank string
        if(data == ''):
            print("Error at %d" % num) #just for bug testing
        f.write(data)
