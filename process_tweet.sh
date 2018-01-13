cat tweet.txt | cut -f 1 -d , > tweet_username.txt
cat tweet.txt | cut -f 2 -d , > tweet_id.txt
cat tweet.txt | cut -f 3 -d , > tweet_text.txt
chasen < tweet_text.txt > tweet_text.txt.chasen
