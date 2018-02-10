import csv
if __name__ == "__main__":

    #opening the supplied csv file in 'Read' mode
    with open('soccer_players.csv','r') as csvfile:

    #putting the contents of the csv file being read as OrderedDcitionary into a variable
        content = csv.DictReader(csvfile)

    #initializing two empty lists of experienced and inexperienced players
        players_with_experience = []
        no_experience = []

    #sorting the players into experienced and inexperienced players
        for columns in content.reader:
            if columns[2] == 'YES':
                players_with_experience.append(columns)
            elif columns[2] == 'NO':
                no_experience.append(columns)

    #initializing the list of the three teams
        sharks = []
        dragons = []
        raptors = []

    #populating the list of teams with equal team members including both experienced and inexperienced players
        for x in range(0,3):
            sharks.append(players_with_experience[x])
            sharks.append(no_experience[x])

        for x in range(3,6):
            dragons.append(players_with_experience[x])
            dragons.append(no_experience[x])

        for x in range(6,9):
            raptors.append(players_with_experience[x])
            raptors.append(no_experience[x])

    #Storing contents of list of teams into a string in order to write to file
    player_string = ''
    for items in sharks:
        for i in range(len(items)):
            player_string += items[i]
            player_string += ', '

        player_string += '\n'

    #Writing team information onto the txt file for sharks
    with open("teams.txt", "a") as my_file:
        my_file.write('Sharks \n')
        my_file.write(player_string)
        my_file.write('\n')

    player_string = ''
    for items in raptors:
        for i in range(len(items)):
            player_string += items[i]
            player_string += ', '

        player_string += '\n'

    #Writing team information onto the txt file for raptors
    with open("teams.txt", "a") as my_file:
        my_file.write('Raptors \n')
        my_file.write(player_string)
        my_file.write('\n')

    player_string = ''
    for items in dragons:
        for i in range(len(items)):
            player_string += items[i]
            player_string += ', '

        player_string += '\n'

    #Writing team information onto the txt file for dragons
    with open("teams.txt", "a") as my_file:
        my_file.write('Dragons \n')
        my_file.write(player_string)
        my_file.write('\n')
