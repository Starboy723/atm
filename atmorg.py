def owner(data):
  if data=="7981602710":
    print("▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎\n▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎")
    print("NAME : CHERUKU RAHUL\nACCOUNT NO : 7981602710\nTYPE : SAVINGS ACCOUNT\nTOTAL BALANCE :",Tamount,"\nBRANCH : WARANGAL\nGMAIL : RAHULCHERUKU@GMAIL.COM ")
    print("▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎\n▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎")
  elif data=="8328307454":
     print("▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎\n▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎")
     print("NAME : AMARAKONDA RAVINDER\nACCOUNT NO : 8328307454\nTYPE : SAVINGS ACCOUNT\nTOTAL BALANCE :",Tamount,"\nBRANCH : KESHAVAPATNAM\nGMAIL : AMARAKONDARAVINDER@GMAIL.COM")
     print("▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎\n▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎")
  elif data=="6300234453":
     print("▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎\n▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎")
     print("NAME : GUNDA VENKATA SAI\nACCOUNT NO : 6300234453\nTYPE : SAVINGS ACCOUNT\nTOTAL BALANCE :",Tamount,"\nBRANCH : GODAVARIKHANI\nGMAIL : GVENKATSAI2003GMAIL.COM")
     print("▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎\n▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎")
  else:
     print("***SORRY BRO!!!INDHULO NI INFORMATION SAVE CHEYALE***")
Tamount=10000
wamount=0
d=0
w=0
a=0
pin=0
pin1=0
count=0
pin2=0
choice1=0
oldpin="1234"
newpin="1234"
print("    WELCOME TO\n   YONO SBI ATM\n")
accno=input("PLEASE ENTER ACCOUNT NUMBER(your phone number): ")
while accno.isnumeric()!=True or len(accno)!=10:
     accno=input("PLEASE ENTER VALID ACCOUNT NUMBER: ")
accpin=accno[6:]
while choice1!=7:
 print("")
 print("1>>>WITHDRAW     2>>>DEPOSIT\n3>>>TRANSFER",end="")
 print("     4>>>BALANCE\n5>>>PIN CHANGE",end="")
 print("   6>>>ACCOUNT INFORMATION\n7>>>EXIT")
 choice=input("ENTER YOUR CHOICE:")
 if choice.isnumeric()==False:
   print("CHOOSE VALID CHOICE")
 elif int(choice)<=7:
   choice1=int(choice)
   if choice1==1:
     print("")
     print("***YOU CHOOSEN WITHDRAW SERVICE**")
     w=input("ENTER AMOUNT TO WITHDRAW: ")
     while w.isnumeric()!=True or int(w)>Tamount:
       if w.isnumeric()==True:
        if int(w)>Tamount:
         print("INSUFFICIENT AMOUNT!!!(avaliable balance:",Tamount,")")
         w=input("ENTER AMOUNT TO WITHDRAW: ")
       else:
         print("ENTER VALID AMOUNT!!")
         w=input("ENTER AMOUNT TO WITHDRAW: ")
     pin=input("ENTER 4 DIGIT PIN: ")  
     while pin!=accpin or pin.isnumeric()!=True:
         print("PLEASE ENTER CORRECT PIN !!")
         if count<=0:
          pin=input("ENTER 4 DIGIT PIN(Last 4 digits of ur account no): ")
         else:
           pin=input("ENTER 4 DIGIT PIN: ")
     wamount=int(w)
     Tamount-=int(wamount)
     print("")      
     print("***WITHDRAWN AMOUNT: ",wamount,"***")
   elif choice1==2:
      print("")
      print("***YOU CHOOSEN DEPOSIT SERVICE***")
      d=input("ENTER AMOUNT TO DEPOSIT: ")
      while d.isnumeric()!=True:
        print("ENTER VALID AMOUNT: ")
        d=input("ENTER AMOUNT TO DEPOSIT: ")
      pin1=input("ENTER 4 DIGIT PIN: ")
      while pin1.isnumeric()!=True or pin1!=accpin:
        print("PLEASE ENTER CORRECT PIN!!")
        pin1=input("ENTER 4 DIGIT PIN: ")
      Tamount+=int(d)
      print("")
      print("***DEPOSITED AMOUNT: ",d,"***")
   elif choice1==3:
       print("")
       print("***YOU CHOOSEN TRANSFER SERVICE***")
       num=input("ENTER ACCOUNT NUMBER TO TRANSFER: ")
       while len(num)!=10 or num.isnumeric()!=True or num==accno:
          #num=input("ENTER VALID ACCOUNT NUMBER: ")
          if num==accno:
            print("YOU CANNOT BE TRANSFER MONEY TO SAME ACCOUNT!!!")
            num=input("ENTER DIFFERENT ACCOUNT NUMBER: ")
          else:
            num=input("ENTER VALID ACCOUNT NUMBER: ")
       print("ACCOUNT NUMBER: ",num)
       num1=input("ENTER AMOUNT: ")
       while num1.isnumeric()!=True or int(num1)>Tamount:
        if num1.isnumeric()==True:
         if int(num1)>Tamount:
          print("INSUFFICIENT AMOUNT!!!(avaliable balance:",Tamount,")")
          num1=input("ENTER AMOUNT TO TRANSFER: ")
        else:
          print("ENTER VALID AMOUNT!!")
          num1=input("ENTER AMOUNT TO TRANSFER: ")
       Tamount-=int(num1)
       pin2=input("ENTER 4 DIGIT PIN:")
       while pin2.isnumeric()!=True or pin2!=accpin:
         pin2=input("PLEASE ENTER CORRECT PIN:")
       print("")
       print("SUCCESSFULLY AMOUNT",num1,"TRANSFERRED TO:",num)
   elif choice1==4:
      print("")
      print("***YOU CHOOSEN BALANCE SERVICE***")
      pin3=input("ENTER 4 DIGIT PIN: ")
      while pin3!=accpin:
        pin3=input("ENTER CORRECT PIN: ")
      #Tamount-=int(wamount)+int(d)
      print("")
      print("***TOTAL BALANCE: ",Tamount,"***")
   elif choice1==5:
     print("")
     print("***YOU SELECTED PIN CHANGE***")
     oldpin=input("ENTER OLD 4 DIGIT PIN: ")
     while oldpin.isnumeric()!=True or oldpin!=accpin:
       print("ENTER CORRECT OLD PIN!!!")
       oldpin=input("ENTER OLD 4 DIGIT PIN: ")
     newpin=input("ENTER NEW 4 DIGIT PIN: ")
     while newpin==oldpin:
       if newpin==oldpin:
          print("OLD PIN NEW PIN CANNOT BE SAME")
          newpin=input("ENTER 4 DIGIT NEW PIN:")
     while newpin.isnumeric()!=True or len(newpin)!=4:
          print("ENTER VALID PIN!!!")
          newpin=input("ENTER 4 DIGIT NEW PIN: ")
          if newpin==oldpin:
             print("OLD PIN NEW PIN CANNOT BE       SAME")
             newpin=input("ENTER 4 DIGIT NEW PIN: ")         
     accpin=newpin
     count+=int(1)
     print("")
     print("***PIN SUCCESSFULLY CHANGED***")
   elif choice1==6:
      print("")
      print("***YOU CHOOSEN ACCOUNT INFORMATION***")
      ownerpin=input("ENTER YOUR 4 DIGIT PIN: ")
      while ownerpin!=accpin:
        ownerpin=input("ENTER CORRECT PIN: ")
      owner(accno)
 else:
   print("CHOOSE VALID CHOICE")
print("")
print("***THANK YOU FOR VISITING***")
     