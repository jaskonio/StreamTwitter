#!/usr/bin/python
# Requeriments
# 'pip install --upgrade pip
# apt install python-pip
# pip install shutil twitter python-twitter
# delete accent pip install unidecode

import unidecode
import shutil
import os
from twitter import *
import subprocess
import tweepy


def elimina_tildes(cadena):
    return unidecode.unidecode(cadena)


def getHashtag():

    config = {
        "consumer_key": "q1XsctQfkyWnzxktoHfiN6ELM",
        "consumer_secret": "1nXXoXK5mklJFCZ0GQtU11JwDHl5XOq8vfZErLPg83xDulBmPF",
        "access_key": "190651136-1WTRHboChmrM4wa0zjd7mnObbr5N7xQXRLTrO3lP",
        "access_secret": "2XmDcL46aZNVYnyOuLMJOPZ73Am22HCFtZmWQYUpGXi5s"
    }

# twitter = Twitter(auth=OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))
# results = twitter.trends.place(_id=23424950)

# print("SPAIN Trends")
# hastasgs = []
# for location in results:
#     for trend in location["trends"]:
#         print(" - %s" % trend["name"])
#         hastasgs.append(trend["name"])

#     return hastasgs

    auth = tweepy.OAuthHandler(
        config["consumer_key"], config["consumer_secret"])
    auth.set_access_token(config["access_key"], config["access_secret"])
    api = tweepy.API(auth)
    trends1 = api.trends_place(23424950)

    print("SPAIN Trends")
    data = trends1[0]
    trends = data['trends']
    hastasgs = []
    names = [trend['name'] for trend in trends]
    #trendsName = ' '.join(names)
    for name in names:
        print(" - %s" % name)
        hastasgs.append(elimina_tildes(name))
    return hastasgs


def existsFileConfig(path):
    return os.path.isfile(path)


def copyFileToFolderTmp(originFile):
    dest = PATH_TMP + "/" + fileName
    shutil.copy(originFile, dest)


def deleteFileConfig():
    os.remove(pathConfigLogstash + fileName)


def rawNewFileConfig(file, hashtag):
    oFile = open(originFileName)
    newFileConfig = open(file, 'w+')

    for line in oFile:
        if "keywords_" in line:
            newFileConfig.write("keywords => " + str(hashtag) + "\n")
            continue

        newFileConfig.write(line)

    oFile.close()
    newFileConfig.close()


def deleteOldConfig():
    os.remove(PATH_TMP + "/" + fileName)


def restart_service(name):
    #command = ['/usr/sbin/service', name, 'restart']
    # shell=FALSE for sudo to work.
    #subprocess.call(command, shell=False)
    command = ["C:\Program Files\Git\/bin\/bash.exe", "--login", "-i",
               "C:\Program Files\Docker Toolbox\start.sh", "docker", "ls"]
    subprocess.call(command, shell=False)


pathConfigLogstash = "../docker/logstash/conf/"
fileName = 'twitter.conf'
originFileName = 'origin-twitter-config.conf'
PATH_TMP = "/tmp"

if __name__ == '__main__':

    listHashtag = getHashtag()
    if (len(listHashtag) != 0):
        print(listHashtag)
        statusFileConfig = existsFileConfig(pathConfigLogstash + fileName)
        print(statusFileConfig)
        if (statusFileConfig):
            print("delete..")
            #copyFileToFolderTmp(pathConfigLogstash + fileName)
            deleteFileConfig()

        rawNewFileConfig(pathConfigLogstash + fileName, listHashtag)

        #if (statusFileConfig):
            #deleteOldConfig()

    #restart_service("logstash")
