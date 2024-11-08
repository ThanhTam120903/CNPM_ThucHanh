# Khởi tạo từ điển Anh-Việt
dictionary = {}


def add_word():
    english = input("Nhập từ tiếng Anh: ")
    vietnamese = input("Nhập nghĩa tiếng Việt: ")
    dictionary[english] = vietnamese
    print(f"Đã thêm: {english} -> {vietnamese}")


def display_dictionary():
    if not dictionary:
        print("Từ điển hiện đang trống.")
    else:
        print(f"Từ điển có {len(dictionary)} từ:")
        for english, vietnamese in dictionary.items():
            print(f"{english} -> {vietnamese}")


def search_word():
    english = input("Nhập từ tiếng Anh cần tìm: ")
    if english in dictionary:
        print(f"Tìm thấy: {english} -> {dictionary[english]}")
    else:
        print("Không tìm thấy từ này trong từ điển.")


def delete_word():
    english = input("Nhập từ tiếng Anh cần xóa: ")
    if english in dictionary:
        del dictionary[english]
        print(f"Đã xóa từ: {english}")
    else:
        print("Không tìm thấy từ này trong từ điển.")


# Menu chính
def main():
    while True:
        print("\nChương trình từ điển Anh-Việt:")
        print("1. Thêm từ mới vào từ điển")
        print("2. Hiển thị từ điển và số lượng từ")
        print("3. Tìm kiếm từ tiếng Anh")
        print("4. Xóa một từ dựa trên từ khóa")
        print("5. Thoát chương trình")

        choice = input("Chọn một chức năng (1-5): ")

        if choice == '1':
            add_word()
        elif choice == '2':
            display_dictionary()
        elif choice == '3':
            search_word()
        elif choice == '4':
            delete_word()
        elif choice == '5':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")


if __name__ == "__main__":
    main()
