def body_mass_index(m, h):
    # tính toán chỉ số BMI của một người với cân nặng m (kg), chiều cao h (m)
    return m / (h * h)


def bmi_information(m, h):
    # đưa ra thông tin về chỉ số BMI cũng như phân loại mức độ gầy - béo của người cân nặng m, chiều cao h
    bmi = m / (h * h)
    if bmi < 18.5:
        return "gay"
    elif 18.5 <= bmi < 25:
        return "binh thuong"
    elif 25 <= bmi < 30:
        return "tien beo phi"
    elif 30 <= bmi < 35:
        return "beo phi cap do 1"
    elif 35 <= bmi < 40:
        return "beo phi cap do 2"
    else:
        return 'beo phi cap do 3'