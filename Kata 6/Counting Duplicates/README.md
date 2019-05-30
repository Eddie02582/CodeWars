# Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.</br>

## Example

abcde" -> 0 # no characters repeats more than once </br>
"aabbcde" -> 2 # 'a' and 'b'</br>
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)</br>
"indivisibility" -> 1 # 'i' occurs six times</br>
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice</br>
"aA11" -> 2 # 'a' and '1'</br>
"ABBA" -> 2 # 'A' and 'B' each occur twice</br>


## Solution
sol 依題意找出重複字元的個數,先轉成小寫取set(),取出字元count >1的長度

```python
def duplicate_count(text):
  return len([c for c in set(text.lower()) if text.lower().count(c)>1])
```	
