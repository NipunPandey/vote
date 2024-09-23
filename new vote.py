def vote_eligibility():
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You are eligible to vote.")
        print("Here are your options: ")
        print("1. BJP")
        print("2. Congress")
        print("3. NOTA (None of the above)")
        vote = int(input("Enter your choice (1/2/3): "))
        if vote == 1:
            print("You voted for BJP.")
        elif vote == 2:
            print("You voted for Congress.")
        elif vote == 3:
            print("You chose NOTA.")
        else:
            print("Invalid choice. Please vote for BJP, Congress, or NOTA.")
    else:
        print("You are not eligible to vote.")

vote_eligibility()

