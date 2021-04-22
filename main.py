from game import game, resume
print ("""Welcome to the escape room.
Nothing will kill you here,
but you need to use your head""")
def menu():
  print("""
  Options:
  1. Start A New Game
  2. Enter A Game Code
  3. Quit""")
  choice = input(":")
  if int(choice) == 1:
    try:
      game()
    except Exception:
      print("Not Implemented")
  if int(choice) == 2:
    try:
      resume()
    except Exception:
      print("Not Implemented")
  if int(choice) == 3:
    try:
      quit()
    except Exception:
      print("Not Implemented")
while True:
  menu()