def calculate_bmi(weight, height):
    """
    Returns the body mass index
    """

    bmi = weight / height ** 2
    bmi = round(bmi, 1)

    if bmi <= 18.5:
        result = 'underweight.'
    elif 18.5 < bmi <= 25:
        result = 'normal weight.'
    elif 25 < bmi <= 29.9:
        result = 'overweight.'
    else:
        result = 'obesity.'

    return f'Your BMI is {bmi}, that is {result}'


if __name__ == '__main__':
    weight = float(input('Your weight in kilos: '))
    height = float(input('Your height in meters: '))
    bmi = calculate_bmi(weight, height)
    print(bmi)
