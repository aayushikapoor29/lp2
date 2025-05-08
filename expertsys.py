def expert_system():
    print("Welcome to MediBot! Please answer the following questions with yes or no.")

    fever = input("Do you have a fever? ").lower()
    cough = input("Do you have a cough? ").lower()
    headache = input("Do you have a headache? ").lower()
    body_pain = input("Do you have body pain? ").lower()
    sore_throat = input("Do you have a sore throat? ").lower()

    if fever == "yes" and cough == "yes" and body_pain == "yes":
        print("MediBot: You may have the flu. Please consult a doctor.")
    elif sore_throat == "yes" and cough == "yes":
        print("MediBot: You may have a throat infection.")
    elif fever == "yes" and headache == "yes":
        print("MediBot: You may have a viral infection.")
    else:
        print("MediBot: Your symptoms are not clear. Please see a doctor for proper diagnosis.")

expert_system()
