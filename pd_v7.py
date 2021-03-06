# 1. Izveidot funkciju, kas printēs konsolē šādu struktūru, funkcijas arguments ir piramīdas augstums:
height = int(input("Height: "))
for i in range(0,height):
  for y in range(0,height):
    if y+i < height-1:
      print(" ", end = '')
    else:
      print("* ", end = '')
  print("\n")


# 2. Izveidot funkciju, kuras arguments ir saraksts ar mājaslapu adresēm. Funkcija atgriež sarakstu ar top-level domain (.com, .net, .lv).
addreses = ['https://www.delfi.lv','https://www.google.co.uk','https://www.wikipedia.org']
domains = []
for i in addreses : 
  domains.append(i.split('.')[-1])
print(f"Addresses: {addreses}")
print(f"Top-level domains: {domains}")


# 3. Izveidot funkciju, kuras arguments ir mājaslapas adrese. Funkcija atgriež status code.
import requests
url = str(input("Enter address: "))
req = requests.head(url)
print(req.status_code)


# 4. Izveidot dekoratoru, kas skaita cik reizes funkcija tika izsaukta.
def call_counter(function):
  def inner():
    inner.calls += 1
    print(f"Function {function.__name__} has been called {inner.calls} times")
    return function()
  inner.calls = 0
  return inner

@call_counter
def print_ok():
  print("Ok")

@call_counter
def print_hi():
  print("Hi")

print_ok()
print_ok()
print_hi()
print_ok()


# 5. Izveidot klasi Phone. Klasei ir klases atribūti brand un os. Ir instances atribūts number, kura vērtība ir nejauši ģenerēts 11 ciparu skaitlis. Uz Phone klases pamata izveidot klasi Samsung un Apple.
import random

class Phone:
  def __init__(self, brand, os):
    self.brand = brand
    self.os = os
    self.number = ''.join([str(random.randint(0, 10)) for i in range(11)])

class Samsung(Phone):
  pass

class Apple(Phone):
  pass

ph1 = Samsung("Galaxy","Android")
print(f"Phone {ph1.brand}, {ph1.os}, {ph1.number}")

ph1 = Apple("iPhone","iOS")
print(f"Phone {ph1.brand}, {ph1.os}, {ph1.number}")
