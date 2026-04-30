def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

print("تبدیل دما:")
print("1. سلسیوس به فارنهایت")
print("2. فارنهایت به سلسیوس")

choice = input("لطفاً یک گزینه را انتخاب کنید (1 یا 2): ")

if choice == '1':
    celsius = float(input("لطفاً دما به درجه سلسیوس را وارد کنید: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius} درجه سلسیوس معادل {fahrenheit} درجه فارنهایت می‌باشد.")
elif choice == '2':
    fahrenheit = float(input("لطفاً دما به درجه فارنهایت را وارد کنید: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit} درجه فارنهایت معادل {celsius} درجه سلسیوس می‌باشد.")
else:
    print("گزینه انتخاب شده معتبر نیست.")
