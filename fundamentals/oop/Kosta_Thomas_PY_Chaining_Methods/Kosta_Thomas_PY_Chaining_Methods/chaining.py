
class User:		
    def __init__(self, first_name, last_name, email, age, is_rewards_member=False, gold_card_points=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points
    def display_info(self):
        attrs = vars(self)
        for item in attrs.items():
            print(f'{item[0]}: {item[1]}')
        print("")
        return self
    def enroll(self):
        if self.is_rewards_member:
            print("User already a member")
            return False
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self
    def spend_points(self, amount):
        if self.gold_card_points - amount < 0:
            print("Insufficient points")
            return False
        self.gold_card_points -= amount
        return self

user1 = User("Jane", "Doe", "jane_d@py.com", 27)
user1.display_info().enroll().display_info().spend_points(50).display_info()

user2 = User("John", "Doe", "john_d@py.com", 30)
user2.enroll().spend_points(80).display_info().enroll()
