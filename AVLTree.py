#username - vaidman1
#id1      - 207001819
#name1    - michael vaidman
#id2      - complete info
#name2    - talya cohen



"""A class represnting a node in an AVL tree"""


class AVLNode(object):

# """
	#
	# @type key: int or None
	# @param key: key of your node
	# @type value: any
	# @param value: data of your node

	# """
	def __init__(self, key, value,isR=True):
		self.parent = None
		self.isR=isR
		if isR==True:
			self.height = 0
			self.size = 1
			self.key = key
			self.value = value
			self.set_left(AVLNode(-1,None,False))
			self.right(AVLNode(-1,None,False))
		else:
			self.size = 0
			self.height=-1
			self.left = None
			self.right = None
			self.key=-1
			self.value=None




	"""
    # returns the key
    #
    # @rtype: int or None
    # @returns: the key of self, None if the node is virtual
    """
	def get_key(self):
		return self.key


	"""returns the value

	@rtype: any
	@returns: the value of self, None if the node is virtual
	"""
	def get_value(self):
		return self.value


	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child (if self is virtual)
	"""
	def get_left(self):
		return self.left


	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child (if self is virtual)
	"""
	def get_right(self):
		return self.right


	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	def get_parent(self):
		return self.parent


	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def get_height(self):
		return self.height


	"""returns the size of the subtree

	@rtype: int
	@returns: the size of the subtree of self, 0 if the node is virtual
	"""
	def get_size(self):
		return self.size


	"""sets key

	@type key: int or None
	@param key: key
	"""
	def set_key(self, key):
		self.key= key


	"""sets value

	@type value: any
	@param value: data
	"""
	def set_value(self, value):
		self.value=value


	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""
	def set_left(self, node):
		self.node=node
		node.set_perant(self)


	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def set_right(self, node):
		self.right=node
		node.set_perant(self)


	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	def set_parent(self, node):
		self.parent=node


	"""sets the height of the node

	@type h: int
	@param h: the height
	"""
	def set_height(self, h):
		self.height=h


	"""sets the size of node

	@type s: int
	@param s: the size
	"""
	def set_size(self, s):
		self.size=s


	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def is_real_node(self):
		return self.isR


	def transform(self,num):
		parent=self.get_parent()
		pr=-1
		if parent.get_key<self.get_key():
			pr=1
		if num==2:
			a=self.get_left()
			num1=a.get_left().get_height()-a.get_right().get_height()
			if num1>=0:
				self.set_left(a.get_right())
				if pr==1:
					parent.set_right(a)
				else:
					parent.set_left(a)
				a.set_right(self)
				self.set_height(self.get_height()-1-num1)
				self.set_size(self.get_size()-a.get_size()+self.get_left().get_size())
				a.set_size(a.get_size()+self.get_size())
				return a
			else:
				b = a.get_right()
				if pr==1:
					parent.set_right(b)
				else:
					parent.set_left(b)
				self.set_left(b.get_right())
				a.set_right(b.get_left())
				b.set_left(a)
				b.set_right(self)
				self.set_height(self.get_height()-2)
				a.set_height(a.get_height()-1)
				b.set_height(a.get_height()+1)
				self.set_size(self.get_size() - a.get_size())
				a.set_size(a.get_size() - b.get_size())
				b.get_size(b.get_size()+a.get_size()+self.get_size())
				return b
		else:
			a = self.get_right()
			num1 = a.get_left().get_height() - a.get_right().get_height()
			if num1 <= 0:
				self.set_right(a.get_left())
				if pr == 1:
					parent.set_right(a)
				else:
					parent.set_left(a)
				a.set_left(self)
				self.set_height(self.get_height() - 1+num1)
				self.set_size(self.get_size() - a.get_size()+self.get_right().get_size())
				a.set_size(a.get_size() + self.get_size())
				return a
			else:
				b = a.get_left()
				if pr == 1:
					parent.set_right(b)
				else:
					parent.set_left(b)
				self.set_right(b.get_left())
				a.set_left(b.get_right())
				b.set_right(a)
				b.set_left(self)
				self.set_height(self.get_height() - 2)
				a.set_height(a.get_height() - 1)
				b.set_height(a.get_height() + 1)
				self.set_size(self.get_size() - a.get_size())
				a.set_size(a.get_size() - b.get_size())
				b.get_size(b.get_size() + a.get_size() + self.get_size())
				return b

"""
A class implementing an AVL tree.
"""

class AVLTree(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):
		self.root = None
		# add your fields here



	"""searches for a value in the dictionary corresponding to the key

	@type key: int
	@param key: a key to be searched
	@rtype: any
	@returns: the value corresponding to key.
	"""
	def search(self, key):
		a=self.get_root()
		while a.get_key()!=key:
			if a.is_real_node()==False:
				return None
			if a.get_key()<key:
				a=a.get_right()
			else:
				a=a.get_left()
		return a

	"""inserts val at position i in the dictionary

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: any
	@param val: the value of the item
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def insert(self, key, val):
		node =AVLNode(key,val)
		if self.get_root() ==None:
			self.root=node
		else:
			a=self.get_root()
			while True:
				if a.get_key()<key:
					a.set_size(a.get_size+1)
					if a.get_right().is_real_node()==False:
						a.set_right(node)
						break
					a=a.get_right()
				else:
					a.set_size(a.get_size + 1)
					if a.get_left().is_real_node()==False:
						a.set_left(node)
						break
					a=a.get_left()
			a=node
			while a.get_parent() is not None:
				if a.get_parent().get_hight()>=a.get_height()+1:
					break
				a=a.get_parent()
				a.set_height(a.get_height()+1)
				r=a.get_right().get_height()
				l=a.get_left().get_height()
				if abs(r-l)>1:
					a.transform(l-r) # to make an AVL
					break



	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, node):
		a=node.get_parent()
		parent=node.get_parent()
		while parent is not None:
			parent.set_size(parent.get_size()-1)
			parent=parent.get_parent()
		pr=-1
		if a.get_key()<node.get_key():
			pr=1
		c=None
		bL=node.get_left()
		bR=node.get_right()
		num =bL.get_height()-bR.get_height()
		parent=node.get_parent()
		if num>0:
			c=bL
			if c.get_right().is_real_node():
				while c.get_right().is_real_node():
					c.set_size(c.get_size()-1)
					c=c.get_right()
				parent = c.get_parent()
				parent.set_right(c.get_left)
				c.set_left(bL)
			c.set_right(bR)
		else:
			c=bR
			if c.get_left().is_real_node():
				while c.get_left().is_real_node():
					c.set_size(c.get_size() - 1)
					c=c.get_left()
				parent = c.get_parent()
				parent.set_left(c.get_left)
				c.set_right(bL)
			c.set_left(bR)
		if pr == 1:
			a.set_right(c)
		else:
			a.set_left(c)
		while parent is not None:
			L=parent.set_left().get_height()
			R=parent.set_right().get_height()
			if R>L:
				parent.set_height(R+1)
			else:
				parent.set_height(L + 1)

			if abs(R-L)==2:
				parent=parent.transform(L-R)
				continue
			h=parent.set_height()
			if R+1==h or L+1==h:
				break
			parent=parent.get_parent()


	"""returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""
	def avl_to_array(self):
		def avll(self, node):
			lst = []
			if node.is_real_node()==False:
				return []
			lst+=avll(node.get_left())
			lst+=[(node.get_key(), node.get_value())]
			lst += avll(node.get_right())
			return lst
		return avll(self.get_root())






	"""returns the number of items in dictionary 

	@rtype: int
	@returns: the number of items in dictionary 
	"""
	def size(self):
		return self.get_root().get_size()	

	
	"""splits the dictionary at a given node

	@type node: AVLNode
	@pre: node is in self
	@param node: The intended node in the dictionary according to whom we split
	@rtype: list
	@returns: a list [left, right], where left is an AVLTree representing the keys in the 
	dictionary smaller than node.key, right is an AVLTree representing the keys in the 
	dictionary larger than node.key.
	"""
	def split(self, node):
		lst=[]
		a=AVLTree()
		b=AVLTree()
		c=self.get_root()
		d=node.get_right()
		if c.get_key()<node.get_key():
			a.root =c
		else:
			b.root =c
		while True:
			if node.get_parent().get_key()<node.get_key():


	
	"""joins self with key and another AVLTree

	@type tree: AVLTree 
	@param tree: a dictionary to be joined with self
	@type key: int 
	@param key: The key separting self with tree
	@type val: any 
	@param val: The value attached to key
	@pre: all keys in self are smaller than key and all keys in tree are larger than key,
	or the other way around.
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
	def join(self, tree, key, val):
		return None


	"""compute the rank of node in the self

	@type node: AVLNode
	@pre: node is in self
	@param node: a node in the dictionary which we want to compute its rank
	@rtype: int
	@returns: the rank of node in self
	"""
	def rank(self, node):
		rank=0
		a=self.get_root()
		while a.get_key()!=node.get_key():
			if a.get_key()<node.get_key():
				rank+=a.get_left().get_size()+1
				a=a.get_right()
			else:
				a=a.get_left()
		rank+=node.get_left().get_size()+1
		return rank


	"""finds the i'th smallest item (according to keys) in self

	@type i: int
	@pre: 1 <= i <= self.size()
	@param i: the rank to be selected in self
	@rtype: int
	@returns: the item of rank i in self
	"""
	def select(self, i):
		a=self.get_root()
		while True:
			if a.get_left().is_real_node():
				size=a.get_left().get_size()
			else:
				size=0
			if size<i:
				if size+1==i:
					return a
				a=a.get_right()
				i-=size+1
			else:
				a=a.get_left()




	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	def get_root(self):
		return self.root()
