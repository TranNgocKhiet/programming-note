---
title: "09_Regular-Expressions"
weight: 9
chapter: false
---

# Regular Expressions

## Finding Text Patterns with Regular Expressions

Input
```python
import re
phone_num_pattern_obj = re.compile(r'\d{3}-\d{3}-\d{4}')
match_obj = phone_num_pattern_obj.search('My number is 415-555-4242.')
print(match_obj.group())
```

Output
```
415-555-4242
```

---

## Grouping with Parentheses

Input
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

Output
```
415
555-4242
415-555-4242
415-555-4242
('415', '555-4242')
415
555-4242
```

---

## Using Escape Characters

Input
```python
import re
pattern = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')\
mo = pattern.search('My phone number is (415) 555-4242.')
print(mo.group(1))
print(mo.group(2))
```

Output
```
(415)
555-4242
```

---

## Matching Characters from Alternate Groups | ```|```

Input
```python
import re
pattern = re.compile(r'Cat(erpillar|astrophe|ch|egory)')
match = pattern.search('Catch me if you can.')
print(match.group())
print(match.group(1))
```

Output
```
Catch
ch
```

---

## Returning All Matches | ```findall()```

Input
```python
import re
pattern = re.compile(r'\d{3}-\d{3}-\d{4}')  # This regex has no groups
print(pattern.findall('Cell: 415-555-9999 Work: 212-555-0000'))
```

Output
```
['415-555-9999', '212-555-0000']
```

<br>

Input
```python
import re
pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')  # This regex has groups.
print(pattern.findall('Cell: 415-555-9999 Work: 212-555-0000'))
```

Output
```
[('415', '555', '9999'), ('212', '555', '0000')]
```

<br>

Input
```python
import re
pattern = re.compile(r'\d{3}')
print(pattern.findall('1234'))
print(pattern.findall('12345'))
print(pattern.findall('123456'))
print(pattern.findall('1234567'))
```

Output
```
['123']
['123']
['123', '456']
['123', '456']
```

---

## Using Character Classes and Negative Character Classes

Input
```python
import re
vowel_pattern = re.compile(r'[aeiouAEIOU]')
print(vowel_pattern.findall('RoboCop eats BABY FOOD.'))
```

Output
```
['o', 'o', 'o', 'e', 'a', 'A', 'O', 'O']
```

<br>

Input
```python
import re
consonant_pattern = re.compile(r'[^aeiouAEIOU]') # By placing a caret character (^) just after the character class’s opening bracket, you can make a negative character class
print(consonant_pattern.findall('RoboCop eats BABY FOOD.'))
```

Output
```
['R', 'b', 'C', 'p', ' ', 't', 's', ' ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']
```

---

## Using Shorthand Character Classes

| Shorthand character class | Represents ...                                                                                         |
|---------------------------|--------------------------------------------------------------------------------------------------------|
| \d                        | Any numeric digit from 0 to 9.                                                                         |
| \D                        | Any character that is not a numeric digit from 0 to 9.                                                 |
| \w                        | Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.) |
| \W                        | Any character that is not a letter, numeric digit, or the underscore character.                        |
| \s                        | Any space, tab, or newline character. (Think of this as matching “space” characters.)                  |
| \S                        | Any character that is not a space, tab, or newline character.                                          |

Input
```python
import re
pattern = re.compile(r'\d+\s\w+') # The regular expression \d+\s\w+ will match text that has one or more numeric digits (\d+), followed by a whitespace character (\s), followed by one or more letter/digit/underscore characters (\w+)
print(pattern.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))
```

Output
```
['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']
```

---

## Matching Everything with the Dot Character | ```.```

Input
```python
import re
at_re = re.compile(r'.at')
print(at_re.findall('The cat in the hat sat on the flat mat.'))
```

Output
```
['cat', 'hat', 'sat', 'lat', 'mat']
```

---

## Being Careful What You Match For

- The best and worst thing about regular expressions is that they will match exactly what you ask for. Here are some common points of confusion regarding character classes:
<br>&emsp;  The [A-Z] or [a-z] character class matches uppercase or lowercase letters, respectively, but not both. You need to use [A-Za-z] to match both cases.
<br>&emsp; + The [A-Za-z] character class matches only plain, unaccented letters. For example, the regex string r'First Name: ([A-Za-z]+)' would match “First Name: ” followed by a group of one or more unaccented letters. But singer Sinéad O’Connor’s first name would match up to the é only, and the group would be set to 'Sin'.
<br>&emsp; + The \w character class matches all letters, including accented letters and characters from other alphabets. But it also matches numbers and the underscore character, so the regex string r'First Name: (\w+)' may match more than you intended.
<br>&emsp; + The \w character class matches all letters, but the regex string r'Last Name: (\w+)' would capture Sinéad O’Connor’s last name only up until the apostrophe character. This means the group would capture her last name as 'O'.
<br>&emsp; + Straight and smart quote characters (' " ‘ ’ “ ”) are considered completely different from each other and must be specified separately.

## Matching an Optional Pattern | ```?```

Input
```python
import re
# The ? part of the regular expression means that the pattern is optional
pattern = re.compile(r'42?!')
print(pattern.search('42!'))
print(pattern.search('4!'))
print(pattern.search('42') == None) # No match
```

Output
```
<re.Match object; span=(0, 3), match='42!'>
<re.Match object; span=(0, 2), match='4!'>
True
```

<br>

Input
```python
import re
pattern = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
match1 = pattern.search('My number is 415-555-4242')
print(match1.group())
match2 = pattern.search('My number is 555-4242')
print(match2.group()) 
```

Output
```
415-555-4242
555-4242
```

---

## Matching Zero or More Qualifiers | ```*```

Input
```python
import re
pattern = re.compile('Eggs( and spam)*')
print(pattern.search('Eggs'))
print(pattern.search('Eggs and spam'))
print(pattern.search('Eggs and spam and spam'))
print(pattern.search('Eggs and spam and spam and spam'))
```

Output
```
<re.Match object; span=(0, 4), match='Eggs'>
<re.Match object; span=(0, 13), match='Eggs and spam'>
<re.Match object; span=(0, 22), match='Eggs and spam and spam'>
<re.Match object; span=(0, 31), match='Eggs and spam and spam and spam'>
```

---

## Matching One or More Qualifiers | ```+```

Input
```python
import re
pattern = re.compile('Eggs( and spam)+')
print(pattern.search('Eggs and spam'))
print(pattern.search('Eggs and spam and spam'))
print(pattern.search('Eggs and spam and spam and spam'))
```

Output
```
<re.Match object; span=(0, 4), match='Eggs'>
<re.Match object; span=(0, 13), match='Eggs and spam'>
<re.Match object; span=(0, 22), match='Eggs and spam and spam'>
<re.Match object; span=(0, 31), match='Eggs and spam and spam and spam'>
```

---

## Matching a Specific Number of Qualifiers

Input
```python
import re
haRegex = re.compile(r'(Ha){3}')
match1 = haRegex.search('HaHaHa')
print(match1.group())
match = haRegex.search('HaHa')
print(match == None)
```

Output
```
HaHaHa
True
```

---

## Greedy and Non-greedy Matching | ```?```, ```*``` and ```+```

- The ? quantifier is the same as {0,1}.
- The * quantifier is the same as {0,}.
- The + quantifier is the same as {1,}.

Input
```python
import re
greedy_pattern = re.compile(r'(Ha){3,5}')
match1 = greedy_pattern.search('HaHaHaHaHa')
print(match1.group())
lazy_pattern = re.compile(r'(Ha){3,5}?')
match2 = lazy_pattern.search('HaHaHaHaHa')
print(match2.group())
```

Output
```
HaHaHaHaHa
HaHaHa
```

---

## Matching Everything | ```.*``` and ```.*?```

Input
```python
import re
name_pattern = re.compile(r'First Name: (.*) Last Name: (.*)')
name_match = name_pattern.search('First Name: Al Last Name: Sweigart')
print(name_match.group(1))
print(name_match.group(2))
```

Output
```
Al
Sweigart
```

- The dot-star uses greedy mode: it will always try to match as much text as possible. To match any and all text in a non-greedy or lazy fashion, use the dot, star, and question mark (.*?). As when it’s used with curly brackets, the question mark tells Python to match in a non-greedy way.

Input
```python
import re
lazy_pattern = re.compile(r'<.*?>')
match1 = lazy_pattern.search('<To serve man> for dinner.>')
print(match1.group())
greedy_re = re.compile(r'<.*>')
match2 = greedy_re.search('<To serve man> for dinner.>')
print(match2.group())
```

Output
```
Al
Sweigart
```

---

## Matching Newline Characters | ```re.DOTALL```

Input
```python
import re
no_newline_re = re.compile('.*')
print(no_newline_re.search('Serve the public trust.\nProtect the innocent. \nUphold the law.').group())
print()
newline_re = re.compile('.*', re.DOTALL)
print(newline_re.search('Serve the public trust.\nProtect the innocent. \nUphold the law.').group())
```

Output
```
Serve the public trust.

Serve the public trust.
Protect the innocent. 
Uphold the law.
```

---

## Matching at the Start and End of a String | ```^```, ```$``` and ```/b```

Input
```python
import re
begins_with_hello = re.compile(r'^Hello')
print(begins_with_hello.search('Hello, world!'))
print(begins_with_hello.search('He said "Hello."') == None)
```

Output
```
<re.Match object; span=(0, 5), match='Hello'>
True
```

<br>

Input
```python
import re
ends_with_number = re.compile(r'\d$')
print(ends_with_number.search('Your number is 42'))
print(ends_with_number.search('Your number is forty two.') == None)
```

Output
```
<re.Match object; span=(16, 17), match='2'>
True
```

<br>

Input
```python
import re
whole_string_is_num = re.compile(r'^\d+$')
print(whole_string_is_num.search('1234567890'))
print(whole_string_is_num.search('12345xyz67890') == None)
```

Output
```
<re.Match object; span=(0, 10), match='1234567890'>
True
```

<br>

Input
```python
import re
pattern = re.compile(r'\bcat.*?\b')
print(pattern.findall('The cat found a catapult catalog in the catacombs.'))
print()
pattern = re.compile(r'\Bcat\B')
print(pattern.findall('certificate')) # Match
print(pattern.findall('catastrophe')) # No match
```

Output
```
['cat', 'catapult', 'catalog', 'catacombs']

['cat']
[]
```

---

## Case-Insensitive Matching | ```re.I```

Input
```python
import re
pattern = re.compile(r'robocop', re.I)
print(pattern.search('RoboCop is part man, part machine, all cop.').group())
print(pattern.search('ROBOCOP protects the innocent.').group())
print(pattern.search('Have you seen robocop?').group())
```

Output
```
RoboCop
ROBOCOP
robocop
```

---

## Substituting Strings | ```sub()```

Input
```python
import re
pattern = re.compile(r'robocop', re.I)
agent_pattern = re.compile(r'Agent \w+')
print(agent_pattern.sub('CENSORED', 'Agent Alice contacted Agent Bob.'))
```

Output
```
CENSORED contacted CENSORED.
```

<br>

Input
```python
import re
agent_pattern = re.compile(r'Agent (\w)\w*')
print(agent_pattern.sub(r'\1****', 'Agent Alice contacted Agent Bob.'))
```

Output
```
A**** contacted B****.
```

---

## Managing Complex Regexes with Verbose Mode | ```re.VERBOSE```

Input
```python
pattern = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # Area code
    (\s|-|\.)?  # Separator
    \d{3}  # First three digits
    (\s|-|\.)  # Separator
    \d{4}  # Last four digits
    (\s*(ext|x|ext\.)\s*\d{2,5})?  # Extension
    )''', re.VERBOSE)
```

---