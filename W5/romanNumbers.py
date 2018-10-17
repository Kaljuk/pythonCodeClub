

def roman(n):
    nums = [1000, 500, 100,  50,  10,   5,  1]
    lets = ['M',  'D', 'C', 'L', 'X', 'V', 'I']
    toRom = ""
    for i in range(len(nums)):
        
        if (n // nums[i] > 3 and i != 0): 
            toRom += lets[i] + lets[i-1]
        else:
            toRom += (n // nums[i]) * lets[i]

        n = n-(nums[i]*(n // nums[i]))
    
    return toRom

# for i in [1,5,10,14,15,199, 25,50,150,200,1500, 3000, 4999]:
#     print(roman(i), "=", i)