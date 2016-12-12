# written by longriyao
#coding: utf-8

import caffe
import cv2
import numpy
import yaml
import os
class GenLayer(caffe.Layer):
    def _get_param(self):
        # parse
        layer_params = yaml.load(self.param_str)
        # get the param
        if layer_params.has_key('output_folder'):
            self._output_folder = layer_params['output_folder']
        else:
            self._output_folder = ""

    def setup(self,bottom,top):
        self._get_param()

        pass

    def forward(self,bottom,top):
        if(bottom[0] is None):
            print "this is no images"
            return 0
        channel_swap = (0, 2, 3, 1)
        images = bottom[0].transpose(channel_swap)
        for i in xrange(len(images)):
            name = os.path.join(self._output_folder,str(i)+".jpg")
            cv2.imwrite(name,images[i])

    def backward(self,bottom,top):
        pass
    def reshape(self,bottom,top):
        pass