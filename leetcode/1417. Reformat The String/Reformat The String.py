def reformat(s):
    numb = []
    alg = []
    ans = []
    for i in s:
        if ord(i) < 59:  # number
            numb.append(i)
        if ord(i) > 59:
            alg.append(i)
    if len(numb) + 1 == len(alg):
        for i in range(len(numb)):
            ans.append(alg[i])
            ans.append(numb[i])
        ans.append(alg[len(alg) - 1])
    elif len(numb) - 1 == len(alg):
        for i in range(len(alg)):
            ans.append(numb[i])
            ans.append(alg[i])
        ans.append(numb[len(alg)])
    elif len(numb) == len(alg):
        for i in range(len(numb)):
            ans.append(numb[i])
            ans.append(alg[i])
    else:
        return ''
    return ''.join(ans)


s = input()
print(reformat(s))
