#!/usr/bin/env python3

#Define the list
my_list =  [ "192.168.0.5", 5060, "UP" ]
#Print the first , second , third items in the list iteratively
print("The first item in the list (IP): " + my_list[0] )
print("The second item in the list (port): " + str(my_list[1]) )
print("The last item in the list (state): " + my_list[2] )
new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]
print( "When I ", new_list[5], " into IP addresses ", str(new_list[3]), " or ", str(new_list[4]), " I am unable to ping ports ", str(new_list[0]), new_list[1], " or ", str(new_list[2]))