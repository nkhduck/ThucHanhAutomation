import re

def bai1():
# 1. Viết regex để kiểm tra xem một chuỗi có phải là email hợp lệ không.
# Email hợp lệ có dạng: chữ cái/số + @ + tên miền + .com
    emails = ["test123@gmail.com", "abc@xyz", "user@domain.com", "invalid@.com"]

    pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.(com)$'

    for email in emails:
        if re.match(pattern, email):
            print(f"{email} ➜ Hợp lệ")
        else:
            print(f"{email} ➜ Không hợp lệ")

def bai2():
# 2. Tìm tất cả số điện thoại (gồm đúng 10 số, chia bởi dấu -)
    phone_text = "Liên hệ 091-234-5678 hoặc 123-4567-890 để được tư vấn. Gọi 987-654-3210 ngay!"

    pattern = r'\b(\d{3}-\d{3}-\d{4}|\d{3}-\d{4}-\d{3})\b'

    phone_numbers = re.findall(pattern, phone_text)

    print("Các số điện thoại tìm được:")
    for phone in phone_numbers:
        print(phone)

def bai3():
# 3. Cho chuỗi đầu vào, kiểm tra xem trong chuỗi có ít nhất một chữ số không.
    digit_text = "Tôi có 2 con mèo và 1 con chó."

    pattern = r'\d'

    if re.search(pattern, digit_text):
        print("Có ít nhất một chữ số trong chuỗi.")
    else:
        print("Không có chữ số nào trong chuỗi.")

def bai4():
# 4. Cho một chuỗi, loại bỏ toàn bộ ký tự không phải chữ cái.
    dirty_text = "Hello! This is test123 #2025."

    pattern = r'[^a-zA-Z]'  

    clean_text = re.sub(pattern, '', dirty_text)
    print(clean_text) 

def bai5():
# 5. Kiểm tra chuỗi mật khẩu có phải là mật khẩu mạnh không.
# Tiêu chí: Tối thiểu 8 ký tự, ít nhất 1 chữ hoa, 1 chữ thường, 1 số
    passwords = ["Abc12345", "abcdef", "ABC123456", "abcD1"]

    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'

    for pwd in passwords:
        if re.match(pattern, pwd):
            print(f"{pwd} ➜ Mật khẩu mạnh")
        else:
            print(f"{pwd} ➜ Mât khẩu yếu")

def bai6():
# 6. Kiểm tra chuỗi có phải là ngày hợp lệ theo định dạng dd/mm/yyyy không
# (không xét tính hợp lệ theo lịch thực tế)
    dates = ["18/06/2025", "31/13/2022", "00/12/2020", "5/6/2020"]

    pattern = r'^\d{2}/\d{2}/\d{4}$'

    for date in dates:
        if re.match(pattern, date):
            print(f"{date} ➜ Đúng định dạng dd/mm/yyyy")
        else:
            print(f"{date} ➜ Sai định dạng")

def bai7():
# 7. Tìm tất cả các từ viết hoa đứng đầu câu trong đoạn văn.
    capital_text = "Today is a good day. My name is Hoa. How are you?"

    pattern = r'(?:^|[.!?]\s)([A-Z][a-z]*)'

    matches = re.findall(pattern, capital_text)

    print("Từ viết hoa đầu câu:")
    for word in matches:
        print(word)

def bai8():
# 8. Từ danh sách URL, trích ra phần tên miền chính (ví dụ: google, facebook).
    urls = ["https://www.google.com", "http://facebook.com", "https://news.yahoo.com"]

    pattern = r'https?://(?:www\.)?([a-zA-Z0-9-]+)\.'

    for url in urls:
        match = re.search(pattern, url)
        if match:
            print(match.group(1))

def bai9():
# 9. Tìm tất cả từ khóa bắt đầu bằng # trong đoạn văn bản.
    hashtag_text = "Tôi yêu #Python và #MachineLearning, bạn có thích #AI không?"

    pattern = r'#\w+'

    matches = re.findall(pattern, hashtag_text)

    print("Các từ tìm được:")
    for tag in matches:
        print(tag)

def bai10():
# 10. Kiểm tra xem chuỗi có phải là số thực dương (thập phân) không.
# Hợp lệ: "3.14", "0.5", "10.0"
# Không hợp lệ: ".", "3.", "abc", "-1.2"
    nums = ["3.14", "0.5", "10.0", ".", "3.", "abc", "-1.2"]

    pattern = r'^[0-9]+\.[0-9]+$'

    for num in nums:
        if re.match(pattern, num):
            print(f"{num} ➜ Hợp lệ")
        else:
            print(f"{num} ➜ Không hợp lệ")

def bai11():
# 11. Tìm và in ra tất cả các email trong chuỗi văn bản.
    email_text = "Liên hệ qua email: support@example.com, admin@domain.org hoặc hello.world123@gmail.com."

    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    matches = re.findall(pattern, email_text)

    print("Các email tìm được:")
    for email in matches:
        print(email)

def bai12():
# 12. Tìm các số nguyên hoặc thập phân dương/âm trong chuỗi.
    number_text = "Nhiệt độ hôm nay là -10.5 độ, hôm qua là 25 và ngày mai có thể là -3."

    pattern = r'-?\d+(?:\.\d+)?'  # Dùng (?:...) thay vì (...) để không tách nhóm

    matches = re.findall(pattern, number_text)

    print("Các số tìm được:")
    for num in matches:
        print(num)

def bai13():
# 13. Tìm tất cả các từ dài hơn 6 ký tự trong câu.
    long_word_text = "Programming in Python is sometimes enjoyable and sometimes frustrating."

    pattern = r'\b\w{7,}\b'

    matches = re.findall(pattern, long_word_text)

    print("Các từ dài hơn 6 ký tự:")
    for word in matches:
        print(word)

def bai14():
# 14. Mã bưu điện VN gồm 5 chữ số. Kiểm tra chuỗi có phải mã hợp lệ không.
    postal_codes = ["70000", "123456", "ABCDE", "00000", "7500"]

    pattern = r'^\d{5}$'

    print("Kết quả kiểm tra mã bưu điện:")
    for code in postal_codes:
        if re.match(pattern, code):
            print(f"{code} ➜ Hợp lệ")
        else:
            print(f"{code} ➜ Không hợp lệ")

def bai15():
# 15. Trích xuất tất cả từ viết hoa toàn bộ (ví dụ như tên viết tắt, hoặc từ nhấn mạnh).
    uppercase_text = "Chúng tôi làm việc với NASA, WHO và các tổ chức như UNICEF, nhưng không phải USAID."

    pattern = r'\b[A-Z]{2,}\b'

    matches = re.findall(pattern, uppercase_text)

    print("Từ viết hoa toàn bộ tìm được:")
    for word in matches:
        print(word)

def menu():
    while True:
        choice = input("\nNhập số bài muốn chạy (1-15), 'all' để chạy tất cả, hoặc 0 để thoát: ")

        if choice == "0":
            print("Kết thúc chương trình.")
            break
        elif choice == "all":
            for i in range(1, 16):
                globals()[f"bai{i}"]()  # Gọi hàm theo tên: bai1(), bai2(), ...
        elif choice.isdigit() and 1 <= int(choice) <= 15:
            globals()[f"bai{int(choice)}"]()
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 15, 'all' hoặc 0 để thoát.")

menu()
