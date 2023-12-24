import re
import random

global randfloor
global randceiling
global randjoin

settings = open("ClothingTweakerStatsRandomizerSettings.txt", "r")
settingcontents = settings.readlines()
settings.close()

randfloor = float(settingcontents[1])
randceiling = float(settingcontents[3])
randtype = settingcontents[5].strip()
randfiles = list(settingcontents[7].strip().split(", "))
print(settingcontents[9])
randcap = settingcontents[9]

def truerandom(filename):
    
    f = open(filename, "r")
    filecontents = f.readlines()
    f.close()    
    numclothing=int((len(filecontents)-2)/7)
    for n in range(numclothing):
        warmth = re.findall(r"(?:\d*\.*\d+)", filecontents[7*n+1])[0]
        rwarmth = float(warmth)*random.uniform(randfloor,randceiling)
        filecontents[7*n+1] = filecontents[7*n+1].replace(str(warmth), str(round(rwarmth,1)))
        
        wetwarmth = re.findall(r"(?:\d*\.*\d+)", filecontents[7*n+2])[0]
        rwetwarmth = float(wetwarmth)*random.uniform(randfloor,randceiling)
        if rwetwarmth > rwarmth and randcap.lower() == "true":
            print("Capping wetwarmth")
            rwetwarmth = rwarmth
        filecontents[7*n+2] = filecontents[7*n+2].replace(wetwarmth, str(round(rwetwarmth,1)))
        
        windproof = re.findall(r"(?:\d*\.*\d+)", filecontents[7*n+3])[0]
        rwindproof = float(windproof)*random.uniform(randfloor,randceiling)
        filecontents[7*n+3] = filecontents[7*n+3].replace(windproof, str(round(rwindproof,1)))
        
        waterproof = re.findall(r"(?:\d*\.*\d+)", filecontents[7*n+4])[0]
        rwaterproof = float(waterproof)*random.uniform(randfloor,randceiling)
        filecontents[7*n+4] = filecontents[7*n+4].replace(waterproof, str(round(rwaterproof,1)))
                
        protection = re.findall(r"(?:\d*\.*\d+)", filecontents[7*n+5])[0]
        rprotection = float(protection)*random.uniform(randfloor,randceiling)
        filecontents[7*n+5] = filecontents[7*n+5].replace(protection, str(round(rprotection,1)))
        
        mobility = re.findall(r"(?:\d*\.*\d+)", filecontents[7*n+6])[0]
        rmobility = float(mobility)*random.uniform(randfloor,randceiling)
        filecontents[7*n+6] = filecontents[7*n+6].replace(mobility, str(round(rmobility,1)))
        
        weight = re.findall(r"(?:\d*\.*\d+)", filecontents[7*n+7])[0]
        rweight = float(weight)*random.uniform(randfloor,randceiling)
        filecontents[7*n+7] = filecontents[7*n+7].replace(weight, str(round(rweight,1)))
    g = open(filename, "w")
    g.writelines(filecontents)

def unifrandom(filename):
  
    numclothing=int((len(filecontents)-2)/7)
    for n in range(numclothing):
        randomscale = random.uniform(randfloor,randceiling)
        warmth = re.findall(r"(?:\d*\.*\d+)", filecontents[7*n+1])[0]
        rwarmth = float(warmth)*randomscale
        filecontents[7*n+1] = filecontents[7*n+1].replace(str(warmth), str(round(rwarmth,1)))
        
        wetwarmth = re.findall(r"(?:\d*\.*\d+)", filecontents[7*n+2])[0]
        rwetwarmth = float(wetwarmth)*randomscale
        filecontents[7*n+2] = filecontents[7*n+2].replace(wetwarmth, str(round(rwetwarmth,1)))
        
        windproof = re.findall(r"(?:\d*\.*\d+)", filecontents[7*n+3])[0]
        rwindproof = float(windproof)*randomscale
        filecontents[7*n+3] = filecontents[7*n+3].replace(windproof, str(round(rwindproof,1)))
        
        waterproof = re.findall(r"(?:\d*\.*\d+)", filecontents[7*n+4])[0]
        rwaterproof = float(waterproof)*randomscale
        filecontents[7*n+4] = filecontents[7*n+4].replace(waterproof, str(round(rwaterproof,1)))
                
        protection = re.findall(r"(?:\d*\.*\d+)", filecontents[7*n+5])[0]
        rprotection = float(protection)*randomscale
        filecontents[7*n+5] = filecontents[7*n+5].replace(protection, str(round(rprotection,1)))
        
        mobility = re.findall(r"(?:\d*\.*\d+)", filecontents[7*n+6])[0]
        rmobility = float(mobility)*randomscale
        filecontents[7*n+6] = filecontents[7*n+6].replace(mobility, str(round(rmobility,1)))
        
        weight = re.findall(r"(?:\d*\.*\d+)", filecontents[7*n+7])[0]
        rweight = float(weight)*randomscale
        filecontents[7*n+7] = filecontents[7*n+7].replace(weight, str(round(rweight,1)))
    g = open(filename, "w")
    g.writelines(filecontents)

for filename in randfiles:
    if randtype.lower() == "true":
        print("True randomizing " + filename)
        truerandom(filename)
    if randtype.lower() == "uniform":
        print("Uniformly randomizing " + filename)
        unifrandom(filename)

input("Done")
