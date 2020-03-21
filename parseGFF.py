{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#open file\n",
    "input_file=open(watermelon.gff\", \"r\")\n",
    "\n",
    "#for each line in watermelon.gff do the following\n",
    "for line in input_file:\n",
    "    #split fields by space\n",
    "    fields = [line.split() for line in input_file]\n",
    "    #sort the fields by col 9 in ascending order\n",
    "    fields = (list.sort(fields, key = lambda x: x[8]))\n",
    "    #skip if files are similar after scanning, do not run the code\n",
    "    for line in fields:\n",
    "        if (line[8] == \"similar\"):\n",
    "            continue\n",
    "        else:\n",
    "            #otherwise print gene names in a list in alphabetical order\n",
    "            gene_name = line[8]\n",
    "        print(genes_names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
