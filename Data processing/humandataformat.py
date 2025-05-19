#https://github.com/sstepput/Avalon-NLU/tree/main

 #Avalon-NLU-main/dataset
import json
import os
import pandas as pd

def read_json(path):
    with open(path, mode="r", encoding="utf-8") as f:
        json_data = json.load(f)
        f.close()
    return json_data

# python humandataformat.py 
# git clone https://github.com/sstepput/Avalon-NLU.git
reformattedDataset = []
fileList  = os.listdir("Avalon-NLU/dataset/") 
print(fileList )
print(len(fileList) )

#print(fileInfo["messages"])
def matchMids(msgs, persuasion, file):
    for m in msgs:
        msg = msgs.get(m)
        
        
        for d in persuasion:
            dec = persuasion.get(d)

            

            if msg.get("mid") == dec.get("mid"):
                msg['file'] = file
                if dec.get("deception") != None:
                    print(dec)
                    dec['label'] = "D"
                else: 
                    dec['label'] = "T"
                    dec.update({'deception': 'none'})


#                print(msgs.get(m) )
                #print(m.get("mid"))
#                print(dec )
                reformattedDataset.append(dict(dec,**msg))


for file in fileList :
    fileInfo = read_json("Avalon-NLU/dataset/"+ file)
    msgs = fileInfo["messages"]
    persuasion = fileInfo["persuasion"]

    matchMids(msgs, persuasion, file)

print(len(reformattedDataset))
print(reformattedDataset)
df = pd.DataFrame(reformattedDataset)
print(df)
df.to_csv('humanLogs.csv', sep='\t')
#df.to_json('humanLogs.json')