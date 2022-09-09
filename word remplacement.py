def replace_word():
    str = "Salut copain, hi hi hi hi"
    word_to_replace = input("Entrer le mot à remplacer : ")
    word_replacement = input("Entrer le mot que vous voulez ajouter : ")
    print(str.replace(word_to_replace, word_replacement))

replace_word()