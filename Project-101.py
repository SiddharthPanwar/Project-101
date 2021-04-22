import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_files(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token = 'z-b14Nrh8zgAAAAAAAAAAYN4web6y24zr-gFdpn3b3bH9hw0NHDyYR_2_NsuP0cI'
    transferData=TransferData(access_token)

    file_from = input('Enter the file path which is to be transfered :  ')
    file_to = input('Enter the full path to upload to dropbox : ')

    transferData.upload_files(file_from,file_to)
    print("Requested File has been dropped to Dropbox")

main()