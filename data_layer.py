# written by longriyao

"""
    The data_layer is provide data to the net
"""
import caffe
import cv2
import yaml

class DataLayer(caffe.Layer):
    def setup(self,bottom,top):
        # setup function

        # parse
        layer_params = yaml.load(self.param_str_)
        #get the param
        if layer_params.has_key('batch_size'):
            batch_size = layer_params['batch_size']
        else:
            batch_size = 32

        if layer_params.has_key('root_folder'):
            root_folder = layer_params['root_folder']
        else:
            root_folder = ""

        if layer_params.has_key('source'):
            source = layer_params['source']
        else:
            print "must write the source field in data_layer"
            assert 0

        if layer_params.has_key('height'):
            height = layer_params['height']
        else:
            height = 64

        if layer_params.has_key('weight'):
            weight = layer_params['weigh   t']
        else:
            weight = 64



