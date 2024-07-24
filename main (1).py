#A function that clears the terminal
import os
def clearTerminal():
    os.system("cls" if os.name == "nt" else "clear")    

#prints and pauses lines
import time
def printPause(Line):
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
economicClasses = ["Lower-Class", "Working-Class", "Lower-Middle Class", "Middle-Class", "Upper-Middle Class", "Upper-Class"]
#Define the winning and losing game conditions
def socialHiearchy(economicClass):
    character.Class = economicClass
    print(f"Updated:- Class: {character.Class}")
#function that prints player stats
def playerStats():
    print("Stats: ")
    printPause(f"Health: {character.Health}")
    printPause(f"Money: £{character.Money}")
    printPause(f"Job: {character.Job}")
    printPause(f"Skills: {character.Skills}")
    printPause(f"Class: {character.Class}")
#Game over function
def gameOver():
    clearTerminal()
    printPause("You've Lost!!")
    playerStats()
    print("Would you like to play again ? (y, n)")
    gameOverChoice = input("> ")
    if gameOverChoice == "y":
        playAgain()
    else:
        while True:
            clearTerminal()
            print("Bye!, Thanks for playing.")
            break
#Lose
if character.Money < -10:
    print("You are in severe debt...")
    gameOver()
    playAgain()
if character.Health <= 0:
    print("Your health condition is critical...")
    gameOver()
    playAgain()
#Win
if character.Class == economicClasses[5]:
  clearTerminal()
  print("You've won, Thanks for playing!")
  playerStats()
  printPause("Would you like to play again ? (y, n)")
  playAgainChoice = input("> ")
  if playAgainChoice == "y":
      playAgain()
  else:
      while True:
        break
#create functions for money & health insrease and decrease and new skills 
def moneyInc(amountInc):
    character.Money += amountInc 
    print(f"Updated:- Money: £{character.Money}(+{amountInc})")
def moneyDec(amountDec):
    character.Money -= amountDec
    print(f"Updated:- Money: £{character.Money}(-{amountDec})")
def healthInc(healthAmountInc):
    character.Health += healthAmountInc 
    print(f"Updated:- Health: {character.Health}(+{healthAmountInc})")
def healthDec(healthAmountDec):
    character.Health -= healthAmountDec 
    print(f"Updated:- Health: {character.Health}(-{healthAmountDec})")
def newSkills(skill_name, skill_level=1):
    if skill_name in character.Skills:
        self.skills[skill_name] += skill_level
    else:
        self.skills[skill_name] = skill_level
    print(f"Added/Updated skill: {skill_name} to level {self.skills[skill_name]}")

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
    import random
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
        printPause("1. Start Game")
        printPause("2. Game Explanation & Rules")
        printPause("3. Quit")
        mainMenuChoice = input("> ")
        if mainMenuChoice == "1":
            clearTerminal()
            gameRun()
        elif mainMenuChoice == "2":
            clearTerminal()
            gameExp()
            printPause("Do you want to start Game? (y,n)")
            gameExpChoice = input("> ")
            if gameExpChoice == "y":
                gameRun()
            elif gameExpChoice == "n":
                break
            else:
                print("Please enter y or n...")
        elif mainMenuChoice == "3":
            break
#Game Explanation
def gameExp():
    print("Game Explanation: ")
    printPause("Your objective is to climb the ranks of the Victorian Socity and Escape poverty.")
    printPause("You win by Getting to the Upper-Class of the Victorian Economy Classes.")
    printPause("You may do that by choosing from different paths leading you to Greatness.")
    printPause("You lose the game if at any time your £Money go in debt or you health is critical(0).")
    printPause("On your Journey you gain skills from least valuble to most valuble.") 
    printPause("Random events can happen any time in the game, Some are good some are bad.")
    printPause("By experience and rising in ranks you can level up your skills 1 being default lowest and 3 being the highest.")
#start of game story
def gameRun():
    printPause("The Victorian Ascent...")
    printPause("You play as Thomas O'Mally.")
    printPause("A young man in his Twenties and a Determined worker in the tough streets of Victorian London.")
    printPause("Driven by his passion to climb up the Victorian Social Hiearchy from the Lower-Class to be a Noble/Aristocrat in the Upper-Class.")
    printPause("You will face a lot of challenges in your way up the Victorian Society.")
    printPause("Always Remember, Your decisions and choices determine your fate.")
    space()
    # I, II, III, IV, V, VI, VII, VIII, IX, and X represent 1, 2, 3, 4, 5, 6, 7, 8, 9 and 10 respectively.
    print("Act(I): The Lower-Class")
    printPause("The Humble Beginnings...")
    space()
    print("Thomas started his transfer as a worker in a textile factory during times of the Industrial Evolution.")
    print(" ")
    printPause("He had to work long hours in harsh conditions and saftey neglections.")
    print(" ")
    playerStats()
    print(" ")
    print("He had to work for long hours getting little to no money, But it is a start.")
    printPause("Early on in your Journey(Career), You have to make a really hard choice.")
    printPause("1. Continue factory work in indoursing conditions, deteriorating health, But making a little money along the way.")
    printPause("2. Seek Apprenticeship & Find work somewhere else.")
    printPause("3. Join a Gang")
    printPause("Choose between 1, 2, 3. Pick wisely!")
    earlyChoice = input("> ")
    if earlyChoice == "1":
        printPause("Outcome: Thomas works hard but his health deteriorates slowly.")
        printPause("He saves some money but is still stuck in a low paying job.")
        healthDec(10)
        moneyInc(10)
        newSkills({"Manual Labor": +1})
        space()
        printPause("Act(II): Diverging Paths")
        print(" ")
        printPause("Factory Worker: ")
        printPause("Thomas contnues work in the Factory saving up some money & Making crucial decisions along the way.")
        printPause("After some time at work in the factory, Thomas gets to know everyone there and is loved by the staff and gets a promotion to head of his department.")
        printPause("All of that at the cost of his health, of course.")
        printPause("After some time Thomas decides to make a daring move: ")
        printPause("1. Unionize the workers under his name.")
        printPause("2. Attend Night Classes & Invest in education.")
        printPause("3. Enroll in illegal activites.")
        factoryChoice = input("> ")
        if factoryChoice == "1":
            print("Thomas decides to make a union with the workers, Improving working Conditions but risking conflicts among staff.")
            healthDec(10)
            moneyInc(15)
            newSkills({"Leadership": 1})
            socialHeiarchy(economicClasses[3])
            space()
            print("Act(III): Middle-Class Ambitions")
            printPause("Thomas is well beloved by the workers and made the textile factory one of the best in town.")
            printPause("So, the workers Decide to ellect him as Union Leader of the factories!!")
            print(" ")
            random_event()
            printPause("Union Leader: ")
            printPause("Thomas becomes a note-worthy union leader, fighting for workers' rights & morality.")
            healthDec(5)
            moneyInc(15)
            newSkills({"Leadership": +1})
            character.Job = "Union Leader"
            socialHeiarchy(economicClasses[4])
            random_event()
            space()
            printPause("Act(IV): Upper-Middle Class Challenges")
            print(" ")
            printPause("After some time, Thomas gets more and more popular, And has to make a Descicion.")
            print(" ")
            printPause("1.Engage in politics using his fame from being a Union Leader.")
            printPause("2.Use this Oppurtunity to steal his funding money and use the workers' money for his own Ambitions.")
            upperMiddleClassChoice = input("> ")
            if upperMiddleClassChoice == "1":
                printPause("Thomas engages in Politics, Using his fame to advocate for workers' rights at a national level.")
                healthInc(10)
                moneyInc(5)
                newSkills({"Public Speach": +1})
                printPause("With this new status Thomas decides to make another daring choice:" )
                print(" ")
                printPause("1. Use his status to run for a seat in the city council.")
                printPause("2. Raise awarness to the povery and Farewells becoming a philanthropist")
                politicalChoice = input("> ")
                if politicalChoice == "1":
                    printPause("Thomas runs for a seat in the city council & wins, becoming an Important Political Leader there.")
                    healthInc(20)
                    moneyInc(70)
                    newSkills({"Politics": +2})
                    character.Job = "Political Leader"
                    socialHeiarchy(economicClasses[5])
                elif politicalChoice == "2":
                    printPause("Thomas raises awarness on the harsh conditions of the lower-classes becoming one of the most famous philanthropists in Victorian London.")
                    healthInc(40)
                    moneyInc(50)
                    newSkills({"Farewell": +2})
                    character.Job = "Philanthropist"
                    socialHeiarchy(economicClasses[5])
                else:
                    print("Please enter 1 or 2 for choice.")
            elif upperMiddleClassChoice == "2":
                printPause("You decided to take the funding money for yourself.")
                printPause("You get caught & arrested, Your reputation goes low.")
                printPause("The court puts you through 3 years of prison and maual labor.")
                printPause("All your money was ceased.")
                character.Money = 0
                gameOver()
                playAgain()
            else:
                print("please enter 1 or 2 for choice.")
        elif factoryChoice == "2":
            print("Thomas joins night classes to learn new skills, hoping to get a better job.")
            healthDec(5)
            moneyDec(10)
            newSkills({"Education": 1})
            socialHeiarchy(economicClasses[2])
            space()
            print("Act(III): Middle-Class Ambitions")
            print(" ")
            printPause("Thomas attends more and more night classes, Using his new education he changed his career to become an Educated Professional teaching accounting or law.")
            healthInc(10)
            moneyInc(25)
            newSkills({"Education": +1})
            character.Job = "Educated Professional"
            socialHeiarchy(economicClasses[3])
            random_event()
            print(" ")
            printPause("Act(IV): Upper-Middle Class Challenges")
            print(" ")
            random_event()
            printPause("Using his education, Thomas decides he wants to make more out of it.")
            printPause("He can decide between: ")
            printPause("1. Use his education and work as a lawyer/accountant")
            printPause("2. Diversify investments in the stock market.")
            printPause("3. Investing in real estate in cities and buying land in the country")
            investmentChoice = Input("> ")
            if investmentChoice == "1":
                healthInc(5)
                moneyInc(20)
                character.Job = "Lawyer/Accountant"
                socialHeiarchy(economicClasses[4])
                printPause("Thomas decides to work as a Lawyer/Accountant.")
                printPause("He .....")
                printPause("1. Work for a bigger Lawyer in town.")
                printPause("2. Open his own Law office.")
                lawChoice = input("> ")
                if lawChoice == "1":
                    printPause("You work hard for a lawyer in town and get promoted.")
                    printPause("He had a daughter your age and you decide to marry into Nobility.")
                    socialHeiarchy(economicClasses[5])
                elif lawChoice == 2:
                    printPause("You decide to open you own Law office..")
                    printPause("You work hard and rise in the prestigious courts of Victorian London.")
                    printPause("This Law office turns into a big buiseness getting hin to becoming a Noble.")
                    healthInc(10)
                    moneyInc(100)
                    newSkills({"Law": +2})
                    socialHeiarchy(economicClasses[5])
                else:
                    print("Choose an option from 1 or 2")
            elif investmentChoice == "2":
                print("You decide to invest your money in the stock market.")
                printPause("At first, Everything goes well making a little profit..")
                printPause("But after a while you get scammed out of your money due to lack of security & insurance in this era.")
                character.Money = 0
                gameOver()
                playAgain()
            elif investmentChoice == "3":
                print("You decided to invest your money in realestate...")
                printPause("With the upcoming rise in Housing in the city you make some profit but at the end you decide to settle in one of the lands in the Countryside.")
                printPause("With your education you start off as a teacher of working hard.")
                printPause("Then you make a choice: ")
                printPause("Either 1.Work hard, Attend new classes & Earn skills. OR ")
                printPause("2. Ditch Law and Accountment and Learning something new.")
                learningChoice = input("> ")
                if learningChoice == "1":
                    print("You decided to work hard and attend new night classes.")
                    healthDec(10)
                    moneyDec(40)
                    newSkills({"Education": +2})
                    printPause("With your new education you become a Proffessor teaching law and accounting on a higher level.")
                    healthInc(20)
                    moneyInc(70)
                    newSkills({"Educated Proffessional": +2})
                    socialHeiarchy(economicClasses[5])
                    random_event()
                elif learningChoice == "2":
                    print("You decided to learn a new skill, So you learned Chemistry.")
                    healthDec(10)
                    moneyDec(30)
                    newSkills({"Chemistry": +1})
                    printPause("With your new chemistry knowlege you can persue a lot of paths but not with this Level, So: ")
                    printPause("1. Invest more and Learn more chemistry.")
                    printPause("2. Ditch that and take an easier, shorter but more dangerous route & Join the new rising Industry of the making of hard drugs.")
                    chemistryChoice = input("> ")
                    if chemistryChoice == "1":
                        print("You decide to Invest more in Chemistry education...")
                        healthDec(20)
                        moneyDec(40)
                        printPause(f"Your health decreases drastically from the studying and night classes late at night and so is your money.")
                        gameOver()
                        playAgain()
                    elif chemistryChoice == "2":
                        print("You decided to take a more dangerous route here...")
                        printPause("You start off working for a local gang...")
                        printPause("You start making small amounts of cocaine at first selling them on the streets..")
                        healthDec(10)
                        moneyInc(20)
                        newSkills({"Stealth": +1})
                        printPause("Your health decreases drastcallty from working with little to no money...")
                        printPause("One day you hear a knock on the door, You open it's the police, You've been caugth.")
                        gameOver()
                        playAgain()
                    else:
                        print("Please enter a choice between 1 or 2.")
                else:
                    print("please enter a choice between 1 or 2.") 
            else:
                   print("please enter a choice between 1 & 3.")
        elif factoryChoice == "3":
            healthDec(15)
            moneyInc(30)
            newSkills({"Stealth": 1})
            print("Thomas decides to do illegal activities on the side to earn more money quickly.")
            space()
            print("Act(III): Middle-Class Ambitions")
            printPause("Using the money he gained from illegal activities as trafficking Cocaine, Thomas buys a Factory becoming an Employer & Rising in Status.")
            healthInc(5)
            moneyInc(40)
            newSkills({"Business Managment": +2})
            character.Job = "Factory Owner"
            socialHeiarchy(economicClasses[4])
            random_event()
            printPause("You decide to traffick even more cocaine and use the factory as a way of money Laundring.")
            printPause("You store the cocaine in one of the factory basements.")
            printPause("You earn more and more money where you can't even launder the money anymore.")
            printPause("You decide to: ")
            printPause("1. Keep laundering money and trafficking the drugs.")
            printPause("2. Go legal and terminate the drugs business")
            launderingChoice = input("> ")
            if launderingChoice == "1":
                print("You decided to keep laundering..")
                printPause("The police get an eye on your tax records..")
                printPause("They start watching you and gain evedince..")
                printPause("They bribe one of your storage department workers, Joe...")
                printPause("And Joe snitches..")
                printPause("One day when unpacking some assets, you are surprised by a sudden Investigation.")
                printPause("The officers say it's a routine...")
                printPause("They found the drugs and you are caught.")
                gameOver()
                playAgain()
            elif launderingChoice == "2":
                print("You decided to shutdown the business and go legit...")
                printPause("You grow your business with your laundered money, Expanding business and becoming a leading industrialist, making huge wealth..")
                healthInc(20)
                moneyInc(200)
                newSkills({"Business Managment": +1})
                character.Job = "Industrial Magnate"
                socialHeiarchy(economicClasses[5])
            else:
                print("Please enter a choice between 1 or 2")
        else:
            print("Please enter a number between 1 & 3.")
    elif earlyChoice == "2":
        printPause("Thomas finds an apprenticeship with a Blacksmith. He works with him in his smithery. His income is low at first but He gains valuble skills.")
        healthDec(5)
        moneyDec(5)
        newSkills({"Skilled Labor": 1})
        socialHeiarchy(economicClasses[1])
        space()
        printPause("Act(II): Diverging Paths")
        print(" ")
        printPause("Thomas's apprenticesip opens up new oppurtunities as he learns valuble skills.")
        printPause("Choices: ")
        printPause("1. Open up own shop")
        printPause("2. Specialize in weaponary")
        blackSmithChoice = input("> ")
        if blackSmithChoice == "1":
            print("Thomas decides to save money and opens his own blacksmith shop in a village, becoming a respected craftsman.")
            healthInc(5)
            moneyInc(20)
            newSkills({"Skilled Labor": +1})
            newSkills({"Business Managment": 1})
            socialHeiarchy(economicClasses[2])
            space()
            print("Act(III): Middle Class Aspirations: ")
            printPause("Thomas wants to start building his community to expand his shop so that he can thrive, He: ")
            printPause("1. Focus on crafting high-quality tools for local farmers and artisans.")
            printPause("2. Start offering custom-made decorative items and ironwork for the wealthier villagers.")
            nicheChoice = input("> ")
            if nicheChoice == "1":
                print("You've decided to serve the farmers and artisans, a wide and loyal customer base.")
                printPause("You build a reputation for making reliable and durable tools.")
                healthInc(5)
                moneyInc(15)
                newSkills({"Craftsmanship": +1})
                newSkills({"Customer Relations": +1})
                socialHeiarchy(economicClasses[1])
                random_event()
                print(" ")
                print(" ")
                printPause("Act(III): Middle-Class Aspirations: ")
                print(" ")
                printPause("Your business gets big but the customer base is very limited.")
                printPause("Your business range is very limited to only the small village, But with very loyal recurring customers.")
                printPause("You decide to: ")
                printPause("1. keep your loyal customer base.")
                printPause("2. Expand your business.")
                customerChoice = input("> ")
                if customerChoice == "1":
                    print("You've decided to keep your loyal customers.")
                    newSkills({"Loyalty": 1})
                    printPause("You keep serving you loyal customer base becoming a known blacksmith in town.")
                    printPause("You decide to settle in this village and marry there.")
                    healthInc(20)
                    moneyInc(15)
                    newSkills({"Skilled Labor": +1})
                    newSkills({"Social Life": +1})
                    character.Job = "Master Blacksmith"
                    socialHeiarchy(economicClasses[3])
                    clearTerminal()
                    print("Your choices have lead thomas to a peaceful life in the village settling in his work and making a family.")
                    printPause("Every once in a while Thomas decides to join in on philanthropist work in the village.")
                    healthInc(10)
                    newSkills({"Philanthropy": +1})
                    newSkills({"Farewell": +1})
                    printPause("Thomas decides to satisfy his goals here and settle in the village being happy in the middle class with his family...")
                    printPause("Thomas never reached the Upper-Class.")
                    gameOver()
                    playAgain()
                elif customerChoice == "2":
                    print("You've decided to expnad your business.")
                    printPause("You pack your stuff and move to the city...")
                    printPause("You start off in the city by: ")
                    printPause("1. seeking mentorship for other renowned blacksmithes there.")
                    printPause("2. Start business right away with your knowledge and gain recognition by your old work.")
                    printPause("3. Look for opportunities to innovate and create unique designs.")
                    cityChoice = input("> ")
                    if cityChoice == "1":
                        print("You decided to seek mentorship from other blacksmithes in the city.")
                        printPause("You gain  substantial knwledge in the field of smithing.")
                        healthDec(5) 
                        moneyDec(20)
                        newSkills({"Smithing": +1})
                        printPause("Now you start to work in the city gaining a lot of requests from your new knowledge.")
                        printPause("Your new business starts to skyrocket..")
                        healthInc(10)
                        moneyInc(30)
                        printPause("You decide between 2 good choices here: ")
                        printPause("1. Keep surving individual customers.")
                        printPause("2. Start partnering with factories as a supplier.")
                        partnerChoice = input("> ")
                        if partnerChoice == "1":
                            print("You have decided to serve individual customers.")
                            printPause("After sometime your business starts to fall off due to lack of Innovation and simialrity of products.")
                            printPause("Your business so is your health start to fall off, You end up quitting.")
                            gameOver()
                            playAgain()
                        if partnerChoice == "2":
                            print("You decided to supply demand for textile factories, coal mines, etc.")
                            printPause("Securing a safe job in the next decades or so.")
                            printPause("You hire employees and staff for the job and you become a successfull CEO & Entrepreneur.")
                            healthInc(30)
                            moneyInc(1000)
                            character.Job = "Entrepreneur"
                            socialHeiarchy(economicClasses[5])
                        else:
                            print("please type a choice between 1 or 2")
                    elif cityChoice == "2":
                        print("You decide to go in with you existing knowlwdge.")
                        printPause("You relize that orders in the city are different and way more complex type of niche.")
                        printPause("In your time in the city you get little to none orders.")
                        printPause("After sometime you go bankrupt & lose your money.")
                        gameOver()
                        playAgain()
                    elif cityChoice == "3":
                        print("You decided to dive into a specific niche of a customer base with new innovative designs.")
                        printPause("You first focus on making this design and launch it to customers.")
                        printPause("It did horribly...")
                        printPause("You make a fast decision to save the product.")
                        printPause("1. Focus on increasing product quality.")
                        printPause("2. Increasing product marketing efforts.")
                        productChoice = input("> ")
                        if productChoice == "1":
                            print("You decide to increase product quality and rely on reviews and word of mouth for advertisment and building a loyal customer base on the long run.")
                            printPause("At first the sales are very low sometimes not making any profit but you trust the proccess.")
                            printPause("It takes a tole on your money and health.")
                            healthDec(10)
                            moneyDec(20)
                            printPause("After sometime you start getting more sales and people love the high qualiy building a loyal customer base buying with profitable prices.")
                            printPause("You become a famous Industrail Magnate.")
                            healthInc(30)
                            moneyInc(100)
                            character.Job = "Industrial Maganate"
                            socialHeiarchy(economicClasses[5])
                        elif productChoice == "2":
                            print("You decided to neglect quality and focus on marketing.")
                            printPause("At first some people buy your product and news go about your product's horrible quality.")
                            printPause("It is too late to save anything.")
                            gameOver()
                            playAgain()
                        else:
                            print("please enter in a choice between 1 or 2")
                    else:
                        print("Please enter a number between 1 & 3")
                else:
                    print("Please enter a choice between 1 or 2")
            elif nicheChoice == "2":
                print("You've decided to serve a wealthier market of people.")
                printPause("A smaller but definitley wealthier niche with higher profits...")
                healthInc(10)
                moneyInc(50)
                newSkills({"Creativity": +1})
                newSkills({"Custom Work": +1})
                socialHeiarchy(economicClasses[3])
                printPause("After sometime, You decide to take business to another level...")
                printPause("1. Expand business")
                printPause("2. Diversify product line to include fine metal furniture & household items.")
                expansionChoice = input("> ")
                if expansionChoice == "1":
                    print("You decide to expand your business by, ")
                    printPause("1. Purchase more land to build a larger workshop and hire more staff.")
                    printPause("2. Open a small storefront in the nearby town to attract more affluent customers.")
                    purshaceChoice == input("> ")
                    if purshaceChoice == "1":
                        print("You have decided to purshace more land and hire more staff.")
                        moneyDec(70)
                        healthDec(40)
                        printPause("That Increase in land and working cost too much plus the additional wages of the workers.")
                        printPause("Without proper macinery, The proccess of making complex furniture and household items is way less efficient and time consuming.")
                        printPause("You lose more and more customers with declining health and money.")
                        moneyDec(20)
                        healthDec(10)
                        gameOver()
                        playAgain()
                    elif purshaceChoice == "2":
                        print("Outcome: Gain exposure to wealthier clients and boost sales.")
                        moneyDec(10)
                        newSkills({"Marketing": +1})
                        newSkills({"Retail Management": +1})
                        printPause("You gain more and more business managing a successfull smithing empire.")
                        character.Job = "Entrepreneur"
                        socialHeiarchy(economicClasses[5])
                elif expansionChoice == "2":
                    print("You have decided to tap into new markets to attract diverse wealthy customer bases.")
                    healthInc(10)
                    moneyInc(70)
                    newSkills({"Diversification": +1})
                    newSkills({"Innovation": +1})
                    printPause("You decide to manage your growing business by investing in new machinery.")
                    printPause("This led to improvement in efficiency and production speed.")
                    printPause("It also cut the wages of workers as the machines took over.")
                    healthInc(5)
                    moneyInc(200)
                    newSkills({"Technological Advancement": +2})
                    newSkills({"Efficiency": +2})
                    printPause("You become a really successful business owner.")
                    character.Job = "business owner"
                    socialHeiarchy(economicClasses[5])
                else:
                    print("Please enter a number between 1 or 2.")
            else:
                print("Please enter a Choice between 1 or 2")
            
        elif blackSmithChoice == "2":
            print("Thomas specializes in making weapons, Making swords, rifles, etc., gaining high profile clients and income.")
            moneyInc(30)
            newSkills({"Weapon Smithing": +1})
            socialHeiarchy(economicClasses[2])
            space()
            print("Act(III): Middle Class Aspirations: ")
            printPause("Thomas get known around the village making hunting knifes, spears and rifles for farmers.")
            printPause("After sometime, Thomas wants to widen his business and gain more customers, He, ")
            printPause("1. Collaborates with many factories & Hunting groups across the country and supply them with weaponary.")
            printPause("2. Invest in building a Smithing school.")
            smithingChoice = input("> ")
            if smithingChoice == "1":
                print("You partnered with many factories & hunting communities becoming a staple in the industry.")
                healthInc(40)
                moneyInc(300)
                socialHeiarchy(economicClasses[5])
            elif smithingChoice == "2":
                print("You decide on building a smithing school.")
                printPause("You host fundraisers and connect with Investors & in no time it is finished.")
                healthInc(20)
                printPause("A lot of people enroll to learn a valuble skill in society.")
                moneyInc(250)
                printPause("You host farewells & do philanthropic work to help your community.")
                newSkills({"Farewell": +1})
                newSkills({"Philanthropy": +1})
                socialHeiarchy(economicClasses[5])
            else:
                print("Please enter a number between 1 & 3")
        else:
            print("Please enter a choice between 1 or 2")
    elif earlyChoice == "3":
        healthDec(15)
        moneyInc(20)
        newSkills({"Stealth": +1})
        printPause("Thomas decides upon joining a local gang on the streets of Victorian London")
        printPause("Leading to Dangerous but pottentially lucrative oppurtunities.")
        space()
        printPause("Act(II): Diverging Paths")
        printPause("After sometime in the gang you decide to , ")
        printPause("1. Take gang work more seriously.")
        printPause("2. Betray the gang.")
        gangChoice = input("> ")
        if gangChoice == "1":
            print("You decided to rise in ranks and secure your place amongst the Crime Lords.")
            printPause("You are taken apon a mission of huge drug trafficking.")
            printPause("You are approached by Reginald Blackwood, a shady but influential figure in the East India Company.")
            printPause("He offers you a chance on a high-stakes opium smuggling mission to Canton, China. Your task is to oversee the transport of a massive opium shipment and secure a lucrative deal with Chinese merchants.")
            printPause("Do you accept the mission ? (y, n)")
            missionChoice = input("> ")
            if missionChoice == "y":
                print("You decided to accept the daring mission.")
                printPause("You discover that Reginald has a hidden agenda. He plans to betray you to cover his own tracks if things go bad. You must now navigate the mission with the knowledge that your benefactor might be your biggest enemy.")
                printPause("You set sail aboard the HMS Endeavour, a ship bound for China. Onboard, you encounter a diverse crew, including Captain Eliza Hawkins, a fierce and resourceful woman, and Dr. Henry Faulkner, a physician with a mysterious past. As you sail, you learn that a rival gang, led by the notorious Opium King, Li Wei, has also set its sights on the same shipment.")
                printPause("Do you,")
                printPause("1. Collaborate with the crew to outsmart Li Wei.")
                printPause("2. Attempt to sabotage Li Wei's plans on your own.")
                liWeiChoice = input("> ")
                if liWeiChoice == "1":
                    print("you choose to collaborate, you uncover a traitor within your crew who is secretly working for Li Wei. Trust is shattered, and you must identify and neutralize the traitor before they jeopardize the mission.")
                    printPause("Upon reaching Canton, you meet with Zhao Ling, a powerful Chinese merchant with connections to both the Emperor and the underworld. Negotiations are tense, and Zhao Ling demands a higher price than expected, leveraging the presence of Li Wei's gang as a bargaining chip.")
                    printPause("You, ")
                    printPause("1. Agree to Zhao Ling's terms and secure the deal.")
                    printPause("2. Attempt to negotiate a better deal, risking angering Zhao Ling.")
                    zhaoLingChoice = input("> ")
                    if zhaoLingChoice == "1":
                        print(" you agree to Zhao Ling's terms, he reveals that he plans to double-cross both you and Li Wei, taking the opium for himself. You must now forge a temporary alliance with Li Wei to confront Zhao Ling and survive the ensuing conflict.")
                        printPause("As the confrontation unfolds, Reginald Blackwood arrives unexpectedly, revealing his plan to kill both you and Li Wei, take the opium, and frame you for the entire operation. The final showdown is a chaotic melee of betrayal and shifting alliances.")
                        printPause("You, ")
                        printPause("1. Confront Reginald and expose his treachery.")
                        printPause("2. Attempt to escape with the opium, leaving the chaos behind.")
                        confrontationChoice = input("> ")
                        if confrontationChoice == "1":
                            print("you confront Reginald, Captain Eliza Hawkins reveals her true allegiance to the Crown and helps you expose Reginald, leading to his arrest and a chance at redemption for you. If you escape, you find yourself pursued by both the British authorities and Li Wei’s gang, leading to a tense and uncertain future.")
                            printPause("You become one of the biggest crime lords in Victorian London.")
                            character.Job = "Crime Lord"
                            socialHeiarchy(economicClasses[5])
                        elif confrontationChoice == "2":
                            print("You attempt to escape with opium, Bribed few of thr crew members & promised a share of profit if you could run away.")
                            printPause("You get out with the assets, flee to a far country & sell the assets & became rich.")
                            printPause("You never had to work agian your entire life, Becoming the king pin of the Blackwood Mission.")
                            healthInc(50)
                            moneyInc(2000)
                            socialHeiarchy(economicClasses[5])
                        else:
                            print("please enter a choice between 1 or 2")
                    elif zhaoLingChoice == "2":
                        print("You start negotiating with the price angering Zhao Ling and not coming with a deal.")
                        printPause("You go home and tell the upper-men in your gang.")
                        printPause("Connections with the chinese merchants are cutt-off.")
                        printPause("Mission Failed...")
                        gameOver()
                        playAgain()
                    else:
                        print("Please enter a choice between 1 or 2")
                elif liWeiChoice == "2":
                    print("You choose to sabotage him, Killing him with your crew.")
                    printPause("His crew members find out sparking war between 2 gangs.")
                    printPause("Mission Failed...")
                    gameOver()
                    playAgain()
                else:
                    print("Please enter a number between 1 or 2.")
            elif missionChoice == "n":
                print("You have rejected the mission ,therefore kicked out of the gang and added to its Blacklist.")
                printPause("You get robbed of your money, Living the rest of your life in poverty and fear of getting killed by one of the gang members.")
                gameOver()
                playAgain()
            else:
                print("Please enter a choice between 1 or 2")
        elif gangChoice == "2":
            print("You decided to betray the gang.")
            printPause("You abort them to the police county and they get locked up.")
            printPause("You didn't though as you were still a thug, low level person in the gang as you didn't take work so seriously.")
            printPause("You got out with some warnings and misdemeanors.")
            healthInc(10)
            newSkills({"Bravery": +1})
            newSkills({"Reputation": +1})
            printPause("With your new profound reputation and bravery, You get to meet important figures in your community.")
            newSkills({"Networking": +1})
            printPause("You start working for the government as an Informant.")
            character.Job = "Government Informant"
            socialHeiarchy(economicClasses[4])
            printPause("You do really good at your new job getting a promotion to a Government Agent.")
            printPause("You marry a woman from a noble wealthy family securing your place among the greats.")
            healthInc(20)
            moneyInc(70)
            socialHeiarchy(economicClasses[5])
        else:
            print("Please enter a number between 1 or 2")
    else:
        print("Please enter a choice between 1 & 3..")
# Ensure the main menu runs when the script is executed
if __name__ == "__main__":
  main_menu()
#Play Again function
def playAgain():   
    clearTerminal()
    main_menu()