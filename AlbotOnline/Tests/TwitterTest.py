import AlbotOnline.TwitterMonteCarlo.Twitter as Albot
import random

sampler = Albot.TwitterSampler()

'''
#Exhaustive Sampling
for y in range(2048):
    for x in range(2048):
        sampler.getSample(x, y)
'''

#Random Sampling
while(True):
    x = random.randint(0, sampler.width)
    y = random.randint(0, sampler.height)
    sampler.getSample(x, y)