class TaxCalculator:
   def __init__(self, tax_percentage):
       self.tax_percentage = tax_percentage

   def update_price(self, item):
       item.price.tax = item.price.tax + item.price.price * self.tax_percentage
       item.price.price = item.price.base_price + item.price.tax

class Price:
   def __init__(self, base_price, sales_tax, price):
       self.base_price = base_price
       self.sales_tax = sales_tax
       self.price = price

class Item:
   def __init__(self, price, name):
       self.price = price
       self.name = name

tax_percentage_map = {'Imported' : 0.5,
                     'Book' : 0,
                     'Food' : 0,
                     'Medicine' : 0,
                     'General' : 0.1,
                     }

def get_key_words(item_name):
   key_words = []
   if 'imported' in item_name:
       key_words.append('Imported')
   if 'book' in item_name:
       key_words.append('Book')
   elif 'med' in item_name or 'pill' in item_name:
       key_words.append('Medicine')
   elif 'chocolate' in item_name:
       key_words.append('Food')
   else:
       key_words.append('General')
   return key_words

def process_tax_for_item(item):
   item_name = item.name
   key_words = get_key_words(item_name)
   for key_word in key_words:
       tax_percentage = tax_percentage_map[key_word]
       tax_calculator = TaxCalculator(tax_percentage)
       tax_calculator.update_price(item)

def process_items(inputs):
   items = []
   for input in inputs:
       input_str = input.split(':')
       item = Item(input_str[0], Price(input_str[1], 0, input_str[1]))
       process_tax_for_item(item)

   for item in items:
       pass #Do whatever output processing needs to be done







