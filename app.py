import packages
from ftplib import FTP
from datetime import datetime
import re

def get_FTP_file(ftp,location) -> None:

    pattern = re.compile('ftp:\/\/(?<=\/\/)(.*?)(?=\:):(?<=\:)(.*?)(?=\@)@(\w+\.\w+\.\w{1,3})\/(\w+\.zip)')
    match = pattern.search(ftp)
    login = match.group(1)
    pw = match.group(2)
    url = match.group(3)
    file = match.group(4)

    #FTP information
    ftp = FTP(url)
    ftp.login(login,pw)

    #Download from FTP
    ftp.retrbinary("RETR " + file ,open(location + file, 'wb').write)
    ftp.close()

if __name__ == "__main__":
    print(packages.ServerAccess().header())
    pass