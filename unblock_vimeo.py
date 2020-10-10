from subprocess import call


print("\n\t Welcome to tool to unblock vimeo privacy block\n\tBy kavindu Chamodh")
url = input("enter the url of the video that you want to get unblocked")
permitted_url = input("Enter a url of a website that allows you to see the video ")
filename = input("Enter a file name to write your output")+'.html'

call('curl --referer '+permitted_url+' -o '+filename+' '+url,shell=True)

#test_yrl = https://player.vimeo.com/video/109727604
#test_urk = https://cybrary.it/