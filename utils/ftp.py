import re
from ftplib import FTP
class FTP:
    def __init__(self) -> None:
        pass 

    def get_FTP_file(self,ftp,location) -> None:

        self.pattern = re.compile('ftp:\/\/(?<=\/\/)(.*?)(?=\:):(?<=\:)(.*?)(?=\@)@(\w+\.\w+\.\w{1,3})\/(\w+\.zip)')
        self.match = self.pattern.search(ftp)
        self.login = self.match.group(1)
        self.pw = self.match.group(2)
        self.url = self.match.group(3)
        self.file = self.match.group(4)

        #FTP information
        ftp = FTP(self.url)
        ftp.login(self.login,self.pw)

        #Download from FTP
        self.ftp.retrbinary("RETR " + self.file ,open(location + self.file, 'wb').write)
        self.ftp.close()
