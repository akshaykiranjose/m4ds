# -*- coding: utf-8 -*-
"""problem 3 & 4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QzHiVAjhIHF5CExLEPU9ta2fH2Yiv_0e

$$x = As$$ $$y = Bx$$ $$y = BAs$$ $$y = Cs$$
"""

from google.colab import drive
drive.mount('/content/drive')

import numpy as np
from scipy.optimize import linprog
import imageio

path_A_inv = "/content/drive/MyDrive/Colab Notebooks/mfds project 1/A_inv.npy"
path_C = "/content/drive/MyDrive/Colab Notebooks/mfds project 1/C.npy"
path_y = "/content/drive/MyDrive/Colab Notebooks/mfds project 1/y.npy"

A_inv = np.load(path_A_inv);
C = np.load(path_C);
y = np.load(path_y);

"""Due to some computational difficulties, a linear approximation of the given constraint function was run, namely
$$y = C s$$ was taken in place of $$||y-Cs||^2_2=0$$
"""

def solve(A, b):
  numRows = A.shape[0] 
  numCols = A.shape[1]

  print("Number of Rows of A = " + str(numRows))
  print("Number of Columns of A = " + str(numCols))

  vF = np.ones([2*numCols, 1])

  mAeq = np.concatenate((A, -A), axis=1)
  vBeq = b

  vLowerBound = np.full([2 * numCols, 1], 0)
  vUpperBound = np.full([2 * numCols, 1], np.inf)
  Bounds = np.concatenate((vLowerBound, vUpperBound), axis=1)

  result = linprog(vF, A_eq=mAeq, b_eq=vBeq, bounds=Bounds)
  vUV = result.x
  s = vUV[0:numCols] - vUV[numCols:];

  return s

A = np.load(path_C);
b = np.load(path_y);

s = solve(A, b)

np.save('s', s)

A_inv = A_inv.astype('float64')
A = np.linalg.inv(A_inv)

x = A.dot(s)
np.save('x', x)

"""
Following the run of the above code, vector $s$ was found and the vector $x$ that was sought was found as $$x = As$$
let's import them into the workspace rather than making it run again.

 """

path_x = "/content/drive/MyDrive/Colab Notebooks/mfds project 1/x.npy"
path_s = "/content/drive/MyDrive/Colab Notebooks/mfds project 1/s.npy"

x = np.load(path_x);
s = np.load(path_s);

y = x.reshape((100,100), order='F')
imageio.imwrite('image.jpg', y)