"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, example_param=1.0):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Estadistica',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32,np.float32,np.float32]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.example_param = example_param
        self.acum_anterior=0

    def work(self, input_items, output_items):
        """example: multiply with constant"""

        ##----------------------------------Creating the algorithm------------------------------

        In=input_items[0] #---------------Selecting the input wanted------------------------
        Promedio=output_items[0] #-------------Selecting the output wanted------------------------
        DesviacionStandar=output_items[1]
        Varianza=output_items[2]


        #----------------------------Process-----------------------------------

        Promedio[:]=np.mean(In)
        DesviacionStandar[:]=np.std(In)
        Varianza[:]=np.var(In)
        

        


       
        return len(In)
