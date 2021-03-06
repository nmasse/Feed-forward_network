import numpy as np
import os

print("--> Loading parameters...")

global par

"""
Independent parameters
"""
par = {
    # Setup parameters
    'save_dir'              : './save_dir/',
    'data_dir'              : './data_dir/',
    'data_filenames'        : ['data_even.mat', 'data_odd.mat'],
    'debug_model'           : False,
    'load_previous_model'   : False,
    'ckpt_load_fn'          : 'model.ckpt',
    'ckpt_save_fn'          : 'model.ckpt',

    # Network configuration
    'layer_dims'            : [9*12-2,120,100,80,50,30,1],
    'init_weight_sd'        : 0.05,
    'nonlinearity'          : 'sigmoid',
    'learning_rate'         : 1e-3,
    'num_iterations'        : 100000,
    'iters_between_eval'    : 250,
    'batch_size'            : 100,
    'hist_size'             : 12,
    'test_reps'             : 50,

    # Dropout
    'keep_prob'             : 1
    }

def update_dependencies():
    """
    Updates all parameter dependencies
    """
    par['num_layers'] = len(par['layer_dims'])

update_dependencies()

print("--> Parameters successfully loaded.\n")
