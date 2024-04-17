"""
define moduals of model
"""
from torch.autograd import Variable
import torch.nn.functional as F
import torch.nn as nn


class CNNModel(nn.Module):
	"""docstring for ClassName"""
	
	def __init__(self, args):
		super(CNNModel, self).__init__()
		##-----------------------------------------------------------
		## define the model architecture here
		## MNIST image input size batch * 28 * 28 (one input channel)
		##-----------------------------------------------------------
		
		## define CNN layers below
		self.conv = nn.sequential( 	# nn.Conv2d(in_channels,...),
									# activation fun,
									# batch normalization (bonus),
									# dropout,
									# nn.Conv2d(in_channels,...),
									# batch normalization (bonus),
									# activation fun,
									# dropout,
									## continue like above,
									## **define pooling (bonus)**,
									
								)

		##-------------------------------------------------
		## write code to define fully connected layers below
		##-------------------------------------------------
		in_size = 
		out_size = 
		# self.fc = nn.Linear(in_size, out_size)

		self.fc = nn.sequential( # nn.Linear(in_size, out_1),
								 # activation fun,
								 # nn.Linear(out_1, out_size),
								)
		

	'''feed features to the model'''
	def forward(self, x):  #default
		
		##---------------------------------------------------------
		## write code to feed input features to the CNN models defined above
		##---------------------------------------------------------
		x_out = 

		## write flatten tensor code below (it is done)
		x = torch.flatten(x_out,1) # x_out is output of last layer
		

		## ---------------------------------------------------
		## write fully connected layer (Linear layer) below
		## ---------------------------------------------------
		result =   # predict y
		
		
		return result
        
		
		
	
		