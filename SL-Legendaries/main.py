#spec lookup dict
specs = {'1': 'beast_mastery', '2': 'marksmanship', '3': 'survival'}

genericLegendaries = []
beastMasteryLegendaries = []
marksmanshipLegendaries = []
survivalLegendaries = []

print('Please enter number for spec:')
for spec in specs:
    print(spec, specs[spec])
selection = input()
spec = specs.get(selection, None)
if spec == None:
    print('Invalid spec selected.')
    quit()
print("Do you want to include generic legendaries? y/n")
genericSelection = input()
print("What ilevel should the legendaries be?")
ilvlSelection = input()

with open(spec + '_legendaries' + '_ilvl' + ilvlSelection + '.simc', 'w') as outputfile:
    outputfile.write("##############################################################")
    outputfile.write("\n#Replace this with your desired base profile /simc etc \n")
    outputfile.write("##############################################################")
    outputfile.write("\ndefault_actions=1\n")

    writeProfile = ''

    outputfile.write(spec)

    outputfile.write(writeProfile)
print('Finished. Please find output in output file.')
