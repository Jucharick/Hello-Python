# from isOdd import isOdd
# # нечетность

# print(isOdd(0))
# print(isOdd(1))
# print(isOdd(4)) 


# import time


# from progress.bar import Bar

# bar = Bar('Processing', max=20)
# for i in range(20):
#     time.sleep(1)
#     bar.next()
# bar.finish()


# import emoji
# print(emoji.emojize('Python is :thumbs_up:'))
# print(emoji.emojize('Python is :thumbsup:', language='alias'))
# print(emoji.demojize('Python is 👍'))
# print(emoji.emojize("Python is fun :red_heart:"))
# print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))
# print(emoji.is_emoji("👍"))



import matplotlib.pyplot as plt
import numpy as np

# plt.style.use('_mpl-gallery')
# # make data:
# np.random.seed(3)
# x = 0.5 + np.arange(8)
# y = np.random.uniform(2, 7, len(x))
# # plot
# fig, ax = plt.subplots()
# ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
# ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#        ylim=(0, 8), yticks=np.arange(1, 8))
# plt.show()

list = [1,2,3,2,7]
plt.plot(list)

plt.show()