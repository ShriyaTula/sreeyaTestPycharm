def vowels(S):
    vs='aeiou'
    s=S.lower()
    count=0
    for each in s:
        if each in vs:
            count+=1
    return count
S='Am a bad girl a eiou'
print(vowels(S))
