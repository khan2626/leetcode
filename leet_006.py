def longest_sub_str(strs):
    prefix = strs[0]

    for string in strs[1:]:
        while string.find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ''
    return prefix

strs = ["flower", "flow", "flight"]
print(longest_sub_str(strs))