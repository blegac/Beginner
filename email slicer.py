def main():
    print("Salut !")

    email = input("Quel est votre adresse email : ")

    (username, domain) = email.split("@")
    (domain, extension) = domain.split(".")

    print("Votre username :", username)
    print("Le domaine : ", domain)
    print("L'extension :", extension)

while True:
    main()