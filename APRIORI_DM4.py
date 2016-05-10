from collections import defaultdict
from itertools import chain, combinations

def extractData(fileName):
    # print("extracting file")
    file = open(fileName, 'r')
    columnDict = {}
    columnCount = 0
    transCount = 0
    transDetails = defaultdict(list)

    print ("Filepath is:" + file.name)
    for everyLine in file:
        values = everyLine.strip().split(",")
        for value in values:
            transDetails[transCount].append(value)
            if value not in columnDict.values():
                columnDict[columnCount] = value
                columnCount += 1
        transCount += 1

    #print columnDict
    #print transDetails
    print "No of transcations ",transCount
    print "No of columns",columnCount
    #print "done reading to dictionary"
    transMatrix = [[0 for i in range(columnCount - 1)] for j in range(transCount - 1)]

    #print "creating matrix"
    # for row in range(transCount - 1):
    #     for column in range(columnCount - 1):
    #         for k, v in transDetails.iteritems():
    #             if k == row:
    #                 if columnDict.get(column) in v:
    #                     # print "columnDict.get(column) is", columnDict.get(column)
    #                     # print "v is", v
    #                     # print row
    #                     # print column
    #                     transMatrix[row][column] = 1
    #print "done matrix"
    return columnDict, transCount, columnCount, transDetails, transMatrix


def genFrequent(columnDict, supportCount, transDetails):
    candSupportDict = {}
    itemSet = set()
    for candidate in columnDict:
        candidateCount = 0.0
        for k, v in transDetails.iteritems():
            if columnDict.get(candidate) in v:
                candidateCount += 1
                candidateSupportCount = float(candidateCount / len(transDetails))
                # print "candidateSupportCount",candidateSupportCount
                if candidateSupportCount > supportCount:
                    candSupportDict[columnDict.get(candidate)] = candidateCount
                    allFrequentCandidateOneDictCount[columnDict.get(candidate)] = candidateCount
                    itemSet.add(frozenset([columnDict.get(candidate)]))
    #print "allFrequentCandidateDictCount", allFrequentCandidateDictCount
    return candSupportDict, itemSet


def genFrequent1(columnDict, supportCount, transDetails):
    candSupportDict = {}
    itemSet = set()
    # print columnDict
    for candidate in columnDict:
        # print candidate
        candidateCount = 0.0
        for k, v in transDetails.iteritems():
            if candidate.issubset(v):
                candidateCount += 1
                candidateSupportCount = float(candidateCount / len(transDetails))
                # print "candidateSupportCount",candidateSupportCount
                if candidateSupportCount > supportCount:
                    candSupportDict[candidate] = candidateCount
                    allFrequentCandidateDictCount[candidate] = candidateCount
                    itemSet.add(frozenset(candidate))
    return candSupportDict, itemSet


def maximal(newItemSet, itemSet):
    for item in itemSet:
        # print "item is",item
        i = 0
        for value in newItemSet:
            i += 1
            # print "value is",value
            if value.issuperset(item):
                # print "break called"
                break
            else:
                # print "i is",i
                # print "range(len(newItemSet))",len(newItemSet)
                if item not in maximalList and i == (len(newItemSet)) and len(newItemSet) > 1:
                    maximalList.append(item)
                    # print "maximalList is", maximalList


def closed(frequentListNew, PrevFrequentList):
    # closedList=[]
    # print "PrevFrequentList is",PrevFrequentList
    # print "frequentListNew is",frequentListNew
    i = -1
    for k, v in PrevFrequentList.items():
        # print k
        tempList = set()
        # tempVList=set()
        i += 1
        if isinstance(k, basestring):
            tempList.add(frozenset([k]))
            # print tempList
            # tempVList.add(v)
            for key, value in frequentListNew.items():
                # print tempList
                # print key
                # print (k in key)
                if k in key and v > value:
                    # print "infor"
                    if tempList not in closedList:
                        closedList.append(tempList)
                elif k in key and v <= value:
                    if k in closedList:
                        closedList.remove(tempList)
                else:
                    continue

        else:
            for key, value in frequentListNew.items():
                # print key
                if k.issubset(key) and v > value:
                    if k not in closedList:
                        closedList.append(k)
                elif k.issubset(key) and v <= value:
                    if k in closedList:
                        closedList.remove(k)
                else:
                    continue
                        # print "closedList is", closedList


def candidate_gen(freq_sets, k):
    """Join a set with itself and returns the n-element itemsets"""
    returnSet = set()
    for i in freq_sets:
        for j in freq_sets:
            if len(i.union(j)) == k:
                returnSet.update(set([i.union(j)]))
    return returnSet

def candiate_genForOne(freq_sets, k, oneItemSet):
    returnSet = set()
    for i in freq_sets:
        for j in oneItemSet:
            if len(i.union(j)) == k:
                returnSet.update(set([i.union(j)]))
    return returnSet

    # return [i.union(j) for i in freq_sets for j in freq_sets if len(i.union(j)) == k]


def getSubsets(element):
    return chain(*[combinations(element, item + 1) for item, a in enumerate(element)])


def fix():
    #print "in fix"
    tempList = []
    for k, v in allFrequentCandidateOneDictCount.items():
        tempList = set()
        # print k
        # print v
        tempList.add(k)
        allFrequentCandidateOneDictCount1[frozenset(tempList)] = v
        # print "allFrequentCandidateDictCount--------------------------------------------------------",allFrequentCandidateOneDictCount1


# def getSupport(item):
#     for k,v in allFrequentCandidateOneDictCount.items():
#         if item != k:
#             for k, v in allFrequentCandidateOneDictCount1.items():
#                 # print "------------------------ELSE-----------------------------------------------------"
#                 if item == k:
#                     print "--------------------------IF---------------"
#                     print float(allFrequentCandidateOneDictCount1[item]) / len(transDetails)
#                     return float(allFrequentCandidateOneDictCount1[item]) / len(transDetails)
#         else:
#             print "------------------------Else--------------------------------------"
#             print float(allFrequentCandidateDictCount[item]) / len(transDetails)
#             return float(allFrequentCandidateDictCount[item]) / len(transDetails)


def getSupport1(item):
    for k, v in allFrequentCandidateOneDictCount1.items():
        return float(allFrequentCandidateOneDictCount1[item]) / len(transDetails)


def getSupport(item):
    for k, v in allFrequentCandidateDictCount.items():
        return float(allFrequentCandidateDictCount[item]) / len(transDetails)


def RuleOuput(items, rules):
    print "***************************** RULES ***************************************************:"
    count =0
    for r, c in sorted(rules, key=lambda (r, c): c):
        count+=1
        preVal, postVal = r
        print "%s ==============> %s ,with confidence, %.3f" % (str(preVal), str(postVal), c)
    print "total rules",count


def rules(itemSet, allFrequentCandidateDict, confidenceThreshold,confidenceNotLift):
    allFrequentCandidateDictSupport = []
    ruleList = []
    Conf=True
    for k, v in allFrequentCandidateDict.items():
        if k == 1:
            for item in v:
                allFrequentCandidateDictSupport.extend([(tuple(item), getSupport1(item))for item in v])
        else:
            for item in v:
                allFrequentCandidateDictSupport.extend([(tuple(item), getSupport(item))for item in v])

    #print "allFrequentCandidateDictSupport is", allFrequentCandidateDictSupport
    #print "allFrequentCandidateDictSupport",allFrequentCandidateDictSupport



    for key, value in allFrequentCandidateDict.items()[1:]:
        for item_set in value:
            # print "item in largeset",item
            possibleSubsets = map(frozenset, [subset for subset in getSubsets(item_set)])
            # print "possibleSubsets",possibleSubsets
            for eachItem in possibleSubsets:
                otherItems = item_set.difference(eachItem)
                # print "remain--------------",remain

                if confidenceNotLift==1:
                    #print "-----------------------------CONFIDENCE----------------------------------------------"
                    if len(otherItems) > 0:
                        if len(eachItem) == 1:
                            confidence = getSupport(item_set) / getSupport1(eachItem)
                            # lift=confidence/getSupport(remain)
                        else:
                            confidence = getSupport(item_set) / getSupport(eachItem)
                            # print "confidence ",confidence
                        if confidence >= confidenceThreshold:
                            ruleList.append(((tuple(eachItem), tuple(otherItems)),confidence))
                else:
                    #print "-----------------------------LIFT----------------------------------------------"
                    if len(otherItems) > 0:
                        #print remain
                        if len(eachItem) == 1:
                            confidence = getSupport(item_set) / getSupport1(eachItem)
                            if len(otherItems) == 1:
                                lift = confidence / getSupport1(otherItems)
                            else:
                                lift = confidence / getSupport(otherItems)
                        else:
                            confidence = getSupport(item_set) / getSupport(eachItem)
                            if len(otherItems) == 1:
                                lift = confidence / getSupport1(otherItems)
                            else:
                                lift = confidence / getSupport(otherItems)
                                # print "confidence ",confidence
                                #print "lift value is", lift
                        if lift >= confidenceThreshold:
                            ruleList.append(((tuple(eachItem), tuple(otherItems)), lift))

    #print "ruleList is", ruleList
    return allFrequentCandidateDictSupport, ruleList


def Apriori(columnDict, supportCount, transDetails, confidenceThreshold,configuration,confidenceNotLift):


    k = 1
    allFrequentCandidateDict = dict()
    allFrequentCandidateDictCount = dict()
    # frequentlstList=[]
    # frequentList={}
    print "*********candidateList count is*****", len(columnDict)
    print "*********candidateList is***********", columnDict
    OneFrequentList, oneItemSet = genFrequent(columnDict, supportCount, transDetails)
    print "******itemset count is*********", len(OneFrequentList)
    print "******itemset is************", OneFrequentList
    itemSetCount=len(OneFrequentList)
    candidateListCount=len(columnDict)
    # print "OneFrequentList is",OneFrequentList
    #print "oneItemSet is", oneItemSet

    itemSet = oneItemSet
    PrevFrequentList = OneFrequentList


    while (itemSet):
        #print "in while"
        k += 1
        allFrequentCandidateDict[k - 1] = itemSet
        # print "allFrequentCandidateDict",allFrequentCandidateDict
        if (configuration == 1):
            candidateList = candidate_gen(itemSet, k)
        else:
            candidateList = candiate_genForOne(itemSet, k, oneItemSet)
        candidateListCount = candidateListCount+len(candidateList)
        #print "candidateList",candidateList
        print "*****candidateList count is********", len(candidateList)
        print "*****candidateList is**************", candidateList
        frequentListNew, newItemSet = genFrequent1(candidateList, supportCount, transDetails)
        print "****itemset count is******", len(newItemSet)
        print "****itemset is************", newItemSet
        itemSetCount=itemSetCount+len(newItemSet)
        # print "PrevFrequentList", PrevFrequentList
        closed(frequentListNew, PrevFrequentList)
        maximal(newItemSet, itemSet)
        # allFrequentCandidateDictCount=frequentListNew
        PrevFrequentList = frequentListNew
        itemSet = newItemSet
        if (itemSet == set([])):
            print "*******total candidates count is*****", candidateListCount
            print "*******total itemset count is*****", itemSetCount
            break
        # print "freq list is", frequentListNew
        #print "itemset is", itemSet

    fix()
    allFrequentCandidateDictSupport, Rules = rules(itemSet, allFrequentCandidateDict, confidenceThreshold,confidenceNotLift)
    print "total rules count",len(Rules)
    RuleOuput(allFrequentCandidateDictSupport, Rules)
    return itemSet

# main

configuration=input("enter 1 for Fk-1*Fk-1 and 2 for Fk-1*F1 ")
confidenceNotLift=input("enter 1 for confidence and 2 for lift  ")



#please change the filename accordingly
#fileName = "nursery.txt"
#fileName = "cmc.data.txt"
fileName="car.txt"


#change the threshold accordingly
supportThreshold = 0.1
confidenceThreshold = 0.6


#globallist for closed and maximal
closedList = []
maximalList = []



allFrequentCandidateOneDictCount = {}
allFrequentCandidateOneDictCount1 = {}
allFrequentCandidateDictCount = {}


columnDict, transCount, columnCount, transDetails, transMatrix = extractData(fileName)
itemSet=Apriori(columnDict, supportThreshold, transDetails, confidenceThreshold,configuration,confidenceNotLift)


print "******************************CLOSED ITEMSETS***************************************************"
print "closed set has ",len(closedList)," itemsets"
print "closed item set is", closedList
print "************************************************************************************************"

print "maximal Itemset has ",len(maximalList)," itemsets"
print "maximalList is", maximalList
#print "allFrequentCandidateOneDictCount", allFrequentCandidateOneDictCount
#print "allFrequentCandidateDictCount", allFrequentCandidateDictCount
#print transMatrix
