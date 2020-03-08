# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 20:17:38 2020

@author: ROTIMI
"""

i = []
for x in range(100000):
    i.append(x * 3)
#print(max(i))


ip_file = open("d_tough_choices.txt", 'r')
op_file = open("output3.txt", 'w')

line_1 = ip_file.readline().split()

total_books = int(line_1[0])

libraries = int(line_1[1])

days = int(line_1[2])

book_scores = [int(a) for a in ip_file.readline().split()]

all_books = {}

all_sign_up = {}

all_bpd = {}
#print(book_scores)

for x in range(libraries):
    lib_line1 = [int(a) for a in ip_file.readline().split()]
    lib_books = int(lib_line1[0])
    sign_up = int(lib_line1[1])
    all_sign_up[x] = sign_up
    bpd = int(lib_line1[2])
    all_bpd[x] = bpd
    book_list = []
    for b in [int(a) for a in ip_file.readline().split()]:
        temp_funct = lambda x,y:y[x]
        book_list.append(temp_funct(b,book_scores))
    all_books[x] = book_list

def work(all_sign_up, all_books, fin_scan_dict = {}):
    if not all_sign_up:
        return fin_scan_dict
    else:
        min_signup = min(all_sign_up.values())
    #    print('min', min_signup)
    #    print(all_sign_up)
        same_signup_dict = {}
        #fin_scan_dict = {}
        
        for x,y in zip(all_sign_up.keys(), all_sign_up.values()):
            if y == min_signup:
        #        same_signup_dict[x] = len(all_books[x])
                same_signup_dict[len(all_books[x])] = x
        
    #    print(same_signup_dict)
                
        new_same_signup = {}
        for x in sorted(same_signup_dict.keys(), reverse=True):
            new_same_signup[x] = same_signup_dict[x]
        #    new_same_signup[x] = sorted(all_books[x])
            
        for x in new_same_signup.values():
            fin_scan_dict[x] = sorted(all_books[x], reverse=True)
            del all_books[x]
            del all_sign_up[x]
        
    fin_scan_dict.update(work(all_sign_up, all_books, fin_scan_dict))
    return fin_scan_dict
#    print(new_same_signup)
#    return fin_scan_dict
#fin_scan_dict[]
    
all_sign_up_copy = all_sign_up.copy()
all_books_copy = all_books.copy()
ans = work(all_sign_up_copy, all_books_copy)

op_file.write(str(libraries) + '\n')

for x in ans:
    op_file.write(str(x) + ' ' + str(days - all_sign_up[x]) + '\n')
    days = days - all_sign_up[x]
    p = []
    for y in ans[x]:
        p.append(str(all_books[x].index(y)))
    for d in p:
        op_file.write(str(d) + ' ')
    op_file.write('\n')
op_file.close()
    
    
    
#print(all_books)
#print(all_sign_up)
#print(all_bpd)
    
    