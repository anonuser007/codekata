ch = input("Enter any character: ")
if ch.isalpha():
 if(ch=='a' or ch=='A' or ch=='e' or ch=='E' or ch=='i' or ch=='I' or ch=='o' or ch=='O' or ch=='u' or ch=='U'):
    print(ch, "is a vowel.\n")
 else:
   print(ch, "is a consonant.\n")
else:
   print("Invalid!")
