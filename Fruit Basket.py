#The second Problem From my Coding Problem PatternNoteBook
# The Fruit Basket 
# We have Some tree types in a given array and two baskets 
# you can only move from left to right
# you can choose any tree to start with
# baskets can store only one type of fruit
# if you pass infront of a tree you past pick 1 fruit (maximum)
# calculate maximum fruits you can pick
# The Leetcode question Link https://leetcode.com/problems/fruit-into-baskets/

def MaxFruitCount(Trees):
  BasketT1 = None
  BasketT2 = None
  FrameStartPos = 0
  MaxCount = 0
  LastSameTypeTreePos = 0
  for i in range(len(Trees)):
    if BasketT1 == None:
      BasketT1 = Trees[i]
    elif BasketT2 == None:
      BasketT2 = Trees[i]
    if Trees[i] != BasketT1 and Trees[i] != BasketT2:
      if i - FrameStartPos > MaxCount:
        MaxCount = i - FrameStartPos
      FrameStartPos = LastSameTypeTreePos
      if Trees[FrameStartPos] == BasketT1:
        BasketT2 = Trees[i]
      else:
        BasketT1 = Trees[i]
    if Trees[LastSameTypeTreePos] != Trees[i]:
      LastSameTypeTreePos = i
    #print(MaxCount,FrameStartPos)
  return MaxCount

print(MaxFruitCount([1,2,3,2,1,3,2,1]))
