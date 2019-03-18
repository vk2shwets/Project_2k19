# -*- coding: utf-8 -*-

import pandas as pd

userItemData = pd.read_csv('ratings.csv',index_col=False)
userItemData.head()
itemList=list(set(userItemData["ItemId"].tolist()))

userCount=len(set(userItemData["ItemId"].tolist()))

itemAffinity= pd.DataFrame(columns=('item1', 'item2', 'score'))
rowCount=0

for ind1 in range(len(itemList)):
    item1Users = userItemData[userItemData.ItemId==itemList[ind1]]["userId"].tolist()
    
    for ind2 in range(ind1, len(itemList)):
        
        if ( ind1 == ind2):
            continue
        item2Users=userItemData[userItemData.ItemId==itemList[ind2]]["userId"].tolist()
        
        commonUsers= len(set(item1Users).intersection(set(item2Users)))
        score=commonUsers / userCount

        itemAffinity.loc[rowCount] = [itemList[ind1],itemList[ind2],score]
        rowCount +=1
   
        itemAffinity.loc[rowCount] = [itemList[ind2],itemList[ind1],score]
        rowCount +=1
        

itemAffinity.head()

sItem=input("Enter the item : ")
searchItem=str(sItem)

recoList=itemAffinity[itemAffinity.item1==searchItem]\
        [["item2","score"]]\
        .sort_values("score", ascending=[0]) 
recoList=recoList.reset_index()
recoList=recoList.drop(recoList[recoList.score<0.0001].index)
print(recoList["item2"])

