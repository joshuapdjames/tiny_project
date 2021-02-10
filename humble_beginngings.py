#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 11:04:18 2021

@author: datasandwich
"""
import pandas as pd
from scipy.io import mmread

matrix=mmread('filtered_gene_bc_matrices/hg19/matrix.mtx')
B=matrix.todense()
matrix_df=pd.DataFrame(B)

ecurd=mmread('zhengdata/E-CURD-55-normalised-files/E-CURD-55.aggregated_filtered_normalised_counts.mtx')
A=matrix.todense()
ecurd_df=pd.DataFrame(A)

barcodes=pd.read_csv('filtered_gene_bc_matrices/hg19/barcodes.tsv')
genes=pd.read_csv('filtered_gene_bc_matrices/hg19/genes.tsv')
sng_cll_mrkers=pd.read_table('Single_cell_markers.txt')
hmn_cll_mrkrs=pd.read_table('human_cell_markers.txt')
