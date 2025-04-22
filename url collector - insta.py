import time
import os
import instaloader
import pickle
import random


L = instaloader.Instaloader()

# L = instaloader.Instaloader(
#     download_pictures=False,
#     download_videos=False,
#     download_video_thumbnails=False,
#     download_geotags=False,
#     download_comments=False,
#     save_metadata=True,
#     post_metadata_txt_pattern="{shortcode}")
'''
username = "alupotol794@gmail.com"
password = "018340.abcA"

L.login(username, password)  # May trigger 2FA
'''

#L.load_session_from_file("aloron007", filename="my_session")

target_list = [
    # "https://www.instagram.com/shawnwells/",
    # "https://www.instagram.com/dr.randmcclain/",
    "https://www.instagram.com/dr.akhan",
    "https://www.instagram.com/dr.williamwallace",
    "https://www.instagram.com/drjosephantoun",
    "https://www.instagram.com/suneeldhandmd",
    # "https://www.instagram.com/daniellebelardomd/",
    # "https://www.instagram.com/wellnessfactvsfiction",
    # "https://www.instagram.com/karenmkarlsen",
    # "https://www.instagram.com/drhalland",
    "https://www.instagram.com/drlibby",
    "https://www.instagram.com/eleatnutrition",
    "https://www.instagram.com/chrismasterjohn"
]

for url in target_list:

    username = url.split("/")[-1]
    useragent_list = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 YaBrowser/21.11.3.855 Yowser/2.5 Safari/537.36",
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    ]
    useragnt = random.choice(useragent_list)
    headers = {
           'user-agent': useragnt,
    }
    L.context._session.headers.update(headers)
    time.sleep(random.uniform(10, 15))
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        full_name = profile.full_name
        print("Full Name:", full_name)
        num_post = 1
        print("Total posts:", profile.mediacount)
        num_total_post = int(profile.mediacount)

        for post in profile.get_posts():
            code = post.shortcode

            file_name = f'post_links\{username}_post_url.txt'
            if os.path.exists(file_name):
                with open(file_name, 'r') as f:
                    lines = f.read()

            else:
                lines = ""


            url_link = f"https://www.instagram.com/{username}/p/{code}"
            print(f"{url_link} >> {num_post} | Left: {num_total_post - num_post} from {num_total_post}")
            num_post += 1
            with open(file_name, 'a') as file:
                if url_link not in lines:
                    file.write(url_link + '\n')
                else:
                    pass


            time.sleep(0.5)

        print(f">> Total Links Created: {num_post}")

    except Exception as E:
        print("Error:", E)