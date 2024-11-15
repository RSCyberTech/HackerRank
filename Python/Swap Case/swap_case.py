def swap_case(s):
    s=list(s)
    for c in range(len(s)):
        if s[c] == s[c].upper():
            s[c]=s[c].lower()
        else:
            s[c]=s[c].upper()
    return ''.join(s)
