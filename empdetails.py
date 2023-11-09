def employee(myname, id, number, company):
    print("emp name:", myname)

    print("emp id:", id)

    print("emp number:", number)

    print("emp company:", company)


while True:

    choice = input("choose a/b:")

    if choice.lower() == "a":

        myname = input("enter u r name : ")

        id = int(input("enter id:"))

        number = int(input("enter number:"))

        company = input("enter company name:")

        employee(myname, id, number, company)

    elif choice.lower() == "b":

        break

    else:

        print("work done");




