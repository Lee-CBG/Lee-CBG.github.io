---
layout: page-fullwidth
title: "Researchcp"
meta_title: ""
subheadline: ""
teaser: ""
permalink: "/researchcp/"
header:
    image_fullwidth: "genvis-dna-bg_optimized_v1a.png"
---

<div data-magellan-expedition="fixed">
  <ul class="sub-nav">
    <li data-magellan-arrival="Overview"><a href="#Overview">Overview</a></li>
    <li data-magellan-arrival="Active_Learning_Framework"><a href="#Active_Learning_Framework">Active Learning Framework for Cost-Effective TCR-Epitope Binding Affinity Prediction</a></li>
    <li data-magellan-arrival="Context_Aware_Amino"><a href="#Context_Aware_Amino">Context-Aware Amino Acid Embedding Advances Analysis of TCR-Epitope Interactions</a></li>
    <li data-magellan-arrival="pite"><a href="#pite">PiTE</a></li>
    <li data-magellan-arrival="ATM_TCR"><a href="#ATM_TCR">ATM-TCR: TCR-Epitope Binding Affinity Prediction using a Multi-Head Self-Attention Model</a></li>
  </ul>
</div>

<h2 data-magellan-destination="Overview">Overview</h2>
<a name="Overview"></a>

The research conducted by this laboratory spans a wide range of topics in genomics, molecular biology, and computational biology, showcasing a multidisciplinary approach to understanding fundamental biological processes. The team has made significant contributions to the field of immunology, particularly in the realm of T-cell receptor (TCR) and epitope interactions. Pioneering work includes the development of advanced computational models such as ATM-TCR, a multi-head self-attention model for predicting TCR-epitope binding affinities, and PiTE, a TCR-epitope binding affinity prediction pipeline utilizing a Transformer-based Sequence Encoder. These computational tools provide valuable insights into the dynamics of immune responses and have potential applications in vaccine development and personalized medicine.

Moreover, the research team delves into the intricacies of DNA replication and transcription processes, shedding light on the factors influencing mutation rates and transcript errors in bacterial pathogens like Salmonella enterica subsp. enterica and Escherichia coli. Their work not only uncovers the complexities of mutagenesis but also challenges existing paradigms, as seen in studies on DNA replication-transcription conflicts and the symmetrical wave pattern of base-pair substitution rates across the E. coli chromosome. Beyond the laboratory bench, the team engages with broader societal issues, addressing privacy and ethical considerations in wastewater monitoring. Their commitment to understanding and advancing both the theoretical and practical aspects of genomics and molecular biology positions this research group at the forefront of innovative scientific inquiry.

<h2 data-magellan-destination="Active_Learning_Framework"></h2>
<a name="Active_Learning_Framework"></a>

{% include project
  title="Active Learning Framework for Cost-Effective TCR-Epitope Binding Affinity Prediction"

  description="A unified data optimization framework (dubbed ActiveTCR) that integrates active learning and TCR-epitope binding affinity prediction models. In two distinct use cases, ActiveTCR demonstrated superior performance over passive learning, notably cutting annotation costs approximately half and minimizing redundancy by over 40% - all without compromising on model performance. ActiveTCR stands as the first systematic exploration into the realm of data optimization for TCR-epitope binding affinity prediction."

  team="Pengfei Zhang, Seojin Bang, Heewook Lee"

  image="/assets/img/research/activetcr.png"

  citation="https://github.com/Lee-CBG/ActiveTCR"
%}

<h2 data-magellan-destination="Context_Aware_Amino"></h2>
<a name="Context_Aware_Amino"></a>

{% include project
  title="Context-Aware Amino Acid Embedding Advances Analysis of TCR-Epitope Interactions"

  description="Introducing catELMo, a groundbreaking and efficient amino acid embedding model, specifically tailored for T cell receptors. This advanced model facilitates an impressive boost of over 20% in absolute AUC when predicting binding affinity for unseen or novel epitopes, outperforming the conventional BLOSUM62. Moreover, catELMo exhibits an extraordinary capacity to maintain comparable performance to BLOSUM62, while reducing about 93% training data, making it a game-changer in the field of TCR analysis."

  team="Pengfei Zhang, Seojin Bang, Michael Cai, Heewook Lee"

  image="/assets/img/research/catelmo.png"

  citation="https://elifesciences.org/reviewed-preprints/88837v1"
%}

<h2 data-magellan-destination="pite"></h2>
<a name="pite"></a>

{% include project
  title="PiTE: TCR-epitope Binding Affinity Prediction Pipeline using Transformer-based Sequence Encoder"

  description="How to better summarize multiple amino-acid-level embeddings into a single sequence-level embedding compared to average pooling? We build sequence encoders utilizing various structures including Transformer, BiLSTM, and ByteNet, and propose PiTE, a state-of-the-art two-step pipeline designed for TCR-epitope binding affinity prediction.."

  team="Pengfei Zhang, Seojin Bang, Heewook Lee"

  image="/assets/img/research/pite.png"

  citation="https://www.worldscientific.com/doi/pdf/10.1142/9789811270611_0032"
%}

<h2 data-magellan-destination="ATM_TCR"></h2>
<a name="ATM_TCR"></a>

{% include project
  title="ATM-TCR: TCR-Epitope Binding Affinity Prediction using a Multi-Head Self-Attention Model"

  description="ATM-TCR leverages multi-head self-attention mechanisms to capture biological contextual information and improves generalization ff TCR-epitope binding affinity prediction models. A novel application of the attention map to improve out-of-sample performance by demonstrating on recent SARS-CoV-2 data."

  team="Michael Cai, Seojin Bang, Pengfei Zhang, Heewook Lee"

  image="/assets/img/research/atm-tcr.png"

  citation="https://www.frontiersin.org/articles/10.3389/fimmu.2022.893247/full"
%}
