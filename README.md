# Finance_Management
Personal Finance Management application that should allow users to record and track their expenses.

Backend Technology Used: Django , Python
Frontend Technolofy Used : HTML, CSS , JavaScript

In this application we can create , edit , delete , search the expenses.

Actors on the scnece
1. Admin : can be created in two methods i) terminal using django-admin createsuperuser {providing name and passwod}
                                         ii) we can use login page where we enter as <username> sueperuser and passwrod
                                         
2. Member : can be created usnig login page we enter as <username> and passwrod


After loging in as Admin : 
        The admin can see all expenses of his own and others expenses . But the CRUD action is given for his own expenses. Another user button is also there to see all user of the applications.
        
After loging in as Member :

        The member can see only his expenses where he can perform CRUD actions.


Search by expense date is given to filter the expenses with respect to entered date.

And alse Search by expense name  is given to filter the expenses with respect to entered name of expense.


Page pagination is added . In one page max of 5 expenses can be seen and other are added in subsequent pages . prev and next navigation is added.


User can log out from application to change his username .



Hope This meets the requirements .

Thank you,
Pramod Naik
