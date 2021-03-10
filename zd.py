# TODO: create the User class
# it must support rank, progress, and the inc_progress(rank) method

class User():
    rank = -8
    progress = 0

    def inc_progress(lv):
        rank_list = [i for i in range(-8, 9) if i != 0]
        if rank_list[rank_list.index(lv) + 1] == user.rank:
            user.progress += 1
        elif rank_list[rank_list.index(lv)] == user.rank:
            user.progress += 3
        elif rank_list[rank_list.index(lv)] > user.rank:
            user.progress += (10 * (lv - user.rank) * (lv - user.rank))
        if user.progress >= 100:
            if user.rank != 8:
                user.rank = rank_list[rank_list.index(user.rank) + (user.progress // 100)]
                user.progress = user.progress % 100
        return user.progress
    
user = User()
user.rank = -8
user.progress = 0
print(User.inc_progress(-8))
print(User.inc_progress(-5))


    
