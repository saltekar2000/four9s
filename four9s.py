import math

four9s_log = dict()

nines = [(9,1),(99,2),(999,3),(9999,4),
         (.9,1),(.99,2),(.999,3),(.9999,4),
            (9.9,2),(9.99,3),(9.999,4),
                (99.9,3),(99.99,4),
                     (999.9,4)]
         

def four9s_solver( flag = False, stack = [], num9s = 0, oplist = [] ):

    # generic condition to limit search depth
    if num9s > 4 or len(oplist) > 12:
        return

    if num9s == 4 and len(stack) is 1 and abs(float(stack[-1])-int(float(stack[-1]))) < 1e-6 and float(stack[-1]) >= 0 and float(stack[-1]) <= 100:
        opstr = ','.join(oplist)
        idx = int(float(stack[-1]))
        if not idx in four9s_log:
            four9s_log[idx] = opstr
        else:
            if four9s_log[idx].count(',')-four9s_log[idx].count('ENTER') > opstr.count(',')-opstr.count('ENTER'):
                four9s_log[idx] = opstr
        return
            
    # 9
    if flag is False:
        four9s_solver( True, stack+['9'], num9s+1, oplist+['9'] )
    else:
        four9s_solver( True, stack[:-1]+[stack[-1]+'9'], num9s+1, oplist+['9'] )

    # .9
    if flag is False:
        four9s_solver( True, stack+['.9'], num9s+1, oplist + ['.9'] )
    elif stack[-1].count('.') == 0:
        four9s_solver( True, stack[:-1]+[stack[-1]+'.9'], num9s+1, oplist+['.9'] )
    
    # ENTER
    if flag is True:
        four9s_solver( False, stack[:-1]+[float(stack[-1])], num9s, oplist+['ENTER'] )
    
    # +
    if len(stack) >= 2 and not oplist[-1] == 'ENTER':
        four9s_solver( False, stack[:-2]+[stack[-2]+float(stack[-1])], num9s, oplist+['+'] )
    
    # - 
    if len(stack) >= 2 and not oplist[-1] == 'ENTER':
        four9s_solver( False, stack[:-2]+[stack[-2]-float(stack[-1])], num9s, oplist+['-'] )
    
    # *
    if len(stack) >= 2 and not oplist[-1] == 'ENTER':
        four9s_solver( False, stack[:-2]+[stack[-2]*float(stack[-1])], num9s, oplist+['*'] )
    
    # /
    if len(stack) >= 2 and not float(stack[-1]) == 0 and not oplist[-1] == 'ENTER':
        four9s_solver( False, stack[:-2]+[stack[-2]/float(stack[-1])], num9s, oplist+['/'] )
    
    # ^
    if (len(stack) >= 2 and stack[-2] > 0 and stack[-2] < 10 and float(stack[-1]) > 0 and float(stack[-1]) < 10):
        four9s_solver( False, stack[:-2]+[stack[-2]**float(stack[-1])], num9s, oplist+['^'] )
    
    # FACTorial
    if (len(stack) >= 1 and float(stack[-1]).is_integer() and float(stack[-1]) > 2 
            and float(stack[-1]) < 20 and not oplist[-1] == 'ENTER'):
        four9s_solver( False, stack[:-1] + [math.factorial(float(stack[-1]))], num9s, oplist+['FACT'] )
    
    # SQRT
    if len(stack) >= 1 and float(stack[-1]) > 1 and not oplist[-1] == 'ENTER': 
        four9s_solver( False, stack[:-1] + [math.sqrt(float(stack[-1]))], num9s, oplist+['SQRT'] )
    

if __name__ == '__main__':
    print('starting')
    four9s_solver()
    for x in range(101):
        if x in four9s_log:
            print(x, ':', four9s_log[x])
        else:
            print(x, ': NOT FOUND')
    
    
            