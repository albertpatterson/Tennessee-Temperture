import numpy as np

def allCombs(x, y, fn):
  ySize = 1 if y.size == y.shape[0] else y.shape[1]
  xVals = x.shape[0]
  yVals = y.shape[0]
  ys = np.swapaxes(np.reshape(np.tile(y, (xVals, 1)), (xVals,yVals,ySize)),0,1)
  return fn(x, ys)