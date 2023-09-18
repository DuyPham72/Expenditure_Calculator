from math import ceil

def giao_dien():
    print('-'*70)
    print('')
    print('Nhấn 1 nếu bạn chưa lên kế hoạch chi tiêu')
    print('Nhấn 2 nếu bạn muốn bỏ thêm tiền vào tiền chi tiêu')
    print('Nhấn 3 nếu bạn muốn rút bớt tiền ra khỏi tiền chi tiêu')
    print('Nhấn 4 nếu bạn muốn lên kế hoạch chi tiêu lại')
    print('Nhấn 5 nếu bạn muốn thống kê chi tiêu tháng nào đó')
    print('Nhấn 6 nếu bạn muốn thoát chương trình')
    chon = str(input('Nhập quyết định của bạn vào đây: '))
    print('')
    print('-'*70)
    if chon == '1':
        return begin()
    elif chon == '2':
        return them()
    elif chon == '3':
        return bot()
    elif chon == '4':
        return again()
    elif chon == '5':
        return thong_ke_thang()
    elif chon == '6':
        return thoat()
    else:
        print('')
        print('Dữ liệu nhập vào không trùng khớp, xin bạn nhập lại: ')
        print('')
        return giao_dien()

def them():
    with open('chi_tieu.txt') as note:
        try:
            data = list(note)[-2]
            tien_chi_tieu = float(data.rstrip())
        except Exception:
            print('-'*70)
            print('')
            print('Không tìm thấy tiền chi tiêu')
            print('Bạn sẽ được đưa về màn hình chính')
            print('')
            print('-'*70)
            return giao_dien()
    
    print('')
    try:
        add = float(input('Nhập số tiền bạn muốn thêm vào tiền chi tiêu: '))
        print('Nhấn 1 nếu là tiền ba má gửi qua cho')
        print('Nhấn 2 nếu là tiền mượn của dì Ba hoặc dượng')
        print('Nhấn 3 nếu là tiền mượn của người khác')
        print('Nhấn 4 nếu là tiền được ai đó cho')
        print('Nhấn 5 nếu là tiền đi làm thêm')
        print('Nhấn 6 nếu là tiền học bổng')
        print('Nhấn 7 nếu là tiền trợ cấp')
        ghi_chu = int(input('Nhập lý do bạn thêm vào: '))
        if ghi_chu not in [1,2,3,4,5,6,7]:
            print('-'*70)
            print('')
            print('Dữ liệu truyền vào không khớp với điều kiện')
            print('Xin vui lòng nhập lại')
            print('')
            print('-'*70)
            return them()
        thang = int(input('Nhập tháng hiện tại của bạn vào (1 -> 12): '))
        if thang not in range(1,13):
            print('-'*70)
            print('')
            print('Không tồn tại tháng này')
            print('Xin bạn vui lòng nhập lại')
            print('')
            print('-'*70)
            return them()
        nam = int(input('Nhập năm hiện tại vào: '))
        if nam < 2020:
            print('-'*70)
            print('')
            print('Không tồn tại năm này')
            print('Xin bạn vui lòng nhập lại')
            print('')
            print('-'*70)
            return them()
    except Exception:
        print('-'*70)
        print('')
        print('Dữ liệu nhập vào không hợp lệ')
        print('Xin bạn nhập lại theo đúng kiểu dữ liệu')
        print('')
        print('-'*70)
        return them()    
    print('')

    print('-'*70)
    print('')
    print('Xác nhận thông tin nhập vào:')
    print('Nhấn 1 nếu mọi thông tin nhập vào là chính xác')
    print('Nhấn 0 nếu bạn muốn sửa lại các thông tin ở trên')
    confirm = str(input('Nhập quyết định của bạn vào đây: '))
    print('')
    print('-'*70)

    if confirm == '1':
        tien_chi_tieu += add

        if ghi_chu == 1:
            ghi_chu = 'Ba ma gui qua cho'
        elif ghi_chu == 2: 
            ghi_chu = 'Muon cua di Ba hoac duong'
        elif ghi_chu == 3:
            ghi_chu = 'Muon cua nguoi khac'
        elif ghi_chu == 4:
            ghi_chu = 'Ai do cho'
        elif ghi_chu == 5:
            ghi_chu = 'Di lam them'
        elif ghi_chu == 6:
            ghi_chu = 'Hoc bong'
        else:
            ghi_chu = 'Tro cap'

        print('')
        with open('chi_tieu.txt', mode='a+') as note:
            data = note.write('+ Thang {0} nam {1}\n'.format(thang,nam))
            data = note.write('Ban da them vao tien chi tieu:\n')
            data = note.write('{0}\n'.format(add))
            data = note.write('Ly do co duoc tien vao la:\n')
            data = note.write('{0}\n'.format(str(ghi_chu)))
            data = note.write('Chi tieu tong hien tai la:\n')
            data = note.write(str(round(tien_chi_tieu,2)))
            data = note.write('\n\n')
           
        print('')
        print('Bạn đã thêm ${0} vào tiền chi tiêu'.format(add))
        print('Tiền chi tiêu hiện tại của bạn là: ${0}'.format(round(tien_chi_tieu,2)))
        return giao_dien()
    elif confirm == '0': 
        return them()
    else:
        print('')
        print('Dữ liệu không hợp lệ, bạn sẽ bị đưa về giao diện ban đầu')
        return giao_dien()

def bot():  
    with open('chi_tieu.txt') as note:
        try:
            data = list(note)[-2]
            tien_chi_tieu = float(data.rstrip())
        except Exception:
            print('-'*70)
            print('')
            print('Không tìm thấy tiền chi tiêu')
            print('Bạn sẽ được đưa về màn hình chính')
            print('')
            print('-'*70)
            return giao_dien()
            
    print('')
    try:
        minus  = float(input('Nhập số tiền bạn muốn rút khỏi tiền chi tiêu: '))
        print('Nhấn 1 nếu mua đồ ăn')
        print('Nhấn 2 nếu mua quần áo')
        print('Nhấn 3 nếu mua đồ dùng học tập')
        print('Nhấn 4 nếu mua thiết bị cá nhân')
        print('Nhấn 5 nếu mua quà tặng bạn')
        print('Nhấn 6 nếu mua tặng quà cho dì Ba hoặc dượng')
        print('Nhấn 7 nếu mua quà tặng ba mẹ')
        print('Nhấn 8 nếu mua đồ giùm ba mẹ')
        print('Nhấn 9 nếu mua đồ giùm người khác')
        print('Nhấn 10 nếu là tiền tiết kiệm')
        ghi_chu = int(input('Nhập lý do bạn rút ra (Có thể bỏ trống, nếu ghi thì không sử dụng dấu): '))
        if ghi_chu not in [1,2,3,4,5,6,7,8,9]:
            print('-'*70)
            print('')
            print('Dữ liệu truyền vào không khớp với điều kiện')
            print('Xin vui lòng nhập lại')
            print('')
            print('-'*70)
            return bot()
        thang = int(input('Nhập tháng hiện tại của bạn vào (1 -> 12): '))
        if thang not in range(1,13):
            print('-'*70)
            print('')
            print('Không tồn tại tháng này')
            print('Xin bạn vui lòng nhập lại')
            print('')
            print('-'*70)
            return bot()
        nam = int(input('Nhập năm hiện tại vào: '))
        if nam < 2020:
            print('-'*70)
            print('')
            print('Không tồn tại năm này')
            print('Xin bạn vui lòng nhập lại')
            print('')
            print('-'*70)
            return bot()
    except Exception:
        print('-'*70)
        print('')
        print('Dữ liệu nhập vào không hợp lệ')
        print('Xin bạn nhập lại theo đúng kiểu dữ liệu')
        print('')
        print('-'*70)
        return bot()    
    print('')

    print('-'*70)
    print('')
    print('Xác nhận thông tin nhập vào:')
    print('Nhấn 1 nếu mọi thông tin nhập vào là chính xác')
    print('Nhấn 0 nếu bạn muốn sửa lại các thông tin ở trên')
    confirm = str(input('Nhập quyết định của bạn vào đây: '))
    print('')
    print('-'*70)

    if minus < tien_chi_tieu:
        if confirm == '1':
            tien_chi_tieu -= minus

            if ghi_chu == 1:
                ghi_chu = 'Mua do an'
            elif ghi_chu == 2: 
                ghi_chu = 'Mua quan ao'
            elif ghi_chu == 3:
                ghi_chu = 'Mua do dung hoc tap'
            elif ghi_chu == 4:
                ghi_chu = 'Mua thiet bi ca nhan'
            elif ghi_chu == 5:
                ghi_chu = 'Mua qua tang ban'
            elif ghi_chu == 6:
                ghi_chu = 'Mua qua cho di Ba hoac duong'
            elif ghi_chu == 7:
                ghi_chu = 'Mua qua tang ba me'
            elif ghi_chu == 8:
                ghi_chu = 'Mua do gium ba me'
            elif ghi_chu == 9:
                ghi_chu = 'Mua do gium nguoi khac'
            else:
                ghi_chu = 'Tiet kiem'

            print('')
            with open('chi_tieu.txt', mode='a+') as note:
                    data = note.write('- Thang {0} nam {1}\n'.format(thang,nam))
                    data = note.write('Ban da rut ra khoi tien chi tieu:\n')
                    data = note.write('{0}\n'.format(minus))
                    data = note.write('Ly do rut tien la:\n')
                    data = note.write('{0}\n'.format(ghi_chu))
                    data = note.write('Chi tieu tong hien tai la: \n')
                    data = note.write(str(round(tien_chi_tieu,2)))
                    data = note.write('\n\n')    

            print('')
            print('Bạn đã rút ${0} vào tiền chi tiêu'.format(minus))
            print('Tiền chi tiêu hiện tại của bạn là: ${0}'.format(round(tien_chi_tieu,2)))
            return giao_dien()
        elif confirm == '0': 
            return bot()
        else:
            print('')
            print('Dữ liệu không hợp lệ, bạn sẽ bị đưa về giao diện ban đầu')
            return giao_dien()
    else:
        print('')
        print('Số tiền rút ra nhiều hơn số tiền trong tài khoản')
        print('Bạn sẽ được đưa về giao diện ban đầu')
        return giao_dien()

def thoat():
    print('')
    print('Xác nhận thông tin nhập vào:')
    print('Nhấn 1 nếu bạn muốn thoát chương trình')
    print('Nhấn 0 nếu bạn muốn hủy bỏ quyết định vừa rồi')
    confirm = str(input('Nhập quyết định của bạn vào đây: '))
    print('')
    print('-'*70)
    if confirm == '1':
        print('Cảm ơn bạn đã sử dụng chương trình'.center(70,'-'))
        ket_thuc = input('(Nhấn Enter để tắt chương trình)'.center(70,'-'))
        return None
    elif confirm == '0':
        return giao_dien()
    else:
        print('')
        print('Dữ liệu truyền vào không hợp lệ, bạn sẽ được đưa về màn hình chính')
        print('')
        return giao_dien()

def begin():
    print('')
    try:
        tien_gui = float(input('Nhập số tiền gửi (VD: 2000): '))
        thang_gia_han_bhyt = int(input('Nhập tháng gần nhất bạn gia hạn BHYT (1 -> 12): '))
        thoi_han_bhyt = int(input('Nhập thời hạn của bảo hiểm y tế (1 -> 12): '))
        tien_bhyt_thang_dau = int(input('Nhập tiền gia hạn BHYT (VD: 181): '))
        tien_bhyt_cac_thang_sau = int(input('Nhập tiền BHYT các tháng kế tiếp (VD: 131): '))
        tien_dth = int(input('Nhập tiền điện thoại hằng tháng (VD: 60): '))
        thang_hien_tai = int(input('Nhập tháng hiện tại (1 -> 12): '))
        if thang_hien_tai not in range(1,13):
            print('-'*70)
            print('')
            print('Không tồn tại tháng này')
            print('Xin bạn vui lòng nhập lại')
            print('')
            print('-'*70)
            return begin()
        thang = int(input('Nhập số tháng bạn muốn tính (1 -> ...): '))
    except Exception:
        print('')
        print('Dữ liệu nhập vào không hợp lệ')
        print('Xin bạn nhập lại theo đúng kiểu dữ liệu')
        print('')
        return begin()    
    print('-'*70)

    print('')
    print('Xác nhận thông tin nhập vào:')
    print('Nhấn 1 nếu mọi thông tin nhập vào là chính xác')
    print('Nhấn 0 nếu bạn muốn sửa lại các thông tin ở trên')
    confirm = str(input('Nhập quyết định của bạn vào đây: '))
    print('-'*70)

    if confirm == '1':
        key = thang // 12
        if key > 0 or key <= 1:
            key = 1
        else:
            key = ceil(key)

        print('')
        for i in range(1,thang+1):
            tien_ban_dau = tien_gui
            tien_chi_tieu = tien_gui
            thang_bat_dau = thang_hien_tai +1
            thang_bat_dau_bhyt_moi = thang_gia_han_bhyt + thoi_han_bhyt 

            for _ in range(i):
                if thang_bat_dau == (thang_gia_han_bhyt or thang_gia_han_bhyt + j for j in range(1,key + 1))  or thang_bat_dau == (thang_bat_dau_bhyt_moi or thang_bat_dau_bhyt_moi + j for j in range(1,key + 1)) :
                    tien_chi_tieu -= tien_bhyt_thang_dau
                    thang_bat_dau += 1
                else:
                    tien_chi_tieu -= tien_bhyt_cac_thang_sau
                    thang_bat_dau += 1

            tong_tien_bhyt = tien_ban_dau - tien_chi_tieu

            thue_dth = (tien_dth /10)
            tien_chi_tieu -= (tien_dth*i + thue_dth*i)
            tong_tien_dth = round(tien_dth*i + thue_dth*i)

            if tien_chi_tieu/ i > 0:
                if i < 10:
                    print('Tiền chi tiêu trong {0} tháng là:\t\t\t${1}'.format(str(i),str(round(tien_chi_tieu,2))))
                    print('Trong đó mỗi tháng được tiêu tối đa là:\t\t${0}'.format(str(round(tien_chi_tieu/ i,2))))  
                    print('Tiền sử dụng để trả BHYT và điện thoại là:\t${0}'.format(round(tong_tien_dth + tong_tien_bhyt,2)))
                    print('')
                else:
                    print('Tiền chi tiêu trong {0} tháng là:\t\t${1}'.format(str(i),str(round(tien_chi_tieu,2))))
                    print('Trong đó mỗi tháng được tiêu tối đa là:\t\t${0}'.format(str(round(tien_chi_tieu/ i,2))))  
                    print('Tiền sử dụng để trả BHYT và điện thoại là:\t${0}'.format(round(tong_tien_dth + tong_tien_bhyt,2)))
                    print('')

        print('-'*70)
        print('')
        print('Các tháng không được in ra là các tháng có chi tiêu dưới $0 '.center(70,'-'))
        print('')
        print('-'*70)

        return luu_thong_tin_begin(tien_gui, thang_hien_tai, thang_gia_han_bhyt, thoi_han_bhyt, tien_bhyt_thang_dau, tien_bhyt_cac_thang_sau, tien_dth)
    elif confirm == '0':
        return begin()
    else:
        print('')
        print('Dữ liệu nhập vào không hợp lệ, bạn sẽ đưa trở về màn hình chính')
        print('')
        return giao_dien()

def again():
    with open('chi_tieu.txt') as note:
        try:
            data = list(note)[-2]
            tien_gui = float(data.rstrip())
        except Exception:
            print('Không tìm thấy tiền chi tiêu')
            print('Bạn sẽ được đưa về màn hình chính')
            return giao_dien()

    print('')
    try:
        thang_gia_han_bhyt = int(input('Nhập tháng gần nhất bạn gia hạn BHYT (1 -> 12): '))
        thoi_han_bhyt = int(input('Nhập thời hạn của bảo hiểm y tế (1 -> 12): '))
        tien_bhyt_thang_dau = int(input('Nhập tiền gia hạn BHYT (VD: 181): '))
        tien_bhyt_cac_thang_sau = int(input('Nhập tiền BHYT các tháng kế tiếp (VD: 131): '))
        tien_dth = int(input('Nhập tiền điện thoại hằng tháng (VD: 60): '))
        thang_hien_tai = int(input('Nhập tháng hiện tại (1 -> 12): '))
        if thang_hien_tai not in range(1,13):
            print('')
            print('Không tồn tại tháng này')
            print('Xin bạn vui lòng nhập lại')
            print('')
            print('-'*70)
            return again()
        thang = int(input('Nhập số tháng bạn muốn tính (1 -> ...): '))
    except Exception:
        print('')
        print('Dữ liệu nhập vào không hợp lệ')
        print('Xin bạn nhập lại theo đúng kiểu dữ liệu')
        print('')
        return again()    
    print('-'*70)

    print('')
    print('Xác nhận thông tin nhập vào:')
    print('Nhấn 1 nếu mọi thông tin nhập vào là chính xác')
    print('Nhấn 0 nếu bạn muốn sửa lại các thông tin ở trên')
    confirm = str(input('Nhập quyết định của bạn vào đây: '))
    print('-'*70)

    if confirm == '1':
        key = thang // 12
        if key > 0 or key <= 1:
            key = 1
        else:
            key = ceil(key)

        print('')
        for i in range(1,thang+1):
            tien_ban_dau = tien_gui
            tien_chi_tieu = tien_gui
            thang_bat_dau = thang_hien_tai +1
            thang_bat_dau_bhyt_moi = thang_gia_han_bhyt + thoi_han_bhyt 

            for _ in range(i):
                if thang_bat_dau == (thang_gia_han_bhyt or thang_gia_han_bhyt + j for j in range(1,key + 1))  or thang_bat_dau == (thang_bat_dau_bhyt_moi or thang_bat_dau_bhyt_moi + j for j in range(1,key + 1)) :
                    tien_chi_tieu -= tien_bhyt_thang_dau
                    thang_bat_dau += 1
                else:
                    tien_chi_tieu -= tien_bhyt_cac_thang_sau
                    thang_bat_dau += 1

            tong_tien_bhyt = tien_ban_dau - tien_chi_tieu
            
            thue_dth = (tien_dth /10)
            tien_chi_tieu -= (tien_dth*i + thue_dth*i)
            tong_tien_dth = round(tien_dth*i + thue_dth*i)

            if tien_chi_tieu/ i > 0:
                if i < 10:
                    print('Tiền chi tiêu trong {0} tháng là:\t\t\t${1}'.format(str(i),str(round(tien_chi_tieu,2))))
                    print('Trong đó mỗi tháng được tiêu tối đa là:\t\t${0}'.format(str(round(tien_chi_tieu/ i,2))))  
                    print('Tiền sử dụng để trả BHYT và điện thoại là:\t${0}'.format(round(tong_tien_dth + tong_tien_bhyt,2)))
                    print('')
                else:
                    print('Tiền chi tiêu trong {0} tháng là:\t\t${1}'.format(str(i),str(round(tien_chi_tieu,2))))
                    print('Trong đó mỗi tháng được tiêu tối đa là:\t\t${0}'.format(str(round(tien_chi_tieu/ i,2))))  
                    print('Tiền sử dụng để trả BHYT và điện thoại là:\t${0}'.format(round(tong_tien_dth + tong_tien_bhyt,2)))
                    print('')    

        print('-'*70)
        print('')
        print('Các tháng không được in ra là các tháng có chi tiêu dưới $0 '.center(70,'-'))
        print('')
        print('-'*70)
        return luu_thong_tin_again(tien_gui, thang_hien_tai, thang_gia_han_bhyt, thoi_han_bhyt, tien_bhyt_thang_dau, tien_bhyt_cac_thang_sau, tien_dth)
    elif confirm == '0':
        return again()
    else:
        print('')
        print('Dữ liệu nhập vào không hợp lệ, bạn sẽ đưa trở về màn hình chính')
        print('')
        return giao_dien()

def luu_thong_tin_begin(tien_gui, thang_hien_tai, thang_gia_han_bhyt, thoi_han_bhyt, tien_bhyt_thang_dau, tien_bhyt_cac_thang_sau, tien_dth):
    print('')
    # Chọn số tháng muốn tính
    try:
        choose = int(input('Chọn số tháng bạn muốn trong các tháng trên để lưu lại: '))
        nam = int(input('Nhập năm hiện tại vào: '))
        if nam < 2020:
            print('-'*70)
            print('')
            print('Không tồn tại năm này')
            print('Xin bạn vui lòng nhập lại')
            print('')
            print('-'*70)
            return luu_thong_tin_begin(tien_gui, thang_hien_tai, thang_gia_han_bhyt, thoi_han_bhyt, tien_bhyt_thang_dau, tien_bhyt_cac_thang_sau, tien_dth)
    except Exception:
        print('')
        print('Dữ liệu nhập vào không hợp lệ')
        print('Xin bạn nhập lại theo đúng kiểu dữ liệu')
        print('')
        return luu_thong_tin_begin(tien_gui, thang_hien_tai, thang_gia_han_bhyt, thoi_han_bhyt, tien_bhyt_thang_dau, tien_bhyt_cac_thang_sau, tien_dth)
    print('-'*70)

    print('')
    print('Xác nhận thông tin nhập vào:')
    print('Nhấn 1 nếu mọi thông tin nhập vào là chính xác')
    print('Nhấn 0 nếu bạn muốn sửa lại thông tin ở trên')
    confirm = str(input('Nhập quyết định của bạn vào đây: '))
    print('-'*70)
    if confirm == '1':
        # Tính chi tiêu trong số đó tháng
        key = choose // 12
        if key > 0 or key <= 1:
            key = 1
        else:
            key = ceil(key)
        tien_ban_dau = tien_gui
        tien_chi_tieu = tien_gui
        thang_bat_dau = thang_hien_tai +1
        thang_bat_dau_bhyt_moi = thang_gia_han_bhyt + thoi_han_bhyt 

        print('')
        for _ in range(choose):
            if thang_bat_dau == (thang_gia_han_bhyt or thang_gia_han_bhyt + j for j in range(1,key + 1))  or thang_bat_dau == (thang_bat_dau_bhyt_moi or thang_bat_dau_bhyt_moi + j for j in range(1,key + 1)) :
                tien_chi_tieu -= tien_bhyt_thang_dau
                thang_bat_dau += 1
            else:
                tien_chi_tieu -= tien_bhyt_cac_thang_sau
                thang_bat_dau += 1

        tong_tien_bhyt = tien_ban_dau - tien_chi_tieu

        thue_dth = (tien_dth /10)
        tien_chi_tieu -= (tien_dth*choose + thue_dth*choose)
        tong_tien_dth = round(tien_dth*choose + thue_dth*choose)

        print('')
        if choose < 10:
            print('Bạn chọn {0} tháng, trong đó: '.format(str(choose)))
            print('Tiền chi tiêu trong {0} tháng là:\t\t\t${1}'.format(str(choose),str(round(tien_chi_tieu,2))))
            print('Trong đó mỗi tháng được tiêu tối đa là:\t\t${0}'.format(str(round(tien_chi_tieu/ choose,2))))
            print('Tiền sử dụng để trả BHYT và điện thoại là:\t${0}'.format(round(tong_tien_dth + tong_tien_bhyt,2)))
        else:
            print('Bạn chọn {0} tháng, trong đó: '.format(str(choose)))
            print('Tiền chi tiêu trong {0} tháng là:\t\t${1}'.format(str(choose),str(round(tien_chi_tieu,2))))
            print('Trong đó mỗi tháng được tiêu tối đa là:\t\t${0}'.format(str(round(tien_chi_tieu/ choose,2))))
            print('Tiền sử dụng để trả BHYT và điện thoại là:\t${0}'.format(round(tong_tien_dth + tong_tien_bhyt,2)))
        print('')
        print('-'*70)

        with open('chi_tieu.txt', mode='a+') as note:
            data = note.write('Thoi diem hien tai la thang {0} nam {1}\n'.format(thang_hien_tai,nam))
            data = note.write('Chi tieu hang thang neu su dung trong {0} thang la: ${1}\n'.format(str(choose),str(round(tien_chi_tieu/ choose,2))))
            data = note.write('Tien su dung de tra BHYT va tien dien thoai la: ${0}\n'.format(round(tong_tien_dth + tong_tien_bhyt,2)))
            data = note.write('Tien BHYT chiem {0}%\n'.format(round((tong_tien_bhyt/(tong_tien_bhyt+tong_tien_dth))*100,2)))
            data = note.write('Tien dien thoai chiem {0}%\n'.format(round((tong_tien_dth/(tong_tien_bhyt+tong_tien_dth))*100,2)))
            data = note.write('Chi tieu tong la: \n')
            data = note.write('{0}'.format(str(round(tien_chi_tieu,2))))
            data = note.write('\n\n')

        print('')
        print('Tiền chi tiêu của bạn đã được thiết lập')
        print('')
        return giao_dien()
    elif confirm == '0':
        return luu_thong_tin_begin(tien_gui, thang_hien_tai, thang_gia_han_bhyt, thoi_han_bhyt, tien_bhyt_thang_dau, tien_bhyt_cac_thang_sau, tien_dth)
    else:
        print('')
        print('Dữ liệu nhập vào không hợp lệ, xin bạn nhập lại')
        print('')
        return giao_dien()

def luu_thong_tin_again(tien_gui, thang_hien_tai, thang_gia_han_bhyt, thoi_han_bhyt, tien_bhyt_thang_dau, tien_bhyt_cac_thang_sau, tien_dth):
    print('')
    # Chọn số tháng muốn tính'
    try:    
        choose = int(input('Chọn số tháng bạn muốn trong các tháng trên để lưu lại: '))
        nam = int(input('Nhập năm hiện tại vào: '))
        if nam < 2020:
            print('-'*70)
            print('')
            print('Không tồn tại năm này')
            print('Xin bạn vui lòng nhập lại')
            print('')
            print('-'*70)
            return luu_thong_tin_again(tien_gui, thang_hien_tai, thang_gia_han_bhyt, thoi_han_bhyt, tien_bhyt_thang_dau, tien_bhyt_cac_thang_sau, tien_dth)
    except Exception:
        print('')
        print('Dữ liệu nhập vào không hợp lệ')
        print('Xin bạn nhập lại theo đúng kiểu dữ liệu')
        print('')
        return luu_thong_tin_again(tien_gui, thang_hien_tai, thang_gia_han_bhyt, thoi_han_bhyt, tien_bhyt_thang_dau, tien_bhyt_cac_thang_sau, tien_dth)
    print('-'*70)

    print('')
    print('Xác nhận thông tin nhập vào:')
    print('Nhấn 1 nếu mọi thông tin nhập vào là chính xác')
    print('Nhấn 0 nếu bạn muốn sửa lại thông tin ở trên')
    confirm = str(input('Nhập quyết định của bạn vào đây: '))
    print('')
    print('-'*70)

    if confirm =='1':
        # Tính chi tiêu trong số đó tháng
        key = choose // 12
        if key > 0 or key <= 1:
            key = 1
        else:
            key = ceil(key)
        tien_ban_dau = tien_gui
        tien_chi_tieu = tien_gui
        thang_bat_dau = thang_hien_tai +1
        thang_bat_dau_bhyt_moi = thang_gia_han_bhyt + thoi_han_bhyt 

        print('')
        for _ in range(choose):
            if thang_bat_dau == (thang_gia_han_bhyt or thang_gia_han_bhyt + j for j in range(1,key + 1))  or thang_bat_dau == (thang_bat_dau_bhyt_moi or thang_bat_dau_bhyt_moi + j for j in range(1,key + 1)) :
                tien_chi_tieu -= tien_bhyt_thang_dau
                thang_bat_dau += 1
            else:
                tien_chi_tieu -= tien_bhyt_cac_thang_sau
                thang_bat_dau += 1

        tong_tien_bhyt = tien_ban_dau - tien_chi_tieu

        thue_dth = (tien_dth /10)
        tien_chi_tieu -= (tien_dth*choose + thue_dth*choose)
        tong_tien_dth = round(tien_dth*choose + thue_dth*choose)

        print('')
        if choose < 10:
            print('Bạn chọn {0} tháng, trong đó: '.format(str(choose)))
            print('Tiền chi tiêu trong {0} tháng là:\t\t\t${1}'.format(str(choose),str(round(tien_chi_tieu,2))))
            print('Trong đó mỗi tháng được tiêu tối đa là:\t\t${0}'.format(str(round(tien_chi_tieu/ choose,2))))
            print('Tiền sử dụng để trả BHYT và điện thoại là:\t${0}'.format(round(tong_tien_dth + tong_tien_bhyt,2)))
        else:
            print('Bạn chọn {0} tháng, trong đó: '.format(str(choose)))
            print('Tiền chi tiêu trong {0} tháng là:\t\t${1}'.format(str(choose),str(round(tien_chi_tieu,2))))
            print('Trong đó mỗi tháng được tiêu tối đa là:\t\t${0}'.format(str(round(tien_chi_tieu/ choose,2))))
            print('Tiền sử dụng để trả BHYT và điện thoại là:\t${0}'.format(round(tong_tien_dth + tong_tien_bhyt,2)))
        print('')
        print('-'*70)

        with open('chi_tieu.txt', mode='a+') as note:
            data = note.write('Thoi diem hien tai la thang {0} nam {1}\n'.format(thang_hien_tai,nam))
            data = note.write('Chi tieu hang thang neu su dung trong {0} thang la: ${1}\n'.format(str(choose),str(round(tien_chi_tieu/ choose,2))))
            data = note.write('Tien su dung de tra BHYT va tien dien thoai la: ${0}\n'.format(round(tong_tien_dth + tong_tien_bhyt,2)))
            data = note.write('Tien BHYT chiem {0}%\n'.format(round((tong_tien_bhyt/(tong_tien_bhyt+tong_tien_dth))*100,2)))
            data = note.write('Tien dien thoai chiem {0}%\n'.format(round((tong_tien_dth/(tong_tien_bhyt+tong_tien_dth))*100,2)))
            data = note.write('Chi tieu tong la: \n')
            data = note.write('{0}'.format(str(round(tien_chi_tieu,2))))
            data = note.write('\n\n')

        print('')
        print('Tiền chi tiêu của bạn đã được cập nhật')
        print('')
        return giao_dien()
    elif confirm == '0':
        return luu_thong_tin_again(tien_gui, thang_hien_tai, thang_gia_han_bhyt, thoi_han_bhyt, tien_bhyt_thang_dau, tien_bhyt_cac_thang_sau, tien_dth)
    else:
        print('')
        print('Dữ liệu nhập vào không hợp lệ, xin bạn nhập lại')
        print('')
        return giao_dien()

def thong_ke_thang():
    with open('chi_tieu.txt') as note:
        try:
            data = list(note)
        except Exception:
            print('')
            print('Chưa có dữ liệu gì trong file')
            print('')
            print('-'*70)
            return giao_dien()
    
    thu_vao = []
    chi_ra = []
    ly_do_thu_vao = []
    ly_do_chi_ra = []
    key = 0

    print('')
    try:
        thang = int(input('Nhập tháng bạn muốn thống kê vào: '))
        if thang not in range(1,13):
            print('-'*70)
            print('')
            print('Không tồn tại tháng này')
            print('Xin bạn vui lòng nhập lại')
            print('')
            print('-'*70)
            return thong_ke_thang()
        nam = int(input('Nhập năm bạn muốn thống kê vào: '))
        if nam < 2020:
            print('-'*70)
            print('')
            print('Không tồn tại năm này')
            print('Xin bạn vui lòng nhập lại')
            print('')
            print('-'*70)
            return thong_ke_thang()
    except Exception:
        print('-'*70)
        print('')
        print('Dữ liệu truyền vào không hợp lệ')
        print('Xin bạn vui lòng nhập lại')
        print('')
        print('-'*70)
        return thong_ke_thang()

    cau_dieu_kien_thu_vao = '+ Thang {0} nam {1}\n'.format(thang,nam)
    cau_dieu_kien_chi_ra = '- Thang {0} nam {1}\n'.format(thang,nam)

    for i in range(len(data)):
        if data[i] == cau_dieu_kien_thu_vao:
            thu_vao.append(float(data[i+2].rstrip()))
            ly_do_thu_vao.append(str(data[i+4].rstrip()))
        elif data[i] == cau_dieu_kien_chi_ra:
            chi_ra.append(float(data[i+2].rstrip()))
            ly_do_chi_ra.append(str(data[i+4].rstrip()))

    print('')
    print('-'*70)
    print('')

    print('Tổng số tiền thu vào của tháng {0} năm {1} là:\t\t${2}'.format(thang, nam, sum(thu_vao)))
    print('Tổng số tiền chi ra của tháng {0} năm {1} là:\t\t${2}'.format(thang, nam, sum(chi_ra)))
    print('Trong đó: ')

    print('')
    print('-'*70)
    print('')

    print('Thống kê lý do thu vào gồm:')
    print('\tSố lần ba má gửi qua cho là:\t\t\t{0} lần'.format(ly_do_thu_vao.count('Ba ma gui qua cho')))
    print('\tSố lần mượn của dì Ba hoặc dượng là:\t\t{0} lần'.format(ly_do_thu_vao.count('Muon cua di Ba hoac duong')))
    print('\tSố lần mượn của người khác là:\t\t\t{0} lần'.format(ly_do_thu_vao.count('Muon cua nguoi khac')))
    print('\tSố lần ai đó cho là:\t\t\t\t{0} lần'.format(ly_do_thu_vao.count('Ai do cho')))
    print('\tSố lần nhận lương đi làm thêm là:\t\t{0} lần'.format(ly_do_thu_vao.count('Di lam them')))
    print('\tSố lần nhận học bổng là:\t\t\t{0} lần'.format(ly_do_thu_vao.count('Hoc bong')))
    print('\tSố lần nhận tiền trợ cấp là:\t\t\t{0} lần'.format(ly_do_thu_vao.count('Tro cap')))

    print('')

    print('Thống kê lý do chi ra gồm:')
    print('\tSố lần mua đồ ăn là:\t\t\t\t{0} lần'.format(ly_do_chi_ra.count('Mua do an')))
    print('\tSố lần mua quần áo là:\t\t\t\t{0} lần'.format(ly_do_chi_ra.count('Mua quan ao')))
    print('\tSố lần mua đồ dùng học tập là:\t\t\t{0} lần'.format(ly_do_chi_ra.count('Mua do dung hoc tap')))
    print('\tSố lần mua thiết bị cá nhân là:\t\t\t{0} lần'.format(ly_do_chi_ra.count('Mua thiet bi ca nhan')))
    print('\tSố lần mua quà tặng bạn là:\t\t\t{0} lần'.format(ly_do_chi_ra.count('Mua qua tang ban')))
    print('\tSố lần mua quà tặng dì Ba hoặc dượng là:\t{0} lần'.format(ly_do_chi_ra.count('Mua qua cho di Ba hoac duong')))
    print('\tSố lần mua quà tặng ba mẹ là:\t\t\t{0} lần'.format(ly_do_chi_ra.count('Mua qua tang ba me')))
    print('\tSố lần mua đồ giùm ba mẹ là:\t\t\t{0} lần'.format(ly_do_chi_ra.count('Mua do gium ba me')))
    print('\tSố lần mua đồ giùm người khác là:\t\t{0} lần'.format(ly_do_chi_ra.count('Mua do gium nguoi khac')))
    print('\tSố lần bỏ tiền vào tiền tiết kiệm là:\t\t{0} lần'.format(ly_do_chi_ra.count('Tiet kiem')))

    return giao_dien()

print('-'*70)
print('Chương trình tính toán chi tiêu cho Duy Phạm'.center(70, '-'))
print('(Lưu ý: Bắt đầu tính từ sau tháng hiện tại)'.center(70,'-'))
giao_dien()