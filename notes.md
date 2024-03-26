1. interesting idea. If in the future more classes/models have attributes of types other than
string, heres an idea:
    have each class have an attribute that stores the editable properties and their types:
    eg. for places:
        attr_types = {
            'number_rooms': int,
            'number_bathrooms': int,
            'max_guest': int,
            'price_by_night': int,
            'latitude': float,
            'longitude': float
        }
    then, whenever a change is to occur for an instance of a class/model,
    check the attribute's type from the dictionary and handle appropriately

2. In my mind, it makes more sense to restrict updates only to properties that a model/class
    already has. eg. update User <id> deez bars fails because Users do not have attribute
    deez. I wonder why we don't do that
