import math

four9s_log = dict()
call_count = 0

#nines_list = [(9,1),(99,2),(999,3),(9999,4),(.9,1),(.99,2),(.999,3),(.9999,4),(9.9,2),
#              (9.99,3),(9.999,4),(99.9,3),(99.99,4),(999.9,4)]
nines_list = [(9,1),(99,2),(.9,1),(.99,2),(9.9,2)]
          
def four9s_solver( stack = [], num9s = 0, oplist = [] ):
    global call_count
    call_count += 1

    # generic condition to limit search depth
    if num9s > 4 or len(oplist) > 12:
        return

    if (num9s == 4 and len(stack) is 1 and abs(stack[-1]-round(stack[-1])) < 1e-10 
            and stack[-1] >= 0 and stack[-1] <= 100):
        opstr = ','.join(oplist)
        idx = int(float(stack[-1]))
        #print( opstr, ' : ', idx )
        if not idx in four9s_log:
            four9s_log[idx] = opstr
        else:
            if four9s_log[idx].count(',') > opstr.count(','):
                four9s_log[idx] = opstr
        return
            
    # enter number 
    for (nines_entry, additional_num9s) in nines_list:
        four9s_solver( stack+[nines_entry], num9s+additional_num9s, oplist+[str(nines_entry)] )

    # +
    if len(stack) >= 2:
        four9s_solver( stack[:-2]+[stack[-2]+stack[-1]], num9s, oplist+['+'] )
    
    # - 
    if len(stack) >= 2:
        four9s_solver( stack[:-2]+[stack[-2]-stack[-1]], num9s, oplist+['-'] )
    
    # *
    if len(stack) >= 2:
        four9s_solver( stack[:-2]+[stack[-2]*stack[-1]], num9s, oplist+['*'] )
    
    # /
    if len(stack) >= 2 and not stack[-1] == 0:
        four9s_solver( stack[:-2]+[stack[-2]/stack[-1]], num9s, oplist+['/'] )
    
    # ^
    if (len(stack) >= 2 and stack[-2] > 0 and stack[-2] < 10 and stack[-1] > 0 and stack[-1] < 10):
        four9s_solver( stack[:-2]+[stack[-2]**stack[-1]], num9s, oplist+['^'] )
    
    # FACTorial
    if (len(stack) >= 1 and float(stack[-1]).is_integer() and stack[-1] > 2 
            and stack[-1] < 10 ):
        four9s_solver( stack[:-1] + [math.factorial(stack[-1])], num9s, oplist+['FACT'] )
    
    # SQRT
    if len(stack) >= 1 and stack[-1] > 1: 
        four9s_solver( stack[:-1] + [math.sqrt(stack[-1])], num9s, oplist+['SQRT'] )
    

if __name__ == '__main__':
    print('starting')
    four9s_solver()
    for x in range(101):
        if x in four9s_log:
            print(x, ':', four9s_log[x])
        else:
            print(x, ': NOT FOUND')
    print( call_count )
    
            