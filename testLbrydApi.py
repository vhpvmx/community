from pybry import LbryApi

# Initialize the API
lbry = LbryApi()

# Just call the method as documented in the LBRYD API
response = lbry.claim_list(name="vhpvmx")
#response = lbry.claim_list(name="bellflower")

print(response)
