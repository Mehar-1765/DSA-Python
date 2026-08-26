#activity selection valid timing
n=int(input("Enter no.of activities: "))
activities=[]
for i in range(n):
    s=int(input(f"Enter start time of activity{i+1}: "))
    e=int(input(f"Enter end time of activity{i+1}: "))
    activities.append((s,e))
activities.sort(key=lambda x: x[1])
print("\nSelected activities: ")
last_finish=-1
for activity in activities:
    if activity[0]>=last_finish:
        print(activity)
        last_finish=activity[1]