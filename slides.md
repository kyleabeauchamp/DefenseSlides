% title: Inferring protein structure and dynamics from simulation and experiment
% author: Kyle A. Beauchamp
% author: Das and Pande Labs

---
title: Biological Macromolecules

<table width="100%">
 <tr>
  <td width="33%"><img height=400 src=figures/4bna.png /></td>
  <td width="33%"><img height=400 src=figures/1zih.png /></td>
  <td width="33%"><img height=400 src=figures/2hbb.png /></td>
 </tr>
</table>

<footer class="source"> Dickerson, 1988; Pardi, 1996; Raleigh, 2007  </footer>

---
title: The Atomistic Basis of Disease

...EVKMD<b><font color="black">A</font></b>EFRHDS...  ...EVKMD<b><font color="black">T</font></b>EFRHDS...  ...EVKMD<b><font color="black">V</font></b>EFRHDS...

<img width=300 src=figures/alanine.png />  <img width=300 src=figures/threonine.png />   <img width=300 src=figures/valine.png />

<img width=300 src=figures/sick.png />  <img width=300 src=figures/healthy.png />   <img width=300 src=figures/sicker.png />

<footer class="source"> 
Jonsson, 2012  A673 T673 V673
</footer>

---
title: Atomistic Medicine

<img width=475 src=figures/tiotropium.png /> <img width=425 src=figures/4daj.png />

<footer class="source"> Wikipedia; Kobilka, 2012  </footer>

---
title: Baby Steps: Protein Folding

<img width=425 src=figures/4daj.png />  <img width=425 src=figures/hp35.png />

<footer class="source"> Wikipedia; Kobilka, 2012  </footer>

---
title: Goal: Predictive, atomic-detail models of protein structure and dynamics (and folding)
class: segue dark nobackground

---
title: What do we <i>really</i> know about proteins?

<img height=225 src=figures/crystal.jpg />  <img height=225 src=figures/HP35_CD.png />  <img height=225 src=figures/HP35_relaxation.png /> 

---
title: What do proteins look like?

Structural biology provides atomic-scale models of <i>selected</i> conformational states.
<center>
<img height=300 src=figures/crystal.jpg />   <img height=300 src=figures/hp35.png/> 
</center>

<footer class="source"> http://cbic.yale.edu/crystallization-automation </footer>

---
title: How do proteins work?
subtitle: Biophysical experiments characterize equilibrium and kinetic properties along <i>selected</i> order parameters.

<img height=300 src=figures/HP35_CD.png />  <img height=300 src=figures/HP35_relaxation.png /> 

---
title: Limitations of current understanding

Structure:

- One protein (condition), one structure
- Unnatural or perturbative sample conditions

Equilibrium / Kinetics:

- Limited structural and temporal resolution 
- Interpreting / integrating data from multiple experiments


---
title: Introduction to Atomistic Simulation
class: segue dark nobackground

---
title: Molecular Dynamics

- Simulate the physical interactions of proteins in solution
- Numerically integrate the equations of motion

<center>
<img height=430 src=figures/hp35_box.png />
</center>

---
title: 100 $\mu s$ of HP35 Dynamics

<center>
<video width="640" height="480" controls>
  <source src="movies/hp35_shaw.ogv" type="video/ogg">
</video>
</center> 

<footer class="source"> 
Shaw, 2011
</footer>

---
title: Goals of Atomistic Simulation

- Calculate experimental observables
- Interpret experimental observables
- Generate atomic-detail hypotheses

---
title: Outline

- Inferring Protein Dynamics from Molecular Simulation
- Quantitative Comparison of villin headpiece simulations and Triple-Triplet Energy Transfer Experiments
- Inferring Conformational Ensembles from Noisy Experiments

---
title: Inferring Protein Dynamics from Molecular Simulation
class: segue dark nobackground

---
title: Two Challenges in Molecular Simulation
subtitle: How to sample biological timescales?

<center>
<img height=450 src=figures/protein_timescales.jpg />
</center>

<footer class="source">
Church, 2011.
</footer>

---

title: Two Challenges in Molecular Simulation
subtitle: How to sample biological timescales?

<img height=300 src=figures/anton.jpg />  <img height=300 src=figures/TitanNew.jpg />

<footer class="source"> 
Shaw et al.  , Eastman et. al.,  NVIDIA / Anandtech.  
</footer>

---

title: Two Challenges in Molecular Simulation
subtitle: Meaningful Connection to experiment

<img height=300 src=figures/hp35_box.png />   <img height=300 src=figures/HP35_relaxation.png />   <img height=300 src=figures/folding_reaction.png />

---
title: Markov State Models

- Run many parallel simulations on commodity hardware
- Build kinetic network model of dynamics
- Quantitively predict structure, equilibrium, and kinetics

<img height=250 src=figures/hp35_box.png /> <img height=250 src=figures/NTL9_network.jpg />   <img height=250 src=figures/HP35_relaxation.png />

<footer class="source"> 
Bowman, Beauchamp, Boxer, Pande, 2009. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Voelz, Bowman, Beauchamp, Pande, 2010.  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Beauchamp, Bowman, Lane, Maibaum, Haque, Pande 2011. <br>
Beauchamp, McGibbon, Lin, Pande, 2012. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Also: Chodera, Huang, Noe, Hummer, Dill, and others.
</footer>

---
title: 100 $\mu s$ of HP35 Dynamics (MSM)

<center>
<video width="640" height="480" controls>
  <source src="movies/hp35_msm.ogv" type="video/ogg">
</video>
</center> 

<footer class="source"> 
<br>
Beauchamp, K. A., Ensign, D. L., Das, R., & Pande, V. S.  PNAS 2011.
</footer>

---
title: Introduction to Markov State Models

<center>
<img height=400 src=figures/NewPaths1.png />
</center>
---
title: Introduction to Markov State Models

<center>
<img height=400 src=figures/NewPaths2.png />
</center>


---
title: Introduction to Markov State Models

<center>
<img height=400 src=figures/NewPaths3.png />
</center>


---
title: Counting Transitions

<center>

<img height=300 src=figures/NewPaths-2State.png />

$\downarrow$

$A = (111222222)$

---
title: Counting Transitions

<center>

$A = (111222222)$


$\downarrow$

$C = \begin{pmatrix} C_{1\rightarrow 1} & C_{1\rightarrow 2} \\\ C_{2 \rightarrow 1} & C_{2 \rightarrow 2} \end{pmatrix} =  \begin{pmatrix}2 & 1 \\\ 0 & 5\end{pmatrix}$

</center>

---
title: Estimating Rates

<center>
$C = \begin{pmatrix} C_{1\rightarrow 1} & C_{1\rightarrow 2} \\\ C_{2 \rightarrow 1} & C_{2 \rightarrow 2} \end{pmatrix} = \begin{pmatrix}2 & 1 \\\ 0 & 5\end{pmatrix}$

$\downarrow$

$T = \begin{pmatrix} T_{1\rightarrow 1} & T_{1\rightarrow 2} \\\ T_{2 \rightarrow 1} & T_{2 \rightarrow 2} \end{pmatrix} = \begin{pmatrix}\frac{2}{3} & \frac{1}{3} \\\ 0 & 1\end{pmatrix}$

</center>

---
title: MSMBuilder

<img height=400 src=figures/msmbuilder.png />  <img height=400 src=figures/msmb_users.png />

<footer class="source">
Contributions from Greg Bowman, Xuhui Huang, John Chodera, Sergio Bacallado, Dan Ensign, Vince Voelz, TJ Lane, Lutz Maibaum, Imran Haque, Robert McGibbon, Christian Schwantes, Toni Giorgino, Gianni de Fabritiis
</footer>

---
title: Progress in MSM Construction
subtitle: Scaling to full protein systems

<center>
<img height=400 src=figures/JCP_cover.jpg/>
</center>


<footer class="source">
Bowman, G. R., Beauchamp, K. A., Boxer, G., & Pande, V. S. (2009). Progress and challenges in the automated construction of Markov state models for full protein systems. The Journal of chemical physics, 131, 124101.
</footer>

---
title: Progress in MSM Construction
subtitle: Reaching millisecond timescales

<center>
<img height=400 src=figures/NTL9_network.jpg />
</center>

<footer class="source">
Voelz, V. A., Bowman, G. R., Beauchamp, K., & Pande, V. S. (2010). Molecular simulation of ab initio protein folding for a millisecond folder NTL9 (1− 39). Journal of the American Chemical Society, 132(5), 1526-1528.
</footer>

---
title: Progress in MSM Construction
subtitle: Algorithms for Accurate MSMs

<center>
<img height=300 src=figures/KCentersCentrality.png />  <img height=300 src=figures/HybridCentrality.png />  <img height=300 src=figures/TwoState-Pops.png />
</center>

<footer class="source">
Beauchamp, K. A., Bowman, G. R., Lane, T. J., Maibaum, L., Haque, I. S., & Pande, V. S. (2011). MSMBuilder2: Modeling conformational dynamics on the picosecond to millisecond scale. Journal of chemical theory and computation, 7(10), 3412-3419.
</footer>

---
title: Progress in MSM Construction
subtitle: Reconciling two and multi-state behavior in protein folding

<center>
<img height=400 src=figures/rate_spectra.png />
</center>

<footer class="source">
Beauchamp, K. A., McGibbon, R., Lin, Y. S., & Pande, V. S. (2012). Simple few-state models reveal hidden complexity in protein folding. Proceedings of the National Academy of Sciences, 109(44), 17807-17813.
</footer>

---
title: Quantitative Comparison of villin headpiece simulations and Triple-Triplet Energy Transfer Experiments
class: segue dark nobackground

---
title: HP35: A Model for Protein Folding


<center>
<img height=500 src=figures/hp35.png />
</center>


---
title: Triplet Triplet Energy Transfer

- Like FRET, but sensitive at the Å level 
- Used to monitor rates of contact formation
- With denaturant, can probe native and unfolded states

---
title: Triplet Triplet Energy Transfer

<center>
<img height=500 src=figures/Structure-23-35.png />
</center>

<footer class="source">
Kiefhaber, 2010.
</footer>

---
title: Triplet Triplet Energy Transfer

<center>
<img height=500 src=figures/Structure-1-35.png />
</center>


<footer class="source">
Kiefhaber, 2010.
</footer>

---
title: Triplet Triplet Energy Transfer

<center>
<img height=500 src=figures/Structure-1-35-star.png />
</center>


<footer class="source">
Kiefhaber, 2010.
</footer>

---
title: Triplet Triplet Energy Transfer

<center>
<img height=500 src=figures/Trace-1-35.png />
</center>


<footer class="source">
Kiefhaber, 2010.
</footer>

---
title: Simulating TTET in Silico
subtitle: A modified MSM can predict the output of TTET experiments

<center>
<img height=430 src=figures/ConformationalMSM.png /> <img height=450 src=figures/ElectronicMSM-full.png />
</center>

---
title: Observed TTET at 4 probe locations

<center>
<img height=430 src=figures/AllTraces-Expt.png />
</center>

---
title: TTET at positions (7,23)

<center>
<img height=400 src=figures/Structure2-7-23.png />
</center>

---
title: TTET at positions (7, 23)

<center>
<img height=500 src=figures/Data-7-23.png />
</center>

---
title: TTET at positions (1, 23)

<center>
<img height=400 src=figures/Structure2-1-23.png />
</center>

---
title: TTET at positions (1, 23)

<center>
<img height=500 src=figures/Data-1-23.png />
</center>

---
title: TTET at positions (23, 35)

<center>
<img height=400 src=figures/Structure2-23-35.png />
</center>

---
title: TTET at positions (23, 35)

<center>
<img height=500 src=figures/Data-23-35.png />
</center>

---
title: TTET at positions (1, 35)

<center>
<img height=400 src=figures/Structure2-1-35.png />
</center>

---
title: TTET at positions (1, 35)

<center>
<img height=500 src=figures/Data-1-35.png />
</center>

---
title: Predicting All TTET Experiments

<center>

<img height=420 src=figures/AllTTET-10424.png />  <img height=420 src=figures/AllTTET-3036.png />

</center>

<footer class="source">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
ff99sb-ildn
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
ff03
</footer>
---
title: TTET Conclusions

- Experimental advances revealed multi-state kinetics in smallest protein system
- MSMs capture multi-state kinetics and recapitulate TTET measurements
- Further work will require improved force fields and better models for experimental observables (TTET)


---
title: Inferring Conformational Ensembles from Noisy Experiments (and simulation)
class: segue dark nobackground

---
title: What if the force fields are broken?

<img height=500 src=figures/elephant.jpg />

<footer class="source">
http://newh2o.com/2012/11/02/gemstones-elephant-in-the-room-free-project/
</footer>

---
title: Conformational ensembles

- Structure + Equilibrium (not kinetics)
- Characterize the population of <b>every</b> conformation
- <b>Rigorous</b> connection to equilibrium measurements

<center>
<img height=250 src=figures/hist_0.png />  <img height=250 src=figures/ALA3_rama_amber96_raw.png />  <img height=250 src=figures/bpti_raw.png />
</center>

---
title: Experiments as Projections

<center>
<img height=525 src=figures/David_Covered.png />
</center>

---
title: Experiments as Projections

<center>
<img height=525 src=figures/David_statue.png />
</center>

---
title: Experiments as Projections

<center>
<img height=525 src=figures/David.png />
</center>

<footer class="source">
Regarded from two sides.  Diet Wiegman, 1984.
</footer>
---
title: Two Models, Same "Data"

<center>
<img height=500 src=figures/david_michelangelo.png /> <img height=500 src=figures/david_metal.png /> 
</center>

---
title: A Third Possibility

<center>
<img height=500 src=figures/david_michelangelo.png />  <img height=500 src=figures/harpoon.png />  <img height=500 src=figures/david_metal.png /> 
</center>


---
title: Ambiguous Measurements

<center>
<img height=500 src=figures/single_karplus.png />
</center>

---
title: Bayesian Energy Landscape Tilting

- Infer conformational ensembles from simulation <b>and</b> experiment
- Simulataneously model structure and population
- Error bars on equilibrium <b>and</b> structural features

---
title: Ingredients for Ensemble Inference

- Equilibrium molecular dynamics simulation, with conformations $x_j$
- Equilibrium experimental measurements $F_i$ with uncertainties $\sigma_i$
- Predicted experimental observables: $f_i(x)$

---
title: Biasing and Reweighting

- Project onto basis of experimental observables
- Reweight populations by a linear free energy: $\pi_j(\alpha) \propto \exp[-\sum_i \alpha_i f_i(x)]$
- $\alpha_i$ tells how populations are perturbed by $i$th experiment


<center>
<img height=300 src=figures/hist_0.png />
</center>
---
title: Biasing and Reweighting

- Project onto basis of experimental observables
- Reweight populations by a linear free energy: $\pi_j(\alpha) \propto \exp[-\sum_i \alpha_i f_i(x)]$
- $\alpha_i$ tells how populations are perturbed by $i$th experiment


<center>
<img height=300 src=figures/hist_2.png />
</center>
---
title: Biasing and Reweighting

- Project onto basis of experimental observables
- Reweight populations by a linear free energy: $\pi_j(\alpha) \propto \exp[-\sum_i \alpha_i f_i(x)]$
- $\alpha_i$ tells how populations are perturbed by $i$th experiment


<center>
<img height=300 src=figures/hist_-2.png />
</center>

---
title: A likelihood framework

<center>

Assume independent normal errors:  

$P(F_i | \alpha) \approx N(\langle f_i(x)\rangle _\alpha, \sigma_i)$

Determine $\alpha$ by sampling the likelihood:

$\log P(\alpha| F_1, ..., F_n) = -\sum_j \frac{1}{2}\frac{(\langle f_j(x)\rangle _\alpha - F_j)^2}{\sigma_i^2} + \log P(\alpha)$

MaxEnt prior: $\log P(\alpha) = \lambda \sum_i \pi_i(\alpha) \log \pi_i(\alpha)$

</center>


---
title: FitEnsemble

<article>
<iframe data-src="http://nbviewer.ipython.org/urls/raw.github.com/kyleabeauchamp/FitEnsemble/master/tutorial/Tutorial1.ipynb"></iframe>
</article>


---
title: Trialanine

- Model for secondary structure / intrinsic disorder
- NMR Data: chemical shifts and scalar couplings

<center>
<img height=500 src=figures/ALA3.png />
</center>


<footer class="source"> Schwalbe, 2007  </footer>

---
title: Idea: Use chemical shifts and scalar couplings to reweight trialanine simulation.

---
title: BELT Corrects Force Field Error

<center>
<img height=500 src=figures/ALA3_chi2.png />
</center>


---
title: Correcting $\beta$ Bias in Amber96

<center>
<img height=500 src=figures/ALA3_rama_amber96_raw.png />
</center>

---
title: Correcting $\beta$ Bias in Amber96

<center>
<img height=500 src=figures/ALA3_rama_amber96_belt.png />
</center>

---
title: Forcefield-Independent Simulations

<center>
<img height=500 src=figures/state_0_by_forcefield.png />
</center>

---
title: Bovine Pancreatic Trypsin Inhibitor

- Workhorse in protein folding, crystallography, and NMR

<center>
<img height=500 src=figures/bpti_native.png />
</center>

<footer class="source"> 
Hope et al. Acta. Cryst., 1996. 
</footer> 

---
title: Bovine Pancreatic Trypsin Inhibitor

- Multiple disulfide (C14-C38) conformations in trypsin binding loop.

<center>
<img height=400 src=figures/C14_C38.png />
</center>

<footer class="source"> 
Palmer et al. JACS, 2003.
</footer> 

---
title: Are BPTI Simulations Consistent with Experiment?

<center>
<img height=450 src=figures/BPTI_RMSD_Shaw.png />
</center>

---
title: Idea: Use chemical shifts to reweight BPTI simulation.


---
title: Simulation Favors Non-Native State

<center>
<img height=500 src=figures/bpti_chi14_raw.png />
</center>



---
title: BELT model Favors Native State

<center>
<img height=500 src=figures/bpti_chi14_belt.png />
</center>

---
title: Models for BPTI

<center>
<img height=320 src=figures/bpti_xray.png />  <img height=320 src=figures/bpti_raw.png />  <img height=320 src=figures/bpti_belt.png />
</center>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; X-Ray &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; MD &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  BELT

---
title: Falsifying BPTI Models with J Couplings

<center>
<img height=320 src=figures/bpti_xray_crossthrough.png />  <img height=320 src=figures/bpti_raw_crossthrough.png />  <img height=320 src=figures/bpti_belt.png />
</center>

&nbsp;&nbsp;&nbsp;&nbsp; $\frac{1}{n}\chi^2 = 15.0$  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  $\frac{1}{n}\chi^2 = 13.7$  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $\frac{1}{n}\chi^2 = 10.4$

---
title: Future Work

- Measure <b>all</b> scalar couplings for BPTI
- Better predictors of experimental observables: chemical shifts, scalar couplings
- Start with better simulations

---
title: Structural (Ensemble?) Biology

- Model combines simulation and experiment
- Error bars on structures
- Overcome forcefield bias

---
title: Conclusion

- MSMs parallelize MD simulation, enabling millisecond-scale dynamics
- MSMs allow both quantitative prediction and intuitive modeling
- BELT enables experiment-driven modeling of structure and equilibrium

---
title: Acknowledgements

Rhiju and Vijay

---
title: Acknowledgements
subtitle: Das Lab

- Pablo Cordero
- Frank Cochran
- Fang-Chieh Chou
- Parin Sripakdeevong

---
title: Acknowledgements
subtitle: Pande Lab / MSMBuilder

<font size="3">

 Greg Bowman

 Robert McGibbon

 Christian Schwantes

 TJ Lane

 Imran Haque

 Sergio Bacallado

 Lutz Maibaum

 Lee-Ping Wang

 Yu-Shan Lin

 Vince Voelz

 Dan Ensign
 
</font>

---
title: Acknowledgements
subtitle: Biochemistry, External

Buzz Baldwin, Thomas Kiefhaber, Dan Herschlag, Pehr Harbury

Folding@Home Donors and Forum Volunteers (Bruce Borden)

OpenMM Team: Joy Ku, Peter Eastman, Mark Friedrichs, Yutong Zhao

BELT: John Chodera, Frank Cochran, TJ Lane

Dissertation Committee: Pehr Harbury, Todd Martinez, Russ Altman


---
title: Personal Acknowledgements


