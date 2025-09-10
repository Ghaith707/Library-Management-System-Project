data = {"title1": "The world of math", "writer1": "Saleh"}
see = "show books"
add = "add"
remove = "delete"
find = "search"
quit = "exit"
print("اختر:", see, "او", add, "او", remove, "او", find, "او", quit)
choice = input("اكتب اختيارك: ")
if choice == see:
    print(data)
elif choice == add:
    t = input("اكتب اسم الكتاب: ")
    w = input("اكتب اسم المؤلف: ")
    idx = len(data) // 2 + 1
    data[f"title{idx}"] = t
    data[f"writer{idx}"] = w
    print("تمت الإضافة ")
    print(data)
elif choice == remove:
    r = input("اكتب المفتاح الذي تريد حذفه: ")
    if r in data:
        del data[r]
        print("تم الحذف ")
    else:
        print(" غير موجود")
    print(data)
elif choice == find:
    word = input("اكتب كلمة للبحث: ")
    hit = False
    for v in data.values():
        if word.lower() in v.lower():
            print(" وجد:", v)
            hit = True
    if not hit:
        print(" لم يتم العثور")
elif choice == quit:
    print("مع السلامة ")
