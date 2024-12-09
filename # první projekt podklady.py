# první projekt podklady
users = {
    "bob": "123",
    "ann" : "pass123",
    "mike": "password123",
    "liz": "pass123"
}
username = input("Zadej uživatelské jméno:")
pasword = input("Zadej heslo:")
if users.get(username) == pasword:
    print("Vítej v aplikaci", username)
    print("Máš 3 texty k analýze.")
else:
    print("Neplatné uživatelské jméno nebo heslo.")

