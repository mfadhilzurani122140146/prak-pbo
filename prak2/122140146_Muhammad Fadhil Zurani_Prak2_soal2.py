def price_info_decorator(func):
    def wrapper(*args, **kwargs):
        weapons_price = {"Vandal": 2900, "Phantom": 2900, "Operator": 4500, "Sheriff": 800}
        weapon = kwargs.get("weapon", None)
        if weapon and weapon in weapons_price:
            print(f"Harga {weapon}: ${weapons_price[weapon]}")
        return func(*args, **kwargs)
    return wrapper

class Agent:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        print(f"{self.name} telah dipilih sebagai seorang {self.role}")

    @price_info_decorator
    def buy_weapon(self, weapon):
        print(f"{self.name} telah membeli senjata: {weapon}")

    @classmethod
    def select_agent(cls, name):
        if name.lower() == "jett":
            return cls("Jett", "Duelist")
        elif name.lower() == "sova":
            return cls("Sova", "Initiator")
        elif name.lower() == "cypher":
            return cls("Cypher", "Sentinel")
        elif name.lower() == "omen":
            return cls("Omen", "Controller")
        else:
            print("Agent tidak ditemukan.")

    @staticmethod
    def select_weapon():
        weapons = ["Vandal", "Phantom", "Operator", "Sheriff"]
        print("Senjata yang tersedia:")
        for weapon in weapons:
            print(weapon)
        choice = input("Pilih senjata Anda: ").strip().capitalize()
        return choice

    def __del__(self):
        print(f"{self.name} telah gugur dalam pertempuran.")


print("Selamat datang di Valorant!")
print("Pilih agent Anda:")
agent_name = input().strip().lower()
selected_agent = Agent.select_agent(agent_name)
if selected_agent:
    selected_weapon = selected_agent.select_weapon()
    if selected_weapon:
        selected_agent.buy_weapon(weapon=selected_weapon)
    else:
        print("Senjata tidak valid.")
else:
    print("Pilihan agent tidak valid.")

