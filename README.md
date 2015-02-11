Instructions:
  1. Infection.py serves as the entry-point to the program, so begin by running from there.
  2. test.py is executed by main. It tests that total_infection gets every connected node. 
  3. test.py runs one instance of limited_infection, but the target number or entry node can be changed.
  
total_infection:
  This function uses the spread method to recursively distribute the infection to all students and coaches of all users.
  
limited_infection:
  When I made the first version of this function I simply modified total infection so that no infections would be done 
  once infections matched a global variable.
  
  This is of course not creative at all. It will lead to many classrooms with some students infected and others not.
  
  I remade the function so that it sorts the students and coaches of a user by the number of students they have. 
  These are added to an adjacency list as tuples in sorted order.
  
  Then the infection spreads recursively in this order, attempting to target users with the smaller number of students,
  so we can reach the target number.
