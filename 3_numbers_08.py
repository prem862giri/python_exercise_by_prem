#Program that asks user for a number of seconds
#Print how many minutes and second that is.
#for instance, 200 seconds is 3 minutes and 20 seconds.
#[Use the // operator to get minutes and the %operator to get seconds]


n = int(input("Enter seconds: "))

minutes = n//60
seconds = n%60

print(f"{n} seconds is {minutes} minutes and {seconds} seconds.")