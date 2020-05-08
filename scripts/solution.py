from __future__ import print_function
import aerospike
import logging

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
logging.info('Testig local Aerospike connectivity')

# Configure the client
config = {
  'hosts': [ ('db', 3000) ]
}

# Create a client and connect it to the cluster
try:
  client = aerospike.client(config).connect()
except:
  import sys
  logging.error("failed to connect to the cluster with", config['hosts'])
  sys.exit(1)


#реализуйте три функции (add_customer, get_ltv_by_id, get_ltv_by_phone) в файле scripts/solution.py
customers_store = {}

def add_customer(customer_id, customer_phone, lifetime_value):
  customers_store[customer_id] = {'customer_phone': customer_phone, 'lifetime': lifetime_value }

def get_ltv_by_id(customer_id):
  ltv_element = customers_store.get(customer_id, {})
  try:
    return ltv_element.get('lifetime')
  except:
    logging.error('Requested non-existent customer ' + str(customer_id))
  

def get_ltv_by_phone(customer_phone):
  for pk in customers_store.values():
    try:
      if (pk['customer_phone'] == customer_phone):
        return pk['lifetime']
    except:
      logging.error('Requested phone number is not found ' + str(customer_phone))

try:
  add_customer(1, 241141, 10)
  logging.info('Customer was added')
except:
  logging.error('There is a problem with customer creations') 

try:
  get_ltv_by_id(1)
  logging.info('ltv was got by id: ')
  print(get_ltv_by_id(1))

except:
  logging.error('There is a problem with get by id func') 


try:
  get_ltv_by_phone(1)
  logging.info('ltv was got by phone num: ')
  print(get_ltv_by_phone(241141))

except:
  logging.error('There is a problem with get by id func') 