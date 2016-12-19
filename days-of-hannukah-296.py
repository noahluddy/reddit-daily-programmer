gifts = [
    'Golden Menorah',
    'Pieces of Gelt',
    'Spinning Dreidels',
    'Circular Kippahs',
    'Waxy Candles',
    'Jewish Stories',
    'Gooey Latkes',
    'Proud Grandparents',
]

nums = [
    'first',
    'second',
    'third',
    'fourth',
    'fifth',
    'sixth',
    'seventh',
    'eighth',
]

for i in range(len(nums)):
    print('\nOn the ' + nums[i] + ' day of Hannukah\nmy bubbe gave to me:')
    for j in range(i+1):
        print(str(j+1) + ' ' + gifts[j])
