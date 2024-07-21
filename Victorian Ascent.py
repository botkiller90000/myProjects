import os
import time

# A variable that defines the game running to make a game over function.
is_running = True

# A function that clears the terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


# Prints and pauses lines
def print_pause(line):
    print(line)
    print(' ')
    time.sleep(2)


# A function to put space between sections in the story
def space():
    print('\n' * 4)


# Defines classes for game character attributes
class Character:
    def __init__(self, name, health, money, job, skills, class_name):
        self.name = name
        self.health = health
        self.money = money
        self.job = job
        self.skills = skills
        self.class_name = class_name


character = Character(
    "Thomas O'Mally", 50, 10, "Factory Worker", {"Manual Labor": 1}, "Lower-Class"
)

# Social Classes
economic_classes = [
    "Lower-Class",
    "Working-Class",
    "Lower-Middle Class",
    "Middle-Class",
    "Upper-Middle Class",
    "Upper-Class",
]


# Define the winning and losing game conditions
def social_hierarchy(economic_class):
    character.class_name = economic_class
    print(f"Updated: Class: {character.class_name}")


# Function that prints player stats
def player_stats():
    print("Stats: ")
    print_pause(f"Health: {character.health}")
    print_pause(f"Money: £{character.money}")
    print_pause(f"Job: {character.job}")
    print_pause(f"Skills: {character.skills}")
    print_pause(f"Class: {character.class_name}")


# Game over function
def game_over():
    global is_running
    is_running = False
    clear_terminal()
    print("You've Lost!!")
    print(" ")
    player_stats()
    print("Would you like to play again? (y, n)")
    game_over_choice = input("> ")
    if game_over_choice == "y":
        play_again()
    else:
        while True:
            clear_terminal()
            print("Bye!, Thanks for playing.")
            break


# Play Again function
def play_again():
    global is_running
    clear_terminal()
    is_running = True


# Health increase function
def health_inc(value):
    character.health += value
    print_pause(f"Health increased by {value}. Current Health: {character.health}")


# Health decrease function
def health_dec(value):
    character.health -= value
    print_pause(f"Health decreased by {value}. Current Health: {character.health}")


# Money increase function
def money_inc(value):
    character.money += value
    print_pause(f"Money increased by £{value}. Current Money: £{character.money}")


# Money decrease function
def money_dec(value):
    character.money -= value
    print_pause(f"Money decreased by £{value}. Current Money: £{character.money}")


# Add new skills
def new_skills(skill_dict):
    character.skills.update(skill_dict)
    print_pause(f"New skills acquired: {skill_dict}")


# Random event placeholder
def random_event():
    print_pause("A random event occurs...")


# Game Explanation
def game_exp():
    print("Game Explanation: ")
    print_pause(
        "Your objective is to climb the ranks of the Victorian Society and "
        "escape poverty."
    )
    print_pause(
        "You win by getting to the Upper-Class of the Victorian Economic Classes."
    )
    print_pause(
        "You may do that by choosing from different paths leading you to greatness."
    )
    print_pause(
        "You lose the game if at any time your £Money goes in debt or your health "
        "is critical (0)."
    )
    print_pause("On your journey, you gain skills from least valuable to most valuable.")
    print_pause("Random events can happen any time in the game, some are good, some are bad.")
    print_pause(
        "By experience and rising in ranks you can level up your skills 1 being "
        "default lowest and 3 being the highest."
    )


# Start of game story
def game_run():
    print_pause("The Victorian Ascent...")
    print_pause("You play as Thomas O'Mally.")
    print_pause("A young man in his twenties and a determined worker in the tough streets of Victorian London.")
    print_pause(
        "Driven by his passion to climb up the Victorian Social Hierarchy from the "
        "Lower-Class to be a Noble/Aristocrat in the Upper-Class."
    )
    print_pause("You will face a lot of challenges in your way up the Victorian Society.")
    print_pause("Always remember, your decisions and choices determine your fate.")
    space()
    print("Act(I): The Lower-Class")
    print_pause("The Humble Beginnings...")
    space()
    print(
        "Thomas started his transfer as a worker in a textile factory during times "
        "of the Industrial Evolution."
    )
    print(" ")
    print_pause("He had to work long hours in harsh conditions and safety neglect.")
    print(" ")
    player_stats()
    print(" ")
    print(
        "He had to work for long hours getting little to no money, but it is a start."
    )
    print_pause(
        "Early on in your journey (career), you have to make a really hard choice."
    )
    print_pause(
        "1. Continue factory work in enduring conditions, deteriorating health, "
        "but making a little money along the way."
    )
    print_pause("2. Seek apprenticeship & find work somewhere else.")
    print_pause("3. Join a gang")
    print_pause("Choose between 1, 2, 3. Pick wisely!")
    early_choice = input("> ")
    if early_choice == "1":
        print_pause("Outcome: Thomas works hard but his health deteriorates slowly.")
        print_pause("He saves some money but is still stuck in a low paying job.")
        health_dec(10)
        money_inc(5)
        space()
        print("Act(II): Diverging Paths")
        print_pause("Thomas realizes he cannot continue like this forever.")
        print_pause(
            "He decides to take evening classes, improve his education, and look "
            "for better opportunities."
        )
        print_pause(
            "1. Continue working in the factory while attending night school."
        )
        print_pause("2. Look for a job as a clerk in a business office.")
        print_pause("3. Join a local union and fight for workers' rights.")
        factory_choice = input("> ")
        if factory_choice == "1":
            print("Thomas continues to work in the factory while attending night school.")
            health_dec(5)
            money_dec(5)
            new_skills({"Education": 1})
            social_hierarchy(economic_classes[3])
            space()
            print("Act(III): Middle-Class Ambitions")
            print_pause("Thomas gains new knowledge and skills, opening up new opportunities.")
            print(" ")
            random_event()
            space()
            print_pause("Union Leader:")
            print_pause("Thomas becomes a note-worthy union leader, fighting for workers' rights & morality.")
            health_dec(5)
            money_inc(15)
            new_skills({"Leadership": 1})
        elif factory_choice == "2":
            print("Thomas attends night classes to improve his education and broaden his skills.")
            health_dec(5)
            money_dec(5)
            new_skills({"Education": 1})
            social_hierarchy(economic_classes[3])
            space()
            print("Act(III): Middle-Class Ambitions")
            print_pause("With new knowledge and skills, Thomas decides to leave the factory job and apply for a better position.")
            print_pause("He secures a job as a clerk in a local business office.")
            print(" ")
            random_event()
            space()
            print_pause("Clerk: ")
            print_pause("Thomas works diligently at his new job, earning more money and furthering his education.")
            health_dec(5)
            money_inc(10)
            new_skills({"Clerical Work": 1})
        elif factory_choice == "3":
            print("Thomas enrolls in illegal activities, seeking quick money at the cost of his morals and safety.")
            health_dec(15)
            money_inc(25)
            new_skills({"Criminal Activities": 1})
            social_hierarchy(economic_classes[2])
            space()
            print("Act(III): Risk and Reward")
            print_pause("Thomas rises quickly in the underground world but faces constant danger and stress.")
            random_event()
            space()
            print_pause("Criminal: ")
            print_pause("Thomas navigates the risky life of crime, making powerful enemies and allies.")
            health_dec(10)
            money_inc(30)
            new_skills({"Negotiation": 1})
    elif early_choice == "2":
        print_pause("Outcome: Thomas leaves the factory to seek better opportunities as an apprentice.")
        print_pause("He learns new trades and skills, improving his future prospects.")
        health_dec(5)
        money_dec(5)
        new_skills({"Apprenticeship": 1})
        space()
        print("Act(II): Diverging Paths")
        print_pause("Thomas realizes that he needs to advance his skills further.")
        print_pause("He decides to explore different opportunities that come his way.")
        print_pause(
            "1. Work hard as an apprentice, mastering his craft and gaining experience."
        )
        print_pause("2. Take on an entrepreneurial venture, starting his own small business.")
                print_pause("3. Pursue a position in a local merchant's guild.")
        apprentice_choice = input("> ")
        if apprentice_choice == "1":
            print_pause("Thomas works diligently as an apprentice, gaining valuable skills and experience.")
            health_dec(5)
            money_inc(10)
            new_skills({"Craftsmanship": 1})
            social_hierarchy(economic_classes[2])
            space()
            print("Act(III): Skilled Artisan")
            print_pause("Thomas becomes a skilled artisan, respected in his trade.")
            random_event()
            space()
            print_pause("Artisan: ")
            print_pause("Thomas's craftsmanship earns him recognition and a stable income.")
            health_dec(5)
            money_inc(20)
            new_skills({"Reputation": 1})
        elif apprentice_choice == "2":
            print_pause("Thomas takes a risk and starts his own small business.")
            health_dec(5)
            money_dec(10)
            new_skills({"Entrepreneurship": 1})
            social_hierarchy(economic_classes[3])
            space()
            print("Act(III): Aspiring Entrepreneur")
            print_pause("Thomas faces many challenges but slowly grows his business.")
            random_event()
            space()
            print_pause("Entrepreneur: ")
            print_pause("Thomas's business begins to thrive, bringing in more money and new opportunities.")
            health_dec(5)
            money_inc(30)
            new_skills({"Business Management": 1})
        elif apprentice_choice == "3":
            print_pause("Thomas joins a local merchant's guild, hoping to climb the ranks.")
            health_dec(5)
            money_dec(5)
            new_skills({"Trade Skills": 1})
            social_hierarchy(economic_classes[3])
            space()
            print("Act(III): Guild Member")
            print_pause("Thomas becomes a prominent member of the merchant's guild.")
            random_event()
            space()
            print_pause("Guild Member: ")
            print_pause("Thomas's involvement in the guild brings him wealth and influence.")
            health_dec(5)
            money_inc(25)
            new_skills({"Networking": 1})
    elif early_choice == "3":
        print_pause("Outcome: Thomas joins a gang, seeking quick money and power.")
        print_pause("He learns the harsh realities of the criminal underworld.")
        health_dec(10)
        money_inc(20)
        new_skills({"Criminal Activities": 1})
        space()
        print("Act(II): The Dark Path")
        print_pause("Thomas quickly rises in the gang, but the risks grow with his power.")
        print_pause(
            "1. Continue climbing the ranks within the gang, accepting more dangerous tasks."
        )
        print_pause("2. Use his connections to start a legitimate business.")
        print_pause("3. Betray the gang and turn to the authorities.")
        gang_choice = input("> ")
        if gang_choice == "1":
            print_pause("Thomas takes on more dangerous tasks within the gang.")
            health_dec(15)
            money_inc(30)
            new_skills({"Intimidation": 1})
            social_hierarchy(economic_classes[1])
            space()
            print("Act(III): Gang Leader")
            print_pause("Thomas becomes a feared and respected gang leader.")
            random_event()
            space()
            print_pause("Gang Leader: ")
            print_pause("Thomas's power grows, but so does the danger around him.")
            health_dec(10)
            money_inc(40)
            new_skills({"Leadership": 1})
        elif gang_choice == "2":
            print_pause("Thomas uses his criminal connections to start a legitimate business.")
            health_dec(5)
            money_dec(10)
            new_skills({"Entrepreneurship": 1})
            social_hierarchy(economic_classes[3])
            space()
            print("Act(III): Reformed Entrepreneur")
            print_pause("Thomas faces many challenges but slowly grows his legitimate business.")
            random_event()
            space()
            print_pause("Reformed Entrepreneur: ")
            print_pause("Thomas's business begins to thrive, bringing in more money and new opportunities.")
            health_dec(5)
            money_inc(30)
            new_skills({"Business Management": 1})
        elif gang_choice == "3":
            print_pause("Thomas betrays the gang and turns to the authorities.")
            health_dec(5)
            money_dec(5)
            new_skills({"Witness Protection": 1})
            social_hierarchy(economic_classes[2])
            space()
            print("Act(III): The Informant")
            print_pause("Thomas becomes an informant, living a life of constant danger and secrecy.")
            random_event()
            space()
            print_pause("Informant: ")
            print_pause("Thomas's information helps the authorities, but he must always watch his back.")
            health_dec(10)
            money_inc(20)
            new_skills({"Survival": 1}")

def main():
    clear_terminal()
    game_exp()
    while is_running:
        game_run()

if __name__ == "__main__":
    main()

