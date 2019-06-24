import requests
from os import system
from bs4 import BeautifulSoup as bs


def format_link(link):
	output = ""
	for char in link:
		if char == "›":
			output += "/"
		elif char == " ":
			output += ""
		else:
			output += char
	return output+' \n\t[support me] (http://github.com/ianwright27)'


def filter(src):
	soup = bs(src, 'html5lib')
	containers = soup.find_all('div',{'class':'ZINbbc xpd O9g5cc uUPGi'})
	print('\nGoogle Results:\n')
	for container in range(0,len(containers)):
		if container >= 4 and container <= len(containers)-2:
			title_div = containers[container].find('div', {'class':'BNeawe vvjwJb AP7Wnd'})
			title = title_div.text
			link_div = containers[container].find('div', {'class':'BNeawe UPmit AP7Wnd'})
			link_ = link_div.text
			link = format_link(link_)
			print(f'[ * ] {title} \n \t[ url ] {link} \n')

def search(string):
	url = f'https://www.google.com/search?q={string}'
	proof = 'Send feedback'
	s = requests.get(url, timeout=60)
	with open('file.html', 'w') as f:
		f.write(s.text)
		system(f'firefox {f.name}')
	filter(s.text)


def main():
	print("""
		            .-'''-.        .-'''-.                                       
           '   _    \     '   _    \           .---.                     
         /   /` '.   \  /   /` '.   \          |   |      __.....__      
  .--./).   |     \  ' .   |     \  '  .--./)  |   |  .-''         '.    
 /.''\\ |   '      |  '|   '      |  '/.''\\   |   | /     .-''"'-.  `.  
| |  | |\    \     / / \    \     / /| |  | |  |   |/     /________\   \ 
 \`-' /  `.   ` ..' /   `.   ` ..' /  \`-' /   |   ||                  | 
 /("'`      '-...-'`       '-...-'`   /("'`    |   |\    .-------------' 
 \ '---.                              \ '---.  |   | \    '-.____...---. 
  /'""'.\                              /'""'.\ |   |  `.             .'  
 ||     ||                            ||     ||'---'    `''-...... -'    
 \'. __//                             \'. __//                           
  `'---'                               `'---'                            
					Author: Ian Wright
					http://www.github.com/ianwright27
	""")
	string = input('Google > ')
	output = ''
	for char in string:
		if char == " ":
			output+="+"
		else:
			output+=char
	search(output)	
	
try:
	main()
except Exception as e:
	print(f'<==END==>')
