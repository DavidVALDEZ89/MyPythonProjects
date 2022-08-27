def arithmetic_arranger(*args):
    problems_list = args[0]  #Define the first argument as the list of problems
    #Start of the solution        
    if len(problems_list) <= 5 :
        arr_problems = ["","","",""]  #same as ["row_0","row_1","row_2","row_3"]
        
        for i in problems_list:
            
            space_x = " "*4  #space between problems
            arr_problems[0] += space_x  #Row 0 + space
            arr_problems[1] += space_x  #Row 1 + space 
            arr_problems[2] += space_x  #Row 2 + space
            arr_problems[3] += space_x  #Row 3 + space
            
            
            # Errors
            if not i.split()[0].isdigit() or not  i.split()[-1].isdigit():
                print ("Error: Numbers must only contain digits.")
            else:
                if len(i.split()[0]) > 4 or  len(i.split()[-1]) > 4:
                    print ("Error: Numbers cannot be more than four digits.")
                else:
                    if "+" in i or "-" in i:

                        # Arrange the problems
                        max_len = max(len(i.split()[0]),len(i.split()[-1])) + 2
                        arr_problems[0] += str(" "*(max_len-len(i.split()[0])) + i.split()[0])
                        arr_problems[1] += str(i.split()[1] + " "*(max_len-len(i.split()[-1])-1) + i.split()[-1])
                        arr_problems[2] += "-"*max_len
                        if True in args:  #Show answer
                            if "+" in i:  #add
                                x = str(int(i.split()[0]) + int(i.split()[-1]))
                                arr_problems[3] += str(" "*(max_len-len(x)) + x)
                            else :  #substract
                                x = str(int(i.split()[0]) - int(i.split()[-1]))
                                arr_problems[3] += str(" "*(max_len-len(x)) + x)
                        else :
                            arr_problems[3] += " "*max_len
                        
                    else:
                        print ("Error: Operator must be '+' or '-'.")

                
        
        print (arr_problems[0]+"\n"+arr_problems[1]+"\n"+arr_problems[2]+"\n"+arr_problems[3]+"\n")  
    else:
        print ("Error: Too many problems.")
        
arithmetic_arranger(["32 + 8", "1 * 3801", "99999 + 9999", "52aAA µ 49", "52aAA µ 49", "52aAA µ 49"])
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49", "523 - 49"])
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
arithmetic_arranger(["32 + 8", "1 * 3801", "99999 + 9999", "52aAA µ 49"])
arithmetic_arranger(["32 + 8", "1 * 3801", "99999 + 9999", "52aAA µ 49", "52aAA µ 49", "52aAA µ 49"])
