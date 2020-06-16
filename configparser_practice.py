import configparser

#Create a config object
config = configparser.ConfigParser({
    'Type': 'Business',
    'Mode': 'Dark',
    'Updated': True
})

#write to a configuratioon file
with open('whatsapp.txt', 'w') as f:
    config.write(f)

#read from a configuration file
whatsapp1 = config.read('whatsapp.txt')

with open('whatsapp.txt', 'r') as f:
    whatsapp2 = config.read_file(f)

#check that a section exists in a configuration file
config.has_section('Mode')

#check that a option exists in a configuration file
config.has_option('Mode', 'Dark')

#lets have all the sections in this configuration file
sections = config.sections()

#lets have all the options under a section
#options = config.options('Mode')

#remove a seection from a config file
whatsapp1_no_mode = config.remove_section('Mode')

#remove an option from a section
#whatsapp1_no_mode_value = config.remove_option('Mode', 'Dark')

#return items in a section
#whatsapp1_mode = config.items('Mode')