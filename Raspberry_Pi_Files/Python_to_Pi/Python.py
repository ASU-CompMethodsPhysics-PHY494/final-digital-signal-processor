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
    "from earsketch import *\n",
    "from Pd import *\n",
    "from numpy import *\n",
    "from scipy import *\n",
    " \n",
    "init()\n",
    "setTempo(101)\n",
    " \n",
    "#Initialise Connections\n",
    "inp = createUGen(Pd.effect, INPUT)\n",
    "output = createUGen(Pd.effect, OUTPUT)\n",
    "\n",
    "connect(input, output)\n",
    "effect = [None] * len(ampLst)\n",
    "TIME = [None] * len(ampLst)\n",
    "VALUE = np.zeros(V)\n",
    "\n",
    "#Create a new effects\n",
    "for i in range(0, len(ampLst) - 1):\n",
    " \n",
    "\n",
    "    distortion[i] = Pd.createUGen(reverbEffect, effect)\n",
    "    reverb[i] = Pd.createUGen(reverbEffect, TIME)\n",
    "    tremelo[i] = Pd.createUGen(reverbEffect, TIME)\n",
    "    chorus[i] = Pd.createUGen(reverbEffect, TIME)\n",
    " \n",
    "    #Defaults:\n",
    "    #Distortion\n",
    "    setParamMin(distortion[i], TIME, 0)\n",
    "    setParamMax(distortion[i], TIME, 1000000)\n",
    "    setParam(distortion[i], TIME, timeList[i])\n",
    "    \n",
    "    setParamMin(distortion[i], VALUE, 0)\n",
    "    setParamMax(distortion[i], VALUE, 5)\n",
    "    setParam(distortion[i], VALUE, ampList[i])\n",
    " \n",
    "\n",
    "    #Reverb\n",
    "    setParamMin(reverb[i], TIME, 0)\n",
    "    setParamMax(reverb[i], TIME, 1000000)\n",
    "    setParam(reverb[i], TIME, timeList[i])\n",
    "    \n",
    "    setParamMin(reverb[i], VALUE, 0)\n",
    "    setParamMax(reverb[i], VALUE, 5)\n",
    "    setParam(reverb[i], VALUE, ampList[i])\n",
    "\n",
    "\n",
    "    #Tremelo\n",
    "    setParamMin(tremelo[i], TIME, 0)\n",
    "    setParamMax(tremelo[i], TIME, 1000000)\n",
    "    setParam(tremelo[i], TIME, timeList[i])\n",
    "    \n",
    "    setParamMin(tremelo[i], VALUE, 0)\n",
    "    setParamMax(tremelo[i], VALUE, 5)\n",
    "    setParam(tremelo[i], VALUE, ampList[i])\n",
    "    \n",
    "    \n",
    "    #Chorus\n",
    "    setParamMin(chorus[i], TIME, 0)\n",
    "    setParamMax(chorus[i], TIME, 1000000)\n",
    "    setParam(chorus[i], TIME, timeList[i])\n",
    "    \n",
    "    setParamMin(chorus[i], VALUE, 0)\n",
    "    setParamMax(chorus[i], VALUE, 5)\n",
    "    setParam(chorus[i], VALUE, ampList[i])\n",
    "    \n",
    "    \n",
    "    connect(Pd.effect, inp, distortion[i], 0, 0)\n",
    "    connect(Pd.effect, reverb[i], TIME[i], 0, 0)\n",
    "    connect(Pd.effect, tremelo[i], output)\n",
    "    connect(Pd.effect, chorus[i], output)\n",
    "\n",
    "finishEffect(Effect)"
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