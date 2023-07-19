# Copyright (c) 2023 Minniti Julien

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import streamlit as st

def resource_page():
    st.header('Introduction')
    st.write("TFinder is a Python easy-to-use web tool for identification of putative Transcription Factor Binding Sites (TFBS) in a sequence. It allows extracting directly the promoter or terminal regions of a gene via the NCBI API for 5 different species, with no limit on the number of genes. The reference pattern (ex: a TFBS) accepts both IUPAC codes and JASPAR entries. It is also possible to generate and to use a Position Weight Matrix (PWM). Finally, the data are presented in tabular form, along with a graph showing the relevance of the TFBSs found as a function of their relative position on the sequence.In this document, we will detail each part of TFinder, the method used and the resulting advantages and limitations. The software has 2 main modules with different sub-modules necessary for its operation. We will not go into the specific details of the underlying code but will explain the principles and processes. We will first look at how to retrieve a nucleotide sequence on NCBI, then how to find a specific pattern in a nucleotide sequence.")
    st.header('NCBI API: region extracter')
    col1, col2 = st.columns(2)
    with col2:
        st.image('https://raw.githubusercontent.com/Jumitti/TFinder/main/img/NCBI%20API.png')
        st.caption('Picture 1: Screenshot of TFinder promoter and terminator extraction tool')
    with col1:
        st.write('To retrieve a promoter or terminal region of a gene, we first need the name of the gene. We usually use the NCBI database to retrieve these regions, so we decided to use the NCBI API to extract them. TFinder accepts gene names and Gene IDs (Step 1.1 and photo). The species is needed especially if you are using gene names. The code recognizes if it is a gene ID or a gene names. If it is a gene name, it uses the species to find the gene ID (Step 1.1 and 1.2). You can mix gene IDs and gene names. However, the named genes only have the selected species. On the other hand, if you put a human ID gene and a mouse ID gene, TFinder will extract in the species of the gene ID. Transcription Factors (TFs) are proteins that bind to DNA to regulate gene expression. They specifically recognize a nucleotide sequence called a Transcription Factor Binding Site (TFBS) present in the 5’ end (most of the time proximal and core promoter regions) and sometimes 3’ end of the regulatory sequences of a gene (terminator regions). TFinder allows the extraction of these 2 regions. You can set the upstream and the downstream with the sliders. (Step 1.4). TFinder can recognize the direction of the gene to always present it in the 5' to 3' direction. After extraction, the sequences are in FASTA format. The NCBI API does not allow the possibility to extract a nucleotide sequence external to a gene. It is then necessary to find the chromosomal coordinates of the gene. The coordinates represent the start and end of the gene on the chromosome. The beginning and the end of the gene are accessible in the GeneBank of the gene in the ACCESSION section. We also find the accession number of the corresponding chromosome that we will use later to extract our region. Therefore, we can know the direction of the genes and use the NCBI API to retrieve a chunk of the gene using upstream and downstream coordinates based on the beginning of the gene or the end.')
    st.header('Transcription Factors Binding Site')
