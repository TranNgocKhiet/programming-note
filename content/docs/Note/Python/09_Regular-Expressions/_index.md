---
title: "09_Regular-Expressions"
weight: 5
chapter: false
---

## Finding Text Patterns with Regular Expressions

```python
import re
phone_num_pattern_obj = re.compile(r'\d{3}-\d{3}-\d{4}')
match_obj = phone_num_pattern_obj.search('My number is 415-555-4242.')
print(match_obj.group())
```
Result:
```
415-555-4242
```

### Grouping with Parentheses

```python
import re
phone_re = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_re.search('My number is 415-555-4242.')
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())
print(mo.groups())
area_code, main_number = mo.groups()
print(area_code)
print(main_number)
```
Result:
```
415
555-4242
415-555-4242
415-555-4242
('415', '555-4242')
415
555-4242
```

### Using Escape Characters

```python
import re
pattern = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')\
mo = pattern.search('My phone number is (415) 555-4242.')
print(mo.group(1))
print(mo.group(2))
```
Result:
```
(415)
555-4242
```

### Matching Characters from Alternate Groups

```python
import re
pattern = re.compile(r'Cat(erpillar|astrophe|ch|egory)')
match = pattern.search('Catch me if you can.')
print(match.group())
print(match.group(1))
```
Result:
```
Catch
ch
```

### Returning All Matches

```python
import re
pattern = re.compile(r'\d{3}-\d{3}-\d{4}')  # This regex has no groups
print(pattern.findall('Cell: 415-555-9999 Work: 212-555-0000'))
```
Result:
```
['415-555-9999', '212-555-0000']
```

```python
import re
pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')  # This regex has groups.
print(pattern.findall('Cell: 415-555-9999 Work: 212-555-0000'))
```
Result:
```
[('415', '555', '9999'), ('212', '555', '0000')]
```

```python
import re
pattern = re.compile(r'\d{3}')
print(pattern.findall('1234'))
print(pattern.findall('12345'))
print(pattern.findall('123456'))
print(pattern.findall('1234567'))
```
Result:
```
['123']
['123']
['123', '456']
['123', '456']
```

### Using Character Classes and Negative Character Classes

```python
import re
vowel_pattern = re.compile(r'[aeiouAEIOU]')
print(vowel_pattern.findall('RoboCop eats BABY FOOD.'))
```
Result:
```
['o', 'o', 'o', 'e', 'a', 'A', 'O', 'O']
```

```python
import re
consonant_pattern = re.compile(r'[^aeiouAEIOU]') # By placing a caret character (^) just after the character class’s opening bracket, you can make a negative character class
print(consonant_pattern.findall('RoboCop eats BABY FOOD.'))
```
Result:
```
['R', 'b', 'C', 'p', ' ', 't', 's', ' ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']
```

### Using Shorthand Character Classes

| Shorthand character class | Represents ...                                                                                         |
|---------------------------|--------------------------------------------------------------------------------------------------------|
| \d                        | Any numeric digit from 0 to 9.                                                                         |
| \D                        | Any character that is not a numeric digit from 0 to 9.                                                 |
| \w                        | Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.) |
| \W                        | Any character that is not a letter, numeric digit, or the underscore character.                        |
| \s                        | Any space, tab, or newline character. (Think of this as matching “space” characters.)                  |
| \S                        | Any character that is not a space, tab, or newline character.                                          |

```python
import re
pattern = re.compile(r'\d+\s\w+') # The regular expression \d+\s\w+ will match text that has one or more numeric digits (\d+), followed by a whitespace character (\s), followed by one or more letter/digit/underscore characters (\w+)
print(pattern.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))
```
Result:
```
['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']
```

### Matching Everything with the Dot Character

```python
import re
at_re = re.compile(r'.at')
print(at_re.findall('The cat in the hat sat on the flat mat.'))
```
Result:
```
['cat', 'hat', 'sat', 'lat', 'mat']
```

### Being Careful What You Match For

The best and worst thing about regular expressions is that they will match exactly what you ask for. Here are some common points of confusion regarding character classes:
- The [A-Z] or [a-z] character class matches uppercase or lowercase letters, respectively, but not both. You need to use [A-Za-z] to match both cases.
- The [A-Za-z] character class matches only plain, unaccented letters. For example, the regex string r'First Name: ([A-Za-z]+)' would match “First Name: ” followed by a group of one or more unaccented letters. But singer Sinéad O’Connor’s first name would match up to the é only, and the group would be set to 'Sin'.
- The \w character class matches all letters, including accented letters and characters from other alphabets. But it also matches numbers and the underscore character, so the regex string r'First Name: (\w+)' may match more than you intended.
- The \w character class matches all letters, but the regex string r'Last Name: (\w+)' would capture Sinéad O’Connor’s last name only up until the apostrophe character. This means the group would capture her last name as 'O'.
- Straight and smart quote characters (' " ‘ ’ “ ”) are considered completely different from each other and must be specified separately.

### Matching an Optional Pattern

```python
import re
# The ? part of the regular expression means that the pattern is optional
pattern = re.compile(r'42?!')
print(pattern.search('42!'))
print(pattern.search('4!'))
print(pattern.search('42') == None) # No match
```
Result:
```
<re.Match object; span=(0, 3), match='42!'>
<re.Match object; span=(0, 2), match='4!'>
True
```

```python
import re
pattern = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
match1 = pattern.search('My number is 415-555-4242')
print(match1.group())
match2 = pattern.search('My number is 555-4242')
print(match2.group()) 
```
Result:
```
415-555-4242
555-4242
```