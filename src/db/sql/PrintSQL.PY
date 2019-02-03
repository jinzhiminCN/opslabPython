x = 1
for i in range(1, 12):
    for y in range(1, 101):
        print("union select COUNT(*) FROM [GroupData" + str(i) + "].[dbo].[Group" + str(x) + "]")
        x += 1
