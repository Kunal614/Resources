
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

'''
Refrence
https://stackoverflow.com/questions/10631042/how-to-generate-access-token-using-refresh-token-through-google-drive-api
https://stackoverflow.com/questions/13871982/unable-to-refresh-access-token-response-is-unauthorized-client
https://stackoverflow.com/questions/13871982/unable-to-refresh-access-token-response-is-unauthorized-client


for token
https://developers.google.com/oauthplayground/?code=4/0AY0e-g6optOZBEIdTUNcWc7hTEUREJcaO1AjtTWpdoHs3WfC6ipHnUfO_s8HawEPLUnbmg&scope=https://www.googleapis.com/auth/drive
'''