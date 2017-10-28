import tweepy
import json

# Twitter API credentials
consumer_key = "ToMJ36rxxLbdi6phSXYEM8Qd0"
consumer_secret = "eMxSeofGj6uK7nyc0uetEJRFNNtlzxyx6k11tXhrYY33Illjeq"
access_key = "924361173214089217-bEHCdGreBj6ndEutzV9nkIFAwLQH9uw"
access_secret = "pjIyb8Kqpr6dv8yaudMYloNtrLtSfr0TCC30asAOSAlq7"


def get_all_tweets(screen_name):
    # Twitter only allows access to a users most recent 3240 tweets with this method

    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    #new_tweets = api.user_timeline(screen_name=screen_name, count=10)

    # save most recent tweets
    #alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    #oldest = alltweets[-1].id - 1
    '''
    # keep grabbing tweets until there are no tweets left to grab
    while (len(alltweets) < 100):
        # all subsequent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=10, max_id=oldest)

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print("...%s tweets downloaded so far" % (len(alltweets)))
    '''

    new_tweets = tweepy.Cursor(api.search, q = "#georelief", lang = "en").items(limit = 100)
    alltweets.extend(new_tweets)

    # write tweet objects to JSON
    file = open("tweet.json", "w", encoding="utf8")
    print("Writing tweet objects to JSON please wait...")
    count = 0
    for status in alltweets:
        count +=1
        print("Tweets downloaded so far: ", count)
        json.dump(status._json, file, sort_keys=True, indent=4)

    # close the file
    print("Done")
    file.close()


if __name__ == '__main__':
    # pass in the username of the account you want to download
    get_all_tweets("@realDonaldTrump")