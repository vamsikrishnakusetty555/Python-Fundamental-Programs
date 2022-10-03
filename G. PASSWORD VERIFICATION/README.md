A website requires the users to input a username and password to register. Write a program to check the validity of password input by users. Following are the criteria for checking the password:

1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
3. At least 1 letter between [A-Z]
4. At least 1 character from [$#@]
5. Minimum length of transaction password: 6
6. Maximum length of transaction password: 12
Your program should accept a sequence of comma-separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.

Input Format:
The input consists of a single line string inputs separated by a comma(,).

Output Format:
The output consists of strings that satisfy the password condition separated by a comma(,). if there is no password that matches the condition, print "No password matches the condition".

Sample Input:
ABd1234@1, a F1#, 2w3E*, 2We3345

Sample Output:
ABd1234@1
