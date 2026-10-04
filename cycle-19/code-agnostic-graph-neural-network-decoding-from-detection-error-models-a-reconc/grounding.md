# Grounding block - source: ce974486-ea75-4a81-82b8-c5f7d19f1f90

## Research idea

A Code-Agnostic Graph Neural Network Decoder from the Detection Error Model — arXiv 2610.01683v1. Auto-candidate from daily research scan; triage for QNFO research fit.

## Existing paper under revision (remediation only)

(none - new paper)

## Source material (fetched from arXiv)

TITLE: arXiv Query: search_query=&amp;id_list=2610.01683&amp;start=0&amp;max_results=1

ABSTRACT: We present POLYMECHANON, a graph neural network (GNN) decoder for quantum error correction whose only input is the detection error model (DEM) of a quantum code under a given noise model. We represent the DEM as a tripartite graph of detectors, error mechanisms and logical observables, where every input feature is computed by using the quantum code as data rather than design choice. In this way, the same architecture decodes in principle any stabiliser code, under any noise model that can be expressed as a detection error model, once trained on the DEM. We test this approach along four directions. Firstly, on the rotated surface code the decoder outperforms correlated MWPM under both phenomenological and circuit-level noise, with up to $25\%$ fewer logical failures. Secondly, on a family of high-rate qLDPC codes it matches BP+OSD on the smaller codes and surpasses it on the larger ones, with up to $16\%$ fewer logical failures on $[\![130,4,6]\!]$. Thirdly, its decoding time does not depend on the physical error rate, whereas that of BP+OSD grows with it: on $[\![130,4,6]\!]$ its effective cost per shot is of the order of a few ms on a single GPU against a few tens of milliseconds for BP+OSD on a single CPU core, and its fixed computational graph makes it a candidate for real-time decoding on neutral-atom processors. Finally, a single model trained across codes of different families outperforms uncorrelated MWPM on the graph-like codes seen during training and stays within $10\%$ of BP+OSD on the others, while it tends to fail to generalize to unseen codes, particularly larger ones. Its probabilistic output enables confidence-based post-selection, lowering the logical error rate by more than an order of magnitude on the surface code while keeping more than $90\%$ of the shots. Since only the DEM changes, new codes and noise models can be decoded without redesigning the decoder.

## Related literature (arXiv, real identifiers)

arXiv:2610.01683v1 | A Code-Agnostic Graph Neural Network Decoder from the Detection Error Model
  We present POLYMECHANON, a graph neural network (GNN) decoder for quantum error correction whose only input is the detection error model (DEM) of a quantum code under a given noise model. We represent the DEM as a tripartite graph of detectors, error mechanisms and logical observables, where every input feature is computed by using the quantum code as data rather than design choice. In this way, t
arXiv:1609.04846v1 | A Tutorial about Random Neural Networks in Supervised Learning
  Random Neural Networks (RNNs) are a class of Neural Networks (NNs) that can also be seen as a specific type of queuing network. They have been successfully used in several domains during the last 25 years, as queuing networks to analyze the performance of resource sharing in many engineering areas, as learning tools and in combinatorial optimization, where they are seen as neural systems, and also
arXiv:1909.10086v3 | Learning Universal Graph Neural Network Embeddings With Aid Of Transfer Learning
  Learning powerful data embeddings has become a center piece in machine learning, especially in natural language processing and computer vision domains. The crux of these embeddings is that they are pretrained on huge corpus of data in a unsupervised fashion, sometimes aided with transfer learning. However currently in the graph learning domain, embeddings learned through existing graph neural netw
arXiv:2207.14742v2 | Graph Neural Networks for Channel Decoding
  In this work, we propose a fully differentiable graph neural network (GNN)-based architecture for channel decoding and showcase a competitive decoding performance for various coding schemes, such as low-density parity-check (LDPC) and BCH codes. The idea is to let a neural network (NN) learn a generalized message passing algorithm over a given graph that represents the forward error correction (FE
arXiv:2108.00580v3 | GraphFPN: Graph Feature Pyramid Network for Object Detection
  Feature pyramids have been proven powerful in image understanding tasks that require multi-scale features. State-of-the-art methods for multi-scale feature learning focus on performing feature interactions across space and scales using neural networks with a fixed topology. In this paper, we propose graph feature pyramid networks that are capable of adapting their topological structures to varying
arXiv:2605.17156v2 | Sparse Mamba Decoder for Quantum Error Correction: Efficient Defect-Centric Processing of Surface Code Syndromes
  Quantum error correction (QEC) is essential for building fault-tolerant quantum computers, requiring decoders that are simultaneously accurate, fast, and scalable. Most state-of-the-art neural decoders achieve high accuracy but process the full dense syndrome array of size $O(d^2 R) $regardless of the actual error rate, where d is the code distance and R is the number of measurement rounds. At phy
arXiv:2502.01654v1 | Predicting concentration levels of air pollutants by transfer learning and recurrent neural network
  Air pollution (AP) poses a great threat to human health, and people are paying more attention than ever to its prediction. Accurate prediction of AP helps people to plan for their outdoor activities and aids protecting human health. In this paper, long-short term memory (LSTM) recurrent neural networks (RNNs) have been used to predict the future concentration of air pollutants (APS) in Macau. Addi
arXiv:2212.05478v1 | Mul-GAD: a semi-supervised graph anomaly detection framework via aggregating multi-view information
  Anomaly detection is defined as discovering patterns that do not conform to the expected behavior. Previously, anomaly detection was mostly conducted using traditional shallow learning techniques, but with little improvement. As the emergence of graph neural networks (GNN), graph anomaly detection has been greatly developed. However, recent studies have shown that GNN-based methods encounter chall

## QNFO corpus context (Vectorize)

QNFO: Comprehensive Technical Framework for Network Isomorphism | DOI 10.5281/zenodo.18199940
  
QNFO: Topological Quantization and Spectral Filtration | DOI 10.5281/zenodo.18042721
  
QNFO: Auditing the BQNN: Does a Tunable Quantum Neural Network on Trapped-Ion and Superconducting Hardware Demonstrate a Route to Near-Term Quantum Advantage? | DOI 10.5281/zenodo.21566035
  We audit the BQNN paper by Lakhdar-Hamina et al. (2025, PRL / arXiv:2507.21222v2) which implements a tunable quantum neural network on three quantum computing platforms. Through a complete Phase 1-4 research pipeline including due diligence, external literature search across 32 papers, and a 9-stage
QNFO: Proof-of-Concept for Auditable Attention using Ultrametric Tree Distances | DOI 10.5281/zenodo.19648274
  

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] TITLE: arXiv Query: search_query=&amp;id_list=2610.01683&amp;start=0&amp;max_results=1

ABSTRACT: We present POLYMECHANON, a graph neural network (GNN) decoder for quantum error correction whose only input is the detection error model (DEM) of a quantum code under a given noise model. We represent the DEM as a tripartite graph of detectors, error mechanisms and logical observables, where every input feature is computed by using the quantum code as data rather than design choice. In this way, the same architecture decodes in principle any stabiliser code, under any noise model that can be expressed as a detection error model, once trained on the DEM. We test this approach along four directions. Firstly, on the rotated surface code the decoder outperforms correlated MWPM under both phenomenological and circuit-level noise, with up to $25\%$ fewer logical failures. Secondly, on a family of high-rate qLDPC codes it matches BP+OSD on the smaller codes and surpasses it on the larger ones, with up to $16\%$ fewer logical failures on $[\![130,4,6]\!]$. Thirdly, its decoding time does not depend on the physical error rate, whereas that of BP+OSD grows with it: on $[\![130,4,6]\!]$ its effec
[2] arXiv:2610.01683v1 | A Code-Agnostic Graph Neural Network Decoder from the Detection Error Model
  We present POLYMECHANON, a graph neural network (GNN) decoder for quantum error correction whose only input is the detection error model (DEM) of a quantum code under a given noise model. We represent the DEM as a tripartite graph of detectors, error mechanisms and logical observables, where every input feature is computed by using the quantum code as data rather than design choice. In this way, t
[3] arXiv:1609.04846v1 | A Tutorial about Random Neural Networks in Supervised Learning
  Random Neural Networks (RNNs) are a class of Neural Networks (NNs) that can also be seen as a specific type of queuing network. They have been successfully used in several domains during the last 25 years, as queuing networks to analyze the performance of resource sharing in many engineering areas, as learning tools and in combinatorial optimization, where they are seen as neural systems, and also
[4] arXiv:1909.10086v3 | Learning Universal Graph Neural Network Embeddings With Aid Of Transfer Learning
  Learning powerful data embeddings has become a center piece in machine learning, especially in natural language processing and computer vision domains. The crux of these embeddings is that they are pretrained on huge corpus of data in a unsupervised fashion, sometimes aided with transfer learning. However currently in the graph learning domain, embeddings learned through existing graph neural netw
[5] arXiv:2207.14742v2 | Graph Neural Networks for Channel Decoding
  In this work, we propose a fully differentiable graph neural network (GNN)-based architecture for channel decoding and showcase a competitive decoding performance for various coding schemes, such as low-density parity-check (LDPC) and BCH codes. The idea is to let a neural network (NN) learn a generalized message passing algorithm over a given graph that represents the forward error correction (FE
[6] arXiv:2108.00580v3 | GraphFPN: Graph Feature Pyramid Network for Object Detection
  Feature pyramids have been proven powerful in image understanding tasks that require multi-scale features. State-of-the-art methods for multi-scale feature learning focus on performing feature interactions across space and scales using neural networks with a fixed topology. In this paper, we propose graph feature pyramid networks that are capable of adapting their topological structures to varying
[7] arXiv:2605.17156v2 | Sparse Mamba Decoder for Quantum Error Correction: Efficient Defect-Centric Processing of Surface Code Syndromes
  Quantum error correction (QEC) is essential for building fault-tolerant quantum computers, requiring decoders that are simultaneously accurate, fast, and scalable. Most state-of-the-art neural decoders achieve high accuracy but process the full dense syndrome array of size $O(d^2 R) $regardless of the actual error rate, where d is the code distance and R is the number of measurement rounds. At phy
[8] arXiv:2502.01654v1 | Predicting concentration levels of air pollutants by transfer learning and recurrent neural network
  Air pollution (AP) poses a great threat to human health, and people are paying more attention than ever to its prediction. Accurate prediction of AP helps people to plan for their outdoor activities and aids protecting human health. In this paper, long-short term memory (LSTM) recurrent neural networks (RNNs) have been used to predict the future concentration of air pollutants (APS) in Macau. Addi
[9] arXiv:2212.05478v1 | Mul-GAD: a semi-supervised graph anomaly detection framework via aggregating multi-view information
  Anomaly detection is defined as discovering patterns that do not conform to the expected behavior. Previously, anomaly detection was mostly conducted using traditional shallow learning techniques, but with little improvement. As the emergence of graph neural networks (GNN), graph anomaly detection has been greatly developed. However, recent studies have shown that GNN-based methods encounter chall
[10] QNFO: Comprehensive Technical Framework for Network Isomorphism | DOI 10.5281/zenodo.18199940
  
[11] QNFO: Topological Quantization and Spectral Filtration | DOI 10.5281/zenodo.18042721
  
[12] QNFO: Auditing the BQNN: Does a Tunable Quantum Neural Network on Trapped-Ion and Superconducting Hardware Demonstrate a Route to Near-Term Quantum Advantage? | DOI 10.5281/zenodo.21566035
  We audit the BQNN paper by Lakhdar-Hamina et al. (2025, PRL / arXiv:2507.21222v2) which implements a tunable quantum neural network on three quantum computing platforms. Through a complete Phase 1-4 research pipeline including due diligence, external literature search across 32 papers, and a 9-stage
[13] QNFO: Proof-of-Concept for Auditable Attention using Ultrametric Tree Distances | DOI 10.5281/zenodo.19648274
  