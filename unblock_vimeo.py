from subprocess import call
from os import path


print("\n\t Welcome to tool to unblock vimeo privacy block\n\tBy kavindu Chamodh")
url = input("\nEnter the url of the video that you want to get unblocked")
permitted_url = input("\nEnter a url of a website that allows you to see the video")
filename = input("\nEnter a file name to write your output")+'.html'


call('curl --referer '+permitted_url+' -o '+filename+' '+url,shell=True)


print('\nOUTPUT SUCCESFULLY SAVED TO '+path.abspath(filename))
