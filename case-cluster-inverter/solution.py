def solve(s: str) -> str:
    n = len(s)
    res = []
    i = 0
    
    while i < n:
        if not s[i].isalpha():
            res.append(s[i])
            i += 1
        else:
            start = i
            while i < n and s[i].isalpha():
                i += 1
            cluster = s[start:i]
            upper_count = sum(1 for c in cluster if c.isupper())
            lower_count = sum(1 for c in cluster if c.islower())
            
            if upper_count > lower_count:
                res.append(cluster.upper())
            else:
                res.append(cluster.lower())
                
    return ''.join(res)
