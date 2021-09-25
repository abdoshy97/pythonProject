class StringOerations:
    def reverse(self,to_be_reversed:str=None):
        print(str(to_be_reversed)[::-1])




class ReversedString(StringOerations):
    def rev(self,revers):
        StringOerations.reverse(self,revers)



rs=ReversedString()
revers=rs.rev("abdoshy")

#If you want the user to enter the value of the variable, this is the code
'''
class StringOerations:
    def reverse(self,to_be_reversed:str=None):
        print('the reverse is',str(to_be_reversed)[::-1])




class ReversedString(StringOerations):
    def rev(self,revers):
        StringOerations.reverse(self,revers)


text=input("Enter your text to reverse :")
rs=ReversedString()
revers=rs.rev(text)
'''