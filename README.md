SDK (plugin) for spay

مستند پیاده سازی درگاه پرداخت پرداختیاری سبا پردازش (سباپی)

پلاگین پرداخت یاری سبا پی با زبان برنامه نویسی پایتون  به نام "spay"جهت  مدیریت درخواست های پرداخت آنلاین طراحی گردیده است. این مستند نحوه نصب و نحوه استفاده از پلاگین را توضیح می دهد.
•	نصب
برای نصب پلاگین، دستور زیر را اجرا فرمایید:

![p-p2](https://github.com/user-attachments/assets/6000d3f0-5399-4443-9d5f-926c20111e7c)


این دستور پلاگین و تمامی  requirements مورد نیاز را به صورت خودکار نصب می کند.

برای استفاده از پلاگین، اطلاعاتی نظیر شناسه پذیرنده (merchant_id) ، آدرس بازگشت (Callback_url) و مبلغ (Amount) مورد نیاز است.  فیلدهای Description، Email و Mobile اختیاری هستند.
مثال کد برای ایجاد تراکنش: 

![p-p4](https://github.com/user-attachments/assets/dd6eeab3-a03b-4312-8729-601ea1a2288a)

توضیحات متدها:
 (get_token): توکن پرداخت را دریافت می کند.
 (request_payment): درخواست پرداخت را با توکن ارسال می کند.
 (verify_payment): وضعیت پرداخت را بررسی می کند.


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Implementation Document for the Sabapay Payment Gateway (Saba Pay)

The "spay" payment plugin, developed in Python, is designed for managing online payment requests. This document explains how to install and use the plugin.

• Installation
To install the plugin, please execute the following command:

![p-p2](https://github.com/user-attachments/assets/6000d3f0-5399-4443-9d5f-926c20111e7c)

This command will automatically install the plugin along with all required dependencies.

To use the plugin, information such as the merchant ID (merchant_id), callback URL (Callback_url), and amount (Amount) is required. The fields for Description, Email, and Mobile are optional.
Code Example for Creating a Transaction:

![p-p4](https://github.com/user-attachments/assets/09c0686b-2896-48de-8773-1efc6adcb6a2)


Method Descriptions:

    get_token: Retrieves the payment token.
    request_payment: Sends a payment request with the token.
    verify_payment: Checks the status of the payment.
