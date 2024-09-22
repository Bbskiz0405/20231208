def display_menu(menu):
    print("菜單:")
    for item, price in menu.items():
        print(f"{item}: {price}元")

def order_food(menu):
    total_cost = 0
    while True:
        display_menu(menu)
        choice = input("請輸入想要點的餐點名稱（若要結束點餐，請按 enter 鍵）: ")
        
        if choice == "":
            break
        
        if choice in menu:
            price = menu[choice]
            total_cost += price
            print(f"您點了: {choice}, 價格: {price}元. 目前總金額: {total_cost}元")
        else:
            print("未找到該餐點，請重新輸入。")

    print(f"點餐結束。帳單總金額: {total_cost}元")

# 菜單範例
menu = {
    "漢堡": 50,
    "薯條": 30,
    "可樂": 20,
    "雞塊": 45
}

order_food(menu)
