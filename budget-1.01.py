from forex_python.converter import CurrencyRates
import math
import time
income = 249.99
while income < 300:
########################################################################################################################################
#                                        Using This Script
#        
#                     The section below defines your fixed costs, housing, utitlites etc. 
#
#                      To add new costs to the calculator follow the steps below:
#
#                     Add in sigle quotes the name of the expence, colon : and then the amount of the expence
#                                           !!!!  IMPORTANT !!!!
#
#                       Ensure that every expence is followed by a comma , except for the last expence
#
#           These Costs are assumed to be monthly, aka per 2 periods, the amounts output for these will be 50% of their total costs
#
#                                   All Calculations are bassed on a 2 week period
#
########################################################################################################################################
    fixed_costs = {
        'housing': 280,
        'utilites':100,
        'internet':20
    }
#######################################################################################################################################
#                                           Flexable expencies
#                       This section is for calculating the expences that are not a fixed amount 
#                       Such as investments, savings, personal spending etc
#                       To add new flexable expencies follow the steps below:
#
#                        Add in single quotes the name of the expence, followed by a colon :
#               The number after the colon represents the percentage of the remaining budget you want to allocate to it
#                                   All of the numbers must add up to 1
#                                   0.1 will be 10%, 0.5 will be 50% etc
#
#                                 !!!! IMPORTANT !!!!!
#
#                       Ensure that every expence is followed by a comma , except for the lat expence
#
####################################################################################################################################

    flex_out = {
        'groceries':0.25,
        'stocks':0.15,
        'crypto':0.1,
        'savings':0.3,
        'personal':0.2

    }

###################################################################################################################################
#                               Threshhold for good budget
#
#                  In the section below, set the minimum amount you want made avalibule for groceries and the maximum
#                   By changing the values shown.
#
##################################################################################################################################
    groceries_min = 50
    groceries_max = 200
#####################################################################################################################################
#
#                                      Do not edit below this line
#
#####################################################################################################################################


    fixed_out = 0
    print('testing income level:',round(income,2))
    time.sleep(1)
    #print('What did you make this period in USD?')
    #income = input()
    #income = float(income)
    flex_total = 0
    invest_amounts = []
    for fc in fixed_costs:
        fixed_out= fixed_out + fixed_costs[fc]/2
        remain = income - fixed_out
    print('remaining is:', remain)
    if income <= fixed_out:
        print('fixed out is:',fixed_out)
        print('You didnt make enough to cover your base costs')
    else:
        if remain < groceries_min:
            print('You do not have enough for thre minimum set to buy groceries, you have $'+str(round(remain,2)),'remaining after paying your fixed costs')
        else:
            for keys,inv in flex_out.items():
                invest_value= remain*inv
                if keys == 'groceries':
                    if invest_value >= groceries_max:
                        invest_value = groceries_max
                        remain = remain-groceries_max
                    elif invest_value < groceries_min:
                        invest_value = groceries_min
                        remain = remain - groceries_min
                        if remain < 0.01:
                            print('///////////////////////////// Output ///////////////////////////////////////////////'+'\n')
                            print('Not enough income to invest this period')
                            break
                invest = keys,invest_value
                invest_amounts.append(invest)
            if remain >1:
                print('//////////////////////////Output //////////////////////////////////'+'\n')
            print('You will need to set aside USD: $'+str(round(fixed_out,2)),'From this periods earnings to cover your fixed costs')
            for i in invest_amounts:
                print('Your payment for '+i[0]+' this month in USD is: $'+str(round(i[1],2)))
    income +=0.01
    print('///////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

    

