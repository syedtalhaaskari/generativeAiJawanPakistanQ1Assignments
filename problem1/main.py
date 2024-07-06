# create a text file and add the below content without quotation marsk
"""
Hi *user*!

We've found the best article for you based on your interest: *title*
Please click *here* to open the article
"""

# task is to read the above file and update the placeholder i.e *user*, *title* and *here*
# and store the updated content in user_email.txt
# run program three times with different name, title and link

# after running the program three times
# the file user_email.txt must have all three users content


fields = ['Name', 'Title', 'Link']

name = input('Please enter your name: ') or 'Anonymous'
interest = input('Please enter your interest: ') or 'Unknown'
link = name.replace(' ', '_') + interest.replace(' ', '_') + '.com'

f = open('blueprint.txt', 'r')

data = f.read()

updated_data = data.replace('*user*', name).replace('*title*', interest).replace('*here*', link) + '\n\n'

f.close()

f = open('user_email.txt', 'a')

f.write(updated_data)

f.close()

print('Content updated successfully in user_email.txt file.')
