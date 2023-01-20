# Open the file "1.txt" in read mode
my_file = open("1.txt", "r")

# Read the contents of the file
data = my_file.read()

# Split the data into a list using newline as the delimiter
data_into_list = data.split("\n")

# Assign the first, second, and third elements of the list to separate variables
list1 = data_into_list[0]
list2 = data_into_list[1]
list3 = data_into_list[2]
list4 = data_into_list[3]
list5 = data_into_list[4]
list6 = data_into_list[5]
list7 = data_into_list[6]
number_amount = len(data_into_list)
reseting_theAccepets = int(number_amount) - 1
print(reseting_theAccepets)
# Concatenate the three user you want to check list{} lists and assign to a new variable
selected_list = list1+list2+list3+list4+list5+list6+list7

# iced list  List  and then made into a turple
Selected_List_Tuple =tuple(selected_list)
# Create an empty list to store the recommended users
listofsugetedUser = []

# Find the intersection of all the lists in the data file
userRemendation = set(list1).intersection(data_into_list)

# Print the intersection of the lists
print(userRemendation)

# Iterate over the selected list
for user in data_into_list:
    # If the user is not already in the list of recommended users, add it
    if  user  not in listofsugetedUser:
        listofsugetedUser.append(user)

# Print the list of recommended users
data_into_list = tuple(listofsugetedUser)


# Tuple displays the users in the networks connections


result_listofsugetedUser = str(data_into_list)# cahnges the infromation found from a list to a string
result_listofsugetedUser1 = result_listofsugetedUser.split('(')[1].split(')')[0] # formates the string

# Find the intersection of the list of recommended users and the selected list in the whole list not just the selected sets
userRemendation = set(list3).intersection(list1, list2, list3, list4, list5, list6)
setT_string = str(userRemendation)


#gives you the recommed set for the user  given to diffrent users freind list
#which user would you like to screach up prompt
# this gives you all poissble recomendation a user can get
#  make a input to ask the  users  which list they want to use and then  get the information and  replace list5 from below input("")
get_user_input = int(input(f"what is the user  you want to look up range 0 to {reseting_theAccepets}")) # get the input  for the user
users_first_Pick = data_into_list[get_user_input]
result = set(data_into_list[get_user_input]).symmetric_difference(set(list1))
result2 =  set(data_into_list[get_user_input]).symmetric_difference(set(list2))

result4 = set(data_into_list[get_user_input]).symmetric_difference(set(list3))
result5 = set(data_into_list[get_user_input]).symmetric_difference(set(list4))
result6 = set(data_into_list[get_user_input]).symmetric_difference(set(list5))
result7 = set(data_into_list[get_user_input]).symmetric_difference(set(list6))
result3_final = set(data_into_list[get_user_input]).symmetric_difference(set(selected_list))
# you need to put a while loop to shorten the amount of work needed to
string_res = str(result)
string_res1 = str(result2)
string_res3 = str(result4)
string_res4 = str(result5)
string_res5 = str(result6)
string_res6 = str(result7)
string_res2= str(result3_final)
# this changes and output from '2' to just 2 so it can be displayed
refactored_result2 = string_res1.replace("'", "")
refactored_result = string_res.replace("'", "")

refactored_result4 = string_res3.replace("'", "")
refactored_result5 = string_res4.replace("'", "")
refactored_result6 = string_res5.replace("'", "")
refactored_result7 = string_res6.replace("'", "")

final_total_recommadtion = string_res2.replace("'", "")




# use a emtpy list to first to gather  the input then append it into it
final_Recommendation_Count = [refactored_result, refactored_result2,refactored_result4, refactored_result5, refactored_result6, refactored_result7,final_total_recommadtion]
counter = -1
while counter < len(final_Recommendation_Count): # this statement is true ontill the conter hits 6 then the code will stop running
    recoresion = final_Recommendation_Count[counter]
    counter += 1
    if counter in range(len(final_Recommendation_Count)):  # if the intersection is not empty



          for inner_counter in range(len(recoresion)):

            string_final_Recommendation_Count = str(recoresion)
            format_output_of_Users1 = string_final_Recommendation_Count.split("',")
            format_output_of_Users1 = string_final_Recommendation_Count.strip("[]''")
            format_output_of_Users1 = string_final_Recommendation_Count.replace("'", "")
            format_output_of_Users_refactore = format_output_of_Users1.replace("[]", "''")


# this will take the  strings in formated user output and then  takes all excess
          cleaned_lst = [] # creates a list  basket which  can be used to store the information
          for intergers in format_output_of_Users_refactore: # for each number in  the list
            for element in intergers.split(','):# take the , out and formate it nicely

                  if element.isdigit():# when we hit a interger
                    cleaned_lst.append(int(element)) # save the interger to the created list ( cleaned list)

                    display_output = cleaned_lst
                    # we are trying to find a way to create a fucntion to better check the list and find out if
                    # the list is empyt if so dont display it and say user count is  dose not have any recommenations with
          if len(cleaned_lst) > 0:
                      print(str(cleaned_lst)+"  are the  user recommadation  after looking at  user : "+str(counter)+" to the given user :"+list6+"list6")
          elif len(cleaned_lst) == 0:
                        print(" no recommadation by user : " + str(
                            counter) + " to the given user :" + list6+"list6")

# get the user input and then uses it to  find the recommaned mate for the user  inputed but for list i
def mysingelUserReccomatio():
    loop_over_functionInputs = str(input("would you like to  check a persons recommaned mates yes or no  "))
    while loop_over_functionInputs == "yes":
      try:
        get_user_input = int(input("what is the user  you want to look up range 0:6"))  # get the input  for the user
        users_first_Pick = data_into_list[get_user_input]  # uses the input to navigater throug out the list
        final_output_Reccomation = set(users_first_Pick).symmetric_difference(
            set(selected_list))  # finds the diffrencresss
        final_output_str = ", ".join(final_output_Reccomation)  # stripps and formates the whole text given
        print(
            f" the user recomation for user {get_user_input}" + "are" + " " + final_output_str)  # output to users after\
        loop_over_functionInputs = str(input("would you like to  check another person yes or No "))
      except IndexError:
          print("not right noww boyyyyy")
# Convert the list elements to integers

mysingelUserReccomatio()


my_file.close()
