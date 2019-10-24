import tensorflow as tf
import numpy as np
from PIL import Image
from tensorflow.nn import conv2d,max_pool
from tensorflow import Variable
from tensorflow.random import normal
from tensorflow.math import add,concat

class Network:

    def __init__(self):

        #Total Number of Epochs
        self.epochs=None
        self.lr=1e-4
        #Path Variables
        self.checkpoint_path='./model_checkpoints/'
        self.train_input_path='./data/train_frames/input/'
        self.train_output_path='./data/train_frames/output/'
        self.test_input_path='./data/test_frames/input/'
        self.test_output_path='./data/test_frames/output/'
        self.val_input_path='./data/val_frames/input/'
        self.val_output_path='./data/val_frames/output/'

        #Previous Ground Truth
        self.prev_gt=None

    def variables_initializer(self):
        pass

    def model_checkpoint(self):
        pass

    def model1(self,input,params,*args):
        pass

    def model2(self,input,params,*args):
        pass

    def model4(self,input,params,*args):
        pass

    def model3(self,input,params,*args):
        pass

    def u_net_1(self,input,params,*args):
        pass

    def u_net_2(self,input,params,*args):
        pass

    def u_net_2_inp_prep(self, model_2_output, model_1_output):
        model_3_inp_1 = concat([model_2_output[0], model_1_output[0]])
        model_3_inp_2 = concat([model_2_output[1], model_1_output[1]])
        model_3_inp_1_final = conv2d(model_3_inp_1)
        model_3_inp_2_final = conv2d(model_3_inp_2)
        return concat([model_3_inp_1_final, model_3_inp_2_final, model_1_output[2], model_1_output[3], model_1_output[4]])

    def main_model(self,inputs,params,*args):
        model_1_output = self.model_1(inputs)
        model_1_concat_output = concat(model_1_output,axis=-1)
        u_net_1_output = self.u_net_1(model_1_concat_output)
        model_2_output=self.model2()
        u_net_2_input = self.u_net_2_inp_prep(model_2_output, model_1_output)
        u_net_2_output = self.u_net_2(u_net_2_input)
        model_4_output = self.model4()
        final_output = self.model3(concat([u_net_2_output, u_net_1_output]))
        pass

    def optimizer(self,*args):
        pass

    def loss_function(self,y_true,y_pred):
        loss=0
        return loss

    def tensorboard(self,*args):
        pass

    def gradient_taping(self,*args):
        pass

    def training(self,inputs):
        pass

    def testing(self,epoch,*args):
        pass

    def validation(self,epoch,*args):
        pass

    def train_dataloader(self, *args):
        pass

    def test_dataloader(self, *args):
        pass

    def val_dataloader(self, *args):
        pass

Network()
