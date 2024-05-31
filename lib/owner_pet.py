class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all=[]
    
    def __init__(self, name, pet_type, owner=None):
        if not isinstance(name, str):
             raise Exception("Name must be a string")
        self.name = name
        self.pet_type = pet_type 
        self.owner = owner
        Pet.all.append(self)
    
    @property
    def pet_type(self):
        return self._pet_type
        
    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {Pet.PET_TYPES}")
        self._pet_type = pet_type
class Owner:
    def __init__(self,name):
        self.name = name
        self.pets = []
    def pets(self):
        return [pet for pet in Pet.all if pet.owner ==self]
    def add_pet(self, pet):
        if not isinstance (pet,Pet):
           raise TypeError("The pet must be an instance of the Pet class")
        pet.owner = self
    def get_sorted_pets(self):
      return sorted(self.pets, key=lambda pet: pet.name)

    owner = Owner("John")
    pet1 = Pet("Fido", "dog", owner)
    pet2 = Pet("Clifford", "dog", owner)
    pet3 = Pet("Whiskers", "cat", owner)
    pet4 = Pet("Jerry", "reptile", owner)

    # Assert that get_sorted_pets() returns the pets sorted by name
    assert owner.get_sorted_pets() == [pet2, pet1, pet4, pet3]
