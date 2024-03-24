import requests

RapidKey = ''  # Enter Here Your Rapid Api Key


def GetProfileInfo(
        LoginData:dict,
        Username:str,
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
          "Username": Username,
        }

    headers = {
        "X-RapidAPI-Key": RapidKey,
        "X-RapidAPI-Host": "namastegram.p.rapidapi.com"
    }

    return requests.get("https://namastegram.p.rapidapi.com/profileInfo", headers=headers, params=querystring).text


if __name__ == '__main__':

    LoginData = {
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
    Username='instagram' # Enter UserName To Get Profile Info
    print(GetProfileInfo(LoginData,Username,Proxy))

    #Success Response

    '''{
  "Message": {
    "data": {
      "user": {
        "ai_agent_type": null,
        "biography": "Discover what's next on Instagram 🔎✨",
        "bio_links": [
          {
            "title": "",
            "lynx_url": "https://l.instagram.com/?u=https%3A%2F%2Fhelp.instagram.com%2F&e=AT0FCTMzs-vt9LijlsHrHFoFELw5tv0ja9IPzkcQTnWsS2MNi2gu9YcdYMW2gZOtyzFm9WU_0VjKU3oLJ0o6RNNWVpuzP9SP2OFb5F4",
            "url": "https://help.instagram.com/",
            "link_type": "external"
          }
        ],
        "fb_profile_biolink": null,
        "biography_with_entities": {
          "raw_text": "Discover what's next on Instagram 🔎✨",
          "entities": []
        },
        "blocked_by_viewer": false,
        "restricted_by_viewer": false,
        "country_block": false,
        "eimu_id": "117943452927407",
        "external_url": "https://help.instagram.com/",
        "external_url_linkshimmed": "https://l.instagram.com/?u=https%3A%2F%2Fhelp.instagram.com%2F&e=AT0lZy_k6IRgHOCBaf6pkwwwzdGnVqkJYiJJmyfq1voN8yqESDR3IdAgJMCE0YMz1HehvF-BlsmQ8T_gnsOEiQb6afPiZyEypH23Svg",
        "edge_followed_by": {
          "count": 671180565
        },
        "fbid": "17841400039600391",
        "followed_by_viewer": true,
        "edge_follow": {
          "count": 133
        },
        "follows_viewer": false,
        "full_name": "Instagram",
        "group_metadata": null,
        "has_ar_effects": true,
        "has_clips": true,
        "has_guides": false,
        "has_chaining": false,
        "has_channel": false,
        "has_blocked_viewer": false,
        "highlight_reel_count": 10,
        "has_requested_viewer": false,
        "hide_like_and_view_counts": false,
        "id": "25025320",
        "is_business_account": false,
        "is_professional_account": true,
        "is_supervision_enabled": false,
        "is_guardian_of_viewer": false,
        "is_supervised_by_viewer": false,
        "is_supervised_user": false,
        "is_embeds_disabled": false,
        "is_joined_recently": false,
        "guardian_id": null,
        "business_address_json": null,
        "business_contact_method": "UNKNOWN",
        "business_email": null,
        "business_phone_number": null,
        "business_category_name": null,
        "overall_category_name": null,
        "category_enum": null,
        "category_name": "Digital creator",
        "is_private": false,
        "is_verified": true,
        "is_verified_by_mv4b": false,
        "is_regulated_c18": false,
        "edge_mutual_followed_by": {
          "count": 99,
          "edges": [
            {
              "node": {
                "username": "aas_khan_14"
              }
            },
            {
              "node": {
                "username": "ali.mollazehi12"
              }
            },
            {
              "node": {
                "username": "ayushmannk"
              }
            }
          ]
        },
        "pinned_channels_list_count": 0,
        "profile_pic_url": "https://scontent-fra3-2.cdninstagram.com/v/t51.2885-19/281440578_1088265838702675_6233856337905829714_n.jpg?stp=dst-jpg_s150x150&nc_ht=scontent-fra3-2.cdninstagram.com&nc_cat=1&nc_ohc=HnsbZxeWU_IAX-TuPVl&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfAZrtfnrKGccvQm19WexzZKOBNBSio0gqiWvuXq5au06Q&oe=66054358&nc_sid=8b3546",
        "profile_pic_url_hd": "https://scontent-fra3-2.cdninstagram.com/v/t51.2885-19/281440578_1088265838702675_6233856337905829714_n.jpg?stp=dst-jpg_s320x320&nc_ht=scontent-fra3-2.cdninstagram.com&nc_cat=1&nc_ohc=HnsbZxeWU_IAX-TuPVl&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfCqfaQpabMnCAJdWt_SxeNm8bqfHLAEwuj5Rn-q58S58w&oe=66054358&nc_sid=8b3546",
        "requested_by_viewer": false,
        "should_show_category": false,
        "should_show_public_contacts": false,
        "show_account_transparency_details": true,
        "transparency_label": null,
        "transparency_product": null,
        "username": "instagram",
        "connected_fb_page": null,
        "pronouns": [],
        "edge_owner_to_timeline_media": {
          "count": 7646,
          "page_info": {
            "has_next_page": true,
            "end_cursor": ""
          },
          "edges": []
        }
      }
    },
    "status": "ok"
  }
}
'''

