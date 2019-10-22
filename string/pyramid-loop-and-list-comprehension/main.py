

base = 11                              
          
for level in range(0, (base+1)//2): # or round(base/2)
    #print([' ']*level + ['*']*(base-level*2) + [' ']*level)
    print(' '*level + '*'*(base-level*2) + ' '*level)

print('-----')

data = [(' '*level + '*'*(base-level*2) + ' '*level) for level in range(0, (base+1)//2)]
print('\n'.join(data))

print('-----')

for level in range((base-1)//2, -1, -1):
    #print([' ']*level + ['*']*(base-level*2) + [' ']*level)
    print(' '*level + '*'*(base-level*2) + ' '*level)

print('-----')

data = [(' '*level + '*'*(base-level*2) + ' '*level) for level in range((base-1)//2, -1, -1)]
print('\n'.join(data))

print('-----')

# --- lists  ---

for level in range((base-1)//2, -1, -1):
    print([' ']*level + ['*']*(base-level*2) + [' ']*level)

print('-----')

data = [([' ']*level + ['*']*(base-level*2) + [' ']*level) for level in range((base-1)//2, -1, -1)]
for row in data:
    print(row)

print('-----')

for level in range(0, (base+1)//2): # round(base/2)
    print([' ']*level + ['*']*(base-level*2) + [' ']*level)

print('-----')

data = [([' ']*level + ['*']*(base-level*2) + [' ']*level) for level in range(0, (base+1)//2)]
for row in data:
    print(row)


