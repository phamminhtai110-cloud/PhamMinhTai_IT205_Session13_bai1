parking_lot = []
next_id = 1
PRICE_MOTOR = 5000
PRICE_CAR = 15000

def show_menu():
    print("\n====================================================")
    print("SMART PARKING SYSTEM - QUAN LY BAI DO XE")
    print("====================================================")
    print("1. Check-in (Gui xe moi)")
    print("2. Bao cao ton kho (Xe dang gui)")
    print("3. Tim kiem xe theo bien so")
    print("4. Check-out (Tinh tien & xoa xe)")
    print("5. Thoat chuong trinh")
    print("----------------------------------------------------")

def get_plate(prompt):
    while True:
        plate = input(prompt).strip().upper()
        if plate == "":
            print("[ERR-01] Bien so khong duoc de trong!")
        else:
            return plate

def get_int(prompt, min_val, max_val):
    while True:
        value_str = input(prompt).strip()
        if not value_str.isdigit():
            print("Loi: Vui long nhap so nguyen.")
            continue
        value = int(value_str)
        if value < min_val or value > max_val:
            print(f"Loi: Gia tri phai tu {min_val} den {max_val}.")
            continue
        return value

def is_plate_exist(plate):
    for v in parking_lot:
        if v["plate"] == plate:
            return True
    return False

def find_vehicle(plate):
    for v in parking_lot:
        if v["plate"] == plate:
            return v
    return None

def check_in():
    global next_id
    print("\n--- CHECK-IN (GUI XE MOI) ---")
    plate = get_plate("Bien so xe: ")
    if is_plate_exist(plate):
        print("[ERR-03] Bien so da co mat trong bai!")
        return
    type_val = get_int("Loai xe (1: Xe may, 2: O to): ", 1, 2)
    entry_hour = get_int("Gio vao (0-23): ", 0, 23)
    parking_lot.append({
        "id": next_id,
        "plate": plate,
        "type": type_val,
        "entry_time": entry_hour
    })
    print(f"Check-in thanh cong! Ma so xe: {next_id}")
    next_id += 1

def show_inventory():
    print("\n--- BAO CAO TON KHO (XE DANG GUI) ---")
    if not parking_lot:
        print("[ERR-02] Bai xe hien dang trong!")
        return
    print("\n+----+-----------------+-----------+-------------+")
    print("| ID | Bien so         | Loai xe   | Gio vao     |")
    print("+----+-----------------+-----------+-------------+")
    for v in parking_lot:
        loai = "Xe may" if v["type"] == 1 else "O to"
        print(f"| {v['id']:<2} | {v['plate']:<15} | {loai:<9} | {v['entry_time']:>2} gio       |")
    print("+----+-----------------+-----------+-------------+")

def search_vehicle():
    print("\n--- TIM KIEM XE THEO BIEN SO ---")
    plate = get_plate("Nhap bien so can tim: ")
    v = find_vehicle(plate)
    if v is None:
        print(f"[ERR-04] Khong tim thay xe {plate} trong bai!")
        return
    loai = "Xe may" if v["type"] == 1 else "O to"
    print("\n========== THONG TIN XE ==========")
    print(f"Ma ID       : {v['id']}")
    print(f"Bien so     : {v['plate']}")
    print(f"Loai xe     : {loai}")
    print(f"Gio vao     : {v['entry_time']} gio")
    print("===================================")

def check_out():
    print("\n--- CHECK-OUT (TINH TIEN & XOA XE) ---")
    plate = get_plate("Nhap bien so xe ra: ")
    v = find_vehicle(plate)
    if v is None:
        print(f"[ERR-04] Khong tim thay xe {plate} trong bai!")
        return
    exit_hour = get_int("Gio ra (0-23): ", 0, 23)
    entry_hour = v["entry_time"]
    if exit_hour < entry_hour:
        print("[ERR-05] Gio ra phai lon hon hoac bang gio vao!")
        return
    hours = exit_hour - entry_hour
    if hours == 0:
        hours = 1
    if v["type"] == 1:
        price = PRICE_MOTOR
        type_name = "Xe may"
    else:
        price = PRICE_CAR
        type_name = "O to"
    total = hours * price
    print("\n========== HOA DON TIEN GUI XE ==========")
    print(f"Bien so          : {plate}")
    print(f"Loai xe          : {type_name}")
    print(f"Gio vao          : {entry_hour}:00")
    print(f"Gio ra           : {exit_hour}:00")
    print(f"So gio do        : {hours} gio")
    print(f"Don gia          : {price:,}d/gio")
    print("-" * 40)
    print(f"Tong tien        : {total:,}d")
    print("=========================================")
    parking_lot.remove(v)
    print("Da xoa xe khoi danh sach. Cam on quy khach!")

def main():
    while True:
        show_menu()
        choice = input("Nhap lua chon (1-5): ").strip()
        if not choice.isdigit() or int(choice) not in (1,2,3,4,5):
            print("[ERR-06] Lua chon khong hop le!")
            continue
        choice = int(choice)
        if choice == 1:
            check_in()
        elif choice == 2:
            show_inventory()
        elif choice == 3:
            search_vehicle()
        elif choice == 4:
            check_out()
        elif choice == 5:
            print("\nCam on ban da su dung Smart Parking System. Tam biet!")
            break

if __name__ == "__main__":
    main()
