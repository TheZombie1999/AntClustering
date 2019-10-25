from models import simpel_clustering_model


"""
# two classes
    model and agent
    
scheduler controlls the order in which agents are activated

step fuction of model advances the intier model by one step
step fuction of agent advances the agent by one step
"""

numAnts = 100
densityOfParticels = 30
stepSize = 10
jumpingDistance = 100

model = simpel_clustering_model(numAnts, densityOfParticels, stepSize, jumpingDistance)
model.step()