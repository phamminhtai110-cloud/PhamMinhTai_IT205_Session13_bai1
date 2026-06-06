break_line = "===================================================="
menu_title_text = "SMART PARKING SYSTEM"
menu_title = f"{break_line}\n{' ' * ((len(break_line) - len(menu_title_text)) // 2)}{menu_title_text}\n{break_line}"

parking_lot = []
next_id = 1
PRICE_MOTOR = 5000
PRICE_CAR = 15000

while True:
    print(menu_title)
    print("1. Check-in (Gửi xe mới)")
    print("2. Báo cáo tồn kho (Xe đang gửi)")
    print("3. Tìm kiếm xe theo biển số")
    print("4. Check-out (Tính tiền & xóa xe)")
    print("5. Thoát chương trình")
    print("-" * 50)
    choice = input("Nhập lựa chọn của bạn (1-5): ").strip()
    if not choice.isdigit() or int(choice) not in range(1, 6):
        print("[ERR-06] Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 5.")
        continue
    choice = int(choice)

    if choice == 1:
        print("\n--- CHECK-IN (GỬI XE MỚI) ---")
        while True:
            plate = input("Nhập biển số xe: ").strip().upper()
            if plate == "":
                print("[ERR-01] Biển số không được để trống!")
            else:
                break
        exist = False
        for v in parking_lot:
            if v["plate"] == plate:
                exist = True
                break
        if exist:
            print("[ERR-03] Biển số đã có mặt trong bãi!")
            continue
        while True:
            type_str = input("Loại xe (1: Xe máy, 2: Ô tô): ").strip()
            if not type_str.isdigit():
                print("Lỗi: Vui lòng nhập số 1 hoặc 2.")
                continue
            type_val = int(type_str)
            if type_val not in (1, 2):
                print("Chỉ nhập 1 (Xe máy) hoặc 2 (Ô tô).")
                continue
            break
        while True:
            hour_str = input("Nhập giờ vào (0-23): ").strip()
            if not hour_str.isdigit():
                print("Lỗi: Vui lòng nhập số nguyên.")
                continue
            entry_hour = int(hour_str)
            if entry_hour < 0 or entry_hour > 23:
                print("Lỗi: Giờ phải từ 0 đến 23.")
                continue
            break
        parking_lot.append({
            "id": next_id,
            "plate": plate,
            "type": type_val,
            "entry_time": entry_hour
        })
        print(f" Check-in thành công! Mã số xe: {next_id}")
        next_id += 1

    elif choice == 2:
        print("\n--- BÁO CÁO TỒN KHO (XE ĐANG GỬI) ---")
        if not parking_lot:
            print("\n[ERR-02] Bãi xe hiện đang trống!")
        else:
            print("\n+----+-----------------+-----------+-------------+")
            print("| ID | Biển số         | Loại xe   | Giờ vào     |")
            print("+----+-----------------+-----------+-------------+")
            for v in parking_lot:
                loai = "Xe máy" if v["type"] == 1 else "Ô tô"
                print(f"| {v['id']:<2} | {v['plate']:<15} | {loai:<9} | {v['entry_time']:>2} giờ      |")
            print("+----+-----------------+-----------+-------------+")

    elif choice == 3:
        print("\n--- TÌM KIẾM XE THEO BIỂN SỐ ---")
        while True:
            plate = input("Nhập biển số cần tìm: ").strip().upper()
            if plate == "":
                print("[ERR-01] Biển số không được để trống!")
            else:
                break
        vehicle = None
        for v in parking_lot:
            if v["plate"] == plate:
                vehicle = v
                break
        if vehicle is None:
            print(f"[ERR-04] Không tìm thấy xe có biển số {plate} trong bãi!")
        else:
            loai = "Xe máy" if vehicle["type"] == 1 else "Ô tô"
            print("\n========== THÔNG TIN XE ==========")
            print(f"Mã ID       : {vehicle['id']}")
            print(f"Biển số     : {vehicle['plate']}")
            print(f"Loại xe     : {loai}")
            print(f"Giờ vào     : {vehicle['entry_time']} giờ")
            print("===================================")

    elif choice == 4:
        print("\n--- CHECK-OUT (TÍNH TIỀN & XÓA XE) ---")
        while True:
            plate = input("Nhập biển số xe ra: ").strip().upper()
            if plate == "":
                print("[ERR-01] Biển số không được để trống!")
            else:
                break
        vehicle = None
        for v in parking_lot:
            if v["plate"] == plate:
                vehicle = v
                break
        if vehicle is None:
            print(f"[ERR-04] Không tìm thấy xe có biển số {plate} trong bãi!")
            continue
        while True:
            hour_str = input("Nhập giờ ra (0-23): ").strip()
            if not hour_str.isdigit():
                print("Lỗi: Vui lòng nhập số nguyên.")
                continue
            exit_hour = int(hour_str)
            if exit_hour < 0 or exit_hour > 23:
                print("Lỗi: Giờ phải từ 0 đến 23.")
                continue
            break
        entry_hour = vehicle["entry_time"]
        if exit_hour < entry_hour:
            print("[ERR-05] Giờ ra phải lớn hơn hoặc bằng giờ vào! Vui lòng nhập lại.")
            continue
        hours = exit_hour - entry_hour
        if hours == 0:
            hours = 1
        if vehicle["type"] == 1:
            price = PRICE_MOTOR
            type_name = "Xe máy"
        else:
            price = PRICE_CAR
            type_name = "Ô tô"
        total = hours * price
        print("\n========== HÓA ĐƠN TIỀN GỬI XE ==========")
        print(f"Biển số          : {plate}")
        print(f"Loại xe          : {type_name}")
        print(f"Giờ vào          : {entry_hour}:00")
        print(f"Giờ ra           : {exit_hour}:00")
        print(f"Số giờ đỗ        : {hours} giờ")
        print(f"Đơn giá          : {price:,}đ/giờ")
        print("-" * 40)
        print(f"Tổng tiền        : {total:,}đ")
        print("=========================================")
        parking_lot.remove(vehicle)
        print(" Đã xóa xe khỏi danh sách. Cảm ơn quý khách!")

    elif choice == 5:
        print("\n Cảm ơn bạn đã sử dụng Smart Parking System. Tạm biệt!")
        break
