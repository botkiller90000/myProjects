#Import statements
import os
import random
import time
#A function that clears the terminal
def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")
#prints and pauses lines
def print_pause(Line):
    print(Line)
    print(" ")
    time.sleep(2)
#a function to put space between sections in the story
def space():
    print(" ")
    print(" ")
    print(" ")
    print(" ")
#defines classes for game character attributes
class Character:
 def __init__(self, Name, Health, Money, Job, Skills, Class):
    self.Name = Name
    self.Health = Health
    self.Money = Money
    self.Job = Job
    self.Skills = Skills
    self.Class = Class
character = Character("Thomas O'Mally", 50, 10, "Factory Worker", {"Manual Labor":1}, "Lower-Class")
#Social Classes
economic_classes = ["Lower-Class", "Working-Class", "Lower-Middle Class", "Middle-Class", "Upper-Middle Class", "Upper-Class"]
#Define the winning and losing game conditions
def social_heiarchy(economic_class):
    character.Class = economic_class
    print(f"Updated:- Class: {character.Class}")
    #Win
    if character.Class == "Upper-Class":
      clear_terminal()
      print("You've won, Thanks for playing!")
      player_stats()
      print_pause("Would you like to play again ? (y, n)")
      play_again_choice = input("> ")
      if play_again_choice == "y":
          play_again()
      elif play_again_choice == "n":
          while True:
              break
      else:
          print("Please enter a choice between 1 or 2")
#function that prints player stats
def player_stats():
    print("Stats: ")
    print_pause(f"Health: {character.Health}")
    print_pause(f"Money: £{character.Money}")
    print_pause(f"Job: {character.Job}")
    print_pause(f"Skills: {character.Skills}")
    print_pause(f"Class: {character.Class}")
#create functions for money & health insrease and decrease and new skills 
def money_inc(amount_inc):
    character.Money += amount_inc 
    print(f"Updated:- Money: £{character.Money}(+{amount_inc})")
def money_dec(amount_dec):
    character.Money -= amount_dec
    print(f"Updated:- Money: £{character.Money}(-{amount_dec})")
    #Lose
    if character.Money < 0:
        print("You are in debt...")
        game_over()
def health_inc(health_amount_inc):
    character.Health += health_amount_inc 
    print(f"Updated:- Health: {character.Health}(+{health_amount_inc})")
def health_dec(health_amount_dec):
    character.Health -= health_amount_dec 
    print(f"Updated:- Health: {character.Health}(-{health_amount_dec})")
    if character.Health <= 0:
        print("Your health condition is critical...")
        game_over()
def new_skills(skill_name, skill_level=1):
    if skill_name in character.Skills:
        character.Skills[skill_name] += skill_level
    else:
        character.Skills[skill_name] = skill_level
    print(f"Added/Updated skill: {skill_name} to level {character.Skills[skill_name]}")
#Random events that may happen in the game
def random_event(self):
    events = [
        {"description": "Caught a Flu/Fever", "health": -10, "money": 0},
        {"description": "Found a hidden stash of money", "health": 0, "money": +15},
        {"description": "Gained new skills through hard work", "health": 0, "money": 0, "skills": {"Manual Labor": +1}},
        {"description": "Mugged on the street", "health": -5, "money": -5},
        {"description": "Attended a free public lecture", "health": 0, "money": 0, "skills": {"Education": +1}},
        {"description": "Caught typhoid from contaminated sewers", "health": 0},
        {"description": "Found a valuble item on the street", "money": +5},
        {"description": "Encounter a Noble", "skills": {"Networking": +1}},
        {"description": "Witness a Crime on the street & Reported it", "skills": {"Bravery": +1}},
        {"decription": "You see a Vestival on the street, So, You Celebrate", "health": +10, "money": -4, "skills": {"Socializing": 1}}
    ]  
    event = random.choice(events)
    print(f"Random Event: {event['description']}")
    self.health += event.get("health", 0)
    self.money += event.get("money", 0)
    for skill, increment in event.get("skills", {}).items():
        if skill in self.skills:
            self.skills[skill] += increment
        else:
            self.skills[skill] = increment
#Main Menu
def main_menu():
    while True:
        print("========================= Main Menu =========================")
        print_pause("1. Start Game")
        print_pause("2. Game Explanation & Rules")
        print_pause("3. Quit")
        main_menu_choice = input("> ")
        if main_menu_choice == "1":
            clear_terminal()
            game_run()
        elif main_menu_choice == "2":
            clear_terminal()
            game_exp()
            time.sleep(5)
            clear_terminal()
            main_menu()
        elif main_menu_choice == "3":
            break
        else:
            print("please enter a choice between 1 & 3.")
#Game Explanation
def game_exp():
    print("Game Explanation: ")
    print_pause("Your objective is to climb the ranks of the Victorian Socity and Escape poverty.")
    print_pause("You win by Getting to the Upper-Class of the Victorian Economy Classes.")
    print_pause("You may do that by choosing from different paths leading you to Greatness.")
    print_pause("You lose the game if at any time your £Money go in debt or you health is critical(0).")
    print_pause("On your Journey you gain skills from least valuble to most valuble.") 
    print_pause("Random events can happen any time in the game, Some are good some are bad.")
    print_pause("By experience and rising in ranks you can level up your skills 1 being default lowest and 3 being the highest.")
#start of game story
def game_run():
    print_pause("The Victorian Ascent...")
    print_pause("You play as Thomas O'Mally.")
    print_pause("A young man in his Twenties and a Determined worker in the tough streets of Victorian London.")
    print_pause("Driven by his passion to climb up the Victorian Social Hiearchy from the Lower-Class to be a Noble/Aristocrat in the Upper-Class.")
    print_pause("You will face a lot of challenges in your way up the Victorian Society.")
    print_pause("Always Remember, Your decisions and choices determine your fate.")
    space()
    # I, II, III, IV, V, VI, VII, VIII, IX, and X represent 1, 2, 3, 4, 5, 6, 7, 8, 9 and 10 respectively.
    print("Act(I): The Lower-Class")
    print_pause("The Humble Beginnings...")
    space()
    print("Thomas started his transfer as a worker in a textile factory during times of the Industrial Evolution.")
    print(" ")
    print_pause("He had to work long hours in harsh conditions and saftey neglections.")
    print(" ")
    player_stats()
    print(" ")
    print("He had to work for long hours getting little to no money, But it is a start.")
    print_pause("Early on in your Journey(Career), You have to make a really hard choice.")
    print_pause("1. Continue factory work in indoursing conditions, deteriorating health, But making a little money along the way.")
    print_pause("2. Seek Apprenticeship & Find work somewhere else.")
    print_pause("3. Join a Gang")
    print_pause("Choose between 1, 2, 3. Pick wisely!")
    early_choice = input("> ")
    if early_choice == "1":
        print_pause("Outcome: Thomas works hard but his health deteriorates slowly.")
        print_pause("He saves some money but is still stuck in a low paying job.")
        health_dec(10)
        money_inc(10)
        new_skills("Manual Labor", +1)
        space()
        print_pause("Act(II): Diverging Paths")
        print(" ")
        print_pause("Factory Worker: ")
        print_pause("Thomas contnues work in the Factory saving up some money & Making crucial decisions along the way.")
        print_pause("After some time at work in the factory, Thomas gets to know everyone there and is loved by the staff and gets a promotion to head of his department.")
        print_pause("All of that at the cost of his health, of course.")
        print_pause("After some time Thomas decides to make a daring move: ")
        print_pause("1. Unionize the workers under his name.")
        print_pause("2. Attend Night Classes & Invest in education.")
        print_pause("3. Enroll in illegal activites.")
        factory_choice = input("> ")
        if factory_choice == "1":
            print("Thomas decides to make a union with the workers, Improving working Conditions but risking conflicts among staff.")
            health_dec(10)
            money_inc(15)
            new_skills("Leadership", 1)
            social_heiarchy(economic_classes[3])
            space()
            print("Act(III): Middle-Class Ambitions")
            print_pause("Thomas is well beloved by the workers and made the textile factory one of the best in town.")
            print_pause("So, the workers Decide to ellect him as Union Leader of the factories!!")
            print(" ")
            random_event()
            print_pause("Union Leader: ")
            print_pause("Thomas becomes a note-worthy union leader, fighting for workers' rights & morality.")
            health_dec(5)
            money_inc(15)
            new_skills("Leadership", +1)
            character.Job = "Union Leader"
            social_heiarchy(economic_classes[4])
            random_event()
            space()
            print_pause("Act(IV): Upper-Middle Class Challenges")
            print(" ")
            print_pause("After some time, Thomas gets more and more popular, And has to make a Descicion.")
            print(" ")
            print_pause("1.Engage in politics using his fame from being a Union Leader.")
            print_pause("2.Use this Oppurtunity to steal his funding money and use the workers' money for his own Ambitions.")
            upperMiddleClass_choice = input("> ")
            if upperMiddleClass_choice == "1":
                print_pause("Thomas engages in Politics, Using his fame to advocate for workers' rights at a national level.")
                health_inc(10)
                money_inc(5)
                new_skills("Public Speach", +1)
                print_pause("With this new status Thomas decides to make another daring choice:" )
                print(" ")
                print_pause("1. Use his status to run for a seat in the city council.")
                print_pause("2. Raise awarness to the povery and Farewells becoming a philanthropist")
                political_choice = input("> ")
                if political_choice == "1":
                    print_pause("Thomas runs for a seat in the city council & wins, becoming an Important Political Leader there.")
                    health_inc(20)
                    money_inc(70)
                    new_skills("Politics", +2)
                    character.Job = "Political Leader"
                    social_heiarchy(economic_classes[5])
                elif political_choice == "2":
                    print_pause("Thomas raises awarness on the harsh conditions of the lower-classes becoming one of the most famous philanthropists in Victorian London.")
                    health_inc(40)
                    money_inc(50)
                    new_skills("Farewell", +2)
                    character.Job = "Philanthropist"
                    social_heiarchy(economic_classes[5])
                else:
                    print("Please enter 1 or 2 for choice.")
            elif upperMiddleClass_choice == "2":
                print_pause("You decided to take the funding money for yourself.")
                print_pause("You get caught & arrested, Your reputation goes low.")
                print_pause("The court puts you through 3 years of prison and maual labor.")
                print_pause("All your money was ceased.")
                character.Money = 0
            else:
                print("please enter 1 or 2 for choice.")
        elif factory_choice == "2":
            print("Thomas joins night classes to learn new skills, hoping to get a better job.")
            health_dec(5)
            money_dec(10)
            new_skills("Education", 1)
            social_heiarchy(economic_classes[2])
            space()
            print("Act(III): Middle-Class Ambitions")
            print(" ")
            print_pause("Thomas attends more and more night classes, Using his new education he changed his career to become an Educated Professional teaching accounting or law.")
            health_inc(10)
            money_inc(25)
            new_skills("Education", +1)
            character.Job = "Educated Professional"
            social_heiarchy(economic_classes[3])
            random_event()
            print(" ")
            print_pause("Act(IV): Upper-Middle Class Challenges")
            print(" ")
            random_event()
            print_pause("Using his education, Thomas decides he wants to make more out of it.")
            print_pause("He can decide between: ")
            print_pause("1. Use his education and work as a lawyer/accountant")
            print_pause("2. Diversify investments in the stock market.")
            print_pause("3. Investing in real estate in cities and buying land in the country")
            investment_choice = Input("> ")
            if investment_choice == "1":
                health_inc(5)
                money_inc(20)
                character.Job = "Lawyer/Accountant"
                social_heiarchy(economic_classes[4])
                print_pause("Thomas decides to work as a Lawyer/Accountant.")
                print_pause("He .....")
                print_pause("1. Work for a bigger Lawyer in town.")
                print_pause("2. Open his own Law office.")
                law_choice = input("> ")
                if law_choice == "1":
                    print_pause("You work hard for a lawyer in town and get promoted.")
                    print_pause("He had a daughter your age and you decide to marry into Nobility.")
                    social_heiarchy(economic_classes[5])
                elif law_choice == 2:
                    print_pause("You decide to open you own Law office..")
                    print_pause("You work hard and rise in the prestigious courts of Victorian London.")
                    print_pause("This Law office turns into a big buiseness getting hin to becoming a Noble.")
                    health_inc(10)
                    money_inc(100)
                    new_skills("Law", +2)
                    social_heiarchy(economic_classes[5])
                else:
                    print("Choose an option from 1 or 2")
            elif investment_choice == "2":
                print("You decide to invest your money in the stock market.")
                print_pause("At first, Everything goes well making a little profit..")
                print_pause("But after a while you get scammed out of your money due to lack of security & insurance in this era.")
                character.Money = 0
            elif investment_choice == "3":
                print("You decided to invest your money in realestate...")
                print_pause("With the upcoming rise in Housing in the city you make some profit but at the end you decide to settle in one of the lands in the Countryside.")
                print_pause("With your education you start off as a teacher of working hard.")
                print_pause("Then you make a choice: ")
                print_pause("Either 1.Work hard, Attend new classes & Earn skills. OR ")
                print_pause("2. Ditch Law and Accountment and Learning something new.")
                learning_choice = input("> ")
                if learning_choice == "1":
                    print("You decided to work hard and attend new night classes.")
                    health_dec(10)
                    money_dec(40)
                    new_skills("Education", +2)
                    print_pause("With your new education you become a Proffessor teaching law and accounting on a higher level.")
                    health_inc(20)
                    money_inc(70)
                    new_skills("Educated Proffessional", +2)
                    social_heiarchy(economic_classes[5])
                    random_event()
                elif learning_choice == "2":
                    print("You decided to learn a new skill, So you learned Chemistry.")
                    health_dec(10)
                    money_dec(30)
                    new_skills("Chemistry", +1)
                    print_pause("With your new chemistry knowlege you can persue a lot of paths but not with this Level, So: ")
                    print_pause("1. Invest more and Learn more chemistry.")
                    print_pause("2. Ditch that and take an easier, shorter but more dangerous route & Join the new rising Industry of the making of hard drugs.")
                    chemistry_choice = input("> ")
                    if chemistry_choice == "1":
                        print("You decide to Invest more in Chemistry education...")
                        health_dec(20)
                        money_dec(40)
                        print_pause(f"Your health decreases drastically from the studying and night classes late at night and so is your money.")
                        game_over()
                    elif chemistry_choice == "2":
                        print("You decided to take a more dangerous route here...")
                        print_pause("You start off working for a local gang...")
                        print_pause("You start making small amounts of cocaine at first selling them on the streets..")
                        health_dec(10)
                        money_inc(20)
                        new_skills("Stealth", +1)
                        print_pause("Your health decreases drastcallty from working with little to no money...")
                        print_pause("One day you hear a knock on the door, You open it's the police, You've been caugth.")
                        game_over()
                    else:
                        print("Please enter a choice between 1 or 2.")
                else:
                    print("please enter a choice between 1 or 2.") 
            else:
                   print("please enter a choice between 1 & 3.")
        elif factory_choice == "3":
            health_dec(15)
            money_inc(30)
            new_skills("Stealth", 1)
            print("Thomas decides to do illegal activities on the side to earn more money quickly.")
            space()
            print("Act(III): Middle-Class Ambitions")
            print_pause("Using the money he gained from illegal activities as trafficking Cocaine, Thomas buys a Factory becoming an Employer & Rising in Status.")
            health_inc(5)
            money_inc(40)
            new_skills("Business Managment", +2)
            character.Job = "Factory Owner"
            social_heiarchy(economic_classes[4])
            random_event()
            print_pause("You decide to traffick even more cocaine and use the factory as a way of money Laundring.")
            print_pause("You store the cocaine in one of the factory basements.")
            print_pause("You earn more and more money where you can't even launder the money anymore.")
            print_pause("You decide to: ")
            print_pause("1. Keep laundering money and trafficking the drugs.")
            print_pause("2. Go legal and terminate the drugs business")
            laundering_choice = input("> ")
            if laundering_choice == "1":
                print("You decided to keep laundering..")
                print_pause("The police get an eye on your tax records..")
                print_pause("They start watching you and gain evedince..")
                print_pause("They bribe one of your storage department workers, Joe...")
                print_pause("And Joe snitches..")
                print_pause("One day when unpacking some assets, you are surprised by a sudden Investigation.")
                print_pause("The officers say it's a routine...")
                print_pause("They found the drugs and you are caught.")
                game_over()
            elif laundering_choice == "2":
                print("You decided to shutdown the business and go legit...")
                print_pause("You grow your business with your laundered money, Expanding business and becoming a leading industrialist, making huge wealth..")
                health_inc(20)
                money_inc(200)
                new_skills("Business Managment", +1)
                character.Job = "Industrial Magnate"
                social_heiarchy(economic_classes[5])
            else:
                print("Please enter a choice between 1 or 2")
        else:
            print("Please enter a number between 1 & 3.")
    elif early_choice == "2":
        print_pause("Thomas finds an apprenticeship with a Blacksmith. He works with him in his smithery. His income is low at first but He gains valuble skills.")
        health_dec(5)
        money_dec(5)
        new_skills("Skilled Labor", 1)
        social_heiarchy(economic_classes[1])
        space()
        print_pause("Act(II): Diverging Paths")
        print(" ")
        print_pause("Thomas's apprenticesip opens up new oppurtunities as he learns valuble skills.")
        print_pause("Choices: ")
        print_pause("1. Open up own shop")
        print_pause("2. Specialize in weaponary")
        blackSmith_choice = input("> ")
        if blackSmith_choice == "1":
            print("Thomas decides to save money and opens his own blacksmith shop in a village, becoming a respected craftsman.")
            health_inc(5)
            money_inc(20)
            new_skills("Skilled Labor", +1)
            new_skills("Business Managment", 1)
            social_heiarchy(economic_classes[2])
            space()
            print("Act(III): Middle Class Aspirations: ")
            print_pause("Thomas wants to start building his community to expand his shop so that he can thrive, He: ")
            print_pause("1. Focus on crafting high-quality tools for local farmers and artisans.")
            print_pause("2. Start offering custom-made decorative items and ironwork for the wealthier villagers.")
            niche_choice = input("> ")
            if niche_choice == "1":
                print("You've decided to serve the farmers and artisans, a wide and loyal customer base.")
                print_pause("You build a reputation for making reliable and durable tools.")
                health_inc(5)
                money_inc(15)
                new_skills("Craftsmanship", +1)
                new_skills("Customer Relations", +1)
                social_heiarchy(economic_classes[1])
                random_event()
                print(" ")
                print(" ")
                print_pause("Act(III): Middle-Class Aspirations: ")
                print(" ")
                print_pause("Your business gets big but the customer base is very limited.")
                print_pause("Your business range is very limited to only the small village, But with very loyal recurring customers.")
                print_pause("You decide to: ")
                print_pause("1. keep your loyal customer base.")
                print_pause("2. Expand your business.")
                customer_choice = input("> ")
                if customer_choice == "1":
                    print("You've decided to keep your loyal customers.")
                    new_skills("Loyalty", 1)
                    print_pause("You keep serving you loyal customer base becoming a known blacksmith in town.")
                    print_pause("You decide to settle in this village and marry there.")
                    health_inc(20)
                    money_inc(15)
                    new_skills("Skilled Labor", +1)
                    new_skills("Social Life", +1)
                    character.Job = "Master Blacksmith"
                    social_heiarchy(economic_classes[3])
                    clear_terminal()
                    print("Your choices have lead thomas to a peaceful life in the village settling in his work and making a family.")
                    print_pause("Every once in a while Thomas decides to join in on philanthropist work in the village.")
                    health_inc(10)
                    new_skills("Philanthropy", +1)
                    new_skills("Farewell", +1)
                    print_pause("Thomas decides to satisfy his goals here and settle in the village being happy in the middle class with his family...")
                    print_pause("Thomas never reached the Upper-Class.")
                    game_over()
                elif customer_choice == "2":
                    print("You've decided to expnad your business.")
                    print_pause("You pack your stuff and move to the city...")
                    print_pause("You start off in the city by: ")
                    print_pause("1. seeking mentorship for other renowned blacksmithes there.")
                    print_pause("2. Start business right away with your knowledge and gain recognition by your old work.")
                    print_pause("3. Look for opportunities to innovate and create unique designs.")
                    city_choice = input("> ")
                    if city_choice == "1":
                        print("You decided to seek mentorship from other blacksmithes in the city.")
                        print_pause("You gain  substantial knwledge in the field of smithing.")
                        health_dec(5) 
                        money_dec(20)
                        new_skills("Smithing", +1)
                        print_pause("Now you start to work in the city gaining a lot of requests from your new knowledge.")
                        print_pause("Your new business starts to skyrocket..")
                        health_inc(10)
                        money_inc(30)
                        print_pause("You decide between 2 good choices here: ")
                        print_pause("1. Keep surving individual customers.")
                        print_pause("2. Start partnering with factories as a supplier.")
                        partner_choice = input("> ")
                        if partner_choice == "1":
                            print("You have decided to serve individual customers.")
                            print_pause("After sometime your business starts to fall off due to lack of Innovation and simialrity of products.")
                            print_pause("Your business so is your health start to fall off, You end up quitting.")
                            game_over()
                        if partner_choice == "2":
                            print("You decided to supply demand for textile factories, coal mines, etc.")
                            print_pause("Securing a safe job in the next decades or so.")
                            print_pause("You hire employees and staff for the job and you become a successfull CEO & Entrepreneur.")
                            health_inc(30)
                            money_inc(1000)
                            character.Job = "Entrepreneur"
                            social_heiarchy(economic_classes[5])
                        else:
                            print("please type a choice between 1 or 2")
                    elif city_choice == "2":
                        print("You decide to go in with you existing knowlwdge.")
                        print_pause("You relize that orders in the city are different and way more complex type of niche.")
                        print_pause("In your time in the city you get little to none orders.")
                        print_pause("After sometime you go bankrupt & lose your money.")
                        game_over()
                    elif city_choice == "3":
                        print("You decided to dive into a specific niche of a customer base with new innovative designs.")
                        print_pause("You first focus on making this design and launch it to customers.")
                        print_pause("It did horribly...")
                        print_pause("You make a fast decision to save the product.")
                        print_pause("1. Focus on increasing product quality.")
                        print_pause("2. Increasing product marketing efforts.")
                        product_choice = input("> ")
                        if product_choice == "1":
                            print("You decide to increase product quality and rely on reviews and word of mouth for advertisment and building a loyal customer base on the long run.")
                            print_pause("At first the sales are very low sometimes not making any profit but you trust the proccess.")
                            print_pause("It takes a tole on your money and health.")
                            health_dec(10)
                            money_dec(20)
                            print_pause("After sometime you start getting more sales and people love the high qualiy building a loyal customer base buying with profitable prices.")
                            print_pause("You become a famous Industrail Magnate.")
                            health_inc(30)
                            money_inc(100)
                            character.Job = "Industrial Maganate"
                            social_heiarchy(economic_classes[5])
                        elif product_choice == "2":
                            print("You decided to neglect quality and focus on marketing.")
                            print_pause("At first some people buy your product and news go about your product's horrible quality.")
                            print_pause("It is too late to save anything.")
                            game_over()
                        else:
                            print("please enter in a choice between 1 or 2")
                    else:
                        print("Please enter a number between 1 & 3")
                else:
                    print("Please enter a choice between 1 or 2")
            elif niche_choice == "2":
                print("You've decided to serve a wealthier market of people.")
                print_pause("A smaller but definitley wealthier niche with higher profits...")
                health_inc(10)
                money_inc(50)
                new_skills("Creativity", +1)
                new_skills("Custom Work", +1)
                social_heiarchy(economic_classes[3])
                print_pause("After sometime, You decide to take business to another level...")
                print_pause("1. Expand business")
                print_pause("2. Diversify product line to include fine metal furniture & household items.")
                expansion_choice = input("> ")
                if expansion_choice == "1":
                    print("You decide to expand your business by, ")
                    print_pause("1. Purchase more land to build a larger workshop and hire more staff.")
                    print_pause("2. Open a small storefront in the nearby town to attract more affluent customers.")
                    purshace_choice == input("> ")
                    if purshace_choice == "1":
                        print("You have decided to purshace more land and hire more staff.")
                        money_dec(70)
                        health_dec(40)
                        print_pause("That Increase in land and working cost too much plus the additional wages of the workers.")
                        print_pause("Without proper macinery, The proccess of making complex furniture and household items is way less efficient and time consuming.")
                        print_pause("You lose more and more customers with declining health and money.")
                        money_dec(20)
                        health_dec(10)
                        game_over()
                    elif purshace_choice == "2":
                        print("Outcome: Gain exposure to wealthier clients and boost sales.")
                        money_dec(10)
                        new_skills("Marketing", +1)
                        new_skills("Retail Management", +1)
                        print_pause("You gain more and more business managing a successfull smithing empire.")
                        character.Job = "Entrepreneur"
                        social_heiarchy(economic_classes[5])
                elif expansion_choice == "2":
                    print("You have decided to tap into new markets to attract diverse wealthy customer bases.")
                    health_inc(10)
                    money_inc(70)
                    new_skills("Diversification", +1)
                    new_skills("Innovation", +1)
                    print_pause("You decide to manage your growing business by investing in new machinery.")
                    print_pause("This led to improvement in efficiency and production speed.")
                    print_pause("It also cut the wages of workers as the machines took over.")
                    health_inc(5)
                    money_inc(200)
                    new_skills("Technological Advancement", +2)
                    new_skills("Efficiency", +2)
                    print_pause("You become a really successful business owner.")
                    character.Job = "business owner"
                    social_heiarchy(economic_classes[5])
                else:
                    print("Please enter a number between 1 or 2.")
            else:
                print("Please enter a Choice between 1 or 2")
            
        elif blackSmith_choice == "2":
            print("Thomas specializes in making weapons, Making swords, rifles, etc., gaining high profile clients and income.")
            money_inc(30)
            new_skills("Weapon Smithing", +1)
            social_heiarchy(economic_classes[2])
            space()
            print("Act(III): Middle Class Aspirations: ")
            print_pause("Thomas get known around the village making hunting knifes, spears and rifles for farmers.")
            print_pause("After sometime, Thomas wants to widen his business and gain more customers, He, ")
            print_pause("1. Collaborates with many factories & Hunting groups across the country and supply them with weaponary.")
            print_pause("2. Invest in building a Smithing school.")
            smithing_choice = input("> ")
            if smithing_choice == "1":
                print("You partnered with many factories & hunting communities becoming a staple in the industry.")
                health_inc(40)
                money_inc(300)
                social_heiarchy(economic_classes[5])
            elif smithing_choice == "2":
                print("You decide on building a smithing school.")
                print_pause("You host fundraisers and connect with Investors & in no time it is finished.")
                health_inc(20)
                print_pause("A lot of people enroll to learn a valuble skill in society.")
                money_inc(250)
                print_pause("You host farewells & do philanthropic work to help your community.")
                new_skills("Farewell", +1)
                new_skills("Philanthropy", +1)
                social_heiarchy(economic_classes[5])
            else:
                print("Please enter a number between 1 & 3")
        else:
            print("Please enter a choice between 1 or 2")
    elif early_choice == "3":
        health_dec(15)
        money_inc(20)
        new_skills("Stealth", +1)
        print_pause("Thomas decides upon joining a local gang on the streets of Victorian London")
        print_pause("Leading to Dangerous but pottentially lucrative oppurtunities.")
        space()
        print_pause("Act(II): Diverging Paths")
        print_pause("After sometime in the gang you decide to , ")
        print_pause("1. Take gang work more seriously.")
        print_pause("2. Betray the gang.")
        gang_choice = input("> ")
        if gang_choice == "1":
            print("You decided to rise in ranks and secure your place amongst the Crime Lords.")
            print_pause("You are taken apon a mission of huge drug trafficking.")
            print_pause("You are approached by Reginald Blackwood, a shady but influential figure in the East India Company.")
            print_pause("He offers you a chance on a high-stakes opium smuggling mission to Canton, China. Your task is to oversee the transport of a massive opium shipment and secure a lucrative deal with Chinese merchants.")
            print_pause("Do you accept the mission ? (y, n)")
            mission_choice = input("> ")
            if mission_choice == "y":
                print("You decided to accept the daring mission.")
                print_pause("You discover that Reginald has a hidden agenda. He plans to betray you to cover his own tracks if things go bad. You must now navigate the mission with the knowledge that your benefactor might be your biggest enemy.")
                print_pause("You set sail aboard the HMS Endeavour, a ship bound for China. Onboard, you encounter a diverse crew, including Captain Eliza Hawkins, a fierce and resourceful woman, and Dr. Henry Faulkner, a physician with a mysterious past. As you sail, you learn that a rival gang, led by the notorious Opium King, Li Wei, has also set its sights on the same shipment.")
                print_pause("Do you,")
                print_pause("1. Collaborate with the crew to outsmart Li Wei.")
                print_pause("2. Attempt to sabotage Li Wei's plans on your own.")
                liWei_choice = input("> ")
                if liWei_choice == "1":
                    print("you choose to collaborate, you uncover a traitor within your crew who is secretly working for Li Wei. Trust is shattered, and you must identify and neutralize the traitor before they jeopardize the mission.")
                    print_pause("Upon reaching Canton, you meet with Zhao Ling, a powerful Chinese merchant with connections to both the Emperor and the underworld. Negotiations are tense, and Zhao Ling demands a higher price than expected, leveraging the presence of Li Wei's gang as a bargaining chip.")
                    print_pause("You, ")
                    print_pause("1. Agree to Zhao Ling's terms and secure the deal.")
                    print_pause("2. Attempt to negotiate a better deal, risking angering Zhao Ling.")
                    zhaoLing_choice = input("> ")
                    if zhaoLing_choice == "1":
                        print(" you agree to Zhao Ling's terms, he reveals that he plans to double-cross both you and Li Wei, taking the opium for himself. You must now forge a temporary alliance with Li Wei to confront Zhao Ling and survive the ensuing conflict.")
                        print_pause("As the confrontation unfolds, Reginald Blackwood arrives unexpectedly, revealing his plan to kill both you and Li Wei, take the opium, and frame you for the entire operation. The final showdown is a chaotic melee of betrayal and shifting alliances.")
                        print_pause("You, ")
                        print_pause("1. Confront Reginald and expose his treachery.")
                        print_pause("2. Attempt to escape with the opium, leaving the chaos behind.")
                        confrontation_choice = input("> ")
                        if confrontation_choice == "1":
                            print("you confront Reginald, Captain Eliza Hawkins reveals her true allegiance to the Crown and helps you expose Reginald, leading to his arrest and a chance at redemption for you. If you escape, you find yourself pursued by both the British authorities and Li Wei’s gang, leading to a tense and uncertain future.")
                            print_pause("You become one of the biggest crime lords in Victorian London.")
                            character.Job = "Crime Lord"
                            social_heiarchy(economic_classes[5])
                        elif confrontation_choice == "2":
                            print("You attempt to escape with opium, Bribed few of thr crew members & promised a share of profit if you could run away.")
                            print_pause("You get out with the assets, flee to a far country & sell the assets & became rich.")
                            print_pause("You never had to work agian your entire life, Becoming the king pin of the Blackwood Mission.")
                            health_inc(50)
                            money_inc(2000)
                            social_heiarchy(economic_classes[5])
                        else:
                            print("please enter a choice between 1 or 2")
                    elif zhaoLing_choice == "2":
                        print("You start negotiating with the price angering Zhao Ling and not coming with a deal.")
                        print_pause("You go home and tell the upper-men in your gang.")
                        print_pause("Connections with the chinese merchants are cutt-off.")
                        print_pause("Mission Failed...")
                        game_over()
                    else:
                        print("Please enter a choice between 1 or 2")
                elif liWei_choice == "2":
                    print("You choose to sabotage him, Killing him with your crew.")
                    print_pause("His crew members find out sparking war between 2 gangs.")
                    print_pause("Mission Failed...")
                    game_over()
                else:
                    print("Please enter a number between 1 or 2.")
            elif mission_choice == "n":
                print("You have rejected the mission ,therefore kicked out of the gang and added to its Blacklist.")
                print_pause("You get robbed of your money, Living the rest of your life in poverty and fear of getting killed by one of the gang members.")
                game_over()
            else:
                print("Please enter a choice between 1 or 2")
        elif gang_choice == "2":
            print("You decided to betray the gang.")
            print_pause("You abort them to the police county and they get locked up.")
            print_pause("You didn't though as you were still a thug, low level person in the gang as you didn't take work so seriously.")
            print_pause("You got out with some warnings and misdemeanors.")
            health_inc(10)
            new_skills("Bravery", +1)
            new_skills("Reputation", +1)
            print_pause("With your new profound reputation and bravery, You get to meet important figures in your community.")
            new_skills("Networking", +1)
            print_pause("You start working for the government as an Informant.")
            character.Job = "Government Informant"
            social_heiarchy(economic_classes[4])
            print_pause("You do really good at your new job getting a promotion to a Government Agent.")
            print_pause("You marry a woman from a noble wealthy family securing your place among the greats.")
            health_inc(20)
            money_inc(70)
            social_heiarchy(economic_classes[5])
        else:
            print("Please enter a number between 1 or 2")
    else:
        print("Please enter a choice between 1 & 3..")
# Ensure the main menu runs when the script is executed
if __name__ == "__main__":
    main_menu()
#Play Again function
def play_again():   
    clear_terminal()
    main_menu()
#game over
#Game over function
def game_over():
    clear_terminal()
    print_pause("You've Lost!!")
    player_stats()
    print("Would you like to play again ? (y, n)")
    game_over_choice = input("> ")
    if game_over_choice == "y":
        play_again()
    else:
        while True:
            clear_terminal()
            print("Bye!, Thanks for playing.")
            break