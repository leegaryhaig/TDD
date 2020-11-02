import unittest, re

with open("config.text", "r") as fd:
			deviceConfig = fd.read()


class ConfigurationParser:	
	def parseCustomerNames(self):
		customerNamePattern = r'ip vrf ([a-zA-Z_]+)\n'
		customerNames = re.findall(customerNamePattern, deviceConfig)
		return customerNames

	def parseCustomerVLAN(self):
		customerVlanPattern = r'dot1Q ([0-9]+)\n'
		customerVlans = re.findall(customerVlanPattern, deviceConfig)
		return customerVlans

	def parseCustomerIP(self):
		customerIPPattern = r'GigabitEthernet0\/0\.\d*\s*([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})'
		customerIPs = re.findall(customerIPPattern, deviceConfig)
		return customerIPs

class TestParse(unittest.TestCase):
	def test_parse_cust_name(self):
		cp = ConfigurationParser()
		expected_names = ['CUSTOMER_A', 'CUSTOMER_B']
		parsed_names = cp.parseCustomerNames()
		self.assertEqual(list, type(parsed_names))
		self.assertEqual(expected_names, parsed_names)

	def test_parse_cust_vlan(self):
		cp = ConfigurationParser()
		expected_vlans = ['100', '101']
		parsed_vlans = cp.parseCustomerVLAN()
		self.assertEqual(list, type(parsed_vlans))
		self.assertEqual(expected_vlans, parsed_vlans)

	def test_parse_cust_ip(self):
		cp = ConfigurationParser()
		expected_ips = ['10.10.100.1', '10.10.101.1']
		parsed_ips = cp.parseCustomerIP()
		self.assertEqual(list, type(parsed_ips))
		self.assertEqual(expected_ips, parsed_ips)
