def singleNumber(nums):
    xorTwo=reduce(lambda x,y: x^y,nums)

    print xorTwo
    xorTwo&=-xorTwo
    
    print xorTwo

    ret=[0,0]
    for n  in nums:
        if n&xorTwo==0:
            ret[0]^=n
        else:
            ret[1]^=n
    return ret

singleNumber([1,2,3,4,5,1,2,4])
