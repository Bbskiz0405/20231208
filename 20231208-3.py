def isLeapYear(year):
    # 閏年是指年份可以被 4 整除但不能被 100 整除，或可以被 400 整除
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# 計算西元 2000 年到 2050 年之間閏年的數量
leap_years = [year for year in range(2000, 2051) if isLeapYear(year)]
print("2000 至 2050 年之間的閏年數量:", len(leap_years))

