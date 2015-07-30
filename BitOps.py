



def testBit(int_type, i):
# returns whether the bit at 'i' is 0 or 1
	return (int_type>>i)&1

def sumBits(int_type,max_bit):
# sums all the bits of 'int_type' up to bit numeber 'max_bit'
	return sum(map(lambda x:(int_type>>x)&1, [ i for i in xrange(max_bit)]))

def sumStagBits(int_type,max_bit,Stag):
# does the same as sum bits, but one can put a staggered mask over the sum for things like staggaret magnetization
	return sum(map(lambda x:((int_type>>x)&1)*Stag[x], [ i for i in xrange(max_bit)]))

def exchangeBits(int_type,i,j):
# takes the bits i and j of 'int_type' and swaps their values, if the bits are both 0 or 1, it returns the same integer, else it returns the
# new integer after the flip.
	ibit=(int_type>>i)&1
	jbit=(int_type>>j)&1
	if ibit==jbit:
		return int_type
	else:
		return int_type^((1<<i)+(1<<j)) 


def flipBit(int_type,i):
# flips a single bit from 0->1 or vice versa at bit 'i'
	return int_type^(1<<i)
