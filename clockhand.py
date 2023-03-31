#program to calculate the difference between clock hand degrees
hour_hand=input("Enter the hour on the clock: ")
minute_hand=input("Enter the minute on the clock: ")
#hour_hand=30degrees/hr
hour_position=int(hour_hand)*30
#minute_hand=60degrees/min
minute_position=int(minute_hand)*60
degree_dif=minute_position-hour_position
print("degree btwn the clock hands:",degree_dif,"degrees")
