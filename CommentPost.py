import requests

RapidKey = ''  # Enter Here Your Rapid Api Key


def DoComments(
        LoginData:dict,
        MediaId:str,
        Commenttext:str,
        Proxy: str,
):
    global RapidKey

    querystring = {
          "Browserversion":LoginData['DeviceInfo']['BrowserVersion'],
          "Rollout": LoginData['Cookies']['x-instagram-rollout'],
          "Useragent": LoginData['DeviceInfo']['User-Agent'],
          "Proxy": Proxy,
          "Igdid":  LoginData['Cookies']['ig_did'],
          "Rur":  LoginData['Cookies']['rur'],
          "Xclaim":  LoginData['Cookies']['x-ig-set-www-claim'],
          "Mid":  LoginData['Cookies']['mid'],
          "Csrftoken":  LoginData['Cookies']['csrftoken'],
          "Appid":  LoginData['Cookies']['x-ig-app-id'],
          "Userid":  LoginData['Cookies']['ds_user_id'],
          "Datr":  LoginData['Cookies']['datr'],
          "Sessionid":  LoginData['Cookies']['sessionid'],
          "Mediaid": MediaId,
          "CommentText":Commenttext
        }

    headers = {
        "X-RapidAPI-Key": RapidKey,
        "X-RapidAPI-Host": "namastegram.p.rapidapi.com"
    }

    return requests.get("https://namastegram.p.rapidapi.com/doComments", headers=headers, params=querystring).text


if __name__ == '__main__':

    LoginData={
            "Cookies": {
            "csrftoken": "GrHLSvBGwori5okhk6Eum2",
            "datr": "9yf_ZfVlokhkSt_gItvea605",
            "dpr": "1.25",
            "ds_user_id": "49078498762",
            "ig_did": "26DUJD72-A134-4249-BD4F-A0467A2503DD",
            "mid": "Zf8n9wAEAAFC2lVUCaxAVIxELyr_",
            "ps_l": "0",
            "ps_n": "0",
            "rur": "\"EAG\\05449078425082\\0541742756733:01f7f72489010d158cae5766f2eb88500e42b15319dbfa5f300092202a5c0a17e203dcac\"",
            "sessionid": "49078498762%3Ay5m90MaIv0987O%3A15%3AAYdCPP41zSDMxsBQyzwVgA0H94mgzrbXhUkljghSLg",
            "x-ig-app-id": "936619743392459",
            "x-ig-set-www-claim": "hmac.AR2qBB1GSfmt5oY6fMLgO9878HzqahJVd4PNtJrkLFuOXORy",
            "x-instagram-rollout": "1012271930"
          },
          "DeviceInfo": {
            "BrowserVersion": "84.0.4147.135",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
          },
          "Message": "LoginDone",
          "Status": {
            "authenticated": True,
            "oneTapPrompt": True,
            "status": "ok",
            "user": True,
            "userId": "49078498762"
          }
        }

    Proxy =''  # Enter Proxy Here In This Format ( username:password@host:port )
    MediaId='' #Enter Post MediaId Where You Want To Comment on Post
    Commenttext='Nice' #Enter Comments Here
    print(DoComments(LoginData,MediaId,Commenttext,Proxy))

    #Success Comment Response

    '''{
  "Message": {
    "id": "18002883893423606",
    "from": {
      "id": "49078425082",
      "username": "namastebots",
      "full_name": "leila abbasi",
      "profile_picture": "https://scontent-fra3-2.cdninstagram.com/v/t51.2885-19/339337884_819005863180828_5257909283479851606_n.jpg?stp=dst-jpg_s150x150\\u0026_nc_ht=scontent-fra3-2.cdninstagram.com\\u0026_nc_cat=104\\u0026_nc_ohc=Jg_3rkFd1xoAX9Ualg1\\u0026edm=AOLdatgBAAAA\\u0026ccb=7-5\\u0026oh=00_AfCRaXs0NaWL_Dp5WPDeWD3KGKOjQvtxBJFkQlOEx5Xu6A\\u0026oe=66039785\\u0026_nc_sid=beb6a3"
    },
    "text": "Nice",
    "created_time": 1711223792,
    "status": "ok"
  }
}'''

