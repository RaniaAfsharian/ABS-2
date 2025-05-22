import pandas as pd
import matplotlib.pyplot as plt

# بارگذاری داده‌ها از فایل CSV
# فرض می‌کنیم فایل CSV با نام 'computer_industry_salaries.csv' در همان مسیر قرار دارد
df = pd.read_csv('computer_industry_salaries.csv')

# نمایش چند سطر اول داده‌ها برای اطمینان از صحت بارگذاری
print(df.head())

# تابعی برای تبدیل حقوق به عدد (در صورتی که داده‌ها به صورت رشته شامل نماد یا واحد باشند)
def convert_salary(salary):
    try:
        # اگر داده عددی باشد مستقیم بازگردانده شود
        return float(salary)
    except:
        # در نمونه داده‌های موجود معمولا عدد ساده است، ولی اگر لازم شد می‌توان این تابع را توسعه داد
        return None

# در اینجا فرض می‌کنیم ستون حقوق متوسط عددی است؛ اگر رشته است تبدیل می‌کنیم
df['حقوق متوسط'] = df['حقوق متوسط'].apply(convert_salary)

# 1- میانگین حقوق هر حرفه در هر کشور
mean_salary = df.groupby(['حرفه', 'کشور'])['حقوق متوسط'].mean().unstack()
print("\nمیانگین حقوق هر حرفه در هر کشور:\n", mean_salary)

# 2- مقایسه حقوق بین کشورها برای یک حرفه خاص (مثلا توسعه‌دهنده نرم‌افزار)
software_dev = df[df['حرفه'] == 'توسعه‌دهنده نرم‌افزار']

# رسم نمودار میله‌ای میانگین حقوق توسعه‌دهندگان نرم‌افزار در کشورها
plt.figure(figsize=(10,6))
plt.bar(software_dev['کشور'], software_dev['حقوق متوسط'], color='skyblue')
plt.title('مقایسه حقوق توسعه‌دهنده نرم‌افزار در کشورهای مختلف (2025)')
plt.xlabel('کشور')
plt.ylabel('حقوق متوسط سالانه (دلار)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('software_developer_salary_comparison.png')
plt.show()

<followUps followUp={{"followingTitle":"# 3- شناسایی بالاترین و پایین‌ترین حقوق هر حرفه","questions":["تأثیر حجم نمونه بر دقت نمودار","مقایسه با نمودارهای دیگر (جعبه\tای، پراکنش)","نمودارهای تعاملی با Plotly"]}} adsContext={{"totalFollowUpCount":1,"idx":0}} />


# 3- شناسایی بالاترین و پایین‌ترین حقوق هر حرفه


max_salary = df.groupby('حرفه')['حقوق متوسط'].max()
min_salary = df.groupby('حرفه')['حقوق متوسط'].min()

print("\nبالاترین حقوق برای هر حرفه:\n", max_salary)
print("\nپایین‌ترین حقوق برای هر حرفه:\n", min_salary)

# 4- نمودار مقایسه کلی میان حرفه‌ها در یک کشور (مثلا آمریکا)
usa_data = df[df['کشور'] == 'آمریکا']

plt.figure(figsize=(10,6))
plt.bar(usa_data['حرفه'], usa_data['حقوق متوسط'], color='lightgreen')
plt.title('مقایسه حقوق حرفه‌های صنعت کامپیوتر در آمریکا (2025)')
plt.xlabel('حرفه')
plt.ylabel('حقوق متوسط سالانه (دلار)')
plt.xticks(rotation=25)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('usa_profession_salary_comparison.png')
plt.show()