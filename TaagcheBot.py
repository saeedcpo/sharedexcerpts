import cv2
import requests
import json
import image_match
import os

#   Description:
#This app will ask you for a tag. It will itirate through all
#images of that tag in Instagram and will save the ones that has the
#template.jpg with more than 80% similarity.
#==============================================
#Hardcoded:  processed_images_file, template logo, folder saving Image
#Note that input dont work with Atom Script
#==============================================
#TODO: Change the storage to Sqlite
#==============================================

#ig_tag = 'کتاب'
ig_tag = input('Enter the tag name you want to search the page:')

processed_images_file = open('processed_images.txt','a+')
list_of_images = os.listdir("images_saved")
url = 'https://www.instagram.com/explore/tags/{0}/?__a=1'.format(ig_tag)

response = requests.get(url)
response_dictionary = json.loads(response.text)
recent_images = response_dictionary['graphql']['hashtag']['edge_hashtag_to_media']['edges']
print ("Total pics that instagram gives us is:",len(recent_images))

for i in range(len(recent_images)):
	j = 0
	eachimage = recent_images[i]['node']
	display_url = eachimage['display_url']
	shortcode = eachimage['shortcode']

	if '%s'%shortcode in open('processed_images.txt').read():
		print ('We have already processed pic %s'%i)
		continue
	else:
		processed_images_file.write('{0} \n'.format(shortcode))

		if '{}.jpg'.format(shortcode) in list_of_images:
			print ('Image {0} is already Saved'.format(i))
			continue
		else:

			print (display_url)
			print ('Processed Pic Number:',i)
			if image_match.doesmatch(display_url):
				print ('Image number {0} is Matched!'.format(i))
				imagefile = image_match.url_to_image(display_url)
				cv2.imwrite('images_saved/{0}.jpg'.format(shortcode), imagefile)
				j +=1
			else:
				continue

print ('####################')
print ('{} files added to folder'.format(j))
print ('####################')
input("Press Enter to continue...")
