#A-Priori algorithm for finding frequent itemsets used in association rule
#author:pzc
#data:2012-9-23 22:07:58
import copy

itemset = {}
basket=[]
basketset = {}
basketID = 0
lasbaskeID = 0

#1.first pass, counting frequent items and store it in itemset
datafile = open('association.txt')

while True:
    line = datafile.readline()
    if not line:
        break
    else:
        #form basketset
        lastbasketID = basketID
        basketID = int(line[0:line.find('\t')])
        item = line[line.rfind('\t') + 1 : -1]        
        if basketID != lastbasketID:
            basketset[lastbasketID] = copy.copy(basket)
            del basket[:]
        basket.append(item)        
        
        #count items' apperence
        if(itemset.has_key(item)):
            itemset[item] += 1
        else:
            itemset[item] = 1

#2.between the pass, use support threshold to filter out non-frequent items
threshold_item = 200
for item in itemset.keys():#note: http://blog.ihipop.info/2010/10/1777.html
    if itemset[item] < threshold_item:
        del itemset[item]

#3.second pass
#loop around the basketset to count the absence of pairs
pairs={}
for basket in basketset.itervalues():
    for itemI in basket:
        for itemJ in basket:
            if itemI != itemJ and itemI in basket and itemJ in basket:
                if (itemJ, itemI) in pairs:
                    continue
                if (itemI, itemJ) in pairs:
                    pairs[(itemI, itemJ)] += 1
                else:
                    pairs[(itemI, itemJ)] = 1
                    
#filter out those pairs whose support is lower than the threshold
threshold_pair = 255
for pair in pairs.keys():
    if pairs[pair] < threshold_pair:
        del pairs[pair]
for pair in pairs:
    print pair, pairs[pair]

