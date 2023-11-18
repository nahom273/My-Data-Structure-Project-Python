def anagram(word):
    if len(word) == 1:
        return [word]
    
    result = []
    firstw = word[0]

    shorter_anag = anagram(word[1:])
    for shorter_anag in shorter_anag:
        for position in range(len(shorter_anag)+1):
            newword = shorter_anag[:position] + firstw + shorter_anag[position:]

            if newword not in result:
                result.append(newword)
            
        
    return result

if __name__ == "__main__":
    print(anagram('ABCW'))


                