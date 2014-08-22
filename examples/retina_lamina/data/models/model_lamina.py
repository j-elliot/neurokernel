# use of 0.0 instead of 0 where float is expected

NEURON_LIST = [
    {'name':'R1', 'model':'port_in_gpot', 'columnar':True, 'output':False,
     'extern':False, 'input':True, 'spiking':False},
    {'name':'R2', 'model':'port_in_gpot', 'columnar':True, 'output':False,
     'extern':False, 'input':True, 'spiking':False},
    {'name':'R3', 'model':'port_in_gpot', 'columnar':True, 'output':False,
     'extern':False, 'input':True, 'spiking':False},
    {'name':'R4', 'model':'port_in_gpot', 'columnar':True, 'output':False,
     'extern':False, 'input':True, 'spiking':False},
    {'name':'R5', 'model':'port_in_gpot', 'columnar':True, 'output':False,
     'extern':False, 'input':True, 'spiking':False},
    {'name':'R6', 'model':'port_in_gpot', 'columnar':True, 'output':False,
     'extern':False, 'input':True, 'spiking':False},
    #
    {'name':'C2', 'model':'port_in_gpot', 'columnar':True, 'output':False,
     'extern':False, 'input':True, 'spiking':False},
    {'name':'C3', 'model':'port_in_gpot', 'columnar':True, 'output':False,
     'extern':False, 'input':True, 'spiking':False},
    {'name':'Mi1', 'model':'port_in_gpot', 'columnar':True, 'output':False,
     'extern':False, 'input':True, 'spiking':False},
    {'name':'Tm1', 'model':'port_in_gpot', 'columnar':True, 'output':False,
     'extern':False, 'input':True, 'spiking':False},
    {'name':'Tm2', 'model':'port_in_gpot', 'columnar':True, 'output':False,
     'extern':False, 'input':True, 'spiking':False},

    #
    {'name':'L1', 'model':'MorrisLecar', 'columnar':True,
     'output':True, 'extern':False, 'public':True, 'spiking':False,
     'V1': -0.001, 'V2':0.015, 'V3': -0.05, 'V4': 0.001, 'phi':0.0025, 
     'initV':-0.05, 'initn':0.5, 'offset':0.02},
    {'name':'L2', 'model':'MorrisLecar', 'columnar':True,
     'output':True, 'extern':False, 'public':True, 'spiking':False,
     'V1': -0.001, 'V2':0.015, 'V3': -0.05, 'V4': 0.001, 'phi':0.0025, 
     'initV':-0.05, 'initn':0.5, 'offset':0.02},
    {'name':'L3', 'model':'MorrisLecar', 'columnar':True,
     'output':True, 'extern':False, 'public':True, 'spiking':False,
     'V1': -0.001, 'V2':0.015, 'V3': -0.05, 'V4': 0.001, 'phi':0.0025, 
     'initV':-0.05, 'initn':0.5, 'offset':0.02},
    {'name':'L4', 'model':'MorrisLecar', 'columnar':True,
     'output':True, 'extern':False, 'public':True, 'spiking':False,
     'V1': -0.001, 'V2':0.015, 'V3': -0.05, 'V4': 0.001, 'phi':0.0025, 
     'initV':-0.05, 'initn':0.5, 'offset':0.02},
    {'name':'L5', 'model':'MorrisLecar', 'columnar':True,
     'output':True, 'extern':False, 'public':True, 'spiking':False,
     'V1': -0.001, 'V2':0.015, 'V3': -0.05, 'V4': 0.001, 'phi':0.0025, 
     'initV':-0.05, 'initn':0.5, 'offset':0.02},
    {'name':'T1', 'model':'MorrisLecar', 'columnar':True,
     'output':True, 'extern':False, 'public':True, 'spiking':False,
     'V1': -0.001, 'V2':0.015, 'V3': -0.05, 'V4': 0.001, 'phi':0.0025, 
     'initV':-0.05, 'initn':0.5, 'offset':0.02},
#    {'name':'C2', 'model':'MorrisLecar', 'columnar':True,
#     'output':True, 'extern':False, 'public':True, 'spiking':False,
#     'V1': -0.001, 'V2':0.015, 'V3': -0.05, 'V4': 0.001, 'phi':0.0025, 
#     'initV':-0.05, 'initn':0.5, 'offset':0.02},
#    {'name':'C3', 'model':'MorrisLecar', 'columnar':True,
#     'output':True, 'extern':False, 'public':True, 'spiking':False,
#     'V1': -0.001, 'V2':0.015, 'V3': -0.05, 'V4': 0.001, 'phi':0.0025, 
#     'initV':-0.05, 'initn':0.5, 'offset':0.02},
    {'name':'Am', 'model':'MorrisLecar', 'columnar':False,
     'num':350, 'output':False, 'extern':False, 'public':False, 'spiking':False,
     'V1': -0.001, 'V2':0.015, 'V3': 0.0, 'V4': 0.03, 'phi':0.2,
     'initV':-0.05184, 'initn':0.0306, 'offset':0}
]

# use of 0.0 instead of 0 where float is expected
SYNAPSE_LIST = [
    { 'prename':'R1', 'postname':'L1', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':-0.08, 'delay':1, 'threshold':-0.05214,
      'slope':0.02, 'power':1, 'saturation':0.0008, 'scale':40,
      'mode':0 },
    { 'prename':'R1', 'postname':'L2', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':-0.08, 'delay':1, 'threshold':-0.05214,
      'slope':0.02, 'power':1, 'saturation':0.0008, 'scale':40,
      'mode':0 },
    #
    { 'prename':'L2', 'postname':'L4', 'model':'power_gpot_gpot',
      'cart':6, 'reverse':0.0, 'delay':1, 'threshold':-0.0505,
      'slope':2, 'power':1, 'saturation':0.03, 'scale':4,
      'mode':0 },
    { 'prename':'L2', 'postname':'L4', 'model':'power_gpot_gpot',
      'cart':5, 'reverse':0.0, 'delay':1, 'threshold':-0.0505,
      'slope':2, 'power':1, 'saturation':0.03, 'scale':2,
      'mode':0 },
    # L4-*
    { 'prename':'L4', 'postname':'R1', 'model':'power_gpot_gpot',
      'cart':3, 'reverse':0.0, 'delay':1, 'threshold':-0.0505,
      'slope':2, 'power':1, 'saturation':0.1, 'scale':1,
      'mode':1 },
    { 'prename':'L4', 'postname':'L4', 'model':'power_gpot_gpot',
      'cart':4, 'reverse':0.0, 'delay':1, 'threshold':-0.0505,
      'slope':2, 'power':1, 'saturation':0.05, 'scale':2,
      'mode':0 },
    { 'prename':'L4', 'postname':'L5', 'model':'power_gpot_gpot',
      'cart':6, 'reverse':0.0, 'delay':1, 'threshold':-0.0505,
      'slope':0.5, 'power':1, 'saturation':0.1, 'scale':1,
      'mode':0 },
    # Rx-L1
    { 'prename':'R2', 'postname':'L1', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':-0.08, 'delay':1, 'threshold':-0.05214,
      'slope':0.02, 'power':1, 'saturation':0.0008, 'scale':43,
      'mode':0 },
    { 'prename':'R3', 'postname':'L1', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':-0.08, 'delay':1, 'threshold':-0.05214,
      'slope':0.02, 'power':1, 'saturation':0.0008, 'scale':37,
      'mode':0 },
    { 'prename':'R4', 'postname':'L1', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':-0.08, 'delay':1, 'threshold':-0.05214,
      'slope':0.02, 'power':1, 'saturation':0.0008, 'scale':38,
      'mode':0 },
    { 'prename':'R5', 'postname':'L1', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':-0.08, 'delay':1, 'threshold':-0.05214,
      'slope':0.02, 'power':1, 'saturation':0.0008, 'scale':38,
      'mode':0 },
    { 'prename':'R6', 'postname':'L1', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':-0.08, 'delay':1, 'threshold':-0.05214,
      'slope':0.02, 'power':1, 'saturation':0.0008, 'scale':45,
      'mode':0 },
    # Rx-L2
    { 'prename':'R2', 'postname':'L2', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':-0.08, 'delay':1, 'threshold':-0.05214,
      'slope':0.02, 'power':1, 'saturation':0.0008, 'scale':43,
      'mode':0 },
    { 'prename':'R3', 'postname':'L2', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':-0.08, 'delay':1, 'threshold':-0.05214,
      'slope':0.02, 'power':1, 'saturation':0.0008, 'scale':37,
      'mode':0 },
    { 'prename':'R4', 'postname':'L2', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':-0.08, 'delay':1, 'threshold':-0.05214,
      'slope':0.02, 'power':1, 'saturation':0.0008, 'scale':38,
      'mode':0 },
    { 'prename':'R5', 'postname':'L2', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':-0.08, 'delay':1, 'threshold':-0.05214,
      'slope':0.02, 'power':1, 'saturation':0.0008, 'scale':38,
      'mode':0 },
    { 'prename':'R6', 'postname':'L2', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':-0.08, 'delay':1, 'threshold':-0.05214,
      'slope':0.02, 'power':1, 'saturation':0.0008, 'scale':45,
      'mode':0 },
    # Rx-L3
    { 'prename':'R1', 'postname':'L3', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':-0.08, 'delay':1, 'threshold':-0.05214,
      'slope':0.02, 'power':1, 'saturation':0.0008, 'scale':11,
      'mode':0 },
    { 'prename':'R2', 'postname':'L3', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':-0.08, 'delay':1, 'threshold':-0.05214,
      'slope':0.02, 'power':1, 'saturation':0.0008, 'scale':10,
      'mode':0 },
    { 'prename':'R3', 'postname':'L3', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':-0.08, 'delay':1, 'threshold':-0.05214,
      'slope':0.02, 'power':1, 'saturation':0.0008, 'scale':4,
      'mode':0 },
    { 'prename':'R4', 'postname':'L3', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':-0.08, 'delay':1, 'threshold':-0.05214,
      'slope':0.02, 'power':1, 'saturation':0.0008, 'scale':8,
      'mode':0 },
    { 'prename':'R5', 'postname':'L3', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':-0.08, 'delay':1, 'threshold':-0.05214,
      'slope':0.02, 'power':1, 'saturation':0.0008, 'scale':6,
      'mode':0 },
    { 'prename':'R6', 'postname':'L3', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':-0.08, 'delay':1, 'threshold':-0.05214,
      'slope':0.02, 'power':1, 'saturation':0.0008, 'scale':12,
      'mode':0 },
    # Rx-ax
    { 'prename':'R1', 'postname':'a1', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.05214,
      'slope':0.01, 'power':1, 'saturation':0.002, 'scale':19,
      'mode':0 },
    { 'prename':'R2', 'postname':'a1', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.05214,
      'slope':0.01, 'power':1, 'saturation':0.002, 'scale':16,
      'mode':0 },
    { 'prename':'R2', 'postname':'a2', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.05214,
      'slope':0.01, 'power':1, 'saturation':0.002, 'scale':22,
      'mode':0 },
    { 'prename':'R3', 'postname':'a2', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':0.0, 'delay':1, 'threshold': -0.05214,
      'slope':0.01, 'power':1, 'saturation':0.002, 'scale':18,
      'mode':0 },
    { 'prename':'R3', 'postname':'a3', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.05214,
      'slope':0.01, 'power':1, 'saturation':0.002, 'scale':20,
      'mode':0 },
    { 'prename':'R4', 'postname':'a3', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.05214,
      'slope':0.01, 'power':1, 'saturation':0.002, 'scale':16,
      'mode':0 },
    { 'prename':'R4', 'postname':'a4', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.05214,
      'slope':0.01, 'power':1, 'saturation':0.002, 'scale':17,
      'mode':0 },
    { 'prename':'R5', 'postname':'a4', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.05214,
      'slope':0.01, 'power':1, 'saturation':0.002, 'scale':26,
      'mode':0 },
    { 'prename':'R5', 'postname':'a5', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.05214,
      'slope':0.01, 'power':1, 'saturation':0.002, 'scale':10,
      'mode':0 },
    { 'prename':'R6', 'postname':'a5', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.05214,
      'slope':0.01, 'power':1, 'saturation':0.002, 'scale':14,
      'mode':0 },
    { 'prename':'R6', 'postname':'a6', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.05214,
      'slope':0.01, 'power':1, 'saturation':0.002, 'scale':22,
      'mode':0 },
    { 'prename':'R1', 'postname':'a6', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.05214,
      'slope':0.01, 'power':1, 'saturation':0.002, 'scale':17,
      'mode':0 },
    # Rx-T1
    { 'prename':'R2', 'postname':'T1', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':-0.07, 'delay':1, 'threshold':-0.05214,
      'slope':0.01, 'power':1, 'saturation':0.002, 'scale':2,
      'mode':0 },
    { 'prename':'R3', 'postname':'T1', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':-0.07, 'delay':1, 'threshold':-0.05214,
      'slope':0.01, 'power':1, 'saturation':0.002, 'scale':2,
      'mode':0 },
    { 'prename':'R4', 'postname':'T1', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':-0.07, 'delay':1, 'threshold':-0.05214,
      'slope':0.01, 'power':1, 'saturation':0.002, 'scale':2,
      'mode':0 },
    # ax-L3
    { 'prename':'a1', 'postname':'L3', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.05284,
      'slope':0.5, 'power':1, 'saturation':0.01, 'scale':1,
      'mode':0 },
    { 'prename':'a2', 'postname':'L3', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.05284,
      'slope':0.5, 'power':1, 'saturation':0.01, 'scale':1,
      'mode':0 },
    { 'prename':'a3', 'postname':'L3', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.05284,
      'slope':0.5, 'power':1, 'saturation':0.01, 'scale':1,
      'mode':0 },
    { 'prename':'a4', 'postname':'L3', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.05284,
      'slope':0.5, 'power':1, 'saturation':0.01, 'scale':3,
      'mode':0 },
    { 'prename':'a5', 'postname':'L3', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.05284,
      'slope':0.5, 'power':1, 'saturation':0.01, 'scale':5,
      'mode':0 },
    { 'prename':'a6', 'postname':'L3', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.05284,
      'slope':0.5, 'power':1, 'saturation':0.01, 'scale':1,
      'mode':0 },
    # ax-T1
    { 'prename':'a1', 'postname':'T1', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.05284,
      'slope':0.5, 'power':1, 'saturation':0.06, 'scale':8,
      'mode':0 },
    { 'prename':'a2', 'postname':'T1', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.05284,
      'slope':0.5, 'power':1, 'saturation':0.06, 'scale':6,
      'mode':0 },
    { 'prename':'a3', 'postname':'T1', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.05284,
      'slope':0.5, 'power':1, 'saturation':0.06, 'scale':7,
      'mode':0 },
    { 'prename':'a4', 'postname':'T1', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.05284,
      'slope':0.5, 'power':1, 'saturation':0.06, 'scale':12,
      'mode':0 },
    { 'prename':'a5', 'postname':'T1', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.05284,
      'slope':0.5, 'power':1, 'saturation':0.06, 'scale':3,
      'mode':0 },
    { 'prename':'a6', 'postname':'T1', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.05284,
      'slope':0.5, 'power':1, 'saturation':0.06, 'scale':13,
      'mode':0 },
    #
    { 'prename':'L2', 'postname':'L4', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.0505,
      'slope':2, 'power':1, 'saturation':0.03, 'scale':4,
      'mode':0 },
    { 'prename':'L2', 'postname':'L5', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.0505,
      'slope':2, 'power':1, 'saturation':0.01, 'scale':1,
      'mode':0 },
#    { 'prename':'L2', 'postname':'R1', 'model':'power_gpot_gpot',
#      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.0505,
#      'slope':1, 'power':1, 'saturation':0.02, 'scale':1,
#      'mode':1 },
#    { 'prename':'L2', 'postname':'R2', 'model':'power_gpot_gpot',
#      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.0505,
#      'slope':1, 'power':1, 'saturation':0.02, 'scale':1,
#      'mode':1 },
    { 'prename':'L2', 'postname':'L1', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.0505,
      'slope':1, 'power':1, 'saturation':0.02, 'scale':3,
      'mode':0 },
    #
#    { 'prename':'L4', 'postname':'R5', 'model':'power_gpot_gpot',
#      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.0505,
#      'slope':0.5, 'power':1, 'saturation':0.1, 'scale':1,
#      'mode':1 },
    { 'prename':'L4', 'postname':'L2', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.0505,
      'slope':0.5, 'power':1, 'saturation':0.1, 'scale':2,
      'mode':0 },
    # [Cx]-[Lx,ax]
    { 'prename':'C2', 'postname':'L1', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':-0.07, 'delay':1, 'threshold':-0.05,
      'slope':1, 'power':1, 'saturation':0.02, 'scale':44,
      'mode':0 },
    { 'prename':'C2', 'postname':'L2', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':-0.07, 'delay':1, 'threshold':-0.05,
      'slope':1, 'power':1, 'saturation':0.02, 'scale':29,
      'mode':0 },
    { 'prename':'C2', 'postname':'L3', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':-0.07, 'delay':1, 'threshold':-0.05,
      'slope':1, 'power':1, 'saturation':0.02, 'scale':15,
      'mode':0 },
    { 'prename':'C2', 'postname':'L5', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':-0.07, 'delay':1, 'threshold':-0.05,
      'slope':1, 'power':1, 'saturation':0.02, 'scale':36,
      'mode':0 },
    { 'prename':'C2', 'postname':'a1', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':-0.07, 'delay':1, 'threshold':-0.05,
      'slope':1, 'power':1, 'saturation':0.02, 'scale':1,
      'mode':0 },
    { 'prename':'C2', 'postname':'a3', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':-0.07, 'delay':1, 'threshold':-0.05,
      'slope':1, 'power':1, 'saturation':0.02, 'scale':2,
      'mode':0 },
    { 'prename':'C2', 'postname':'a5', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':-0.07, 'delay':1, 'threshold':-0.05,
      'slope':1, 'power':1, 'saturation':0.02, 'scale':2,
      'mode':0 },
    { 'prename':'C2', 'postname':'a6', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':-0.07, 'delay':1, 'threshold':-0.05,
      'slope':1, 'power':1, 'saturation':0.02, 'scale':1,
      'mode':0 },
    { 'prename':'C3', 'postname':'L1', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':-0.07, 'delay':1, 'threshold':-0.05,
      'slope':1, 'power':1, 'saturation':0.02, 'scale':3,
      'mode':0 },
    { 'prename':'C3', 'postname':'L2', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':-0.07, 'delay':1, 'threshold':-0.05,
      'slope':1, 'power':1, 'saturation':0.02, 'scale':42,
      'mode':0 },
    { 'prename':'C3', 'postname':'L5', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':-0.07, 'delay':1, 'threshold':-0.05,
      'slope':1, 'power':1, 'saturation':0.02, 'scale':9,
      'mode':0 },
    { 'prename':'C3', 'postname':'a1', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':-0.07, 'delay':1, 'threshold':-0.05,
      'slope':1, 'power':1, 'saturation':0.02, 'scale':1,
      'mode':0 },
    { 'prename':'C3', 'postname':'a2', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':-0.07, 'delay':1, 'threshold':-0.05,
      'slope':1, 'power':1, 'saturation':0.02, 'scale':3,
      'mode':0 },
    { 'prename':'C3', 'postname':'a3', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':-0.07, 'delay':1, 'threshold':-0.05,
      'slope':1, 'power':1, 'saturation':0.02, 'scale':2,
      'mode':0 },
    { 'prename':'C3', 'postname':'a4', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':-0.07, 'delay':1, 'threshold':-0.05,
      'slope':1, 'power':1, 'saturation':0.02, 'scale':2,
      'mode':0 },
    { 'prename':'C3', 'postname':'a5', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':-0.07, 'delay':1, 'threshold':-0.05,
      'slope':1, 'power':1, 'saturation':0.02, 'scale':2,
      'mode':0 },
    { 'prename':'C3', 'postname':'a6', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':-0.07, 'delay':1, 'threshold':-0.05,
      'slope':1, 'power':1, 'saturation':0.02, 'scale':3,
      'mode':0 },
    #
#    { 'prename':'R5', 'postname':'C2', 'model':'power_gpot_gpot',
#      'cart':None, 'reverse':-0.08, 'delay':1, 'threshold':-0.05214,
#      'slope':1, 'power':1, 'saturation':0.02, 'scale':1,
#      'mode':0 },
#    { 'prename':'R3', 'postname':'C3', 'model':'power_gpot_gpot',
#      'cart':None, 'reverse':-0.08, 'delay':1, 'threshold':-0.05214,
#      'slope':1, 'power':1, 'saturation':0.02, 'scale':2,
#      'mode':0 },
    # L4-neighbor 5
#    { 'prename':'L4', 'postname':'R3', 'model':'power_gpot_gpot',
#      'cart':3, 'reverse':0.0, 'delay':1, 'threshold':-0.0505,
#      'slope':2, 'power':1, 'saturation':0.1, 'scale':2,
#      'mode':1 },
#    { 'prename':'L4', 'postname':'R4', 'model':'power_gpot_gpot',
#      'cart':3, 'reverse':0.0, 'delay':1, 'threshold':-0.0505,
#      'slope':2, 'power':1, 'saturation':0.1, 'scale':1,
#      'mode':1 },
    { 'prename':'L4', 'postname':'L1', 'model':'power_gpot_gpot',
      'cart':3, 'reverse':0.0, 'delay':1, 'threshold':-0.0505,
      'slope':2, 'power':1, 'saturation':0.1, 'scale':1,
      'mode':0 },
    { 'prename':'L4', 'postname':'L2', 'model':'power_gpot_gpot',
      'cart':3, 'reverse':0.0, 'delay':1, 'threshold':-0.0505,
      'slope':2, 'power':1, 'saturation':0.1, 'scale':4,
      'mode':0 },
    { 'prename':'L4', 'postname':'L4', 'model':'power_gpot_gpot',
      'cart':3, 'reverse':0.0, 'delay':1, 'threshold':-0.0505,
      'slope':2, 'power':1, 'saturation':0.05, 'scale':1,
      'mode':0 },
    { 'prename':'L4', 'postname':'L5', 'model':'power_gpot_gpot',
      'cart':3, 'reverse':0.0, 'delay':1, 'threshold':-0.0505,
      'slope':1, 'power':1, 'saturation':0.5, 'scale':2,
      'mode':0 },
    # L4 - Rx neighbor 6
#    { 'prename':'L4', 'postname':'R1', 'model':'power_gpot_gpot',
#      'cart':2, 'reverse':0.0, 'delay':1, 'threshold':-0.0505,
#      'slope':1, 'power':1, 'saturation':0.1, 'scale':1,
#      'mode':1 },
#    { 'prename':'L4', 'postname':'R2', 'model':'power_gpot_gpot',
#      'cart':2, 'reverse':0.0, 'delay':1, 'threshold':-0.0505,
#      'slope':1, 'power':1, 'saturation':0.1, 'scale':1,
#      'mode':1 },
#    { 'prename':'L4', 'postname':'R3', 'model':'power_gpot_gpot',
#      'cart':2, 'reverse':0.0, 'delay':1, 'threshold':-0.0505,
#      'slope':1, 'power':1, 'saturation':0.1, 'scale':1,
#      'mode':1 },
#    { 'prename':'L4', 'postname':'R5', 'model':'power_gpot_gpot',
#      'cart':2, 'reverse':0.0, 'delay':1, 'threshold':-0.0505,
#      'slope':1, 'power':1, 'saturation':0.1, 'scale':2,
#      'mode':1 },
#    { 'prename':'L4', 'postname':'R6', 'model':'power_gpot_gpot',
#      'cart':2, 'reverse':0.0, 'delay':1, 'threshold':-0.0505,
#      'slope':1, 'power':1, 'saturation':0.1, 'scale':1,
#      'mode':1 },
    # L4 - Lx neighbor 6
    { 'prename':'L4', 'postname':'L2', 'model':'power_gpot_gpot',
      'cart':2, 'reverse':0.0, 'delay':1, 'threshold':-0.0505,
      'slope':1, 'power':1, 'saturation':0.2, 'scale':3,
      'mode':0 },
    { 'prename':'L4', 'postname':'L3', 'model':'power_gpot_gpot',
      'cart':2, 'reverse':0.0, 'delay':1, 'threshold':-0.0505,
      'slope':1, 'power':1, 'saturation':0.05, 'scale':1,
      'mode':0 },
    { 'prename':'L4', 'postname':'L4', 'model':'power_gpot_gpot',
      'cart':2, 'reverse':0.0, 'delay':1, 'threshold':-0.0505,
      'slope':1, 'power':1, 'saturation':0.05, 'scale':1,
      'mode':0 },
    # ax-[Lx,Cx]
#    { 'prename':'a4', 'postname':'C2', 'model':'power_gpot_gpot',
#      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.05184,
#      'slope':0.3, 'power':1, 'saturation':0.06, 'scale':1,
#      'mode':0 },
#    { 'prename':'a4', 'postname':'C3', 'model':'power_gpot_gpot',
#      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.05184,
#      'slope':0.3, 'power':1, 'saturation':0.06, 'scale':1,
#      'mode':0 },
    { 'prename':'a4', 'postname':'L5', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.05184,
      'slope':0.3, 'power':1, 'saturation':0.06, 'scale':4,
      'mode':0 },
    { 'prename':'a4', 'postname':'L4', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.05184,
      'slope':0.3, 'power':1, 'saturation':0.06, 'scale':1,
      'mode':0 },
    { 'prename':'a5', 'postname':'L4', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.05184,
      'slope':0.3, 'power':1, 'saturation':0.06, 'scale':3,
      'mode':0 },
#    { 'prename':'a3', 'postname':'C2', 'model':'power_gpot_gpot',
#      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.05184,
#      'slope':0.3, 'power':1, 'saturation':0.06, 'scale':1,
#      'mode':0 },
#    { 'prename':'a2', 'postname':'C3', 'model':'power_gpot_gpot',
#      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.05184,
#      'slope':0.3, 'power':1, 'saturation':0.06, 'scale':1,
#      'mode':0 }
    { 'prename':'L1', 'postname':'L5', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.05184,
      'slope':0.3, 'power':1, 'saturation':0.06, 'scale':100,
      'mode':0 },
    { 'prename':'L2', 'postname':'L5', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.05184,
      'slope':0.3, 'power':1, 'saturation':0.06, 'scale':35,
      'mode':0 },
    { 'prename':'L5', 'postname':'L2', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.05184,
      'slope':0.3, 'power':1, 'saturation':0.06, 'scale':5,
      'mode':0 },
    { 'prename':'L5', 'postname':'L1', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.05184,
      'slope':0.3, 'power':1, 'saturation':0.06, 'scale':20,
      'mode':0 },

    #
    { 'prename':'Mi1', 'postname':'L1', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.05184,
      'slope':0.3, 'power':1, 'saturation':0.06, 'scale':8,
      'mode':0 },
    { 'prename':'Mi1', 'postname':'L5', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.05184,
      'slope':0.3, 'power':1, 'saturation':0.06, 'scale':8,
      'mode':0 },
    { 'prename':'Tm1', 'postname':'L5', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.05184,
      'slope':0.3, 'power':1, 'saturation':0.06, 'scale':13,
      'mode':0 },
    { 'prename':'Tm2', 'postname':'L5', 'model':'power_gpot_gpot',
      'cart':None, 'reverse':0.0, 'delay':1, 'threshold':-0.05184,
      'slope':0.3, 'power':1, 'saturation':0.06, 'scale':13,
      'mode':0 },








]