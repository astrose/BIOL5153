{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import re"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Q1 Accession Names\n",
    "acc_names= [\"xkn59438\", \"yhdck2\", \"eihd39d9\", \"chdsye847\", \"hedle3455\", \"xjhd53e\", \"45da\", \"de37dp\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\taccession name: xkn59438 contains number 5\n",
      "\taccession name: hedle3455 contains number 5\n",
      "\taccession name: xjhd53e contains number 5\n",
      "\taccession name: 45da contains number 5\n"
     ]
    }
   ],
   "source": [
    "#contains the number 5\n",
    "for acc in acc_names:\n",
    "    if re.search(r\"5\", acc):\n",
    "        print (\"\\t\" + \"accession name: \" + acc + \" contains number 5\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\taccession name: yhdck2 contains d or e\n",
      "\taccession name: eihd39d9 contains d or e\n",
      "\taccession name: chdsye847 contains d or e\n",
      "\taccession name: hedle3455 contains d or e\n",
      "\taccession name: xjhd53e contains d or e\n",
      "\taccession name: 45da contains d or e\n",
      "\taccession name: de37dp contains d or e\n"
     ]
    }
   ],
   "source": [
    "#contain the letter d or e\n",
    "for acc in acc_names:\n",
    "    if re.search(r\"(d|e)\", acc) :\n",
    "                 print(\"\\t\" + \"accession name: \" + acc + \" contains d or e\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\taccession name: chdsye847 contains d followed by e\n",
      "\taccession name: hedle3455 contains d followed by e\n",
      "\taccession name: xjhd53e contains d followed by e\n",
      "\taccession name: de37dp contains d followed by e\n"
     ]
    }
   ],
   "source": [
    "#contain the letters d and e in that order\n",
    "for acc in acc_names:\n",
    "    if re.search(r\"d.*e\", acc):\n",
    "        print(\"\\t\" + \"accession name: \" + acc + \" contains d followed by e\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\taccession name: eihd39d9 contains d and e in any order\n",
      "\taccession name: chdsye847 contains d and e in any order\n",
      "\taccession name: hedle3455 contains d and e in any order\n",
      "\taccession name: xjhd53e contains d and e in any order\n",
      "\taccession name: de37dp contains d and e in any order\n"
     ]
    }
   ],
   "source": [
    "#contain both the letters d and e in any order\n",
    "for acc in acc_names:\n",
    "    if re.search(r\"d.*e\",acc) or re.search(r\"e.*d\", acc):\n",
    "        print(\"\\t\" + \"accession name: \" + acc + \" contains d and e in any order\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\taccession name: xkn59438 contains x or y\n",
      "\taccession name: yhdck2 contains x or y\n",
      "\taccession name: xjhd53e contains x or y\n"
     ]
    }
   ],
   "source": [
    "#start with x or y\n",
    "for acc in acc_names:\n",
    "    if re.search(r\"^(x|y)\", acc):\n",
    "        print(\"\\t\" + \"accession name: \" + acc + \" contains x or y\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\taccession name: xjhd53e starts with x or y and ends with e\n"
     ]
    }
   ],
   "source": [
    "#start with x or y and end with e\n",
    "for acc in acc_names:\n",
    "    if re.search(r\"^(x|y).*e$\", acc):\n",
    "        print(\"\\t\" + \"accession name: \" + acc + \" starts with x or y and ends with e\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\taccession name: xkn59438 contains 3 or more numbers in a row\n",
      "\taccession name: chdsye847 contains 3 or more numbers in a row\n",
      "\taccession name: hedle3455 contains 3 or more numbers in a row\n"
     ]
    }
   ],
   "source": [
    "#contain three or more numbers in a row\n",
    "for acc in acc_names:\n",
    "    if re.search(r\"\\d{3,}\", acc):\n",
    "        print(\"\\t\" + \"accession name: \" + acc + \" contains 3 or more numbers in a row\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\taccession name: 45da ends with d followed by a, r or p\n",
      "\taccession name: de37dp ends with d followed by a, r or p\n"
     ]
    }
   ],
   "source": [
    "#end with d followed by either a, r or p\n",
    "for acc in acc_names:\n",
    "    if re.search(r\"d[arp]$\", acc):\n",
    "        print(\"\\t\" + \"accession name: \" + acc + \" ends with d followed by a, r or p\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\taccession name: hedle3455 contains the d and e in that order, with a letter between them\n"
     ]
    }
   ],
   "source": [
    "#contain the letters d and e in that order with a single letter between them\n",
    "for acc in acc_names:\n",
    "    if re.search(r\"d.e\", acc):\n",
    "        print(\"\\t\" + \"accession name: \" + acc + \" contains the d and e in that order, with a letter between them\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "import re\n",
    "#Q2 Double Digest\n",
    "dna=open(\"dna.txt\").read().rstrip(\"\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "all_cuts=[0]\n",
    "#AbcI cut position\n",
    "for match in re.finditer(r\"A[ATGC]TAAT\",dna):\n",
    "    all_cuts.append(match.start() +3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "#AbcII cut position\n",
    "for match in re.finditer(r\"GC[AG][AT]TG\", dna):\n",
    "    all_cuts.append(match.start() + 4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 488, 1143, 1577, 1628, 2012]\n"
     ]
    }
   ],
   "source": [
    "#final position added\n",
    "all_cuts.append(len(dna))\n",
    "sorted_cuts = sorted(all_cuts)\n",
    "print(sorted_cuts)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "one fragment size is 488\n",
      "one fragment size is 655\n",
      "one fragment size is 434\n",
      "one fragment size is 51\n",
      "one fragment size is 384\n"
     ]
    }
   ],
   "source": [
    "for i in range(1,len(sorted_cuts)):\n",
    "    this_cut_position = sorted_cuts[i]\n",
    "    previous_cut_position = sorted_cuts[i-1]\n",
    "    fragment_size = this_cut_position - previous_cut_position\n",
    "    print(\"one fragment size is \" + str(fragment_size))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
