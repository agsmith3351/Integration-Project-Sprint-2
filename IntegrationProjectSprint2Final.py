# Amanda Smith
# In this program I hope to give the user a better understanding of the rules of lacrosse
# a workout plan to help become game ready
# and any other needed information about lacrosse
print("Hello!" * 10)
# I used the string operator * to say hello ten times
print("This is Everything you need to know about Women's Lacrosse!")
name = input("What is your name? ")
print("Welcome " + name)
# I used the string operator + to join welcome and the variable name together
print("Let's get started with some important rules and information!")

number_of_players_on_field = input("How many players do you think are on the field at once?")
number_of_players_on_field = int(number_of_players_on_field)
print(12 == number_of_players_on_field)
print("The Correct Answer is 12")
goal_circle_question = input("Who is allowed in the goal crease, 1: the goalie 2: any player on the field")
goal_circle_question = int(goal_circle_question)
print(goal_circle_question == 1)
print("The correct answer is 1, only the goalie")
restraining_line = input("How many players must stay behind the restraining line while the ball is at one end?")
restraining_line = int(restraining_line)
print(restraining_line == 4)
print("The correct answer is 4")
seconds_rule = input(
    "How long is a defender allowed to stand in the 8 meter without being a sticks length away from an attacker?")
seconds_rule = int(seconds_rule)
print(seconds_rule == 3)
print("The correct answer is 3 seconds")
shooting_space = input(
    "What is the result of shooting space call in the 8 meter, 1: free possession 2: a free 8 meter shot")
shooting_space = int(shooting_space)
print(shooting_space == 2)
print("The correct answer is 2, an 8 meter shot")
# I plan on adding more rules in sprint 3

user_wants_to_learn = int(input("If you would like to see a fun fact type '2', if not type '1': "))
if user_wants_to_learn == 2:
    # I used == to determine if the input given was 2
    print("The modern rules of lacrosse date back to 1974")
    print("when they were drafted for a match between the Native American communities of Seneca and Mohawks.")
# This fact was found on https://www.explosion.com/132077/8-interesting-facts-about-lacrosse-you-didnt-know/


print("Now let's look at the total cost after buying equipment")
print("to make these calculations suitable for you google or find prices of these items that you would like to buy")
users_budget = input("Please enter your budget: ")
users_budget = float(users_budget)
goggles = input("How much do the pair of goggles you want cost? ")
goggles = float(goggles)
mouth_guard = input("How much does your mouth guard cost? ")
mouth_guard = float(mouth_guard)
stick_shaft = input("How much does that stick shaft you chose cost? ")
stick_shaft = float(stick_shaft)
stick_head = input("How much does the lacrosse stick head you chose cost? ")
stick_head = float(stick_head)
cleats = input("How much do your cleats cost? ")
cleats = float(cleats)
# I used + as addition to find the total cost of buying each item at said amount
overall_total = cleats + stick_head + stick_shaft + mouth_guard + goggles
print("Your total cost after purchasing all your lacrosse gear is: $", format(overall_total, '.2f'), sep="")
# I used an if/else statement to tell the code which output to produce
if overall_total > users_budget:
    print("This total is over your budget by ${:,.2f}".format(overall_total - users_budget))
else:
    print("This total is under your budget by ${:,.2f}".format(users_budget - overall_total))

print("Now let's go through a workout to get you game ready! ")
print("This Workout should be completed in 1 hour or less")
# I used flood division and modulus to do the mathematics
# to show how many minutes and how many seconds each exercise should take
print(60 // 5, "minutes", 60 % 5, "seconds, per exercise")
print("This workout is easy to stay consistent with because it only takes 1 hour out of your", 24 - 1, "!")
# I used - to show how many hours are left in the day after doing my lacrosse workout
print("Start with 3 sets of 20 passes with each hand ")
print(3 * 20, "reps")
# I used * multiplication to show a total of reps
print("Next do 50 ground ball pick ups in under 2 minutes", 120 / 60, "per second")
# I used division to calculate how many reps per second
print("Do 3 full field sprints twice so", 3 + 3, "total")
# I used addition to show the total amount of sprints to complete
print("Next practice shooting with 100 shots")
print("Practice cradling the ball while running")
print("Repeat all 5 exercises 5 times throughout the week so", 5 ** 2, "times total")
# I used ** to raise 5 to the second power to show 5 times itself twice


print("Lets start getting some statistics!")
print("Set a timer for one minute and count how many shots you make")
print("Repeat three times!")

# I am assigning these variables values outside of the for loop so they exist
shooting_average = 0
counter_of_shots = 0
player_name_for_shooting = input("Enter your name: ")
# I am using a for loop because I know how many values are going to be entered.
for value_input in range(3):
    shots_per_minute = int(input("Enter how many shots were made in one minute: "))
    counter_of_shots += shots_per_minute
    # I am using the variable counter to count up the values going into the variable shots_per_minute
shooting_average = counter_of_shots / 3
print("Name:", player_name_for_shooting)
print("Shooting Average:", format(shooting_average, '.2f'))
# I used format '.2f' so the average only displays two decimal points


if (shooting_average >= 0) and (shooting_average <= 25):
    print("This is a below average shooting average")
elif not (shooting_average < 25):
    print("This is a great shooting average!")

print("Now lets calculate your catching percentage")
print("Play wall ball for one minute and count how many passes are caught")
print("Type '-13' when you are done inputting caught passes")
num_of_caught_passes = int(input("Type number of caught passes: "))
counter_of_passes = 0
passing_average = 0
num_of_times_user_trys = 0
# I am using a while loop so the user can input as many numbers as they please
# I am using != 3 to stop the code when the user inputs number 3
while num_of_caught_passes != -13:
    counter_of_passes = counter_of_passes + num_of_caught_passes
    num_of_times_user_trys = num_of_times_user_trys + 1
    num_of_caught_passes = int(input("Type number of caught passes: "))
passing_average = counter_of_passes / num_of_times_user_trys
print("Passing Average:", format(passing_average, '.2f'))

# I used if, elif, and else to have three different possible outcomes depending on the players score
if 20 <= passing_average <= 40:
    print("This is a good passing average!")
elif passing_average > 40:
    print("This is a great passing average!")
else:
    print("This is a below average passing average")

if (shooting_average > passing_average) or (shooting_average >= passing_average):
    print("Your shooting average is better or equal to your passing average")
elif shooting_average < passing_average:
    print("Your passing average is greater than your shooting average")

print("Lets calculate the total amount of time participating in a game takes")


def total_amount_of_time_at_lax(game_time, half_time, warm_up, drive_time):
    total_time_spent = game_time + half_time + warm_up + drive_time
    print(total_time_spent, "minutes is your total time spent")
    return total_time_spent


wu = 60
dt = int(input("Enter your drive time to fields in minutes: "))
gt = 50
ht = 10
total_amount_of_time_at_lax(wu, gt, ht, dt)
