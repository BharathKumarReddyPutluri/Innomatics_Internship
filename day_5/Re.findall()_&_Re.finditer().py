import re
o = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])',input().strip(), re.IGNORECASE)
if o:
    for i in o:
        print(i)
else:
    print(-1)
        
