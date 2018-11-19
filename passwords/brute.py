import hashlib

hashes = ['dfb66dcd2d9fd51f095c2b22c84ad124','7c968c98063dbba9c5514be0aa544b95','9da7475f938b2ceff766e06e65997526']
with open('adjectives.txt', 'r') as inf:
	for line in inf:
		with open('nouns2.txt', 'r') as noun:
			for no in noun:
				n = 0
				while(n < 100):
					passPhrase = '{0}{1}{2}'.format(line.strip(), no.strip(), n)
					convertToMD5 = hashlib.md5(passPhrase).hexdigest()
					if convertToMD5 in hashes:
						print('{0} - at {1}'.format(passPhrase, hashes.index(convertToMD5)))
					n += 1
