#Create variables with the input method and ask the user to input words
noun1 = input('Noun: ')
plural_noun1 = input('Plural Noun: ')
adjective1 = input('Adjective: ')
plural_noun2 = input('Plural Noun: ')
plural_noun3 = input('Plural Noun: ')
number = input('Number: ')
adjective2 = input('Adjective: ')
adjective3 = input('Adjective: ')
noun2 = input('Noun: ')
adjective4 = input('Adjective: ')
verb = input('Verb: ')
part_of_body = input('Part of body: ')
noun3 = input('Noun: ')
adjective5 = input('Adjective: ')
plural_noun4 = input('Plural Noun: ')
plural_noun5 = input('Plural Noun: ')

#The main paragraph with the variables in the text
The_Olympics = f'''
Every four years, countries from all over the {noun1} send their best {plural_noun1} 
to compete in {adjective1} games and win {plural_noun2}. These games are called the 
Olympic {plural_noun3}, and they started {number} years ago in {adjective2} Greece.
When a winner receives his or her {adjective3} medal at the games, the national {noun2}
of his or her country is played by a/an {adjective4} band. As the band {verb}, the citizens
of that country put their {part_of_body} to their chest and join in the singing of their
national {noun3}. Thanks to television, these {adjective5} events can now be watched by over
a billion {plural_noun4} throughout the world every four {plural_noun5}.
'''

#Print and show the paragraph to the user
print(The_Olympics)
