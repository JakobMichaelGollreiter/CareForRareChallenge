# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 15:07:25 2022

@author: robin
"""
import torch.nn as nn
from .Autoencoder_setup import Autoencoder


class NN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, enlarging_factor, autoencoder: Autoencoder = None):
        super().__init__()

        self.NN = nn.Identity()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.enlarging_factor = enlarging_factor
        if autoencoder:
            self.encoder = autoencoder.return_encoder()

            l1 = nn.Linear(self.input_size, self.hidden_size)
            nn.init.xavier_uniform_(l1.weight)
            l2 = nn.Linear(self.hidden_size, self.hidden_size)
            nn.init.xavier_uniform_(l2.weight)
            l3 = nn.Linear(self.hidden_size, self.output_size)
            nn.init.xavier_uniform_(l3.weight)

            # define model architecture and move to cuda
            self.NN = nn.Sequential(
                l1,
                nn.Tanh(),
                l2,
                nn.Tanh(),
                l3,
                nn.Sigmoid()
            )

        else:
            self.encoder = None

            l1 = nn.Linear(self.input_size, self.hidden_size)
            nn.init.xavier_uniform_(l1.weight)
            l2 = nn.Linear(self.hidden_size, self.hidden_size)
            nn.init.xavier_uniform_(l2.weight)
            l3 = nn.Linear(self.hidden_size, self.output_size)
            nn.init.xavier_uniform_(l3.weight)

            # define model architecture and move to cuda
            self.NN = nn.Sequential(
                l1,
                nn.Tanh(),
                l2,
                nn.Tanh(),
                l3,
                nn.Sigmoid()
            )

    def forward(self, x):

        if self.encoder:
            x = self.encoder(x)

        x = self.NN(x)
        return x
