from instafollower import InstaFollower

username = input("Please provide your instagram username: ")
password = input("And your password also: ")
print("Almost done! just one more thing")
target = input("Please type the target instagram id(without any mistake): ")
print("Now the next input will determine weather you want to choose followers or following of the\n"
      "targeted id to either follow or unfollow.")
what = input("choose followers or following(Type f1 or f2): ")
print("This input will decide weather you want to follow them or unfollow")
what_to_do = input("Type 'fl' to follow or 'ufl' to unfollow: ")
print("for example if you chose f1 and fl that means the program will find all followers of the targeted id "
      "and follow them.\n"
      "Likewise if you chose f1 and ufl, then that means the program will find all followers or the targeted id "
      "and unfollow them.")
bot = InstaFollower()
bot.username = username
bot.password = password
bot.target_id = target
bot.login()

if what == "f1" and what_to_do == "fl":
    bot.find_followers()
    bot.follow()
elif what == "f1" and what_to_do == "ufl":
    bot.find_followers()
    bot.unfollow()
elif what == "f2" and what_to_do == "fl":
    bot.find_following()
    bot.follow()
elif what == "f2" and what_to_do == "ufl":
    bot.find_following()
    bot.unfollow()
else:
    print("Your provided wrong input! Try again.")
