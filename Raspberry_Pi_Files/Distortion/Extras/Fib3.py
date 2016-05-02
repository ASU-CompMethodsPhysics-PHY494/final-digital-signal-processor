{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def Fib3(x,y)\n",
    "    fib3=np.array([1,2,3,5,8,13,21,1,2,3,5,8,13,21,1,2,3,5,8,13,21,1,2,3,5,\n",
    "                   8,13,21,1,2,3,5,8,13,21,1,2,3,5,8,13,21,1,2,3,5,8,13,21,\n",
    "                   1,2,3,5,8,13,21,1,2,3,5,8,13,21,1,2,3,5,8,13,21])\n",
    "    x=np.linspace(-np.pi,np.pi,100)\n",
    "    y=np.zeros(100)\n",
    "    count=0\n",
    "    for i in range(100): \n",
    "        if i%2==0:\n",
    "            y[i]=(-1)**count*.1*fib2[count]+np.sin(-np.pi+(2*np.pi)/100*i)\n",
    "            count+=1\n",
    "        else: \n",
    "            y[i]=np.sin(-np.pi+(2*np.pi)/100*i)\n",
    "    return(x)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
