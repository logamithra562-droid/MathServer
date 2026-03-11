# Ex.04 Design a Website for Server Side Processing
## Date:27-02-2026

## AIM:
To create a web page to calculate total bill amount with GST from price and GST percentage using server-side scripts.

## FORMULA:
Bill = P + (P * GST / 100)
<br> P --> Price (in Rupees)
<br> GST --> GST (in Percentage)
<br> Bill --> Total Bill Amount (in Rupees)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create a HTML file to implement form based input and output.

### Step 5:
Create python programs for views and urls to perform server side processing.

### Step 6:
Receive input values from the form using request.POST.get().

### Step 7:
Calculate the total bill amount (including GST).

### Step 8:
Display the calculated result in the server console.

### Step 9:
Render the result to the HTML template.

### Step 10:
Publish the website in Localhost.

## PROGRAM:
```
views.py

from django.shortcuts import render

def calculate_Total(request):

    P = 0
    GST = 0
    Total = 0

    if request.method == "POST":
        P = float(request.POST.get('Price', 0))
        GST = float(request.POST.get('GST', 0))
        Total = P + (P * GST / 100)

        print("Price =", P)
        print("GST =", GST)
        print("Total =", Total)

    return render(request, 'mathapp/math.html', {'P': P, 'GST': GST, 'Total': Total})

    urls.py

    from django.urls import path
from mathapp import views
urlpatterns = [path('', views.calculate_Total, name='Total')]

math.html

<html>
<head>
<title>Total Bill Calculator</title>

<style>
body{
    background-color: lightblue;
    text-align: center;
    font-family: Arial;
}

.box{
    background-color: blue;
    color: white;
    width: 300px;
    margin: 100px auto;
    padding: 20px;
    border-radius: 10px;
}

h2{
    color: pink;
}
</style>

</head>

<body>

<div class="box">

<h1>TOTAL BILL AMOUNT</h1>
<h2>logamithra.k (25005891)</h2>

<form method="POST">
{% csrf_token %}

<label>Price:</label><br>
<input type="number" name="Price" step="any" required><br><br>

<label>GST (%):</label><br>
<input type="number" name="GST" step="any" required><br><br>

<button type="submit">Calculate</button>

<br><br>

<label>Total:</label><br>
<input type="text" value="{{ Total }}" readonly>

</form>

</div>

</body>
</html>

```

## OUTPUT - SERVER SIDE:
![alt text](<Screenshot 2026-03-11 200954.png>)

## OUTPUT - WEBPAGE:
![alt text](<Screenshot 2026-03-11 200927.png>)

## RESULT:
The a web page to calculate total bill amount with GST from price and GST percentage using server-side scripts is created successfully.
