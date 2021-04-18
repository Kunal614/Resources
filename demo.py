
import requests
url = 'https://oauth2.googleapis.com/token'
data = {
    "client_id": "1091937598228-5aan4ts4lm6u28r38q29926b81jatcts.apps.googleusercontent.com",
    "client_secret": "ZkzCCfgnau4hEhaH__PYflke",
    "refresh_token": "1//04vfemCPfDdMICgYIARAAGAQSNwF-L9IrHy8vb_Pzgf6eV6wZyf7mVaHDkZCF_AJnsGFDgyjtwuv28D34Z7TcJW7YK2uZzIQSusU",
    "grant_type": "refresh_token"
}

res  = requests.post(url ,  data=data)
print(res.json()['access_token'])