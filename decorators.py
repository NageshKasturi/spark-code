from datetime import *
import time

def retry_call_api(func):
    def wrap_retry(user,**kwargs):
        if len(kwargs)==0:
            retry_time=1
        else:
            retry_time=kwargs['retry_time']
            print ("the new retry value is::::::::::",retry_time)
        while(True):

            print ("This is from wrappper class")
            new_times=datetime.now().second+retry_time
            print ("The new time is: {}".format(new_times))
            time.sleep(retry_time)
            if datetime.now().second==new_times:
                func(user)
    return wrap_retry



@retry_call_api
def call_api(user, **kwargs):

    print ("The time is: {}".format(datetime.now()))

    for k,v in kwargs.items():
        print("The value of {} is: {}".format(k,v))

    print ("The {} has called this API call !".format(user))


call_api("Nagesh", retry_time=3)