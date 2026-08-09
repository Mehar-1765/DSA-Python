# exp=input('Enter an expression: ')
# stack2=[]
# open=0
# close=0
# count=0
# bracket=0
# stack3=[]
# for i in exp:
#     if i=='(':
#         open+=1
#     elif i==')':
#         close+=1
# if open<close:
#     for i in range(len(exp)):
#         stack2.append(exp[i])
#         if exp[i]=='(':
#             bracket=i
# # print(bracket)
#     for ch in exp:
#         count+=1
#         if ch==')' and close-open==1 and stack2[count-4]!='(':
#             stack3.append(stack2[count-3])
#             stack3.append(stack2[count-2])
#             stack3.append(stack2[count-1])
#             a=stack2.pop()
#             b=stack2.pop()
#             c=stack2.pop()
#             d=stack2.pop()
#             stack2.append('(')
#             stack2.append(d)
#             stack2.append(c)
#             stack2.append(b)
#             stack2.append(a)
#             break
#         elif ch==')' and close-open==1 and stack2[bracket-3]!='(':
#             minus=3
#             temp_stack = []
#             for _ in range(bracket-3):
#                 temp_stack.append(stack2.pop())
#                 stack2.append('(')
#                 while temp_stack:
#                     stack2.append(temp_stack.pop())
#                 break
#     print(*stack2)
# else:
#     print('Given expression is balanced',exp)
def fix_expression(exp):
    open_brace = exp.count('(')
    close_brace = exp.count(')')
    
    # Case 1: c+d)*(a+b) -> (c+d)*(a+b)
    if ')*(' in exp:
        close_pos = exp.find(')')
        if close_pos != -1 and close_pos + 1 < len(exp) and exp[close_pos + 1] == '*':
            open_pos = exp.find('(', close_pos)
            if open_pos != -1:
                before = exp[:close_pos]
                middle = exp[close_pos + 1:open_pos]
                after = exp[open_pos:]
                return '(' + before + ')' + middle + after
    
    # Case 2: c*a+b) -> c*(a+b)
    if open_brace < close_brace:
        extra_close = exp.rfind(')')
        
        # Check if there's a '*' before the last '('
        last_open = exp.rfind('(')
        
        if last_open != -1 and last_open > 0:
            # Check if there's a '*' before '('
            if exp[last_open - 1] == '*':
                # Get everything before the '*'
                before = exp[:last_open - 1]
                inside = exp[last_open + 1:extra_close]
                
                # Split before by '*'
                parts = before.split('*')
                
                if len(parts) >= 2:
                    first = parts[0]
                    rest = '*'.join(parts[1:])
                    
                    # Build: first*(rest*(inside))
                    # For d*c*(a+b)): d*(c*(a+b))
                    return first + '*(' + rest + '*(' + inside + '))'
                else:
                    # For c*(a+b)): c*(a+b)
                    return before + '*(' + inside + ')'
        
        # Case 3: e*d*(c*(a+b))) -> e*(d*(c*(a+b)))
        # Remove extra ')' and process
        exp_fixed = exp[:-1]
        
        while True:
            open_pos = exp_fixed.rfind('(')
            if open_pos == -1:
                break
            
            # Find matching ')'
            close_pos = -1
            open_count = 0
            for i in range(open_pos + 1, len(exp_fixed)):
                if exp_fixed[i] == '(':
                    open_count += 1
                elif exp_fixed[i] == ')':
                    if open_count == 0:
                        close_pos = i
                        break
                    else:
                        open_count -= 1
            
            if close_pos == -1:
                break
            
            if open_pos > 0 and exp_fixed[open_pos - 1] == '*':
                before = exp_fixed[:open_pos - 1]
                inside = exp_fixed[open_pos + 1:close_pos]
                
                parts = before.split('*')
                if len(parts) >= 2:
                    first = parts[0]
                    rest = '*'.join(parts[1:])
                    exp_fixed = first + '*(' + rest + '*(' + inside + '))'
                    continue
            
            break
        
        return exp_fixed
    
    return exp

# Test
exp = input('Enter an expression: ')
result = fix_expression(exp)
print(result)