def arithmetic_arranger(problems,show_ans=False):
    a=[]
    b=[]
    op=[]
    ans = []
    
    arranged_problems = ''
    
    if len(problems)>5:
        return "Error: Too many problems."
    
    for i in problems:
        x,y,z = i.split()
        
        if y not in ['+','-']:
            return "Error: Operator must be '+' or '-'."
        elif not x.isnumeric() or not z.isnumeric():
            return "Error: Numbers must only contain digits."
        elif len(x)>4 or len(z)>4:
            return "Error: Numbers cannot be more than four digits."
        
        else:
            a.append(x); b.append(z); op.append(y)
        
    for i in range(len(problems)):
        length = len(a[i]) if len(a[i])>len(b[i]) else len(b[i])
        if i+1 == len(problems):
            arranged_problems+= '{:>{}}'.format(a[i],length+2)
        else:
            arranged_problems+= '{:>{}}'.format(a[i],length+2)+'    '
        
    arranged_problems+='\n'
        
    for i in range(len(problems)):
        length = len(a[i]) if len(a[i])>len(b[i]) else len(b[i])
        if i+1 == len(problems):
            arranged_problems+='{}{:>{}}'.format(op[i],b[i],length+1)
        else:
            arranged_problems+='{}{:>{}}'.format(op[i],b[i],length+1)+'    '
        
    arranged_problems+='\n'
    
    for i in range(len(problems)):
        length = len(a[i]) if len(a[i])>len(b[i]) else len(b[i])
        if i+1 == len(problems):
            arranged_problems+='{}'.format('-'*(length+2))
        else:
            arranged_problems+='{}'.format('-'*(length+2))+'    '
    
     

    if show_ans==True:
        for i in range(len(a)): 
            if op[i]=='+':
                ans.append(int(a[i]) + int(b[i]))
            else:
                ans.append(int(a[i]) - int(b[i]))
        arranged_problems+='\n'     
        for i in range(len(problems)):
            length = len(a[i]) if len(a[i])>len(b[i]) else len(b[i])
            if i+1 == len(problems):
                arranged_problems+='{:>{}}'.format(ans[i],length+2)
            else:
                arranged_problems+='{:>{}}'.format(ans[i],length+2)+'    '
            
    return arranged_problems
        