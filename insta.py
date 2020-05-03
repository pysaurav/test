from instagram_private_api import Client, ClientCompatPatch



api = Client(user_name, password)

# user_feed_info = api.user_feed('329452045', count=1)
# print(user_feed_info)
# for post in user_feed_info:
#     print("post",post)
    # print(f"{post['link']}, {post['user']['username']}")

see = api.autocomplete_user_list()

print(see)
# following = api.user_following('123456','1')
# for user in following:
#     print(user['username'])

results = api.feed_timeline()
items = [item for item in results.get('feed_items', [])
         if item.get('media_or_ad')]
for item in items:
    # Manually patch the entity to match the public api as closely as possible, optional
    # To automatically patch entities, initialise the Client with auto_patch=True
    ClientCompatPatch.media(item['media_or_ad'])
    print(item['media_or_ad']['code'])

# from instagram_web_api import Client, ClientCompatPatch, ClientError, ClientLoginError
#
# # Without any authentication
# web_api = Client(auto_patch=True, drop_incompat_keys=False)
# user_feed_info = web_api.user_feed('329452045', count=10)
# for post in user_feed_info:
#     print('%s from %s' % (post['link'], post['user']['username']))
#
# # Some endpoints, e.g. user_following are available only after authentication
# authed_web_api = Client(
#     auto_patch=True, authenticate=True,
#     username='saauraav ', password='eXPRESSION21')
#
# following = authed_web_api.user_following('123456')
# for user in following:
#     print(user['username'])