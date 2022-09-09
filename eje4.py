from random import random, seed

seed(1029384756)

# 9  - 0.3 prob
# 10 - 0.4 prob
# 11 - 0.3 prob

probDist = {"9":0.3, "10":0.4, "11":0.3}

def simulate(newspapers, days):

  simActives = 0
  simDebt = 0
  simulatedResult = 0

  for i in range(days):

    randNum = random()

    options = []
    probs = []

    simPapers = 0

    for item in probDist.keys():
      options.append(item)
      probs.append(probDist[item])
    
    currentProb = probs[0]

    # print("rand: ", randNum)

    for p in range(len(probs)):
      if randNum <= currentProb:
        simPapers = int(options[p])
        break
      if p+1 < len(probs):
        currentProb += probs[p+1]
    
    # print("Simulated: ", simPapers)
    simDebt += simPapers * 1.5 # Price paid for each paper

    if newspapers < simPapers:
      simActives += (simPapers - newspapers) * 0.5 # Refund
    simActives += simPapers * 2.5 # Selled
  
  print(f"### Simulation Results - {newspapers} Newspapers - {days} Days ###")
  print(f"Actives: {simActives}")
  print(f"Debt: {simDebt}")
  print(f"Total profit: {simActives - simDebt}")

# Month simulation for 9 newspapers
simulate(9, 30)

# Year simulation for 9 newspapers
simulate(9, 365)

# 10 Year simulation for 9 newspapers
simulate(9, 365 * 10)

# Month simulation for 10 newspapers
simulate(10, 30)

# Year simulation for 10 newspapers
simulate(10, 365)

# 10 Year simulation for 10 newspapers
simulate(10, 365 * 10)

# Month simulation for 11 newspapers
simulate(11, 30)

# Year simulation for 11 newspapers
simulate(11, 365)

# 10 Year simulation for 11 newspapers
simulate(11, 365 * 10)
