def parenthesis(m):
    result_of = parent_helper('', m, m)
    print(result_of)

def parent_helper(prefix, left, right, result=[]):
    if right == 0: result.append(prefix)
    if left > 0:
        parent_helper(prefix + '(', left - 1, right)
    if right > left:
        prefix += ')'
        parent_helper(prefix, left ,right - 1)
    return result

#use list as container
def parent_list(m):
    result_f = parent_list_helper(m, m)
    print(result_f)

def parent_list_helper( left, right, prefix=[],result=[]):
    if right == 0: result.append(prefix[:])
    if left > 0:
        prefix.append('(')
        parent_list_helper(left - 1, right, prefix, result)
    
    if right > left:
        prefix.append(')')
        parent_list_helper(left, right - 1, prefix, result)
   
    if prefix != []:
        prefix.pop()
    return result

if __name__ == '__main__':
   parenthesis(3)
   parent_list(3)