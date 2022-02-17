# The MIT License (MIT)
# Copyright © 2021 Yuma Rao

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
# documentation files (the “Software”), to deal in the Software without restriction, including without limitation 
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, 
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of 
# the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION 
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
# DEALINGS IN THE SOFTWARE.

from .text import template_miner,template_server,advanced_server,core_validator,sgmoe_validator, multitron_server

__all_neurons__ =  { 'text_template_miner': template_miner.neuron, 
                     'text_core_validator': core_validator.neuron,
                     'text_template_server':template_server.neuron,
                     'text_advanced_server':advanced_server.neuron,
                     'sgmoe_validator':sgmoe_validator.neuron,
                     'multitron_server': multitron_server}
__text_neurons__ =  { 'template_miner': template_miner.neuron, 
                     'template_validator': core_validator.neuron,
                     'template_server':template_server.neuron,
                     'advanced_server':advanced_server.neuron,
                     'sgmoe_validator':sgmoe_validator.neuron,
                     'multitron_server': multitron_server}