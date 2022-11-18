from youtubeSearch import *
from random_querry_sequence import *
import numpy as np
API_KEY = "AIzaSyBmNyRDR1G5HC8ynzrNbwFnKPhS6_X8o0A"
channel_id = "UCvFOwWIU2vgppuzQbNFK9kQ"

yt = YTSearch(API_KEY , channel_id)

querry_search = "game kinh dị chơi cùng bạn bè trên điện thoại"
random_seq = RandomSeq(querry_search)
n = 3
while n > 0:

    q_random = random_seq.generate_seq(random_seq.create_tos(querry_search))
    print(q_random)
    # q = "game"
    url = yt.get_results_querry_url(q_random,5)     
    yt.dump(querry_search , url)
    n -= 1
