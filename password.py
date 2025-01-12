#import the neccessary library 
import tkinter as tk 

#Creating the GUI window storing the login window
Identifier = tk.Tk()
Identifier.geometry("800x500") 
Identifier.title("Employee Login")
Identifier.config(bg='gray')

#Label for the "username:"
InputUser = tk.Label(Identifier, text="Username:", font=("Times New Roman", 15))
InputUser.config(bg="gray")
InputUser.place(x = 300, y= 150)
#InputUser.pack() [geometry manager not needed; however this autocorrects to placement]



#Entry box in GUI that requires authentication for username input
user = tk.Entry(Identifier, width = 41)
user.place(x=295,y=180);

#Password Label 
InputUser = tk.Label(Identifier, text="Password:", font=("Times New Roman", 15))
InputUser.config(bg="gray")
InputUser.place(x = 300, y= 210)


#Password entry Authenticator
password = tk.Entry(Identifier, width = 41)
password.place(x = 295, y= 240);

#Welcoming Message
Welcome = tk.Label(Identifier, text="Welcome to Employee Login", font =("Times New Roman", 15))
Welcome.config(bg="gray")
Welcome.place(x = 300, y = 100)

#Stored variables 
username1 = "BugsBunny123"
password1 = "LooneyTunes98"

#Function testing for variables implemented and authenticating credentials the user inputs
def verified_input():
    val_corr = user.get()  
    pal_corr = password.get()
    if val_corr == username1 and pal_corr == password1:
           root = tk.Tk()
           root.geometry("500x500")
           root.title("Employee Directory")
           EmployeeHomePage = tk.Label(root, text="Welcome", font =("Times New Roman", 50) )
           EmployeeHomePage.place(x=120, y=150)
           
    else:
            Verify = tk.Label(Identifier, text = f'Access Denied Credentianls Not Found For: "{val_corr}"', 
            foreground = "red")
            Verify.place(x = 295, y = 295)  
            Verify.config(bg="gray")  
        
    print("Done!")



#Interactive button to run the function 'verified_input'       
validation = tk.Button(Identifier, text = "Validate", command=verified_input)
validation.place( x= 300, y= 265)

Identifier.mainloop()