def max_and_min(values):
    # Write your code here
    max_num = values[0]
    min_num = values[0]
    for i in values:
        
        if max_num > i:
            max_num = i
        
        if min_num < i:
            min_num = i
            
    tup = (max_num, min_num)
    
    return tup

print(max_and_min((5,4,3,2,1)))

bar = ("a", "b")
foo = ("a", "b")
bat = bar
bar = foo

print(bat is foo)


### slicing for the tuple, then join back ###
def change_value_at_index(tpl, index, value):
    # Your code here
    if index >= len(tpl):
        return tpl
    if index < -len(tpl):
        return tpl
        
    first_half_tpl = tpl[:index]
    second_half_tpl = tpl[index+1:]
    new_value = (value,)
    
    return first_half_tpl + new_value + second_half_tpl

print(change_value_at_index((1, 2, 3), 1, -1))



def even_rank(tup):
    #Write your code here
    new_tup = ()
    add_tup = ()
    for i in range(0, len(tup)):
        #i = 1, i = 3, i = 5
        if i == 1:
            add_tup = (tup[1],)
            new_tup = new_tup + add_tup
            
        if i % 2 != 0 and i != 1:
            add_tup =(tup[i],)
            new_tup = new_tup + add_tup
        
        
print(even_rank((3, 1, 4, 3, 2, 3, 19, 7, -90)))

def odd_even_sums(val):
    #Write your code here
    sum_odd = 0
    sum_even = 0
    
    if len(val) == 0:
        return val
    
    for i in range(len(val)):
        if i % 2 == 0:
            sum_odd = sum_odd + val[i]
        else:
            sum_even = sum_even + val[i]

    return (sum_odd, sum_even)

print(odd_even_sums((1, 3, 2, 4, 5, 7, 9, 10, 2, 5)))

def hanoi(n, src, dsc, aux):
    #Write your code here
    if n == 0:
        return ()
    elif n == 1:
        return (src, dsc)
    else:
        hanoi(n - 1, src, aux, dsc)
        print(src, dsc)
        hanoi(n - 1, aux, dsc, src)
        
        
print(hanoi(1, 1, 2, 3))