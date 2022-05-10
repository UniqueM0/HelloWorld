

# def power(r, n):
#     value = 1
#     for i in range(1, n + 1):
#         value = r * value
#         return value



# print ("results", power(2, 3))






# def power(r, n):
    # if n == 1:
    #     return r
    # return r *power(r, n -1)
    # can use top or bottom does the same thing

    # return r if n == 1 else r *power(r, n -1)


# or can keep like this below 
def power(r, n):
    return r if n ==1 else r *power(r, n-1)


print ("results", power(2, 3))


