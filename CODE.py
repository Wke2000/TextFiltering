import re
def custom_split(s):
    result = []
    buffer = ''
    in_angle_bracket = False
    in_curly_bracket = False

    for c in s:
        if c == '<':
            in_angle_bracket = True
        elif c == '>':
            in_angle_bracket = False
        elif c == '{':
            in_curly_bracket = True
        elif c == '}':
            in_curly_bracket = False

        buffer += c

        if c == ' ' and not (in_angle_bracket or in_curly_bracket):
            if buffer.strip():
                result.append(buffer.strip())
                buffer = ''

    if buffer.strip():
        result.append(buffer.strip())

    return result



def has_pattern(s):
    pattern = r'\d+_[^_]+_\d+'
    return bool(re.search(pattern, s))
def find_pattern(s):
    pattern = r'\d+_[^_]+_\d+'
    match = re.search(pattern, s)
    return match.group(0) if match else None

def patterns_equal(s1, s2):
    pattern1 = find_pattern(s1)
    pattern2 = find_pattern(s2)
    return pattern1 == pattern2

import pandas as pd
df = pd.read_excel('/content/tag respiration 230917.xlsx')
#for i in df.index:
result=[]
for i in df.index:
    s2=str(df.iloc[i,2])
    s1=str(df.iloc[i,1])
    s1=custom_split(s1)
    s2=custom_split(s2)
    tmp_s1=[]
    tmp_s2=[]
    for i in s1:
        if(has_pattern(i)):
            tmp_s1.append(i)
    for j in s2:
        if(has_pattern(i)):
            tmp_s2.append(j)
    for p in tmp_s1:
        for q in tmp_s2:
            if(patterns_equal(p,q)):
                result.append([p,q])

result=pd.DataFrame(result)
# result.to_excel('result.xlsx')