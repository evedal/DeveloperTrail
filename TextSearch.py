def naive_text_search(pattern, search_text):
    for i in range(len(search_text) - len(pattern)):
        for j in range(len(pattern)):
            if search_text[i+j] != pattern[j]:
                break
        else:
            return i
    return -1

def simplified_boyer_moore(pattern, search_text):
    count = 0
    while len(search_text)-len(pattern) >= count:
        if search_text[count+len(pattern)-1] not in pattern:
            count += len(pattern)
            continue
        for i in range(len(pattern)):
            if search_text[count+i] != pattern[i]:
                count += 1
                break
        else:
            return count
    return -1

def boyer_moore(pattern, search_text):
    count = 0
    pattern_indexes = {}
    for i, char in enumerate(reversed(pattern)):
        if char not in pattern_indexes:
            pattern_indexes.update({char:i})

    while len(search_text)-len(pattern) >= count:
        if search_text[count+len(pattern)-1] not in pattern_indexes:
            count += len(pattern)
            continue

        count += pattern_indexes.get(search_text[count+len(pattern)-1])
        for i in range(len(pattern)):
            if search_text[count+i] != pattern[i]:
                count += 1
                break
        else:
            return count
    return -1

