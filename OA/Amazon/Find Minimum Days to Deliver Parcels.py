# Find Minimum Days to Deliver Parcels
# There is N delivery centers. 
# Each Delivery Outlet has some packages to be delivered, denoted by parcels[i]. 
# There is a Rule how delivery should be completed.
# On each day, an equal number of parcerls are to be dispatched from each 
# delivery center that has atleast one parcel remaining.
# Find minimum nunmber of days needed to deliver all the parcels.
#Input:
#parcels= {2,3,4,3,3}

#Output
#3

#*/


def get_days(parcels):
    return len(set(parcels)-{0})

parcels = [4,2,2]   
print("total days:", get_days(parcels))