#username - vaidman1
#id1      - 207001819
#name1    - michael vaidman
#id2      - 212830392
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
			self.left = AVLNode(-1,None,False)
			self.right = AVLNode(-1,None,False)
			self.left.parent=self
			self.right.parent=self
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


	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def set_right(self, node):
		self.right=node


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
		if num==2:
			a=self.get_left()
			num1=a.get_left().get_height()-a.get_right().get_height()
			if num1==1:
				a.get_right().set_parent(self)
				self.set_left(a.get_right())
				a.set_parent(self.parent)
				a.set_right(self)
				self.set_parent(a)
				self.set_height(self.get_height()-2)
			else:
				b = a.get_right()
				self.set_left(b.get_right())
				b.set_parent(self.get_parent())
				self.set_parent(b)
				a.set_right(b.get_left())
				a.set_parent(b)
				b.set_left(a)
				b.set_right(self)
				self.set_height(self.get_height()-2)
				a.set_height(a.get_height()-1)
				b.set_height(a.get_height()+1)
		else:
			a = self.get_right()
			num1 = a.get_left().get_height() - a.get_right().get_height()
			if num1 == -1:
				a.get_left().set_parent(self)
				self.set_right(a.get_left())
				a.set_parent(self.parent)
				a.set_left(self)
				self.set_parent(a)
				self.set_height(self.get_height() - 2)
			else:
				b = a.get_left()
				self.set_right(b.get_left())
				b.set_parent(self.get_parent())
				self.set_parent(b)
				a.set_left(b.get_right())
				a.set_parent(b)
				b.set_right(a)
				b.set_left(self)
				self.set_height(self.get_height() - 2)
				a.set_height(a.get_height() - 1)
				b.set_height(a.get_height() + 1)


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
						a.get_right.set_parent(None)
						node.set_perant(a)
						a.set_right(node)
						break
					a=a.get_right()
				else:
					a.set_size(a.get_size + 1)
					if a.get_left().is_real_node()==False:
						a.get_left().set_parent(None)
						node.set_perant(a)
						a.set_left(node)
						break
					a=a.get_left()
			a=node
			while a.get_parent() is not None:
				if a.get_parent().get_hight()>a.get_height()+1:
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
		return -1


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
		res=[]
		node_1 = node
		while node.get_parent() is not None:
			if (node.get_parent().get_key() < node.get_key()) and (node.get_left() is not None):
				node.get_parent().get_left().join(node.get_left(), node.get_key(), node.get_value())
			node = node.get_parent()
		T = AVLTree()
		T.root = node
		res.insert(0 , T)
		while node_1.get_parent() is not None :
			if (node_1.get_parent.get_key() > node_1.get_key()) and (node_1.get_right() is not None):
				node_1.get_parent.get_right().join(node_1.get_right(), node_1.get_key(), node_1.get_value())
			node_1 = node_1.get_parent()
		T_1 = AVLTree()
		T_1.root = node_1
		res.insert(1,T_1)
		return res

	
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
		node_s = self.get_root()
		node_t = tree.get_root()
		h = node_s.get_height()
		h_t = node_t.get_height()
		node_new = AVLNode(key, val)
		if h == h_t:
			if node_t.get_key() < node_s.get_key():
				self = tree.join(self, key, val)
			node_new.set_left(node_s)
			node_new.set_right(node_t)
			node_new.set_height(max(node_s.get_height(), node_t.get_height()) + 1)
			tree = None
			return 1
		if node_s.get_key() < node_t.get_key():
			if h < h_t:
				while node_t.get_left.get_height() > h:
					node_t = node_t.get_left()
				node_t.get_parent().set_left(node_new)
				node_new.set_left(node_s)
				node_new.set_right(node_t)
				node_new.set_height(h + 1)
				s = node_new.get_left().get_size() + 1
				self.root = tree.get_root()
			else:
				while node_s.get_right.get_height > h_t:
					node_s = node_s.get_right()
				node_s.get_parent().set_right(node_new)
				node_new.set_right(node_t)
				node_new.set_left(node_s)
				node_new.set_height(h_t+1)
				s = node_new.get_right().get_size() + 1
			node = node_new.get_parent()
			while node.get_parent() is not None:
				node.set_size(node.get_size() + s)
				node = node.get_parent()
			bf = node_new.get_height() - node_new.get_parent().get_right().get_height()
			if abs(bf) == 2:
				node_new.get_parent().tranform(bf)
			node_new.set_size(node_new.get_left().get_size() + 1 + node_new.get_right().get_size())
		else:
			self = tree.join(self, key, val)
		tree = None
		return abs(h-h_t)+1


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
