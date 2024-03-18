def encodeTalker(stringVal):
    encodedList = []
    prevChar = stringVal[0]
    count = 0
    for char in stringVal:
        if prevChar != char:
            encodedList.append((prevChar, count))
            count = 0
        prevChar = char
        count = count + 1
    encodedList.append((prevChar, count))
    return encodedList

line_Counter = 0
line_Dictionary = {} # Initialized empty Dictionary
lineList = []

tmp = """
                    *****************
               ******               ******
           ****                           ****
        ****                                 ***
      ***                                       ***
     **           ***               ***           **
   **           *******           *******          ***
  **            *******           *******            **
 **             *******           *******             **
 **               ***               ***               **
**                                                     **
**       *                                     *       **
**      **                                     **      **
 **   ****                                     ****   **
 **      **                                   **      **
  **       ***                             ***       **
   ***       ****                       ****       ***
     **         ******             ******         **
      ***            ***************            ***
        ****                                 ****
           ****                           ****
               ******               ******
                    *****************"""
tmp2 = tmp.split('\n')

length = len(tmp.split('\n')) # This would count how many lines are in the string

for i in range(0, length): # This would loop for as many line breaks there are
    line_Counter += 1
    line_Dictionary.update({line_Counter: tmp2[i]}) # Adds values to Dictionary

    lineList.append({line_Counter: tmp2[i]})
print(line_Dictionary)

def decodeTalker(encodedList):
    decodedStr = ''
    for item in encodedList:
        decodedStr = decodedStr + item[0] * item[1]
    return decodedStr


print(encodeTalker(tmp))

print(str(decodeTalker(encodeTalker(tmp))))


